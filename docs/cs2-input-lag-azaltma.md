---
title: "cs2 input lag azaltma"
description: "cs2 input lag azaltma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 Input Lag Azaltma Rehberi: Sistem ve Oyun İçi Teknik Optimizasyonlar

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği yenilenmiş fizik mantığı ve **Sub-tick** sistemi nedeniyle girdi gecikmesine (input lag) karşı CS:GO’ya kıyasla çok daha hassastır. Oyunda farenin tıklandığı an ile eylemin ekrana yansıdığı an arasındaki milisaniyelik gecikmeler, sprey kontrolünü ve tepe tepki süresini doğrudan etkiler. 

Bu rehber; donanım, işletim sistemi, ekran kartı sürücüleri ve oyun içi ayarlar düzeyinde **CS2 sistem gecikmesini (system latency) en alt seviyeye indirmek** için uygulamanız gereken teknik adımları içerir.

---

## 1. Oyun İçi Grafik Ayarları ile Render Gecikmesini Düşürme

CS2'de grafik yükü arttıkça GPU kullanım oranı %99 seviyelerine ulaşır. GPU tam yükte çalıştığında render kuyruğu (render queue) uzar ve bu durum ciddi bir input lag oluşturur.

* **NVIDIA Reflex Low Latency:** **AÇIK + BOOST (On + Boost)** olarak ayarlanmalıdır. "Boost" seçeneği, GPU'nun güç tasarrufu modlarına geçmesini engelleyerek çekirdek saat hızlarını (core clocks) sürekli yüksek tutar ve işlemci-ekran kartı arasındaki veriyi en hızlı şekilde işler.
* **Görüntü Modu:** Mutlaka **Tam Ekran (Fullscreen)** seçilmelidir. "Pencereli" veya "Sınırlandırılmamış Pencereli" modlar, Windows Masaüstü Pencere Yöneticisi'nin (DWM) dikey senkronizasyon (V-Sync) katmanını devreye sokarak gecikmeyi artırır.
* **Dikey Eşitleme (V-Sync):** **Kapat**. V-Sync, kareleri monitörün tazeleme hızına zorlarken devasa bir girdi gecikmesi yaratır.
* **NVIDIA G-Sync / AMD FreeSync:** Yarışmacı (competitive) seviyede en düşük gecikme için **Kapatılması** önerilir. Eğer ekran yırtılmaları sizi çok rahatsız ediyorsa; G-Sync + Reflex ikilisi kullanılabilir ancak salt en düşük gecikme için kapalı kalmalıdır.
* **Çoklu Örneklemeli Kenar Yumuşatma (MSAA):** **2x MSAA** veya **CMAA**. 4x ve 8x MSAA, GPU render süresini (frame time) uzatarak gecikmeyi artırır.
* **FidelityFX Super Resolution (FSR):** **Devre Dışı (Devre Dışı - En Yüksek Kalite)**. FSR işlem yükünü azaltsa da görüntüye ölçekleme algoritmaları eklediği için milisaniyelik işleme gecikmeleri ekleyebilir. Yalnızca GPU'nuz çok zayıfsa açılmalıdır.

---

