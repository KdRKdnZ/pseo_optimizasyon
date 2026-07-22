---
title: "valorant en iyi ayarlar"
description: "valorant en iyi ayarlar hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Valorant En İyi Ayarlar: Rekabetçi Grafik, FPS ve Hassasiyet Rehberi

Valorant gibi mikrosaniye düzeyindeki tepki sürelerinin kazananı belirlediği taktiksel FPS oyunlarında, sistem optimizasyonu ve doğru oyun içi ayarlar kritik önem taşır. Bu rehber; kare hızını (FPS) en üst düzeye çıkarmak, sistem girdi gecikmesini (input lag) minimize etmek ve görsel netliği artırmak için teknik olarak doğrulanmış en ideal Valorant ayarlarını içermektedir.

---

## 1. Temel Grafik ve Video Ayarları (Maksimum FPS ve Minimum Gecikme)

Valorant, Ekran Kartı (GPU) ağırlıklı olmaktan ziyade İşlemci (CPU) bağımlı bir oyundur. Grafik ayarlarını düşürmek, ekran kartı üzerindeki yükü azaltarak işlemcinin kareleri daha hızlı işlemesini sağlar.

### Genel Video Ayarları
* **Görüntü Modu:** Tam Ekran (Fullscreen)
  * *Teknik Açıklama:* Pencereli veya Çerçevesiz Pencereli modlar Windows Masaüstü Pencere Yöneticisi'ni (DWM) araya sokarak 10-15 ms ek girdi gecikmesine neden olur. Tam Ekran modu oyuna doğrudan donanım erişimi sağlar.
* **Çözünürlük:** Monitörün Doğal (Native) Çözünürlüğü ve Maksimum Yenileme Hızı (Örn: 1920x1080 240Hz)
* **En Boy Oranı Metodu:** Doldur (Fill)
* **Pil Enerjisinde FPS Sınırla:** Kapalı
* **Menülerde FPS Sınırla:** Açık (60 FPS - Ekran kartının boştayken ısınmasını önler)
* **Arka Planda FPS Sınırla:** Açık (10 FPS)
* **Kısıtlamasız FPS:** Kapalı (FPS kısıtlaması sistem gecikmesini artırır)

### Grafik Kalitesi Ayarları
| Ayar | Önerilen Değer | Teknik Sebebi |
| :--- | :--- | :--- |
| **Materyal Kalitesi** | Düşük | VRAM kullanımını ve yüzey kaplama yükünü azaltır. |
| **Doku Kalitesi** | Düşük | Doku süzme yükünü düşürür, FPS'i artırır. |
| **Detay Kalitesi** | Düşük | Haritadaki gereksiz dekoratif objeleri (yapraklar, çöp vb.) kaldırarak görüşü netleştirir. |
| **Arayüz Kalitesi** | Düşük | HUD elemanlarının işlemciye getirdiği yükü minimize eder. |
| **Nitelik Sınırı (Vignette)** | Kapalı | Ekran kenarlarını karartan efekti kapatır, görüş alanını genişletir. |
| **V-Sync (Dikey Eşitleme)** | Kapalı | **Kesinlikle Kapalı.** Yüksek oranda girdi gecikmesine (Input Lag) yol açar. |
| **Kenar Yumuşatma (Anti-Aliasing)** | MSAA 2x veya FXAA / Kapalı | MSAA 2x, kenar tırtıllarını giderirken performans kaybını minimumda tutar. Düşük sistemlerde "Kapalı" yapılmalıdır. |
| **Eşyönsüz Filtreleme (Anisotropic Filtering)** | 1x veya 2x | Uzaktaki dokuların netliğini ayarlar; 1x en yüksek performansı verir. |
| **Netliği Artır (Improve Clarity)** | Açık | Piksel kontrastını artırarak düşman modellerinin seçilebilirliğini yükseltir (Performans etkisi yok denecek kadar azdır). |
| **Deneysel Keskinleştirme** | Kapalı | Görüntüyü yapay olarak keskinleştirir, kenar yumuşatma ile çakışabilir. |
| **Bloom (Işık Parlaması)** | Kapalı | Yetenek efektlerinin gözü almasını ve ekranı kaplamasını engeller. |
| **Bozulma (Distortion)** | Kapalı | Patlama ve yeteneklerdeki kırılma efektlerini kapatır, FPS düşüşlerini önler. |
| **Gölge Dökümü (Cast Shadows)** | Kapalı | Karakterlerin kendi üzerine düşen gölgelerini kapatır. Harita gölgelerine etkisi yoktur. |

---

## 2. NVIDIA ve Sistem Tarafı Gecikme Ayarları

Görsel performanın ötesinde, fareye tıklandığı an ile eylemin ekrana yansıması arasındaki süreyi (End-to-End Latency) düşürmek gerekir.

### NVIDIA Reflex Düşük Gecikme (NVIDIA Reflex Low Latency)
* **Önerilen Ayar:** **Açık + Takviye (On + Boost)**
* *Teknik Açıklama:* "Açık" modu, render kuyruğunu sıfırlayarak CPU ve GPU'yu senkronize eder. "+ Takviye" (Boost) ise GPU'nun çekirdek hızlarını (clock speed) sürekli maksimumda tutarak işlemci tabanlı darboğazlarda bile saat hızlarının düşmesini engeller.

