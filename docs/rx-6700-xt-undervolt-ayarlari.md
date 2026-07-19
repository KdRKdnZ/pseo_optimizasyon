---
title: rx 6700 xt undervolt ayarları
description: rx 6700 xt undervolt ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# RX 6700 XT Undervolt Ayarları: Sıcaklık Düşürme ve Performans Artırma Rehberi

AMD’nin RDNA 2 mimarisine dayanan **Radeon RX 6700 XT**, 1440p çözünürlükte yüksek performans sunan başarılı bir grafik kartıdır. Ancak, fabrikasyon çıkışlı voltaj değerleri (stock voltage), AMD tarafından "silikon piyangosu" (silicon lottery) riskini sıfırlamak amacıyla optimum seviyenin oldukça üzerinde belirlenir. Bu durum kartın gereksiz yere fazla güç tüketmesine, yüksek sıcaklıklara ulaşmasına ve fan gürültüsüne neden olur.

Bu teknik rehberde, RX 6700 XT ekran kartınızın sıcaklık değerlerini 5 ila 10°C arasında düşürürken, güç tüketimini azaltan ve termal darboğazı (thermal throttling) engelleyerek performansı optimize eden **en kararlı RX 6700 XT undervolt ayarları** adım adım açıklanmıştır.

---

## RX 6700 XT Undervolt Nedir ve Neden Yapılmalıdır?

Undervolt, GPU çekirdeğine giden voltajı, saat hızını (clock speed) düşürmeden veya çok az düşürerek azaltma işlemidir. Yarı iletken fiziğinde güç tüketimi ve ısı üretimi, voltajın karesi ile doğru orantılıdır ($P \propto V^2 \cdot f$). Voltajdaki küçük bir düşüş, sıcaklık ve güç tüketiminde çarpan etkisiyle büyük bir düşüş sağlar.

**RX 6700 XT için undervolt yapmanın avantajları:**
*   **Düşük Sıcaklık:** GPU bağlantı noktası (Junction Temperature) ve genel çekirdek sıcaklığı ciddi oranda düşer.
*   **Sessiz Çalışma:** Sıcaklık düştüğü için fan devir hızı (RPM) azalır, akustik konfor artar.
*   **Daha Kararlı Boost Frekansları:** Kart termal sınırlara takılmadığı için oyunlarda daha stabil FPS değerleri sunar.
*   **Enerji Tasarrufu:** Kartın güç tüketimi ortalama 230W seviyesinden 170W-180W seviyelerine geriler.

---

## Adım Adım RX 6700 XT Undervolt Ayarları

Bu işlem için üçüncü parti bir yazılıma gerek yoktur. AMD'nin resmi sürücüsü olan **AMD Software: Adrenalin Edition** üzerinden bu ayarlar güvenle yapılabilir.

### 1. Hazırlık ve Gerekli Araçlar
İşleme başlamadan önce sistem kararlılığını ölçmek için aşağıdaki yazılımları indirin:
*   **AMD Software: Adrenalin Edition** (Güncel sürüm)
*   **HWInfo64** (Sıcaklık ve güç tüketimi takibi için)
*   **Superposition Benchmark** veya **3DMark Time Spy** (Yük testi için)

### 2. Adrenalin Arayüzü Yapılandırması
1.  Masaüstüne sağ tıklayın ve **AMD Software: Adrenalin Edition**'ı açın.
2.  Üst menüden **Performans** > **Ayarlanıyor** (Tuning) sekmesine gidin.
3.  Ayarlama Kontrolü bölümünden **Özel** (Custom) seçeneğini seçin.
4.  **GPU Ayarı**, **Fan Ayarı**, **VRAM Ayarı** ve **Güç Ayarı** sekmelerini etkinleştirin (Etkin/Gelişmiş Kontrol konumuna getirin).

---

## Güvenli ve Kararlı RX 6700 XT Undervolt Değerleri

Her GPU silikon kalitesi aynı değildir. Bu nedenle doğrudan "en agresif" değerleri uygulamak yerine, aşağıda belirtilen üç farklı profilden sisteminize en uygun olanını seçerek test etmelisiniz.

| Profil Türü | Min Frekans (MHz) | Max Frekans (MHz) | Voltaj (mV) | Güç Limiti (Power Limit) |
| :--- | :--- | :--- | :--- | :--- |
| **Fabrika Çıkışlı (Stock)** | 2300 | 2600+ | 1200 mV | %0 |
| **Güvenli Profil (Her Kart İçin)** | 2400 | 2550 | **1150 mV** | %0 |
| **Dengeli Profil (Önerilen)** | 2450 | 2580 | **1115 mV** | +%10 |
| **Agresif Profil (Silikonu İyi Kartlar)** | 2450 | 2600 | **1075 mV** | +%15 |

