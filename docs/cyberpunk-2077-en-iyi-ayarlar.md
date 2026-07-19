---
title: cyberpunk 2077 en iyi ayarlar
description: cyberpunk 2077 en iyi ayarlar hakkında detaylı optimizasyon ve donanım rehberi.
---

# Cyberpunk 2077 En İyi Ayarlar: Performans ve Görsel Kalite Rehberi

Cyberpunk 2077, REDengine 4 oyun motorunun sınırlarını zorlayan, DirectX 12 Ultimate API'si üzerine inşa edilmiş, hem CPU hem de GPU sınırlarını sonuna kadar kullanan bir yapımdır. Bu rehberde, donanım kaynaklarınızı en verimli şekilde kullanarak görsel kaliteden minimum ödünle maksimum FPS elde etmenizi sağlayacak **Cyberpunk 2077 en iyi ayarlar** optimizasyonunu teknik detaylarıyla ele alacağız.

---

## Donanım Mimarisi ve REDengine 4 İlişkisi

REDengine 4, asenkron hesaplama (asynchronous compute) ve çoklu iş parçacığı (multi-threading) mimarisini yoğun şekilde kullanır. Bu nedenle, grafik ayarlarını optimize etmeden önce oyunun donanım bileşenlerinizle nasıl etkileşime girdiğini anlamak kritik önem taşır.

### CPU Darboğazını Önleme ve SMT Ayarları

Cyberpunk 2077, özellikle kalabalık şehir merkezlerinde (örneğin Kabuki veya Corpo Plaza) işlemciye aşırı yük bindirir. 

*   **AMD SMT (Simultaneous Multithreading):** Oyunun eski sürümlerinde yaşanan AMD işlemcilerdeki SMT optimizasyon sorunu 2.0+ güncellemeleriyle büyük oranda çözülmüştür. Ancak yine de oyun içi ayarlardan **Oynanış > Performans > AMD SMT** seçeneğini **Otomatik** veya **Açık** konumuna getirmek, 6 ve 8 çekirdekli Ryzen işlemcilerde %10'a varan minimum FPS (1% Low) artışı sağlar.
*   **Intel E-Cores (Verimlilik Çekirdekleri):** Hibrit mimarili Intel işlemcilerde (12, 13 ve 14. nesil), arka plan işlemlerinin P-çekirdeklerini (Performans) işgal etmesini önlemek için Windows Oyun Modu'nun açık olduğundan emin olun.

### VRAM Yönetimi ve Doku Kalitesi

Doku Kalitesi (Texture Quality), ekran kartınızın VRAM (Video RAM) kapasitesiyle doğrudan ilişkilidir ve bu ayar **yalnızca ana menüdeyken** değiştirilebilir.

*   **8 GB VRAM ve Altı:** 1080p çözünürlükte **Orta (Medium)**, Ray Tracing kapalı ise **Yüksek (High)**.
*   **10 GB - 12 GB VRAM:** 1440p çözünürlükte **Yüksek (High)**.
*   **16 GB VRAM ve Üstü:** 4K çözünürlük dahil tüm senaryolarda **Yüksek (High)**.

*Not: VRAM sınırının aşılması, anlık takılmalara (stuttering) ve FPS'in aniden yarı yarıya düşmesine neden olur.*

---

## En Yüksek FPS İçin Grafik Ayarları Optimizasyonu

Aşağıdaki tabloda, görsel etki ve performans maliyeti analiz edilerek belirlenmiş optimum ayarlar listelenmiştir.

| Grafik Ayarı | Performans Etkisi | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- | :--- |
| **Ekran Alanı Yansımaları (SSR)** | Çok Yüksek (%12-15) | **Düşük** veya **Orta** | "Ultra" ve "Psycho" modları ışın izleme olmadan yansıma kalitesini artırır ancak GPU'yu aşırı yorar. |
| **Hacimsel Sis Çözünürlüğü** | Yüksek (%10-12) | **Orta** | Işık süzmeleri ve sis kalitesini belirler. Yüksek ile Orta arasındaki görsel fark minimaldir, performans kazancı büyüktür. |
| **Kademeli Gölgeler Çözünürlüğü** | Orta (%6-8) | **Orta** | Uzaktaki gölgelerin keskinliğini ayarlar. Performans/görsel denge noktası Orta'dır. |
| **Kalabalık Yoğunluğu** | Yüksek (CPU Bağlı) | **Orta** | CPU darboğazını engellemek için en kritik ayardır. Yüksek ayar, işlemciyi felç edebilir. |
| **Alan Derinliği (DoF)** | Düşük (%2) | **Kapalı** | Kişisel tercihe bağlıdır ancak kapatılması hem netliği artırır hem de ufak bir performans kazandırır. |
| **Hareket Bulanıklığı (Motion Blur)** | Düşük (%1-2) | **Kapalı** | Hızlı dönüşlerde görüntü netliğini bozduğu için kapatılması önerilir. |

### Performansı En Çok Etkileyen Kritik Ayarlar

1.  **Ekran Alanı Yansımaları (Screen Space Reflections - SSR):** Bu ayar, ıslak sokaklardaki ve metalik yüzeylerdeki yansımaların kalitesini belirler. "Psycho" seçeneği, Ray Tracing'e yakın bir yük bindirir. En dengeli ayar **Orta (Medium)** seviyesidir.
2.  **Hacimsel Sis Çözünürlüğü (Volumetric Fog Resolution):** Gece lambalarının ve neon ışıkların havada süzülme efektini kontrol eder. "Ultra" seviyesinden "Medium" seviyesine geçiş, görsel kalitede %5 kayba karşılık **%10 FPS artışı** sağlar.

### Görsel Kaliteden Ödün Vermeden Kısılabilecek Ayarlar

