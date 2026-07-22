# Cyberpunk 2077 En İyi Grafik Ayarları ve Optimizasyon Rehberi

Cyberpunk 2077, 2.0 güncellemesi ve *Phantom Liberty* genişleme paketi ile birlikte donanım gereksinimlerini önemli ölçüde artırdı. REDengine 4 motorunun sınırlarını zorlayan oyunda yüksek FPS ve yüksek görsel kaliteyi aynı anda yakalamak, doğru konfigürasyonla mümkündür.

Bu rehber; işlemci (CPU), ekran kartı (GPU) ve VRAM kullanımını optimize ederek sisteminizden maksimum performans almanızı sağlayacak teknik ayarları içerir.

---

## 1. Görselliğe Etkisi Düşük, Performans Maliyeti Yüksek Ayarlar

Aşağıdaki ayarlar, kapatıldığında veya düşürüldüğünde görsellikte minimal kayıp yaşatırken **FPS değerini %30 ila %45 oranında artırır**.

*   **Volumetric Fog Resolution (Hacimsel Sis Çözünürlüğü):** *Orta (Medium)*
    *   *Teknik Neden:* Ultra seviyesi, ekran kartının gölgelendirme birimlerine (Shaders) aşırı yük bindirir. *Orta* seviye, sis kalitesini bozmadan ciddi bir FPS artışı sağlar.
*   **Volumetric Clouds Quality (Hacimsel Bulut Kalitesi):** *Orta (Medium)*
    *   *Teknik Neden:* Gökyüzü render maliyetini düşürür. Oyun içi dinamik havada farkı anlamak zordur.
*   **Screen Space Reflections Quality (Ekran Alanı Yansımaları Kalitesi):** *Düşük (Low) veya Orta (Medium)*
    *   *Teknik Neden:* Ray Tracing kapalıysa en çok GPU tüketen ayardır. *Ultra* ayarında ciddi "noise" (karıncalanma) ve performans düşüşü yaşanır. *Orta* seviye en ideal dengedir.
*   **Cascaded Shadows Resolution (Kademeli Gölge Çözünürlüğü):** *Orta (Medium)*
    *   *Teknik Neden:* Uzaktaki nesnelerin gölge netliğini belirler. *Ultra* yerine *Orta* kullanmak VRAM ve GPU kullanımını rahatlatır.
*   **Crowd Density (Kalabalık Yoğunluğu):** *Düşük (Low) veya Orta (Medium)*
    *   *Teknik Neden:* **Tamamen İşlemci (CPU) odaklıdır.** Night City merkezinde ve Dogtown bölgesinde yaşanan ani FPS düşüşlerinin (stuttering) birincil sebebidir. Güçlü bir işlemciniz (örn. Ryzen 7800X3D veya i7-13700K) yoksa *Orta* veya *Düşük* seçilmelidir.

---

## 2. Detaylı Grafik Ayarları Konfigürasyon Listesi

Oyun içi menüde yer alan tüm ayarlar için önerilen "En Optimal" değerler:

| Grafik Ayarı | Önerilen Seviye | Performans Etkisi |
| :--- | :--- | :--- |
| **Field of View (FOV)** | 80 - 90 | Düşük-Orta |
| **Anisotropy (Doku Süzme)** | 16x | Çok Düşük (Her sistemde 16x olmalı) |
| **Local Shadow Mesh Quality** | High (Yüksek) | Düşük |
| **Local Shadow Quality** | Medium (Orta) | Orta |
| **Cascaded Shadows Range** | Medium (Orta) | Orta |
| **Distant Shadows Resolution** | High (Yüksek) | Düşük |
| **Volumetric Fog Resolution** | Medium (Orta) | **Yüksek** |
| **Volumetric Clouds Quality** | Medium (Orta) | Orta |
| **Max Dynamic Decals** | Ultra | Düşük |
| **Screen Space Reflections Quality** | Low / Medium | **Çok Yüksek** |
| **Subsurface Scattering Quality** | High (Yüksek) | Düşük (Yüz kalitesi için önemli) |
| **Ambient Occlusion** | Low / Medium | Orta |
| **Color Precision** | Medium (Orta) | Düşük |
| **Chromatically Aberration** | Kapalı (Off) | Kişisel Tercih (Netliği artırır) |
| **Depth of Field (Derinlik Alanı)**| Kişisel Tercih | Sıfır |
| **Lens Flare** | Açık (On) | Sıfır |
| **Motion Blur (Hareket Bulanıklığı)**| Kapalı (Off) | Sıfır (Görüntü netliği için önerilir) |

---

## 3. Yapay Zeka Ölçeklendirme (Upscaling) ve Frame Generation