### İnce Ayar Detayları (Adrenalin Üzerinden Giriş)

*   **GPU Min Frekans:** Maksimum frekansın **100-150 MHz** altında ayarlanmalıdır. Bu, oyun içi geçişlerde ve yük değişimlerinde anlık FPS düşüşlerini (stuttering) engeller.
*   **GPU Max Frekans:** Kartın kararlı çalışması için referans değer olan **2550 - 2580 MHz** aralığı idealdir.
*   **Voltaj (Voltage):** Fabrika çıkışı 1200 mV olan bu değeri kademeli olarak düşüreceğiz. İlk hedefiniz **1120 mV** olmalıdır.
*   **Güç Limiti (Power Limit):** Bu değeri **+%10 veya +%15** yapın. Güç limitini artırmak kartın daha fazla elektrik çekmesini sağlamaz; aksine undervolt yapıldığı için kartın anlık güç dalgalanmalarında frekans kısmasını (throttling) engeller.

---

## VRAM ve Fan Eğrisi Optimizasyonu

Maksimum verim elde etmek için voltaj düşürme işlemini VRAM hızlandırma ve özel bir fan eğrisi ile desteklemek gerekir.

### VRAM Ayarları
*   **Bellek Ayarı:** Etkinleştirin ve **Hızlı Zamanlama** (Fast Timing) moduna alın.
*   **Maksimum Frekans:** **2100 MHz** seviyesine çekin (Varsayılan 2000 MHz'dir). RX 6700 XT bellekleri undervolt ile açılan termal bütçeyi kullanarak performans artışına katkı sağlar.

### Fan Eğrisi Ayarları
Varsayılan fan eğrisi genellikle sessizlik odaklıdır ancak kartın 80°C üzerine çıkmasına izin verir. Aşağıdaki agresif olmayan ama etkili fan eğrisini uygulayın:

*   **30°C** -> %20 Fan Hızı
*   **50°C** -> %35 Fan Hızı
*   **65°C** -> %50 Fan Hızı
*   **80°C** -> %65 Fan Hızı

---

## Kararlılık Testi (Stress Test) Nasıl Yapılır?

Yaptığınız ayarların kararlı (stable) olup olmadığını anlamak için sistemi ağır yük altında test etmeniz gerekir.

1.  **Superposition Benchmark** testini 1080p Extreme veya 4K Optimized modunda çalıştırın. Test esnasında ekranda yırtılma, renk pikselleşmesi (artifact) veya siyah ekran olup olmadığını gözlemleyin.
2.  Test başarıyla tamamlanırsa, **Cyberpunk 2077**, **Red Dead Redemption 2** veya **Metro Exodus** gibi GPU'yu %99 yük altında bırakan ağır grafikli oyunları en az 30 dakika oynayın.
3.  **Sistem Çökerse (Siyah Ekran/Sürücü Zaman Aşımı):** Bu durum ekran kartınıza zarar vermez. AMD sürücüsü kendini güvenli moda alır ve varsayılan ayarlara döner. Çökme yaşarsanız, voltaj değerini **10-15 mV artırarak** (örneğin 1115 mV'tan 1130 mV'a) testi tekrarlayın.

## Sıkça Sorulan Sorular (SSS)

### Undervolt işlemi RX 6700 XT'yi garanti dışı bırakır mı?
Hayır. AMD Software: Adrenalin Edition üzerinden yapılan voltaj düşürme işlemleri yazılımsal limitler dahilindedir ve ekran kartını **garanti dışı bırakmaz**.

### Undervolt ekran kartının ömrünü kısaltır mı?
Aksine, undervolt işlemi kartın üzerindeki termal yükü ve elektrik stresini azalttığı için bileşenlerin (özellikle VRM ve kapasitörlerin) **ömrünü uzatır**.

### Her RX 6700 XT aynı voltaj değerinde çalışır mı?
Hayır. Üretim bandındaki mikroskobik farklar nedeniyle her GPU'nun silikon kalitesi farklıdır. Bir kart 1075 mV değerinde stabil çalışırken, diğer bir kart en düşük 1130 mV değerinde kararlı kalabilir. Bu duruma **silikon piyangosu** denir.