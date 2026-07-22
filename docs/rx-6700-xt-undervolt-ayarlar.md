---
title: "rx 6700 xt undervolt ayarları"
description: "rx 6700 xt undervolt ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# AMD Radeon RX 6700 XT Undervolt Rehberi: Optimal Ayarlar ve Performans Artışı

AMD Radeon RX 6700 XT (Navi 22 mimarisi), fabrika çıkışlı olarak yüksek voltaj değerleriyle gelir. AMD, silikon piyangosu farklılıklarını tolere edebilmek adına stok voltajı güvenli alanın üstünde belirler. Voltaj düşürme (undervolt) işlemi; kartın sıcaklık değerlerini düşürmek, güç tüketimini azaltmak, fan gürültüsünü kesmek ve thermal throttling'i (ısıya bağlı frekans düşürme) engelleyerek daha kararlı yüksek FPS elde etmek için yapılan en etkili optimizasyondur.

Bu rehberde, RX 6700 XT için stabil undervolt parametrelerini, test metodolojisini ve dikkat edilmesi gereken teknik detayları bulabilirsiniz.

---

## RX 6700 XT Undervolt Mantığı ve Avantajları

Stok durumdaki bir RX 6700 XT genellikle **1200 mV** voltaj ve **2500-2600 MHz** arası değişken frekans değerlerinde çalışır. Bu yüksek voltaj, özellikle GPU'nun sıcak nokta (Junction Temperature) değerinin 95°C–100°C seviyelerine çıkmasına neden olur.

Başarılı bir undervolt işlemi sonrasında elde edilecek teknik kazanımlar:

*   **Sıcaklık Düşüşü:** GPU çekirdek sıcaklığında 5–10°C, Junction (bağlantı) sıcaklığında 10–15°C düşüş.
*   **Güç Tasarrufu:** Tüketimde 30W ile 50W arasında azalma.
*   **Daha Yüksek Sürekli Frekans:** Isı düştüğü için kart maks frekansı kısıtlamaz, oyun içi FPS dalgalanmaları (1% Low değerleri) iyileşir.
*   **Sessizlik:** Fan devir hızları %15–25 oranında düşürülebilir.

---

## Undervolt İçin Gerekli Araçlar

1.  **AMD Software: Adrenalin Edition** (Güncel sürücü)
2.  **HWiNFO64** (Sıcaklık ve voltaj değerlerini detaylı izlemek için)
3.  **Stress Test Yazılımları:** 3DMark Time Spy, UNIGINE Superposition veya FurMark.
4.  **Ağır Yüklü Oyunlar:** Cyberpunk 2077, Red Dead Redemption 2 veya Returnal (Sentetik testlerden geçip oyunda çöken profiller için nihai doğrulama).

---

## Adım Adım RX 6700 XT Undervolt Ayarları

Ayarlara ulaşmak için: **AMD Adrenalin Software > Performans > Ayarlanıyor (Tuning)** sekmesine gidin. "Özel" (Custom) modunu seçin.

### 1. GPU Ayarları (GPU Tuning)
*   **GPU Ayarlaması:** Etkin (Enabled)
*   **Gelişmiş Kontrol:** Etkin (Enabled)
*   **Maksimum Frekans (MHz):** `2550 MHz` (Stok değer genelde 2600+ üzerindedir, kararlılık için 2550 MHz ideal bir başlangıçtır.)
*   **Voltaj (mV):** Stok değer 1200 mV'dur. Başlangıç noktası olarak **`1100 mV`** ayarlayın. *(Silikon kalitenize göre bu değer 1075 mV veya 1050 mV seviyesine kadar düşebilir).*