Cyberpunk 2077'yi yerel (native) çözünürlükte çalıştırmak yüksek kartlarda bile zordur. Bu nedenle güncel ölçeklendirme teknolojilerini kullanmak zorunluluktur.

### Nvidia RTX Kullanıcıları için:
*   **DLSS Super Resolution:** *Quality (Kalite)* veya *Balanced (Dengeli)*
    *   1080p için: **DLSS Kalite**
    *   1440p (2K) için: **DLSS Kalite**
    *   2160p (4K) için: **DLSS Dengeli** veya **Performans**
*   **DLSS Frame Generation (Sadece RTX 40 Serisi):** *Açık (On)*
    *   *Not:* Gecikmeyi azaltmak için **NVIDIA Reflex Low Latency** seçeneğini *On + Boost* konumuna getirin.
*   **DLSS Ray Reconstruction (DLSS 3.5):** *Açık (On)*
    *   Ray Tracing kullanıyorsanız kesinlikle açılmalıdır. Işık kırılmalarındaki kumlanmayı temizler ve performansı cüzi miktarda artırır.

### AMD RX Kullanıcıları için:
*   **FSR 2.1 / FSR 3:** *Quality (Kalite)*
    *   FSR, görüntüyü DLSS kadar keskin işleyemeyebilir. Oyun içi keskinleştirme (Sharpening) ayarını **0.35 ile 0.50** arasında tutmanız önerilir.

---

## 4. Ray Tracing (Işın İzleme) Optimizasyonu

Ray Tracing (RT), Cyberpunk 2077'nin görsel tepe noktasıdır ancak maliyeti son derece yüksektir.

*   **Giriş/Orta Seviye RT (RTX 3060, RTX 4060, RX 7700 XT):**
    *   Ray Tracing: *Açık*
    *   RT Reflections: *Kapalı*
    *   RT Sun Shadows: *Kapalı*
    *   **RT Lighting:** *Medium (Orta)*
    *(Bu kombinasyon performans kaybettirmeden en iyi atmosferi sunar.)*

*   **Üst Seviye RT (RTX 4070 Ti, RTX 4080, RTX 4090):**
    *   Tüm RT ayarları *Açık* veya **Path Tracing (Ray Tracing Overdrive)** modu active edilebilir.
    *   *Path Tracing kullanırken DLSS Frame Generation ve Ray Reconstruction açılması zorunludur.*

---

## 5. Donanım Segmentine Göre Hazır Profil Önerileri

### A. Bütçe Dostu / Eski Sistemler (1080p - 45-60 FPS)
*(GTX 1660 Super, RTX 2060, RX 6600, 6GB VRAM)*
*   **Çözünürlük Ölçekleme:** DLSS/FSR Kalite
*   **Grafik Profili:** Özel (Önerilen ayarlar tablosundaki Low/Medium dengesi)
*   **Crowd Density:** Low
*   **Ray Tracing:** Kapalı

### B. Dengeli Sistemler (1080p/1440p - 75-100 FPS)
*(RTX 3070, RTX 4060 Ti, RX 6700 XT, 8GB-12GB VRAM)*
*   **Çözünürlük Ölçekleme:** DLSS Kalite / FSR Kalite
*   **Grafik Profili:** High (Yüksek) temelli; *Volumetric Fog* ve *SSR* "Medium" seviyesinde.
*   **Crowd Density:** Medium
*   **Ray Tracing:** Sadece RT Lighting (Medium)

### C. Performans / Ultra Sistemler (1440p/4K - 100+ FPS)
*(RTX 4080, RTX 4090, RX 7900 XTX)*
*   **Çözünürlük Ölçekleme:** DLSS Kalite + Frame Generation
*   **Grafik Profili:** Ultra / Path Tracing
*   **Crowd Density:** High
*   **Ray Tracing:** Overdrive Mode (Path Tracing) + Ray Reconstruction

---

## 6. İşletim Sistemi ve Sürücü Düzeyinde Teknik Adımlar

1.  **SSD Kullanımı Zorunludur:** Oyun HDD üzerine kurulduğunda dokuların geç yüklenmesi (texture pop-in) ve takılmalar kaçınılmazdır. Oyun içi ayarlardan **Slow HDD Mode** ayarını yalnızca oyun NVMe SSD dışındaki yavaş bir diske kuruluysa açın.
2.  **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):**
    *   *Windows Ayarları > Grafik Ayarları > Donanım Hızlandırmalı GPU Zamanlaması'nı Açın.* (DLSS Frame Generation için gereklidir).
3.  **VRAM Limitini Aşmamak:** 8 GB VRAM'e sahip kartlarda 1440p çözünürlükte Ray Tracing açmak VRAM darboğazına (stuttering) yol açar. 8 GB VRAM sınırındaysanız Ray Tracing kapalı tutulmalıdır.