## 2. Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin.
3. **Düşük Gecikme Oranı Modu (Low Latency Mode):** Oyun içinde NVIDIA Reflex açık olduğu durumlarda Reflex bu ayarı devralır. Ancak genel sistem kararlılığı için **Ultra** veya **Açık** konumuna getirin.
4. **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et**. (GPU'nun voltaj D3 durumlarına geçip gecikme yaratmasını önler).
5. **Bağlantılı Optimizasyon (Threaded Optimization):** **Açık**. (CS2'nin çoklu çekirdek kullanımını optimize eder).
6. **Doku Süzme - Kalite:** **Yüksek Performans**.
7. **Shader Önbellek Boyutu (Shader Cache Size):** **10 GB** veya **Sınırsız (Unlimited)**. (Oyun sırasında anlık takılmaları ve buna bağlı input lag sıçramalarını engeller).

### AMD Radeon Software Ayarları
1. **Radeon Anti-Lag:** **Etkin**. (İşlemci ile ekran kartı arasındaki kare iletim temposunu eşitleyerek gecikmeyi düşürür).
2. **Radeon Boost:** **Devre Dışı**. (Dinamik çözünürlük değişimleri sprey tutarlılığını bozar).
3. **Radeon Image Sharpening:** **Devre Dışı**.

---

## 3. Fare (Mouse) ve Çevre Birimleri Optimizasyonu

Fare girdilerinin sisteme iletilme hızı ve sensörün işlenme süresi doğrudan fare ayarlarına bağlıdır.

* **DPI ve Sensör Latansı:** Düşük DPI (örn. 400 DPI) kullanmak, yüksek DPI (örn. 1600 DPI) kullanmaya kıyasla sensörün hareketi algılama süresini (initial motion latency) birkaç milisaniye geciktirir. **1600 DPI** kullanıp oyun içi hassasiyeti (sensitivity) düşürmek, fare sensörünün tepki süresini teknik olarak hızlandırır.
* **Polling Rate (Raporlama Hızı):** Minimum **1000 Hz** kullanılmalıdır. 2000 Hz, 4000 Hz veya 8000 Hz destekleyen farelerde işlemciniz (CPU) yeterince güçlü ise (örn. Ryzen 7 7800X3D seviyesi) daha yüksek Hz değerleri girdi gecikmesini düşürür. Ancak zayıf CPU'larda bu durum kare hızı düşüşlerine (FPS drops) yol açabilir.
* **Windows İşaretçi Hassasiyetini Artır:** **Kapat**. (Windows arama çubuğuna `main.cpl` yazıp Fare Seçenekleri altından bu tiki kaldırın).

---

## 4. Windows ve İşletim Sistemi Optimizasyonları

Windows arka planındaki süreçler, kesme istekleri (IRQ) ve güç yönetimi protokolleri latency artışına neden olur.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `cs2.exe` dosyasını bulun (Genellikle: `Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64`).
2. `cs2.exe` dosyasına sağ tıklayıp **Özellikler > Uyumluluk** sekmesine gidin.
3. **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.

### Windows Oyun Modu ve HAGS
* **Oyun Modu (Game Mode):** **AÇIK**. Windows 10/11'de Oyun Modu, işlemci kaynaklarını doğrudan CS2'ye aktararak arka plan işlemlerinin gecikme yaratmasını engeller.
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Bu ayar ekran kartına göre değişiklik gösterir. Genellikle NVIDIA RTX serisi kartlarda **AÇIK** tutulması kare sürelerini (frame time) iyileştirirken, bazı sistemlerde mikro takılmalara yol açabilir. Test edilerek karar verilmelidir.

### Güç Planı Ayarları
* Windows Güç Seçenekleri'nden **Yüksek Performans** veya **Nihai Performans (Ultimate Performance)** modunu seçin. Bu sayede işlemci çekirdekleri "parking" (uyku) moduna geçmez ve sürekli maksimum frekansta kalır.

---

## 5. CS2 FPS Limitleme ve Konsol Komutları

CS2'de FPS'i tamamen serbest bırakmak (fps_max 0) her zaman en düşük gecikmeyi sağlamaz. GPU kullanımı %99'a dayandığında sistem gecikmesi tavan yapar.

* **FPS Kısıtlama Stratejisi:** Eğer ekran kartınız sürekli %99 kullanımda çalışıyorsa, FPS'i sisteminizin rahatlıkla verebildiği ve GPU kullanımını %90-95 civarında tutan bir değere sabitlemek (`fps_max 300` veya `fps_max 400` gibi) render gecikmesini stabilized eder.
* **NVIDIA Reflex Aktifken:** Oyun içi Reflex açık olduğunda, sistem FPS'i otomatik olarak monitör tazeleme hızının ve GPU limitinin hemen altında sınırlandırarak en optimal latency eğrisini yakalar.

### CS2 Başlatma Seçenekleri (Launch Options)
Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kısmına aşağıdaki komutları ekleyebilirsiniz:

```text
-nojoy -high -threads [Çekirdek_Sayısı + 1]
```
*(Not: `-threads` komutuna fiziki çekirdek sayınızı girmelisiniz, sanal çekirdekleri dahil etmek bazı işlemcilerde gecikmeyi artırabilir.)*

---

## Özet Teknik Kontrol Listesi

| Parametre | Tavsiye Edilen Ayar | Nedeni |
| :--- | :--- | :--- |
| **NVIDIA Reflex** | On + Boost | GPU saat hızını yüksek tutar, render kuyruğunu sıfırlar. |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | DWM masaüstü gecikmesini baypas eder. |
| **Fare DPI / Hz** | 1600 DPI / 1000Hz+ | Sensörün başlangıç hareket gecikmesini düşürür. |
| **V-Sync / G-Sync** | Kapalı (Off) | Ekran eşitleme tampon belleğini (buffer) kaldırır. |
| **Güç Planı** | Nihai Performans | CPU/GPU voltaj düşüşlerinden kaynaklı lag'ı önler. |