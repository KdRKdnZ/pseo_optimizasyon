---
title: "cyberpunk 2077 en iyi ayarlar"
description: "cyberpunk 2077 en iyi ayarlar hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Cyberpunk 2077 En İyi Grafik Ayarları ve FPS Optimizasyon Rehberi (v2.0+)

Cyberpunk 2077, 2.0 güncellemesi ve Phantom Liberty genişlemesi ile birlikte grafik motorunu ve sistem gereksinimlerini ciddi oranda güncelledi. Bu rehber, görsel kaliteden minimum düzeyde ödün vererek **en yüksek FPS değerini** elde etmenizi sağlayan teknik optimizasyon ayarlarını içermektedir.

---

## 1. Temel Optimizasyon ve Ön Hazırlıklar

Grafik ayarlarını değiştirmeden önce sistem seviyesinde şu adımların tamamlanması gerekir:

*   **Sürücü Güncellemesi:** NVIDIA (GeForce Game Ready 537.34 veya üzeri) / AMD (Adrenalin 23.9.2 veya üzeri) sürücülerini yükleyin.
*   **Depolama:** Oyunu mutlaka bir **NVMe M.2 SSD** üzerine kurun. HDD kullanımı, 2.0 sürümüyle birlikte kaplama gecikmelerine (texture pop-in) ve anlık takılmalara (stuttering) yol açmaktadır.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Windows ayarlarından bu özelliği açın (NVIDIA DLSS Frame Generation için zorunludur).

---

## 2. En İyi Grafik Ayarları (Sweet Spot / En Uygun Denge)

Aşağıdaki ayarlar, "Ultra" preset'e kıyasla görsel kalitede yalnızca %5 ila %8 arasında belirsiz bir kayıp oluştururken **%40 ila %60 arasında FPS artışı** sağlar.

