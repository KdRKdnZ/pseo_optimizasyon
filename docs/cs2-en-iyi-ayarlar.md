---
title: "cs2 en iyi ayarlar"
description: "cs2 en iyi ayarlar hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 En İyi Ayarlar: Maksimum FPS, Düşük Gecikme ve Optimum Görüş Rehberi

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği yeni dinamikler, geliştirilmiş ışıklandırma ve yenilenmiş alt adımlı (sub-tick) mimari ile yüksek sistem kaynakları talep eden bir yapıya sahiptir. Rekabetçi avantaj elde etmek; yüksek kare hızına (FPS), minimum girdi gecikmesine (input lag) ve net düşman görünürlüğüne dayanır. 

Bu rehber, CS2'deki grafik, ses, oyun içi ve başlatma seçeneklerini teknik detaylarıyla optimize etmeniz için hazırlanmıştır.

---

## 1. Temel Video Ayarları (Display Settings)

Ekran ayarları, sisteminizin monitörünüzle olan iletişimini ve işleme çözünürlüğünü doğrudan etkiler.

*   **Ekran Modu (Display Mode):** `Tam Ekran (Fullscreen)`
    *   *Teknik Neden:* Pencereli modlar Windows Masaüstü Pencere Yöneticisi'ni (DWM) araya sokarak girdi gecikmesini artırır. Tam Ekran, GPU'nun doğrudan oyuna odaklanmasını sağlar.
*   **Çözünürlük (Resolution):** `1280x960` veya `1440x1080` (4:3 Stretched) veya `1920x1080` (16:9)
    *   *Teknik Neden:* 4:3 genişletilmiş (stretched) oran, oyuncu modellerini yatayda genleştererek hedef almayı görsel olarak kolaylaştırır ve piksel sayısını düşürdüğü için FPS artışı sağlar. 16:9 ise daha geniş bir görüş alanı (FOV) sunar.
*   **Yenileme Hızı (Refresh Rate):** `Maksimum (Örn: 144Hz, 240Hz, 360Hz)`
    *   Monitörünüzün desteklediği en yüksek değeri seçin.
*   **Görüntü Tasarrufu (Laptop Power Saving):** `Devre Dışı (Disabled)`

---

## 2. Gelişmiş Video Ayarları (Advanced Video Settings)

Grafik ayarlarındaki temel amaç, gereksiz görsel efektleri kapatıp rakip görünürlüğünü ve gölge avantajını maksimuma çıkarmaktır.

| Ayar | Tavsiye Edilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Görünürlüğü** | **Etkin (Enabled)** | Karanlık arka planlardaki oyuncu modellerinin etrafına hafif bir kontrast efekti ekler. Reaksiyon süresini doğrudan iyileştirir. |
| **Çoklu Örneklemeli Kenar Yumuşatma** | **4x MSAA** veya **2x MSAA** | CS2'de "Devre Dışı" (No AA) veya FXAA seçeneği kenarlarda şiddetli tırtıklanmaya yol açar. 4x MSAA, piksel netliğini korurken performansı dengeler. |
| **Küresel Gölge Kalitesi** | **Yüksek (High)** veya **Orta (Medium)** | CS2'de rakiplerin gölgeleri kilit öneme sahiptir. "Düşük" seviyede gölge mesafesi azalır. Yüksek/Orta seviye, duvar arkasından yaklaşan düşmanın gölgesini önceden görmenizi sağlar. |
| **Model / Doku Kalitesi** | **Düşük (Low)** veya **Orta (Medium)** | GPU belleğini (VRAM) rahatlatır, piksel işleme yükünü düşürür. |
| **Doku Filtreleme Modu** | **Eşyönsüz 4x (Anisotropic 4x)** | Performansa etkisi ihmal edilebilir düzeydedir. Eğik açılardan bakıldığında dokuların net kalmasını sağlar. |
| **Efekt Detayı** | **Düşük (Low)** | Molotof patlamaları ve sis kenarlarındaki kare hızı düşüşlerini (FPS drop) engeller. |
| **Kaplama Detayı (Shader)** | **Düşük (Low)** | Yüzeylerdeki gereksiz yansımaları kapatır, göz yorgunluğunu azaltır ve FPS artırır. |
| **Parçacık Detayı** | **Düşük (Low)** | Kan ve patlama parçacıklarının sistem yükünü azaltır. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı (Disabled)** | Köşe birleşim yerlerine derinlik gölgesi ekler. Rekabetçi oyunda düşman tespitini zorlaştırır ve FPS düşürür. |
| **Yüksek Dinamik Aralık (HDR)** | **Performans (Performance)** | Işık geçişlerindeki işleme yükünü azaltır, görsel kalite kaybı minimumdur. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (En Yüksek Kalite)** | FSR, görüntüyü düşük çözünürlükte işleyip ölçeklendirir. Bu durum CS2'de aşırı bulanıklığa ve gecikmeye sebep olur. |
| **NVIDIA Reflex Low Latency** | **Etkin + Boost (Enabled + Boost)** | GPU saat hızlarını yüksek tutarak sistem gecikmesini (system latency) en alt seviyeye çeker. CPU sınırına takılan durumlarda gecikmeyi ciddi oranda düşürür. |

