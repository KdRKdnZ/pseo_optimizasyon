# Android FPS Artırma Rehberi: Donanım ve Yazılım Odaklı Teknik Çözümler

Android işletim sisteminde FPS (Frames Per Second - Saniye Başına Kare Sayısı) değerini artırmak, yalnızca görsel akıcılığı değil, aynı zamanda dokunmatik gecikmesini (input lag) düşürerek oyun içi tepki süresini optimize etmeyi sağlar. Android'in açık kaynaklı yapısı; GPU yük dağılımı, arka plan işlem sınırlandırmaları ve çözünürlük ölçekleme gibi alt seviye ayarlarla sistem performansını maksimuma çıkarmaya izin verir.

Bu rehberde, root işlemi gerektiren ve gerektirmeyen teknik yöntemlerle Android cihazlarda FPS artırma adımları incelenmektedir.

---

## 1. Geliştirici Seçenekleri (Developer Options) Üzerinden GPU Optimizasyonu

Geliştirici seçenekleri, Android donanım hızlandırma parametrelerine müdahale etmenin en doğrudan yoludur.

### Geliştirici Seçeneklerini Aktif Etme:
* **Ayarlar > Telefon Hakkında > Yazılım Bilgileri** yolunu izleyin.
* **Yapım Numarası (Build Number)** seçeneğine 7 kez üst üste dokunun.

### Kritik Sistem Ayarları:

* **HW Katmanlarını Devre Dışı Bırak (Disable HW Overlays):**
  * **Teknik Açıklama:** Standart şartlarda Android, ekran derlemesi (screen composition) için CPU ve GPU arasında geçiş yapar. HW katmanları devre dışı bırakıldığında, ekran derleme işlemi tamamen GPU'ya aktarılır.
  * **Sonuç:** GPU üzerindeki hafif yük artışına karşın, CPU darboğazı (bottleneck) engellenir ve kare iletim süresi (frame delivery time) düşer.

* **4x MSAA'yı Zorla (Force 4x MSAA):**
  * **Teknik Açıklama:** OpenGL ES 2.0 uygulamalarında Çoklu Örnekli Kenar Yumuşatmayı (Multisample Anti-Aliasing) zorlar.
  * **Uyarı:** Bu ayar grafik kalitesini artırır ancak orta/düşük segment GPU'larda FPS düşüşüne ve aşırı ısınmaya neden olabilir. Üst segment cihazlarda grafik pürüzlerini gidermek için kullanılmalıdır. FPS kazanımı odaklı düşük segment cihazlarda **kapalı** kalmalıdır.

* **Grafik Sürücüsü Tercihleri (Graphics Driver Preferences):**
  * Android 10 ve üzeri cihazlarda belirli oyunların sistem grafik sürücüsü yerine özel güncellenmiş grafik sürücülerini (Sistem Grafik Sürücüsü) kullanmasını sağlayın. Bu işlem, oyun içi API çağrılarının (Vulkan/OpenGL) doğrudan GPU'ya iletilmesini sağlar.

---

## 2. ADB (Android Debug Bridge) İle Çözünürlük ve DPI Ölçekleme

GPU'nun render etmek zorunda olduğu piksel sayısını azaltmak, FPS artırmanın en etkili donanımsal yoludur. 1080p (FHD) bir ekranı 720p (HD) seviyesine çekmek, GPU yükünü yaklaşık %40 oranında azaltır.

### Gerekli Adımlar:
1. Bilgisayarınıza **ADB Drivers** ve **Platform Tools** kurun.
2. Telefonda **USB Hata Ayıklama** modunu açın.
3. Komut satırını (CMD/Terminal) açıp cihazı doğrulayın:
   ```bash
   adb devices
   ```

### Çözünürlük Düşürme Komutları:
Cihazınızın mevcut çözünürlüğünü kontrol etmek için:
```bash
adb shell wm size
```

Çözünürlüğü 720p seviyesine düşürmek için (Örnek: 1080x2400 ekranda):
```bash
adb shell wm size 720x1600
```

DPI değerini yeni çözünürlüğe uygun olarak yeniden ölçekleyin:
```bash
adb shell wm density 280
```

> **Not:** Varsayılan ayarlara dönmek için `adb shell wm size reset` ve `adb shell wm density reset` komutlarını kullanabilirsiniz.

---

## 3. Termal Throttling (Isıl Sınırlandırma) Yönetimi

Android cihazlar, SoC (System on Chip) sıcaklığı kritik eşiğe (genellikle 40°C - 45°C) ulaştığında frekans düşürür (Thermal Throttling). Bu durum ani FPS düşüşlerinin (stuttering) ana nedenidir.

