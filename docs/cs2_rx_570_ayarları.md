# CS2 RX 570 En İyi Grafik, Performans ve FPS Ayarları Rehberi

AMD Radeon RX 570 (4GB / 8GB), Source 2 motoruna geçen Counter-Strike 2'de (CS2) doğru optimize edildiğinde 144Hz ve üzeri monitörler için yeterli FPS değerlerini verebilen bir ekran kartıdır. Ancak, CS:GO'ya kıyasla CS2'nin ekran kartı (GPU) kullanımı çok daha yüksektir. 

Bu rehber, RX 570 mimarisinden (Polaris) maksimum Kare/Saniye (FPS) oranını almak ve girdi gecikmesini (input lag) en aza indirmek için hazırlanmış teknik konfigürasyonları içerir.

---

## CS2 Oyun İçi Video (Grafik) Ayarları

CS2'deki görsel netliği koruyarak ekran kartı yükünü hafifletmek için aşağıdaki ayarları uygulayın:

### Gelişmiş Video Ayarları

| Ayar Sekmesi | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Kontrastı** | **Etkin (Enabled)** | Düşmanların karanlık alanlarda fark edilmesini sağlar. FPS etkisi ihmal edilebilir düzeydedir. |
| **Dikey Eşitlemeyi Bekle (VSync)** | **Devre Dışı (Disabled)** | Girdi gecikmesini (Input Lag) artırır, kesinlikle kapatılmalıdır. |
| **Çoklu Örneklemeli Kenar Yumuşatma** | **2x MSAA** veya **CMAA2** | RX 570 için 4x MSAA performans kaybı yaratır. CMAA2 maksimum FPS sağlar, 2x MSAA ise pikselleşmeyi engeller. |
| **Evrensel Gölge Kalitesi** | **Düşük (Low)** veya **Orta (Medium)** | Gölgeler rakibin yerini anlamak için kritiktir. RX 570 için "Düşük" en kararlı FPS'i verir. |
| **Model / Doku Detayı** | **Düşük (Low)** | RX 570 4GB modeli kullanıyorsanız VRAM sınırına takılmamak için "Düşük" seçilmelidir. |
| **Doku Süzme Modu** | **Çift Hatlı (Bilinear)** | Ekran kartı üzerindeki bant genişliği yükünü azaltır. |
| **Shader Detayı** | **Düşük (Low)** | Işıklandırma ve cam yansımalarının GPU'yu yormasını engeller. |
| **Parçacık Detayı** | **Düşük (Low)** | Sis ve bomba patlamalarındaki ani FPS düşüşlerini (Stutter) engeller. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı (Disabled)** | RX 570 mimarisini en çok zorlayan ayarlardan biridir. Tamamen kapatılmalıdır. |
| **Yüksek Dinamik Aralık (HDR)** | **Hızlı (Performance)** | CS2'de tamamen kapatılamaz; "Hızlı" seçeneği GPU kullanımını düşürür. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Disabled)** | FSR görüntüyü bulanıklaştırır ve CS2'de gecikmeye sebep olabilir. Doğal çözünürlük tercih edilmelidir. |

### Çözünürlük ve Ekran Ayarları
* **Görüntü Modu:** Tam Ekran (Fullscreen) - *Penceresiz mod gecikmeyi artırır.*
* **Çözünürlük:** 1280x960 veya 1024x768 (4:3 Stretched)
  * *Not:* 1080p (16:9) çözünürlükte RX 570, sis bombası (Volumetric Smoke) içinde FPS düşüşleri yaşayabilir. 4:3 stretched çözünürlükler GPU yükünü hafifletir ve FPS'i %30-40 oranında artırır.

---

## AMD Software: Adrenalin Edition Ayarları

RX 570 için AMD sürücü panelinde yapılacak özelleştirmeler, oyun içi ayarlardan daha kritik performans artışları sağlayabilir.

