# AMD Radeon RX 570 Maksimum Oyun Performansı Rehberi: Overclock, Sürücü ve Grafik Ayarları

AMD'nin Polaris mimarisine (GCN 4.0) dayanan Radeon RX 570, 1080p çözünürlükte fiyat/performans odaklı sistemlerin uzun süredir bel kemiğini oluşturmaktadır. Ancak güncel oyunların artan sistem gereksinimleri karşısında karttan maksimum verimi almak; doğru yazılım konfigürasyonu, ince donanım ayarları ve optimum grafik tercihlerini gerektirir. 

Bu rehber, RX 570 (4GB ve 8GB) ekran kartınızdan en yüksek FPS değerini ve en kararlı kare sürelerini (frametime) elde etmeniz için gereken tüm teknik adımları kapsamaktadır.

---

## 1. RX 570 Teknik Profil ve Performans Potansiyeli

RX 570, fabrikasyon çıkış değerleri itibarıyla 1080p orta/yüksek ayarlarda akıcı bir deneyim sunmak üzere tasarlanmıştır. Ancak mimarinin sunduğu hız aşırtma (overclock) ve voltaj düşürme (undervolt) marjı yüksektir.

*   **Çekirdek Mimarisi:** Ellesmere PRO (14nm FinFET)
*   **Akış İşlemcileri (Stream Processors):** 2048
*   **Taban / Boost Çekirdek Hızı:** 1168 MHz / 1244 MHz
*   **Bellek Hızı ve Bant Genişliği:** 1750 MHz (7.0 Gbps eff.), 224 GB/s (256-bit GDDR5)
*   **TDP:** 150W

---

## 2. AMD Software: Adrenalin Edition İdeal Sürücü Ayarları

Sürücü seviyesindeki optimizasyon, oyun içi grafik ayarlarını değiştirmeden önce doğrudan gecikmeyi düşürür ve FPS kararlılığını artırır. AMD Adrenalin panelinde şu ayarlar uygulanmalıdır:

*   **Ekran Kartı Profili:** Özel (Custom)
*   **Radeon Anti-Lag:** **Açık** (Giriş gecikmesini minimize eder, özellikle rekabetçi oyunlarda kritiktir).
*   **Radeon Chill:** **Kapalı** (Maksimum performans için devre dışı bırakılmalıdır; gücü sınırlayabilir).
*   **Radeon Boost:** **Kapalı** (Dinamik çözünürlük ölçeklemesi bazı oyunlarda görüntü çamurlaşmasına neden olabilir).
*   **Radeon Image Sharpening (RIS):** **Açık (%70 - %80)** (Düşük çözünürlük veya FSR kullanıldığında netliği artırır).
*   **Gelişmiş Ayarlar:**
    *   **Doku Filtreleme Kalitesi:** Performans
    *   **Yüzey Biçim Entegrasyonu:** Açık
    *   **Tessellation (Mozaikleme) Modu:** Sürücü ayarlarının üstüne yaz -> **Maksimum Mozaikleme Seviyesi: 8x veya 16x** (AMD Polaris mimarisi yüksek tessellation yüklerinde zorlanır, 8x/16x sınırlandırması görsel kayıp olmadan yüksek FPS kazandırır).

---

## 3. Maksimum Güç: Undervolt ve Overclock (OC) Kombinasyonu

RX 570 kartlar sıklıkla güç ve sıcaklık limitine (thermal throttling) takılır. Kartı sadece overclock etmek sıcaklığı artıracağı için frekans düşüşüne sebep olur. **En yüksek performansı almanın yolu Undervolt + Overclock yapmaktır.**

AMD Adrenalin paneli üzerinden *Performans > Ayarlanıyor (Tuning)* sekmesinde uygulanacak referans değerler:

### Güç ve Sıcaklık Limitleri
*   **Güç Limiti (Power Limit):** %20 ile %50 arası artırın (+50% kartın güç çekmesini serbest bırakır, frekans dalgalanmasını önler).
*   **Sıcaklık Hedefi:** Maksimum 75°C, Hedef 65°C.