---

## 3. Ses Ayarları (Audio Settings)

CS2'deki yenilenmiş ses motoru, sesin çıktığı yönü ve mesafesini tespit etmeyi kritik hale getirmiştir.

*   **Master Volume:** Kişisel tercih (Genelde %60 - %100).
*   **Audio EQ Profile:** `Crisp` (Gevrek) veya `Natural` (Doğal)
    *   *Crisp:* Yüksek frekansları (ayak sesleri, şarjör değiştirme) öne çıkarır.
*   **L/R Isolation (Sol/Sağ İzolasyonu):** `%50 - %70`
    *   Değer %0'a yakın olduğunda sesler daha birleşik gelir. %100'e yaklaştığında sol ve sağ ayrımı keskinleşir ancak merkeze gelen seslerin takibi zorlaşabilir. %50-70 arası ideal mekânsal algı sunar.
*   **Perspective Correction (Perspektif Düzeltme):** `Evet (Yes)`
    *   Seslerin oyuncunun baktığı açıya (FOV) göre dinamik olarak konumlandırılmasını sağlar.

---

## 4. Rekabetçi Oyun ve Görüş Alanı (Viewmodel) Ayarları

Görüş alanı (Viewmodel) ayarları, silahın ekranda kapladığı alanı küçülterek sağ ve alt kör noktaları minimuma indirmeyi amaçlar.

Geliştirici konsoluna (`~`) aşağıdaki komutları girerek optimum görüş alanını sağlayabilirsiniz:

```gdb
cl_crosshair_friendly_warning 0
viewmodel_fov 68
viewmodel_offset_x 2.5
viewmodel_offset_y 0
viewmodel_offset_z -1.5
viewmodel_presetpos 0
```

---

## 5. CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizde CS2'ye sağ tıklayıp *Özellikler > Genel > Başlatma Seçenekleri* alanına eklenebilecek güncel ve kararlı komutlar:

```text
-nojoy -high -freq [MonitörHz] +exec autoexec.cfg
```

*   `-nojoy`: Joypad/Controller desteğini kapatır, VRAM ve RAM yükünü hafifletir.
*   `-high`: İşlemci önceliğini CS2'ye verir (Sistemde kararsızlık yaratırsa kaldırılmalıdır).
*   `-freq 240`: Monitörün yenileme hızını doğrudan oyuna zorlar (Kendi Hz değerinizi yazın).

*(Not: CS:GO döneminden kalma `-threads`, `-nod3d9ex`, `-novid` gibi komutlar CS2 Source 2 motorunda işlevsizdir veya performans sorunlarına yol açabilir.)*

---

## 6. Windows ve Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları:
1. **Görüntü Ayarlarını Önayarla Yap:** *Benim tercihlerimi kullan ve şunlara önem ver:* **Performans**.
2. **3D Ayarlarının Yönetilmesi:**
   * **Güç Yönetimi Modu:** `Maksimum performansı tercih et`
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** `Açık (On)` veya `Ultra`
   * **Doku Süzme - Kalite:** `Yüksek Performans`
   * **Dikey Eşitleme (V-Sync):** `Kapat`

### Windows Ayarları:
* **Oyun Modu (Game Mode):** `Açık` (Windows kaynaklarını oyuna önceliklendirir).
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Açık` (Girdi gecikmesini düşürür).
* **Tam Ekran İyileştirmelerini Devre Dışı Bırak:** CS2.exe dosyasına sağ tıklayıp *Uyumluluk* sekmesinden bu seçeneği işaretleyin.

---

## Özet Performans Kontrol Listesi

1. **FPS sabitlemeyin** (`fps_max 0` komutunu kullanın veya ekran kartınızın sınırlarına göre `fps_max [Hz * 2]` yapın).
2. Oyunu mutlaka **NVMe SSD** üzerine kurun (Source 2 kaplama yüklemeleri için yüksek okuma hızı gerektirir).
3. **NVIDIA Reflex / AMD Anti-Lag** teknolojilerini mutlaka aktif tutun.
4. Gölge kalitesini asla **Düşük** seviyeye çekmeyin (Taktiksel avantaj kaybı).