1. **AMD Adrenalin** yazılımını açın ve **Oyun > CS2** profiline gidin.
2. Aşağıdaki teknik parametreleri uygulayın:

* **Radeon Anti-Lag:** **Etkin (Enabled)**
  * *Açıklama:* CS2'de NVIDIA Reflex eşdeğeri olarak çalışır, işlemci ile ekran kartı senkronizasyonunu sağlayıp girdi gecikmesini düşürür.
* **Radeon Chill:** **Devre Dışı (Disabled)**
* **Radeon Boost:** **Devre Dışı (Disabled)** (Dinamik çözünürlük ölçeklemesi takılmalara yol açabilir).
* **Radeon Image Sharpening (RIS):** **Etkin (%70 - %80)**
  * *Açıklama:* Düşük çözünürlükte (örneğin 1280x960) oynuyorsanız, pikselleşmeyi yok eder ve keskin bir görüntü sunar. FPS düşürmez.
* **Ekran Kartı Dokusu ve Mozaikleme (Tessellation) Ayarları:**
  * **Örtüşme Önleme Modu:** Uygulama ayarlarını kullan
  * **Doku Süzme Kalitesi:** Performans
  * **Yüzey Biçim Entegrasyonu:** Etkin
  * **Mozaikleme Modu (Tessellation):** Uygulama ayarlarını geçersiz kıl -> **Maksimum Mozaikleme Düzeyi: Off veya 4x/8x**
    * *Kritik İpucu:* Polaris (RX 500 serisi) mimarisi yüksek mozaikleme yüklerinde zorlanır. Bunu 4x veya 8x ile sınırlandırmak CS2 haritalarındaki FPS drop sorununu çözer.

---

## CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizden CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** alanına aşağıdaki komutları ekleyin:

```text
-high -threads 5 -novid -nojoy +cl_showfps 1
```

* `-high`: CS2 işlemini CPU üzerinde yüksek öncelikli hale getirir.
* `-threads X`: İşlemcinizin fiziksel çekirdek sayısı + 1 (Örn: 4 çekirdekli i5-7500 için `-threads 5`).
* `-nojoy`: Joystik/Gamepad girdi denetimini kapatır, RAM ve işlemci yükünü azaltır.

---

## RX 570 Özelinde Sistem ve VRAM Optimize İşlemleri

* **4GB VRAM Sınırı:** RX 570'in 4GB versiyonuna sahipseniz, arka planda Chrome veya Discord donanım ivmesini açık bırakmak CS2'nin VRAM sınırını aşmasına ve oyunun çökmesine/takılmasına neden olur. CS2 oynarken arka plan uygulamalarını kapatın.
* **Windows Grafik Ayarları:** Windows 10/11 arama çubuğuna "Grafik Ayarları" yazın. **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** seçeneğini kapalı konuma getirin (RX 500 serisi kartlarda HAGS bazen kararsızlığa yol açabilir).
* **Sürücü Sürümü:** RX 570 artık AMD tarafından "Legacy" (Eski) sürücü desteği statüsüne geçtiği için en güncel WHQL onaylı kararlı sürücüyü (23.11.1 veya üzeri) kullanın.

---

## Beklenen Performans Değerleri

Yukarıdaki yapılandırmalar uygulandığında, RX 570 ve ortalama bir işlemci (Örn: Ryzen 5 2600 / Ryzen 5 3600 veya i5-9400F) konfigürasyonunda alacağınız tahmini FPS değerleri:

* **1280x960 (Düşük-Orta Ayarlar):** 140 - 220 FPS (Savaş ve sis anlarında ortalama 120+ FPS)
* **1080p Native (Düşük Ayarlar):** 90 - 140 FPS

*CS2'nin işlemci odaklı (CPU-bound) bir oyun olduğu unutulmamalıdır. Ekran kartınız RX 570 olsa dahi, tam performansı almak için işlemcinizin tek çekirdek performansının yeterli düzeyde olması gerekir.*