### GPU Çekirdek Frekansı ve Voltajı (Manuel Tuning)
*   **P-State 7 (En Yüksek Durum):** ~1350 MHz - 1400 MHz (Silikon kalitesine göre değişir).
*   **P-State 7 Voltajı:** 1050 mV - 1100 mV seviyesine düşürün (Stok değer genelde 1150 mV'dur). 
    *   *Teknik Avantaj:* Düşük voltaj sıcaklığı düşürür, kart thermal throttling yapmadan yüksek frekansta sabit kalır.

### VRAM (Bellek) Ayarları
*   **Bellek Frekansı:** Stok 1750 MHz değerini **1900 MHz - 2000 MHz** seviyesine çıkarın.
*   **Bellek Zamanlaması (Memory Timing):** Seviye 2 (Level 2) veya Fast Timings olarak ayarlayın (Gecikmeyi düşürür, bant genişliğini artırır).

> **Not:** Yapılan ayarları *HWiNFO* veya *MSI Afterburner* ile stres testine (örneğin FurMark veya 3DMark Time Spy) sokarak sistem kararlılığını test edin.

---

## 4. Oyun İçi Grafik Ayarları Optimizasyon Stratejisi

RX 570 ile 1080p'de maksimum performans elde etmek için GPU yükünü en çok artıran ancak görselliğe etkisi az olan ayarlar kısılmalıdır.

| Grafik Ayarı | Tavsiye Edilen Seviye | Performans/Görsel Etkisi |
| :--- | :--- | :--- |
| **Gölge Kalitesi (Shadow Quality)** | Orta (Medium) | Yüksek FPS Kazancı |
| **Hacimsel Sis/Işık (Volumetric Fog/Lighting)** | Düşük (Low) / Kapalı | ÇOK Yüksek FPS Kazancı |
| **Kenar Yumuşatma (Anti-Aliasing)** | FXAA veya TAA (Low) | Orta FPS Kazancı |
| **Yansımalar (Screen Space Reflections)** | Kapalı veya Düşük | Yüksek FPS Kazancı |
| **Doku Kalitesi (Texture Quality)** | Yüksek / Ultra | VRAM Yetiyorsa (8GB) FPS Kaybettirmez |
| **Eşyönsüz Filtreleme (Anisotropic Filtering)**| 16x | GPU Yükü Yok Detay Artışı Yüksek |
| **AMD FSR (FidelityFX Super Resolution)** | Kalite (Quality) | **%25 - %40 FPS Artışı** |

---

## 5. Güncel Oyunlarda 1080p Performans Beklentileri (Optimize Edilmiş)

Sistemde Ryzen 5 3600/i5 10400F seviyesinde bir işlemci ve 16GB Dual-Channel RAM olduğu varsayımıyla optimize edilmiş ortalama FPS değerleri:

*   **CS2 / Valorant:** 140 - 220 FPS (Düşük/Orta Ayarlar)
*   **GTA V / Apex Legends:** 75 - 95 FPS (Yüksek Ayarlar)
*   **Red Dead Redemption 2:** 50 - 65 FPS (Doku Yüksek, Diğer Ayarlar Orta/Düşük + FSR Kalite)
*   **Cyberpunk 2077:** 45 - 55 FPS (Düşük/Orta Ayarlar + FSR 2.1 Dengeli/Kalite)
*   **God of War:** 45 - 60 FPS (Orijinal/Orta Ayarlar + FSR Kalite)

---

## 6. Darboğazı (Bottleneck) Önleme ve Sistem Sinerjisi

RX 570'in tam potansiyeline ulaşması için sistemin geri kalanı ekran kartını besleyebilmelidir:

1.  **Çift Kanal (Dual-Channel) RAM Şarttır:** Tek kanal (1x8GB) RAM, Polaris mimarisinde %15 ila %25 arasında ani FPS düşüşlerine (stuttering) ve düşük ortalama FPS'e neden olur. Sistem mutlaka **2x8GB** konfigürasyonunda çalışmalıdır.
2.  **İşlemci Limiti:** FX serisi eski AMD işlemciler veya 2. / 3. nesil i5 işlemciler RX 570'e belirgin şekilde darboğaz yapar. Minimum 4 çekirdek / 8 izlekli (örneğin Ryzen 3 3100, i3 10100F) bir işlemci gereklidir.
3.  **PCIe Hat Hızı:** Kartın PCIe 3.0 x16 modunda çalıştığından GPU-Z yazılımı üzerinden emin olunmalıdır.

---

## Özet

RX 570 ile maksimum oyun performansı elde etmek; **8x Tessellation sınırı koymak**, **%20-%50 güç limitini artırmak**, **1350+ MHz Çekirdek / 1900+ MHz VRAM hızlarına ulaşıp voltajı düşürmek** ve modern oyunlarda **AMD FSR Teknolojisini (Kalite Modu)** aktif etmekten geçer. Bu konfigürasyon, kartın varsayılan performansına kıyasla ortalama **%15 - %25 oranında FPS artışı** sağlar.