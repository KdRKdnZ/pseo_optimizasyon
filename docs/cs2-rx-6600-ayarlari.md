---
title: cs2 rx 6600 ayarları
description: cs2 rx 6600 ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 RX 6600 Ayarları: En Yüksek FPS ve En Düşük Gecikme Rehberi

AMD Radeon RX 6600, RDNA 2 mimarisi, 8 GB GDDR6 belleği ve 32 MB Infinity Cache yapısı ile 1080p çözünürlükte yüksek fiyat/performans sunan bir grafik kartıdır. Ancak Valve’ın Source 2 motoruna geçiş yaptığı Counter-Strike 2 (CS2), işlemci (CPU) darboğazına ve gecikme sürelerine (input lag) karşı son derece hassastır. 

Bu rehber, RX 6600 ekran kartınızdan maksimum kare hızını (FPS) alırken, milisaniyelik gecikmeleri en aza indirmek için optimize edilmiş donanım, sürücü ve oyun içi ayarlarını içermektedir.

---

## 1. AMD Software: Adrenalin Edition Sürücü Ayarları

Ekran kartınızın işletim sistemi seviyesindeki davranışını optimize etmek, oyun içi ayarlardan daha kritik bir öneme sahiptir. AMD Adrenalin paneli üzerinden yapılması gereken spesifik ayarlar şunlardır:

*   **Ekran Kartı Profili:** Standart (Standart profil, arka planda gereksiz gecikme yaratabilecek tüm filtreleri devre dışı bırakır).
*   **Radeon Anti-Lag:** **Etkin (Enabled)**. CS2'de NVIDIA Reflex'in AMD tarafındaki karşılığıdır. CPU'nun GPU'yu bekleme süresini azaltarak giriş gecikmesini (input lag) minimize eder.
*   **Radeon Boost:** **Devre Dışı (Disabled)**. Dinamik çözünürlük ölçeklemesi rekabetçi oyunlarda piksel hassasiyetini bozduğu için kesinlikle kapatılmalıdır.
*   **Radeon Image Sharpening (Görüntü Keskinleştirme):** **Etkin (Enabled) - %10 ila %20 arası**. CS2'de düşük çözünürlük (örneğin 4:3 stretched) kullanıyorsanız, piksellenmeyi önlemek ve düşman hatlarını netleştirmek için bu ayarı hafifçe açın.
*   **Radeon Enhanced Sync:** **Devre Dışı (Disabled)**. Ekran yırtılmalarını önlese de mikro takılmalara (stuttering) yol açar.
*   **Doku Filtreleme Kalitesi (Texture Filtering Quality):** **Performans**. Görüntü kalitesinden ödün vermeden doku süzme yükünü azaltır.
*   **Yüzey Biçimi Optimizasyonu (Surface Format Optimization):** **Etkin (Enabled)**.
*   **Mozaikleme Modu (Tessellation Mode):** **Uygulama ayarlarını geçersiz kıl** -> **Kapalı** veya **AMD Optimize Edilmiş**. Source 2 motorunun gereksiz tessellation yükünü sınırlar.

---

## 2. Donanım Seviyesinde Optimizasyon: Smart Access Memory (SAM)

RX 6600’ün PCIe 4.0 x8 veri yolu genişliği, özellikle işlemci yoğun sahnelerde darboğaz yaratabilir. Bunu aşmak için **Smart Access Memory (SAM)** teknolojisini aktif etmeniz gerekir.

1.  Bilgisayarınızı yeniden başlatın ve BIOS ekranına girin.
2.  **Advanced** (Gelişmiş) menüsünden **PCI Subsystem Settings** sekmesine gidin.
3.  **Above 4G Decoding** seçeneğini **Enabled** yapın.
4.  **Re-Size BAR Support** seçeneğini **Auto** veya **Enabled** konumuna getirin.
5.  Ayarları kaydedip çıkın. AMD Adrenalin panelinde "Performans" -> "Ayar" sekmesinde SAM'in etkin olduğunu doğrulayın. Bu işlem, CS2'de minimum FPS değerlerinizi (1% Low) %8 ila %12 oranında artıracaktır.

---

## 3. CS2 Oyun İçi Grafik Ayarları

Source 2 motoru, CS:GO'ya kıyasla GPU'ya çok daha fazla yük bindirir. RX 6600 için hem görsel netliği koruyan hem de 300+ FPS hedefleyen optimize edilmiş oyun içi ayarlar tablosu aşağıdadır:

| Ayar Adı | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır** | Etkin (Enabled) | Karanlık köşelerdeki düşman modellerinin görünürlüğünü artırır. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı (Disabled) | Ciddi oranda giriş gecikmesine (input lag) neden olur. |
| **Çoklu Örnekleme Kenar Yumuşatma** | 4x MSAA | 2x MSAA piksellenmeye neden olur, 8x ise RX 6600'ün Infinity Cache sınırını zorlar. 4x en dengeli ayardır. |
| **Evrensel Gölge Kalitesi** | Orta (Medium) | Yüksek ayar gölgeleri netleştirir ancak FPS düşürür. Düşük ayar ise düşman gölgelerini tamamen yok edebilir. Orta ayar idealdir. |
| **Model / Doku Detayı** | Düşük (Low) veya Orta | VRAM kullanımı açısından RX 6600 için fark yaratmaz ancak işlemci yükünü azaltmak için Düşük önerilir. |
| **Shader Detayı** | Düşük (Low) | Source 2'nin ağır ışıklandırma ve yansıma efektlerini azaltarak FPS dalgalanmalarını önler. |
| **Parçacık Detayı** | Düşük (Low) | Molotof ve el bombası patlamalarındaki ani FPS düşüşlerini (frame drop) engeller. |
| **Çevre Perdeleme (Ambient Occlusion)** | Devre Dışı (Disabled) | Rekabetçi avantajı yoktur, GPU'ya gereksiz statik gölge yükü bindirir. |
| **Yüksek Dinamik Aralık (HDR)** | Performans (Performance) | Görsel kaliteyi korurken ışık geçişlerindeki GPU yükünü azaltır. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (Disabled) | FSR, CS2'de görüntüde çamurlaşmaya ve karıncalanmaya yol açar. RX 6600 saf güçte yeterlidir, FSR kapalı kalmalıdır. |

### Çözünürlük Seçimi: 1080p vs 4:3 Stretched
*   **1920x1080 (Native):** RX 6600 bu çözünürlükte yukarıdaki ayarlarla ortalama **240-320 FPS** verir. Görsel netlik maksimum düzeydedir.
*   **1280x960 (4:3 Stretched):** Profesyonel oyuncuların tercihidir. GPU üzerindeki yükü minimize eder, darboğazı tamamen CPU'ya kaydırır. RX 6600 ile bu çözünürlükte **350-450+ FPS** değerlerine ulaşmak mümkündür.

---

## 4. Windows ve Başlatma Seçenekleri (Launch Options) Optimizasyonu

Yazılım mimarisi perspektifinden, işletim sisteminin arka plan servislerinin CS2'nin ana iş parçacığı (main thread) üzerindeki önceliğini optimize etmek gerekir.

### Windows Grafik Ayarları
1.  Windows Arama çubuğuna "Grafik Ayarları" yazın.
2.  **Donanım hızlandırmalı GPU zamanlaması (HAGS)** seçeneğini **Açık** konuma getirin.
3.  Aşağıdaki listeden CS2.exe'yi bulun (Yol: `Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64\cs2.exe`) ve **Yüksek Performans** (RX 6600) olarak ayarlayın.

### CS2 Başlatma Seçenekleri (Launch Options)
Steam kütüphanenizde CS2'ye sağ tıklayıp Özellikler -> Genel sekmesindeki Başlatma Seçenekleri bölümüne şu komutları ekleyin:

```text
-high -threads 7 -nojoy +cl_updaterate 128
```

*   `-high`: İşlemcinin CS2 işlemine öncelik vermesini sağlar.
*   `-threads [Değer]`: RX 6600 ile en çok kullanılan Ryzen 5 5600 gibi 6 çekirdek/12 izlekli (thread) işlemcilerde, fiziksel çekirdek sayısının 1 fazlasını (örneğin 7) yazmak Source 2 motorunda kare dağılımını (frametime consistency) stabilize eder.
*   `-nojoy`: Joystick sürücülerini devre dışı bırakarak RAM ve CPU üzerindeki mikro yükü kaldırır.

---

## 5. Performans Analizi ve Beklenen Sonuçlar

Bu optimizasyonlar uygulandıktan sonra, **Ryzen 5 5600 / Core i5-12400F** ve **AMD Radeon RX 6600** kombinasyonuna sahip bir sistemde elde edilecek tahmini performans verileri şu şekildedir:

*   **1080p En Düşük %1 FPS Değeri (Frametime):** 140 FPS seviyesinden **190+ FPS** seviyesine yükselir. Bu, ani dönüşlerdeki takılma hissini tamamen ortadan kaldırır.
*   **Ortalama FPS (1280x960 Çözünürlükte):** 380-420 FPS bandında stabilizasyon sağlanır.
*   **Sistem Gecikmesi (End-to-End Latency):** Radeon Anti-Lag ve SAM aktifken ortalama gecikme süresi **5.2 ms** seviyesine kadar düşer, bu da rekabetçi sunucularda mermilerin tescil edilme (hit registration) oranını doğrudan artırır.