---
title: cs2 en iyi ayarlar
description: cs2 en iyi ayarlar hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 En İyi Ayarlar: FPS Artırma ve Gecikme Azaltma Rehberi

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği fiziksel tabanlı ışıklandırma, dinamik sis bombaları ve yenilenmiş alt-piksel (sub-tick) kayıt sistemiyle oyun içi mekanikleri tamamen değiştirdi. Bu rehberde, donanım kaynaklarınızı en verimli şekilde kullanarak maksimum FPS ve en düşük girdi gecikmesini (input lag) elde etmenizi sağlayacak, teknik olarak kanıtlanmış **CS2 en iyi ayarlar** optimizasyonunu gerçekleştireceğiz.

---

## Source 2 Motorunun Teknik Yapısı ve Performans İlişkisi

CS:GO'nun kullandığı eski Source motorunun aksine, Source 2 modern GPU mimarilerinden (DirectX 11/12 seviyesi) çok daha fazla yararlanır. CS:GO büyük oranda CPU limitli (işlemci darboğazlı) bir oyunken, CS2 ekran kartına (GPU) çok daha fazla yük bindirir.

### CPU ve GPU Dengesi (Darboğaz Analizi)
CS2'de kararlı bir kare hızı (frametime) elde etmek için işlemci ve ekran kartı arasındaki iş yükü dağılımını optimize etmek gerekir. İşlemcinizin tek çekirdek performansı, oyunun saniyede üretebileceği maksimum kare sınırını belirlerken; ekran kartınız, çözünürlük ve gölge kalitesi gibi grafiksel yükleri sırtlar. Gecikmeyi azaltmak için GPU kullanım oranını %90-95 seviyelerinde tutmak, ancak %99 doygunluğa ulaştırmamak (GPU bottleneck kaynaklı girdi gecikmesini önlemek için) idealdir.

### Sub-tick Sistemi ve Ağ Ayarları
CS2, 64 veya 128 tick rate yerine "sub-tick" adı verilen yeni bir sunucu iletişim protokolü kullanır. Bu sistemde oyun, fare hareketlerinizi ve ateş etme komutlarınızı kareler (frame) arasındaki milisaniyelerde kaydeder. Bu nedenle, yüksek ve dalgalanmayan bir FPS değeri, sub-tick sisteminin sunucuya gönderdiği verilerin hassasiyetini doğrudan artırır.

---

## En İyi CS2 Görüntü (Video) Ayarları

Oyun içi grafik ayarları, rekabetçi avantajı kaybetmeden performansı maksimize edecek şekilde yapılandırılmalıdır. Aşağıdaki tabloda, her ayarın teknik açıklaması ve önerilen değeri yer almaktadır.

| Ayar | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır (Boost Player Contrast)** | **Etkin (Enabled)** | Karakter modellerinin arka plandan ayrışmasını sağlar, piksel bazlı tespiti kolaylaştırır. CPU'ya çok az yük bindirir. |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı (Disabled)** | V-Sync, kareleri monitör yenileme hızıyla senkronize ederek ciddi bir girdi gecikmesine (input lag) yol açar. |
| **Çoklu Örneklemeli Kenar Yumuşatma Modu** | **4x MSAA** | Kenar kırılmalarını önler. 2x MSAA pikselleşmeye neden olurken, 8x MSAA gereksiz GPU yükü yaratır. 4x MSAA en dengeli seçenektir. |
| **Evrensel Gölge Kalitesi (Global Shadow Quality)** | **Yüksek (High)** | **Kritik Ayar:** Düşük gölge kalitesi, rakiplerin gölgelerini görmenizi engeller. Rekabetçi avantaj için en az "Orta" veya "Yüksek" olmalıdır. |
| **Model / Doku Detayı** | **Düşük (Low)** | VRAM kullanımını azaltır ve doku yükleme kaynaklı anlık takılmaları (stuttering) önler. |
| **Doku Filtreleme Modu** | **Eşyönsüz 4x (Anisotropic 4x)** | Performans kaybı yaratmadan uzak mesafedeki zemin dokularının net görünmesini sağlar. |
| **Parçacık Detayı (Particle Detail)** | **Düşük (Low)** | El bombası patlamaları ve molotof alevlerinin yarattığı FPS düşüşlerini (frame drop) minimize eder. |
| **Karakter Detayı (Ambient Occlusion)** | **Devre Dışı (Disabled)** | Köşelerdeki gölgelendirmeleri kapatarak karanlık alanlardaki düşmanların daha net görünmesini sağlar ve FPS artırır. |
| **Yüksek Dinamik Aralık (HDR)** | **Performans (Performance)** | Renk doğruluğundan ödün vermeden ışık patlamalarının GPU üzerindeki yükünü azaltır. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Disabled - Ultra Quality)** | FSR, görüntüyü upscale ederek çamurlaşmaya ve piksel titremelerine yol açar. Sadece çok düşük donanımlarda açılmalıdır. |
| **NVIDIA Reflex Düşük Gecikme** | **Etkin + Takviye (Enabled + Boost)** | GPU kuyruğunu temizleyerek girdi gecikmesini en aza indirir. CPU limitli senaryolarda işlemci frekansını yüksek tutar. |