### Genişletilmiş (Oynanış ve Sistem)
*   **Kalabalık Yoğunluğu (Crowd Density):** Orta *(Yüksek işlemci yükünü azaltır, şehir canlılığını korur).*
*   **Alan Derinliği (Depth of Field):** Açık (Kişisel tercih, FPS'e etkisi yok).
*   **Hareket Bulanıklığı (Motion Blur):** Kapalı (Görüntü netliğini artırır, mikro takılma hissini azaltır).
*   **Kromatik Sapma (Chromatic Aberration):** Kapalı.
*   **Göz Kamşatması (Lens Flare):** Açık.

### Grafik (Temel Yüzey ve Işıklandırma)
*   **Yüzey Altı Saçılımı Kalitesi (Subsurface Scattering Quality):** Yüksek *(Karakter ten kalitesini artırır, performansa etkisi %1'den azdır).*
*   **Alan Derinliği Kalitesi (Field of View):** 80 - 90 arası.
*   **Anizotropik Süzme (Anisotropic Filtering):** 16x *(Modern GPU'larda performans kaybı yaratmaz, uzak kaplamaları netleştirir).*
*   **Kademeli Gölge Çözünürlüğü (Cascaded Shadows Resolution):** Orta *(Performansa etkisi en yüksek gölge ayarıdır; Ultra ile Orta arasındaki FPS farkı %10-12'dir).*
*   **Uzak Gölgeler Çözünürlüğü (Distant Shadows Resolution):** Yüksek.
*   **Hacimsel Sis Kalitesi (Volumetric Fog Resolution):** Orta *(Sistem kaynaklarını en çok tüketen ayarlardan biridir. Ultra'dan Orta'ya çekmek %15 FPS kazandırır).*
*   **Hacimsel Bulutlar Kalitesi (Volumetric Clouds Quality):** Orta.
*   **Maksimum Dinamik Decal (Max Dynamic Decals):** Yüksek.
*   **Ekran Alanı Yansımaları Kalitesi (Screen Space Reflections):** Düşük veya Orta *(Ultra modu ekran kartını aşırı zorlar. Ray Tracing kapalıysa 'Düşük' getirdiği performans artışı nedeniyle önerilir).*
*   **Subsurface Scattering:** Yüksek.
*   **Ortam Kapatma (Ambient Occlusion):** Düşük veya Orta *(Gölgelerin derinliğini belirler, 'Düşük' seviye %6-8 FPS kazandırır).*
*   **Renk Hassasiyeti (Color Precision):** Yüksek.
*   **Ayna Kalitesi (Mirror Quality):** Orta.
*   **Anizotropik Doku Süzme (Texture Detail):** Yüksek *(VRAM'iniz 6GB ve üzeriyse kesinlikle Yüksek tutun).*

---

## 3. Ray Tracing (Işın İzleme) ve Path Tracing Optimizasyonu

Işın İzleme, Cyberpunk 2077'de görsel devrim yaratsa da maliyeti çok yüksektir. 

| Ayar | Önerilen Konum | Açıklama |
| :--- | :--- | :--- |
| **Ray Tracing (Genel Switch)** | Açık / Kapalı | RTX 3070 / RX 6800 XT altındaki kartlar için **Kapalı** tutulmalıdır. |
| **RT Yansımalar (Reflections)** | Açık | Görsel etki/performans oranı en dengeli RT ayarıdır. |
| **RT Gölge (Shadows)** | Kapalı | Görsel fark düşüktür, FPS kaybı yüksektir. |
| **RT Aydınlatma (Lighting)** | Orta | Şehir atmosferini tamamen değiştirir. 'Ultra' yerine 'Orta' seçilmelidir. |
| **Path Tracing (Full RT)** | Kapalı | Yalnızca RTX 4070 Ti ve üzeri kartlarda DLSS 3.5 ile kullanılmalıdır. |

---

## 4. Ölçeklendirme Teknolojileri (DLSS, FSR, XeSS)

Cyberpunk 2077, yapay zeka ölçeklendirmesi olmadan yüksek çözünürlüklerde (1440p/4K) akıcı oynaması zor bir oyundur.

### NVIDIA Kullanıcıları
*   **Çözünürlük Ölçekleme:** DLSS Super Resolution
*   **DLSS Modu:** 
    *   1080p için: **Kalite (Quality)**
    *   1440p için: **Kalite (Quality)** veya **Dengeli (Balanced)**
    *   4K için: **Performans (Performance)**
*   **DLSS Frame Generation:** Açık *(Yalnızca RTX 40 serisi kartlarda mevcuttur. FPS'i neredeyse ikiye katlar).*
*   **DLSS Ray Reconstruction (DLSS 3.5):** Açık *(Ray Tracing açıksa netliği artırır ve gürültüyü temizler).*

### AMD Kullanıcıları
*   **Çözünürlük Ölçekleme:** AMD FSR 2.1 (Veya FSR 3 Modları)
*   **FSR Modu:** 1080p/1440p için **Kalite (Quality)**.

---

## 5. Donanım Segmentine Göre Hızlı Reçete

### Giriş Seviyesi (GTX 1660 Super, RTX 3050, RX 6600 - 1080p)
*   **Preset:** Orta (Medium)
*   **Hacimsel Sis:** Düşük
*   **Ekran Alanı Yansımaları:** Kapalı / Düşük
*   **DLSS/FSR:** Kalite Modu
*   **Hedef FPS:** 50 - 65 FPS

### Orta Seviye (RTX 3060 Ti, RTX 4060, RX 6700 XT - 1080p / 1440p)
*   **Preset:** Yukarıdaki "Sweet Spot" Rehberi
*   **Ray Tracing:** Kapalı
*   **DLSS/FSR:** Kalite Modu
*   **Hedef FPS:** 75 - 90 FPS

### Üst Seviye (RTX 4070 Ti, RTX 4080, RX 7900 XTX - 1440p / 4K)
*   **Preset:** Yüksek / Ultra
*   **Ray Tracing:** Açık (Yansımalar Açık, Aydınlatma Orta)
*   **DLSS:** Kalite + Frame Generation Açık
*   **Hedef FPS:** 100+ FPS