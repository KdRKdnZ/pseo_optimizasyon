# Mobil Oyun Performansını Artırma Rehberi: FPS Düşüşlerini ve Isınmayı Engelleyin

Mobil cihazlarda yüksek grafikli oyunlar oynarken karşılaşılan FPS (Saniye Başına Kare) düşüşleri, gecikme (lag) ve aşırı ısınma sorunları, genellikle yetersiz sistem optimizasyonundan kaynaklanır. Bu rehber; Android ve iOS işletim sistemlerinde **telefon oyun performansını artırma** amacıyla uygulanabilecek en etkili teknik yöntemleri, donanım düzeyindeki ayarları ve grafik optimizasyonlarını içermektedir.

---

## 1. Donanım ve Sistem Düzeyinde Optimizasyonlar

Oyun performansını doğrudan etkileyen ilk katman, işletim sisteminin çekirdek ve donanım yönetimi ayarlarıdır.

### Geliştirici Seçenekleri Ayarları (Android)
Android cihazlarda gizli olan "Geliştirici Seçenekleri" menüsü, GPU (Grafik İşleme Birimi) kullanımını zorlamak için kritik parametreler sunar:

*   **4x MSAA'yı Zorla (Force 4x MSAA):** OpenGL ES 2.0 oyunlarında kenar yumuşatmayı artırır. Grafik kalitesini yükseltirken GPU'ya yük bindirir; güçlü bir işlemciniz varsa performans sapmalarını engeller.
*   **HW Örtüşmelerini Devre Dışı Bırak (Disable HW Overlays):** Ekran oluşturma işleminde CPU yükünü alır ve doğrudan GPU kullanımını zorunlu kılar. Bu ayar, kare hızlarındaki kararsızlığı azaltır.
*   **Arka Plan İşlem Sınırı:** "Arka planda işlem yok" veya "En çok 1 işlem" olarak ayarlandığında, RAM'in tamamı aktif oyuna ayrılır.

### Ekran Yenileme Hızı ve Çözünürlük Skalalaması
*   **Yenileme Hızı (Hz):** Cihazınız 90Hz veya 120Hz ekran paneline sahipse, sistem ayarlarından bu değeri sabitleyin. Değişken yenileme hızları (Adaptive Refresh Rate) bazı oyunlarda takılmalara (stuttering) neden olabilir.
*   **Çözünürlük Düşürme:** Samsung (Game Game Booster Plus) veya Xiaomi (Game Turbo) gibi arayüzlerde yer alan çözünürlük ölçekleyiciyi %75-%80 seviyesine çekmek, GPU yükünü önemli ölçüde hafifletir ve FPS artışı sağlar.

---

## 2. Termal Yönetim ve Thermal Throttling Engelleme

Mobil işlemciler (SoC) belirli bir sıcaklık eşiğine (genellikle 40-45°C) ulaştığında, donanımı korumak için saat hızlarını düşürür. Buna **Thermal Throttling (Isıl Sınırlama)** denir.

*   **Şarj Esnasında Oyun Oynamayın:** Batarya doldurulurken oluşan kimyasal ısı ile işlemci ısısı birleştiğinde cihaz hızla throttling eşiğine ulaşır.
*   **Kılıf Kullanımı:** Silikon ve deri kılıflar ısı dağılımını engeller. Yoğun oyun seanslarında kılıfı çıkarın.
*   **Harici Soğutucu Kullanımı:** Peltier (yarı iletken) teknolojisine sahip fanlı telefon soğutucuları, arka kapak sıcaklığını 10-15°C düşürerek işlemcinin maksimum frekansta kalmasını sağlar.

---

## 3. Oyun İçi Grafik Ayarlarının Teknik Optimizasyonu

Oyun içi grafik ayarlarını "En Yüksek" seviyeye çekmek yerine, FPS/Görsellik dengesini kuracak teknik konfigürasyon yapılmalıdır:

| Grafik Ayarı | Önerilen Seviye | Performansa Etkisi | Açıklama |
| :--- | :--- | :--- | :--- |
| **Kare Hızı (Frame Rate)** | Aşırı / Aşırı Yüksek (Max) | Doğrudan FPS | Her zaman en yüksek değerde olmalıdır. |
| **Gölgeler (Shadows)** | Düşük / Kapalı | %15-20 FPS Artışı | Dinamik gölgeler GPU'yu en çok yoran ögedir. |
| **Yansımalar / Su Kalitesi** | Düşük / Kapalı | %10-15 FPS Artışı | Anlık hesaplama gerektiren gölgelendiricileri (shaders) kapatır. |
| **Alan Derinliği (Depth of Field)**| Kapalı | %5 FPS Artışı | Görsel derinlik efektini kaldırarak GPU yükünü azaltır. |
| **Anti-Aliasing (AA)** | Kapalı veya 2x | %10 FPS Artışı | Pürüzsüzleştirme efektini kapatarak RAM ve VRAM kullanımını düşürür. |

---

## 4. İşletim Sistemine Özel Performans İpuçları

### Android İçin:
1.  **Android System WebView Güncellemesi:** Oyun içi web bileşenlerinin ve veri akışının takılmaması için WebView ve Google Play Hizmetleri’nin güncel olduğundan emin olun.
2.  **Game Game Booster / Game Turbo Ayarları:**
    *   "Performans Modu"nu aktif edin.
    *   Dokunma hassasiyetini ve tepki süresini maksimuma çıkarın.
    *   Oyun sırasında bellek temizleme (RAM Auto-clean) özelliğini devreye sokun.

### iOS (iPhone) İçin:
1.  **Düşük Güç Modunu Kapatın:** Düşük Güç Modu, CPU performansını %30 ila %50 arasında kısıtlar. Oyuna girmeden önce mutlaka kapatılmalıdır.
2.  **Arka Plan Uygulama Yenileme:** `Ayarlar > Genel > Arka Plan Uygulama Yenileme` sekmesinden bu özelliği tamamen kapatın.
3.  **Depolama Alanı Yönetimi:** NVMe tabanlı depolama birimlerinde okuma/yazma hızının düşmemesi için cihaz belleğinde en az %15-%20 oranında boş alan bırakın.

---

## 5. Yazılım Önbelleği ve Bellek (RAM) Temizliği

*   **Önbellek (Cache) Temizliği:** Uzun süre oynanan oyunların biriken önbellek dosyaları veri okuma süresini uzatabilir. `Ayarlar > Uygulamalar > [Oyun Adı] > Depolama > Önbelleği Temizle` adımı takip edilmelidir. (Verileri temizlememeye dikkat edin).
*   **Sanal RAM (RAM Expansion) Özelliği:** Xiaomi, OPPO, Realme gibi cihazlarda bulunan "Sanal RAM" özelliği, yavaş dahili depolamayı RAM gibi kullanır. Oyunlarda **gecikmeye (micro-stuttering) yol açabileceği için bu özelliğin kapatılması** önerilir.

---

## Özet Performans Kontrol Listesi (Checklist)

* [ ] Oyun öncesi tüm arka plan uygulamaları kapatıldı.
* [ ] Düşük Güç Modu / Güç Tasarrufu kapatıldı.
* [ ] Ekran parlaklığı otomatikten çıkarılıp sabitlendi.
* [ ] Telefon kılıfı çıkarıldı ve cihaz şarjda değil.
* [ ] Oyun içi ayarlarında Kare Hızı "Maksimum", Gölgeler "Kapalı" konuma getirildi.
* [ ] Cihazın dahili depolama alanında en az 10 GB boş yer bırakıldı.