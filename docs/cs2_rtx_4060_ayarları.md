# CS2 RTX 4060 Ayarları: Maksimum FPS ve Düşük Gecikme Rehberi

NVIDIA GeForce RTX 4060 (Ada Lovelace mimarisi), Counter-Strike 2 (CS2) gibi Source 2 motorunu kullanan ve hem GPU hem de CPU optimizasyonu isteyen oyunlarda oldukça yüksek performans sunar. Ancak CS2'de yalnızca yüksek FPS almak yeterli değildir; **kare zamanlaması (frame pacing)**, **girdi gecikmesi (input lag)** ve **görsel netlik** dengesini doğru kurmak gerekir.

Bu rehberde, RTX 4060 ekran kartı için CS2 oyun içi, NVIDIA Denetim Masası ve sistem düzeyindeki en optimum ayarları teknik detaylarıyla inceliyoruz.

---

## 1. CS2 Oyun İçi Gelişmiş Video Ayarları

CS2'de grafik ayarları sadece görselliği değil, doğrudan düşmanların görünebilirliğini ve sistem gecikmesini etkiler. RTX 4060 (8 GB VRAM) bu ayarların çoğunu rahatlıkla kaldırabilir ancak rekabetçi avantaj için aşağıdaki kombinasyon uygulanmalıdır:

| Grafik Ayarı | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır (Boost Player Contrast)** | **Etkin (Enabled)** | Düşman modellerinin karanlık arka planlarda netleşmesini sağlar. GPU yükü çok düşüktür. |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı (Disabled)** | Girdi gecikmesini (input lag) artırır. Kesinlikle kapatılmalıdır. |
| **Çoklu Örneklemeli Kenar Yumuşatma (MSAA)** | **4x MSAA** | 2x MSAA'ya göre kenar kırılmalarını belirgin şekilde azaltır. RTX 4060 için performans kaybı önemsizdir (%1-2). |
| **Evrensel Gölge Kalitesi (Global Shadow Quality)** | **Yüksek (High)** | Düşmanların gölgelerini daha uzaktan ve net görmenizi sağlar. Taktiksel avantaj sunar. |
| **Model / Doku Kalitesi (Model / Texture Detail)** | **Orta (Medium)** | Yüksek VRAM kullanımını önler, GPU bellek bant genişliğini rahatlatır ve kare kararlılığını artırır. |
| **Doku Filtreleme Modu (Texture Filtering)** | **Anizotropik 4x / 8x** | Dokuların açısal netliğini artırır. RTX 4060 bellek kontrolcüsü için yük oluşturmaz. |
| **Ayrıntılı Gölge Kalitesi (Shader Detail)** | **Düşük (Low)** | Cam, su ve fırlatılabilirlerin neden olduğu gereksiz ışık yansımalarını kapatır, ani FPS düşüşlerini (stuttering) engeller. |
| **Parçacık Ayrıntısı (Particle Detail)** | **Düşük (Low)** | Sis ve molotof efektlerindeki işlemci/grafik yükünü azaltır, patlamalarda FPS'in sabit kalmasını sağlar. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı (Disabled)** | Derinlik gölgelerini kapatır. Rekabetçi oyunda düşman tespitini zorlaştırabilir ve FPS düşürür. |
| **Yüksek Dinamik Aralık (HDR)** | **Kalite (Quality)** | Renk geçişlerini optimize eder. "Hız" moduna göre görüntü netliği daha iyidir, RTX 4060'ta performans farkı yaratmaz. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Disabled - Highest Quality)** | FSR, görüntüyü bulanıklaştırır ve piksel bazlı gecikme ekler. Yerel çözünürlük (Native) kullanılmalıdır. |
| **NVIDIA Reflex Low Latency** | **Etkin + Boost (Enabled + Boost)** | GPU saat hızlarını maksimumda tutarak sistem gecikmesini minimuma indirir. CS2 için en kritik ayardır. |

---

## 2. NVIDIA Denetim Masası Ayarları

CS2'ye özel bir profil oluşturarak NVIDIA sürücü düzeyinde optimizasyon yapmak, kare iletim hızını optimize eder.

1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** > **Program Ayarları** sekmesine gidin.
3. Listeden `Counter-Strike 2 (cs2.exe)` dosyasını seçin (Yoksa "Ekle" butonundan seçin).

Aşağıdaki değerleri uygulayın:

* **Düşük Gecikme Oranı Modu (Low Latency Mode):** `Açık (On)` veya `Ultra` *(Oyun içi NVIDIA Reflex açık olduğu için sürücü seviyesindeki bu ayar Reflex ile senkronize çalışır).*
* **Güç Yönetimi Modu (Power Management Mode):** `Maksimum Performansı Tercih Et (Prefer Maximum Performance)`. GPU'nun boşta düşük frekansa düşmesini engeller.
* **Doku Filtreleme - Kalite (Texture Filtering - Quality):** `Yüksek Performans (High Performance)`.
* **Doku Filtreleme - Trilinear Optimizasyon:** `Açık (On)`.
* **Eşyönsüz Örnek Optimizasyonu:** `Açık (On)`.
* **Eşzamansız Kare Sayısı (Max Frame Rate):** `Kapalı (Off)` *(FPS sabitlemesi oyun içinden `fps_max` komutu ile yapılmalıdır).*
* **Bağlantılı Optimizasyon (Threaded Optimization):** `Açık (On)`. İşlemci çekirdeklerinin verimli kullanılmasını sağlar.
* **G-Sync / FreeSync:** Rekabetçi odaklı oynuyorsanız kapatılması önerilir. Eğlence odaklı ve yırtılmasız görüntü için açık kalabilir.

---

## 3. Çözünürlük ve Boyut Oranı (Aspect Ratio) Seçimi

RTX 4060, 1080p (FHD) çözünürlükte CS2 için fazlasıyla yeterlidir. Seçenekler kullanım amacına göre ayrılır:

* **16:9 (1920x1080 - Native):** En geniş görüş açısını (FOV) sunar. Görsel netlik maksimumdur, uzak mesafedeki kafaları seçmek kolaydır.
* **4:3 Stretched (Örn: 1280x960 veya 1440x1080):** Oyuncu modellerini yatayda genişletir, hedefleri vurmayı algısal olarak kolaylaştırır. FOV daralır ancak piksel yoğunluğu odaklı oynayan profesyonellerin tercihidir.

> **Teknik Not:** 4:3 stretched modunda RTX 4060 üzerindeki yük azalır ve darboğaz tamamen CPU'ya kayar. Sisteminizdeki CPU (Örn: Ryzen 5 5600 / Core i5-13400F) yetersizse 4:3 çözünürlükte FPS artışı görmeyebilirsiniz.

---

## 4. Windows ve Sürücü Düzeyi Optimizasyonları

### Hardware-Accelerated GPU Scheduling (HAGS)
Windows 10/11 ayarlarından **Grafik Ayarları** menüsüne gidin ve **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** özelliğini **AÇIK** konuma getirin. Ada Lovelace (RTX 40 Serisi) mimarisi HAGS ile oldukça stabil çalışır, VRAM yönetimini iyileştirir.

### Resizable BAR (ReBAR)
RTX 4060'ın 8 GB PCIe 4.0 x8 veri yolunu tam kapasite kullanabilmesi için BIOS üzerinden **Resizable BAR** (veya Above 4G Decoding) seçeneğinin açık olduğundan emin olun. Bu ayar, 1% Low FPS değerlerini gözle görülür şekilde artırarak takılmaları önler.

---

## 5. Başlatma Seçenekleri (Launch Options)

CS2 (Source 2), CS:GO'daki birçok eski komutu desteklememektedir. Gereksiz komutlar çökme ve performans kaybına neden olabilir. Steam kütüphanesinde CS2'ye sağ tıklayıp **Özellikler > Başlatma Seçenekleri** kısmına sadece şu komutları ekleyin:

```text
-novid -nojoy
```

* `-novid`: Açılış introsunu atlar.
* `-nojoy`: Oyun kolu (joystick) girdilerini kapatır, az miktarda RAM ve CPU kaynağı tasarrufu sağlar.

*(Not: CS2'de `-high`, `-threads` gibi komutlar Source 2 iş parçacığı yöneticisini bozabileceği için önerilmez.)*

---

## Özet Performans Beklentisi

Doğru ayarlanmış bir **RTX 4060** ve güncel bir orta-üst seviye işlemci (örneğin Ryzen 5 7600 veya i5-13600K) ile 1080p çözünürlükte elde edilecek ortalama değerler:

* **Rekabetçi Ayarlarda Ortalama FPS:** 300 - 450 FPS
* **1% Low FPS:** 160 - 220 FPS
* **Sistem Gecikmesi (Reflex On+Boost):** ~5 ms - 9 ms

Bu değerler, 240 Hz veya 360 Hz e-spor monitörlerinin tam performansla kullanılmasını sağlar.