### Termal Performansı Koruma Yöntemleri:
* **Kılıf Kullanımını Bırakın:** Isı dağılımını (heat dissipation) engelleyen silikon veya kalın plastik kılıflar cihazın soğumasını geciktirir.
* **Harici Soğutucu Kullanımı:** Peltier tabanlı harici telefon soğutucuları, termal eşiğe ulaşılmasını engelleyerek CPU/GPU çekirdeklerinin maksimum frekansta (Max Clock Speed) kararlı çalışmasını sağlar.
* **Şarj Esnasında Oyun Oynamayın:** Batarya doldurulurken oluşan kimyasal ısı ile SoC entegresinin ısısı birleştiğinde throttle süreci hızlanır.

---

## 4. Ekran Yenileme Hızı ve Oyun İçi İdeal Ayarlar

Ekran yenileme hızı (Hz) ile kare hızı (FPS) senkronize olmalıdır. 120Hz ekrana sahip bir cihazda oyun 60 FPS kilitli çalışıyorsa, panel tam verimle kullanılmıyor demektir.

* **Yenileme Hızını Sabitleyin:** **Ayarlar > Ekran > Pürüzsüz Hareket** sekmesinden ekranı en yüksek değere (90Hz / 120Hz / 144Hz) getirin.
* **Oyun İçi Grafik Konfigürasyonu:**
  * **Shadows (Gölgeler):** CPU ve GPU üzerine en çok yük bindiren ögedir. Minimuma getirilmelidir.
  * **Reflections / Shaders:** Kapatılmalıdır.
  * **Frame Rate (Kare Hızı):** Grafik kalitesini "Düşük" seviyeye çekip, Kare Hızını "Aşırı" veya "90 FPS" seçeneğine getirmek, render önceliğini akıcılığa verir.

---

## 5. Arka Plan İşlemlerini ve Bloatware'i Temizleme

Android’in RAM yönetimi (LPDDR RAM) arka planda çalışan uygulamaları askıya alsa da, işlemci döngülerinden (CPU Cycles) pay alabilirler.

* **Arka Plan İşlem Sınırı:** Geliştirici seçeneklerinden "Arka plan işlem sınırı" sekmesini **En fazla 2 işlem** olarak ayarlayın.
* **Bloatware Kaldırma:** Sistemle birlikte gelen ve arka planda çalışan gereksiz üretici uygulamalarını ADB üzerinden kaldırın:
  ```bash
  adb shell pm uninstall -k --user 0 uygulama_paket_adi
  ```

---

## 6. Root'lu Cihazlar İçin İleri Seviye Optimizasyonlar (Gelişmiş)

Eğer cihazınızda Root erişimi ve Magisk/KernelSU mevcutsa, performans artışı doğrudan çekirdek (kernel) seviyesinde sağlanabilir.

* **Custom Kernel Kullanımı:** LKM (Loadable Kernel Modules) desteğine sahip, termal limitleri gevşetilmiş ve GPU governor ayarları "performance" moduna alınmış özel kernel'lar (örneğin Franco Kernel, ElementalX) flash edilebilir.
* **Thermal Modülleri:** Magisk üzerinden yüklenen "Thermal Engine Mod" paketleri, cihazın ısınma kısıtlamalarını devre dışı bırakır. *Risk:* Cihazın aşırı ısınmasına yol açabilir.
* **FPS Unlocker (LSposed/Xposed):** Oyunların cihaz modelini kontrol ederek kapalı tuttuğu 90/120 FPS seçeneklerini, cihaz kimliğini (Build.prop) üst segment bir modele (örneğin Asus ROG Phone) maskeleyerek açabilirsiniz.

---

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Etki Alanı | Beklenen FPS Artışı | Zorluk Seviyesi |
| :--- | :--- | :--- | :--- |
| **ADB Çözünürlük Düşürme** | GPU Yükü | %20 - %40 | Orta |
| **HW Katmanlarını Devre Dışı Bırakma** | CPU/GPU Yük Dağılımı | %5 - %10 | Kolay |
| **Grafik Düzeyini Düşürüp FPS Limiti Açma** | Genel Render | %30 - %50 | Kolay |
| **Harici Soğutma Kullanımı** | Termal Throttling Engelleme | Kararlı FPS (Drop Önleme) | Kolay |
| **Custom Kernel / Root Tweak** | Çekirdek Frekansları | %15 - %30 | İleri Seviye |