*   **Alt Yüzey Dağılımı (Subsurface Scattering):** Karakterlerin cilt dokusunun ışığı geçirme miktarını ayarlar. **Yüksek** seviyede tutulmalıdır; performansa etkisi %1'den azdır ancak yüz detaylarını ciddi oranda iyileştirir.
*   **Anizotropik Filtreleme (Anisotropic Filtering):** Dokuların açılı bakıldığında net görünmesini sağlar. Günümüz GPU'larında performansa etkisi yok denecek kadar azdır. Doğrudan **16x** olarak ayarlanmalıdır.

---

## Ray Tracing ve Path Tracing: Ne Zaman Açılmalı?

Cyberpunk 2077, ışın izleme teknolojisinin en gelişmiş uygulandığı oyunlardan biridir. Ancak bu teknolojinin donanım maliyeti oldukça yüksektir.

```
[Standart Rasterizasyon] ---> %100 Performans (Referans)
[Ray Tracing: Orta]      ---> %50-60 Performans Kaybı
[Ray Tracing: Ultra]     ---> %70 Performans Kaybı
[Path Tracing (Overdrive)]--> %120+ Performans Kaybı (Yapay Zeka Desteği Şart)
```

*   **Ray Tracing (Işın İzleme):** Yalnızca **RTX 3070 Ti / RX 6800 XT** ve üzeri kartlarda, çözünürlük ölçekleme (DLSS/FSR) açıkken aktifleştirilmelidir. Sadece **RT Yansımaları** ve **RT Aydınlatma (Orta)** açılması, en optimum görsel/performans dengesini sunar.
*   **Path Tracing (Işın İzleme: Overdrive):** Bu mod, sahnedeki tüm ışık kaynaklarını fiziksel olarak doğru simüle eder. **RTX 40 serisi** (DLSS 3 Frame Generation destekli) bir ekran kartınız yoksa oynanabilir kare hızları elde etmek mümkün değildir.

### DLSS, FSR ve XeSS Yapılandırması

Yapay zeka tabanlı çözünürlük ölçekleme teknolojileri, Cyberpunk 2077'de akıcı bir deneyim için zorunludur.

*   **NVIDIA DLSS (Deep Learning Super Sampling):** RTX kart sahipleri için en iyi seçenektir. 1080p için **Kalite (Quality)**, 1440p için **Kalite** veya **Dengeli (Balanced)**, 4K için **Performans (Performance)** modu seçilmelidir.
*   **DLSS Ray Reconstruction (Işın Yeniden Yapılandırma - DLSS 3.5):** Eğer Ray Tracing veya Path Tracing kullanıyorsanız, bu ayarı kesinlikle **Açık** konuma getirin. Görüntüdeki gürültüyü (noise) azaltır ve netliği artırır.
*   **AMD FSR 2.1 / 3.0:** AMD ve GTX serisi kartlar için alternatiftir. FSR keskinlik ayarını **0.2 - 0.4** arasında tutmak, karıncalanma efektini (shimmering) minimuma indirir.

---

## Sistem Segmentlerine Göre Hazır Profil Önerileri

### Giriş Seviyesi Sistemler (GTX 1660 / RX 580 ve Dengi)
*   **Hedef:** 1080p / 45-60 FPS
*   **Çözünürlük Ölçekleme:** FSR 2.1 (Dengeli)
*   **Doku Kalitesi:** Orta
*   **Ekran Alanı Yansımaları (SSR):** Düşük veya Kapalı
*   **Hacimsel Sis Çözünürlüğü:** Düşük
*   **Kalabalık Yoğunluğu:** Düşük

### Orta Seviye Sistemler (RTX 3060 / RX 6700 XT ve Dengi)
*   **Hedef:** 1080p Ultra veya 1440p / 60+ FPS
*   **Çözünürlük Ölçekleme:** DLSS / FSR (Kalite)
*   **Doku Kalitesi:** Yüksek
*   **Ekran Alanı Yansımaları (SSR):** Orta
*   **Hacimsel Sis Çözünürlüğü:** Orta
*   **Kalabalık Yoğunluğu:** Orta
*   **Ray Tracing:** Kapalı

### Üst Seviye Sistemler (RTX 4070 / RX 7800 XT ve Üzeri)
*   **Hedef:** 1440p/4K / 90+ FPS (Ray Tracing Aktif)
*   **Çözünürlük Ölçekleme:** DLSS (Kalite) + Kare Oluşturma (Frame Generation) Açık
*   **Doku Kalitesi:** Yüksek
*   **Ray Tracing:** Açık (Yansımalar: Açık, Aydınlatma: Ultra)
*   **Ekran Alanı Yansımaları (SSR):** Ultra (RT kapalıysa) veya RT Yansımaları aktifse devre dışı
*   **Kalabalık Yoğunluğu:** Yüksek

---

## Sonuç ve İnce Ayar Kontrol Listesi

Cyberpunk 2077'de en iyi performansı elde etmek için grafik ayarlarını değiştirdikten sonra şu adımları kontrol edin:

1.  **Windows Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Ayarlar > Sistem > Monitör > Grafik bölümünden bu ayarı açın. Özellikle DLSS Frame Generation için bu ayar zorunludur.
2.  **Sanal Bellek (Pagefile) Boyutu:** Oyunun çökmesini önlemek için Windows'un kurulu olduğu SSD'de en az 16 GB sanal bellek ayrıldığından emin olun.
3.  **HDD Modu:** Oyunu kesinlikle bir **SATA veya NVMe SSD** üzerine kurun. Eğer HDD kullanmak zorundaysanız, oyun içi ayarlardan **HDD Modu** seçeneğini **Açık** konuma getirin.