### Windows ve Sürücü Optimizasyonları
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Windows ayarlarından **Açık** konuma getirilmelidir.
* **Oyun Modu (Game Mode):** Windows Oyun Modu **Açık** olmalıdır. Arka plan işlemlerini kısıtlayarak Valorant'a işlemci önceliği tanır.
* **Tam Ekran İyileştirmelerini Devre Dışı Bırakma:** Valorant executable dosyasına (`VALORANT-Win64-Shipping.exe`) sağ tıklayıp *Özellikler > Uyumluluk > Tam ekran iyileştirmelerini devre dışı bırak* seçeneği işaretlenmelidir.

---

## 3. Profesyonel Hassasiyet (Sensitivity) ve Fare Ayarları

Valorant'ta isabetli atış yapmanın (Aim) temeli tutarlılıktır (Consistency). Yüksek hassasiyet mikroskobik düzeltmeleri zorlaştırır.

### eDPI Hesaplama ve İdeal Aralık
eDPI (Etkili DPI), farenizin donanımsal DPI değeri ile oyun içi hassasiyetinizin çarpımıdır:
$$\text{eDPI} = \text{Fare DPI} \times \text{Oyun İçi Hassasiyet}$$

* **Profesyonel Oyuncu Ortalaması:** 200 - 400 eDPI
* **Örnek Yapılandırma:** 800 DPI fare için **0.25 ile 0.4** arası oyun içi hassasiyet.

### Ham Girdi Tamponu (Raw Input Buffer)
* **Önerilen Ayar:** **Açık**
* *Teknik Açıklama:* Windows'un fare imleç işleme katmanını tamamen atlayarak farenin ürettiği veriyi doğrudan oyuna iletir. Özellikle 1000 Hz ve üzeri (2000Hz/4000Hz/8000Hz) Raporlama Hızına (Polling Rate) sahip farelerde CPU kullanımını azaltır ve girdi gecikmesini düşürür.

---

## 4. Görüş ve Düşman Anahat Renk Ayarları

İnsan gözü yeşil/sarı spektrumundaki renkleri kırmızıya kıyasla daha hızlı algılar. Düşman anahat (Highlight) rengini değiştirmek, tepki süresini (Reaction Time) 10-20 ms kadar iyileştirebilir.

* **Düşman Anahat Rengi:** **Sarı (Deuteranopia)** veya **Sarı (Protanopia)**
  * *Sebebi:* Sarı renk, Valorant haritalarının çoğundaki (Bind, Ascent, Haven) koyu veya gri arka planlardan yüksek kontrastla ayrılır.

---

## 5. Optimal Nişangah (Crosshair) Özellikleri

Görüşü kapatmayan, sabit ve yüksek kontrastlı nişangahlar rekabetçi avantaj sağlar.

* **Renk:** Camgöğü (Cyan), Yeşil veya Beyaz (Siyah dış çizgili)
* **İç Çizgiler:** Açık (Saydamlık: 1, Uzunluk: 4, Kalınlık: 2, Ofset: 2)
* **Dış Çizgiler:** Kapalı
* **Merkez Nokta:** Kapalı (Kişisel tercihe bağlı, ancak uzak mesafelerde kafayı kapatmamalıdır)
* **Hareket/Ateş Etme Hatası:** Kapalı (Nişangahın hareket ederken veya ateş ederken genişlemesi görsel kirlilik yaratır)

---

## 6. Ses ve Mekansal Algı Ayarları (HRTF)

Düşmanların ayak seslerini ve yetenek seslerinin konumunu (3D uzamsal konumlandırma) doğru algılamak için ses ayarları kritik faktördür.

* **HRTF (Head-Related Transfer Function):** **Açık**
  * *Teknik Açıklama:* Kulaklıklar için özel simüle edilmiş 3D ses algoritmasıdır. Düşmanın önünüzde, arkanızda, yukarınızda veya aşağıda olduğunu hassas bir şekilde ayırt etmenizi sağlar.
* **Windows Uzamsal Ses (Dolby Atmos / Windows Sonic):** **Kapalı**
  * *Uyarı:* HRTF oyunda açıkken Windows ses efektlerinin kapalı olması gerekir. Aksi takdirde iki farklı 3D algoritması çakışır ve seslerin yönü bozulur.
* **Hoparlör Yapılandırması:** Stereo

---

## Özet Ayar Tablosu (Hızlı Kontrol)

| Kategori | Ayar | Değer |
| :--- | :--- | :--- |
| **Ekran** | Görüntü Modu | Tam Ekran |
| **Performans** | Bütün Grafik Detayları | Düşük |
| **Gecikme** | NVIDIA Reflex | Açık + Takviye |
| **Görsel** | Netliği Artır | Açık |
| **Fare** | Ham Girdi Tamponu | Açık |
| **Görüş** | Düşman Anahat Rengi | Sarı (Deuteranopia) |
| **Ses** | HRTF | Açık |