### Çözünürlük ve En-Boy Oranı (Aspect Ratio)
*   **4:3 Stretched (Örn: 1280x960 veya 1440x1080):** Profesyonel oyuncuların %90'ı bu modu tercih eder. Karakter modelleri yatay olarak genişler ve hedef almayı kolaylaştırır. Ayrıca çizilen piksel sayısı azaldığı için FPS önemli ölçüde artar.
*   **16:9 Native (Örn: 1920x1080):** Daha geniş bir görüş açısı (FOV) sunar ve görüntü netliğini maksimuma çıkarır. Güçlü GPU'ya sahip sistemler için önerilir.

---

## NVIDIA ve AMD Ekran Kartı Denetim Masası Ayarları

Sürücü seviyesinde yapılan optimizasyonlar, oyun içi ayarlardan bağımsız olarak kare sürekliliğini (frame pacing) iyileştirir.

### NVIDIA Denetim Masası Optimizasyonu
1.  Masaüstüne sağ tıklayın ve **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3.  Aşağıdaki ayarları uygulayın:
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık (İşlemcinin çoklu çekirdek desteğini CS2 için etkinleştirir).
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık (NVIDIA Reflex oyun içinde aktifse bu ayar oyun tarafından yönetilir, ancak sürücü seviyesinde de aktif kalması önerilir).
    *   **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** Sınırsız (Unlimited) veya 10GB (CS2'de harita yüklenirken oluşan anlık takılmaları/stuttering tamamen engeller).
    *   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
    *   **Doku Süzme - Kalite:** Yüksek Performans.

### AMD Radeon Software Optimizasyonu
1.  **AMD Software: Adrenalin Edition** uygulamasını açın.
2.  **Oyun (Gaming) > Ekran Kartları (Graphics)** sekmesine gelin.
3.  Aşağıdaki özellikleri yapılandırın:
    *   **Radeon Anti-Lag:** Etkin (Girdi gecikmesini azaltır).
    *   **Radeon Image Sharpening:** Etkin (%10-20 arası bir değer netliği artırır).
    *   **Doku Filtreleme Kalitesi (Texture Filtering Quality):** Performans.

---

## Windows ve Başlatma Seçenekleri (Launch Options)

İşletim sistemi seviyesindeki arka plan işlemlerini sınırlamak, CS2'nin donanım kaynaklarına doğrudan erişmesini sağlar.

### En İyi CS2 Başlatma Seçenekleri Kodları
Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kısmına aşağıdaki kodları ekleyin:

```text
-novid -high -threads 9 -nojoy +cl_updaterate 128 +cl_interp_ratio 1 +cl_interp 0.015625
```

*   `-novid`: Giriş videosunu atlayarak oyunun daha hızlı açılmasını sağlar.
*   `-high`: Windows'un işlemci önceliğini CS2 işlemine (process) vermesini sağlar.
*   `-threads [Çekirdek Sayısı + 1]`: CS2'nin işlemcinizin fiziksel çekirdeklerini doğru şekilde kullanmasını zorlar (Örn: 8 çekirdekli bir işlemci için `-threads 9` yazılmalıdır).
*   `-nojoy`: Joystick desteğini kapatarak RAM ve CPU üzerindeki gereksiz yükü kaldırır.

### Windows Grafik ve Güç Ayarları
1.  **Grafik Ayarları (Graphics Settings):** Windows arama çubuğuna "Grafik Ayarları" yazın. **Donanım hızlandırmalı GPU zamanlaması (HAGS)** seçeneğini aktif hale getirin. Aşağıdan CS2.exe'yi seçip "Yüksek Performans" olarak ayarlayın.
2.  **Nihai Performans Modu:** Komut İstemi'ni (CMD) yönetici olarak açın ve şu kodu yapıştırarak en agresif güç planını etkinleştirin:
    ```cmd
    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
    ```
    Ardından Denetim Masası > Güç Seçenekleri altından **Nihai Performans**'ı seçin.