### 2. VRAM Ayarları (VRAM Tuning)
*   **VRAM Ayarlaması:** Etkin (Enabled)
*   **Bellek Zamanlama (Memory Timing):** Hızlı Zamanlama (Fast Timings)
*   **Maksimum Frekans (MHz):** `2100 MHz` (Stok değer 2000 MHz'dir. RX 6700 XT bellekleri genellikle 2100-2125 MHz kadar sorunsuz hız aşırtılabilir).

### 3. Güç Ayarları (Power Tuning)
*   **Güç Ayarlaması:** Etkin (Enabled)
*   **Güç Limiti (%):** `+%15` (Sınırı en sağa çekin. Bu işlem kartın fazladan güç çekmesini zorlamaz, aksine voltaj düştüğü için kartın anlık güç limitine takılmasını önler).

### 4. Fan Ayarları (Fan Tuning)
*   **Fan Ayarlaması:** Etkin (Enabled)
*   **Gelişmiş Kontrol:** Etkin (Enabled)
*   **Sıfır RPM:** İsteğe bağlı (Boştayken fanların durmasını istiyorsanız açık tutun).
*   **Eğri Ayarı:** Junction sıcaklığı 85°C'yi geçmeyecek şekilde max fan hızını %50–%60 civarında sabitleyin.

---

## Önerilen Profiller (Referans Tablosu)

Silikon kalitesine (Silicon Lottery) göre uygulayabileceğiniz 3 farklı varsayılan profil:

| Parametre | Stok Ayar | Güvenli / Dengeli Profil | Agresif / Düşük Tüketim Profil |
| :--- | :--- | :--- | :--- |
| **Max Frekans** | ~2620 MHz | **2550 MHz** | **2450 MHz** |
| **Voltaj** | 1200 mV | **1100 mV - 1115 mV** | **1050 mV - 1075 mV** |
| **VRAM Frekansı**| 2000 MHz | **2100 MHz (Fast Timing)**| **2050 MHz (Default)** |
| **Güç Limiti** | %0 | **+%15** | **+%0 veya +%5** |
| **Ort. Güç Tüketimi**| ~210W - 230W | **~160W - 180W** | **~140W - 150W** |

---

## Stabilite Testi ve İnce Ayar (Fine-Tuning)

Undervolt işleminde en önemli aşama kararlılık testidir. Yapılan ayarların sistem tarafından kabul edilmesi, kartın her oyunda stabil çalışacağı anlamına gelmez.

1.  **Sentetik Test:** Ayarları kaydettikten sonra **UNIGINE Superposition (1080p Extreme veya 4K)** testini başlatın. Test sırasında ekranda yırtılma, "artifact" (yeşil/mor karelenmeler) veya sürücü çökmesi olup olmadığını gözlemleyin.
2.  **Sıcaklık Kontrolü:** HWiNFO64 üzerinden *GPU Temperature* (65°C altı ideal) ve *GPU Junction Temperature* (85°C altı ideal) değerlerini denetleyin.
3.  **Oyun Testi:** Sentetik testi geçen ayarları en az 30-45 dakika boyunca AAA kalitesinde bir oyunda test edin.

### Kararsızlık Durumunda Ne Yapılmalı?

*   Oyun veya test sırasında **WattMan hatası** alırsanız ya da sistem kilitlenirse voltajı yetersiz gelmiştir.
*   Voltajı **+10 mV** artırın (Örn: 1100 mV -> 1110 mV) ve tekrar test edin.
*   Alternatif olarak, voltajı değiştirmeden **Max Frekansı -25 MHz** düşürün (Örn: 2550 MHz -> 2525 MHz).

---

## Sık Yapılan Hatalar ve Önemli İpuçları

*   **Profili Kaydetme:** Kararlı ayarları bulduğunuzda Adrenalin yazılımının sağ üst köşesindeki **"Profi Yükle/Kaydet"** butonundan `.xml` formatında profili bilgisayarınıza kaydedin. Sürücü çöktüğünde ayarlar sıfırlanabilir, bu sayede tek tıkla geri yüklersiniz.
*   **Hızlı Başlat Özelliği:** Windows'un "Hızlı Başlat" (Fast Startup) özelliği Adrenalin ayarlarının bilgisayar her açıldığında sıfırlanmasına yol açabilir. Denetim Masası > Güç Seçenekleri üzerinden Hızlı Başlat'ı kapatmanız önerilir.
*   **VRAM Sıcaklığı:** VRAM frekansını artırırken HWiNFO64 üzerinden *Memory Temperature* değerini izleyin. 90°C üzeri risklidir; böyle bir durumda VRAM frekansını stok değere (2000 MHz) çekin.