# AMD Radeon RX 6700 XT Undervolt Rehberi: Adım Adım En İdeal Ayarlar

AMD Radeon RX 6700 XT, RDNA 2 mimarisinin en başarılı orta-üst segment ekran kartlarından biridir. Ancak fabrika çıkışlı voltaj değerleri (stok ayarlar) gereğinden yüksek belirlendiği için kart fazla ısınabilir, yüksek fan gürültüsü üretebilir ve watt başına düşen performans oranı azalabilir. 

Undervolt (voltaj düşürme) işlemi; ekran kartının çekirdek frekansını koruyarak veya artırarak, kartın çektiği voltajı azaltma işlemidir. Bu işlem sonucunda **5-10°C sıcaklık düşüşü**, **30-50 Watt daha az güç tüketimi** ve thermal throttling (sıcaklığa bağlı frekans düşüşü) engellendiği için **daha kararlı FPS değerleri** elde edilir.

---

## RX 6700 XT Undervolt Öncesi Hazırlık ve Araçlar

İşleme başlamadan önce sisteminizde aşağıdaki yazılımların güncel olduğundan emin olun:

* **AMD Software: Adrenalin Edition** (En güncel WHQL sürücüsü)
* **HWInfo64** (Sıcaklık, Hotspot/Junction temp ve güç tüketimi takibi için)
* **3DMark (Time Spy) / Unigine Superposition veya Heavy Gaming** (Cyberpunk 2077, Red Dead Redemption 2 vb. test için)

---

## RX 6700 XT Stok vs. İdeal Undervolt Değerleri

Her ekran kartının silikon kalitesi (Silicon Lottery) farklıdır. Aşağıdaki tabloda referans stok değerler ile test edilmiş en stabil "Sweet Spot" (En İdeal) voltaj değerleri karşılaştırılmıştır.

| Parametre | Stok Değerler | Önerilen Başlangıç | Agresif / İdeal Ayar |
| :--- | :--- | :--- | :--- |
| **Max GPU Frekansı (MHz)** | ~2581 MHz | 2500 MHz | 2550 - 2600 MHz |
| **Min GPU Frekansı (MHz)** | ~500 MHz | 2400 MHz | 2450 - 2500 MHz |
| **Voltaj (mV)** | 1200 mV | 1125 mV | **1075 mV - 1100 mV** |
| **VRAM Frekansı (MHz)** | 2000 MHz | 2050 MHz | 2100 - 2120 MHz |
| **VRAM Zamanlaması** | Varsayılan | Hızlı Zamanlama (Fast Timing) | Hızlı Zamanlama |
| **Güç Sınırı (Power Limit)** | %0 | +%10 | +%15 |

---

## Adım Adım AMD Adrenalin Sürücüsü Üzerinden Undervolt Yapma

İşlemi gerçekleştirmek için herhangi bir üçüncü taraf yazılıma (MSI Afterburner vb.) ihtiyaç yoktur. AMD Adrenalin yazılımı bu işlem için en stabil platformdur.

### 1. Ayar Menüsüne Erişim
1. Masaüstüne sağ tıklayıp **AMD Software: Adrenalin Edition**’ı açın.
2. Üst menüden **Performans** sekmesine, ardından **Ayarlanıyor** (Tuning) alt sekmesine geçin.
3. Manuel Ayarla seçeneğini **Özel** (Custom) konumuna getirin.

### 2. GPU Ayarları (Gelişmiş Kontrolü Açın)
* **GPU Ayarlanıyor:** Etkinleştirin.
* **Gelişmiş Kontrol:** Etkinleştirin.
* **Maksimum Frekans (MHz):** `2550` değerini girin.
* **Minimum Frekans (MHz):** Oyunlardaki anlık takılmaları (stuttering) önlemek için Maksimum Frekansın 100 MHz altına sabitleyin. Örn: `2450` MHz.
* **Voltaj (mV):** Stok değer olan 1200 mV'yi aşamalı olarak düşürün. Başlangıç noktası olarak **1100 mV** girin.

### 3. VRAM Ayarları
* **VRAM Ayarlanıyor:** Etkinleştirin.
* **Gelişmiş Kontrol:** Etkinleştirin.
* **Bellek Zamanlaması:** **Hızlı Zamanlama** (Fast Timing) olarak seçin. (Gecikmeyi düşürür, FPS'e doğrudan katkı sağlar).
* **Maksimum Frekans (MHz):** `2100` MHz yapın. (Görüntüde bozulma olursa `2050` MHz'e çekin).

### 4. Güç Ayarları (Power Limit)
* **Güç Ayarlanıyor:** Etkinleştirin.
* **Güç Limiti (%):** Kaydırıcıyı sağa çekerek **+%15** yapın. Bu ayar kartın daha fazla güç çekmesini sağlamaz; voltajı düşürdüğümüz için kartın yüksek frekanslarda güç limitine takılmadan sürekli kalabilmesine olanak tanır.

### 5. Fan Eğrisi (Fan Curve) Ayarları
* **Fan Ayarlanıyor:** Etkinleştirin ve **Gelişmiş Kontrolü** açın.
* Sıcaklığa bağlı fan hızlarını aşağıdaki gibi optimize edebilirsiniz:
  * 50°C -> %35 Fan Hızı
  * 65°C -> %45 Fan Hızı
  * 75°C -> %60 Fan Hızı
  * 85°C Junction -> %75 Fan Hızı

---

## Kararlılık Testi (Stability Test) Nasıl Yapılır?

Ayarları uyguladıktan sonra sağ üstteki **Değişiklikleri Uygula** butonuna basın ve profili kaydedin. Kartınızın bu voltajda stabil çalışıp çalışmadığını anlamak için:

1. **Unigine Superposition veya 3DMark Time Spy** testini çalıştırın. Test sırasında ekranda çizgi, renk bozulması (artifact) veya oyunun kapanıp masaüstüne atma durumu olup olmadığını gözlemleyin.
2. **Ağır Bir Oyunda 30 Dakika Test Edin:** Cyberpunk 2077 veya Metro Exodus gibi GPU'yu %100 kullanan oyunlarda test yapın.
3. **Çökme Durumunda:** Eğer sistem kilitlenir veya sürücü çökerse, voltajı **10-15 mV artırın** (Örn: 1080 mV -> 1095 mV yapın) ve tekrar test edin.
4. **Sorun Yoksa:** Sistem stabilse, voltajı **10 mV daha düşürerek** (Örn: 1080 mV -> 1070 mV) kartınızın sınırını bulana kadar devam edebilirsiniz.

---

## RX 6700 XT Undervolt Sonrası Elde Edilen Kazançlar

Başarılı bir undervolt işlemi sonrasında elde edilecek ortalama değerler:

* **Sıcaklık (GPU Core):** 72°C'den **62-64°C** seviyesine düşer.
* **Bağlantı Sıcaklığı (Junction/Hotspot):** 95°C'den **78-82°C** seviyesine geriler.
* **Güç Tüketimi:** ~215W değerinden **~165W - 175W** aralığına iner.
* **Performans:** Yüksek frekanslar kararlı tutulduğu için stok hale kıyasla **%2 - %5 FPS artışı** sağlanır.

---

## Sıkça Sorulan Sorular (SSS)

### Undervolt ekran kartının garantisini bozar mı?
Hayır. AMD Adrenalin yazılımı üzerinden yapılan yazılımsal voltaj düşürme işlemleri ekran kartını garanti kapsamı dışına çıkarmaz.

### Undervolt karta zarar verir mi?
Hayır. Aksine, voltaj ve sıcaklık düştüğü için elektronik bileşenlerin ömrü uzar. En kötü senaryoda voltaj yetersiz gelir, sistem sürücüyü sıfırlar ve stok ayarlara döner.

### Bilgisayarı her açtığımda ayarlar sıfırlanıyor, ne yapmalıyım?
Windows'un "Hızlı Başlat" (Fast Startup) özelliği Adrenalin sürücü ayarlarının sıfırlanmasına neden olabilir. Denetim Masası > Güç Seçenekleri üzerinden Hızlı Başlat'ı kapatmak bu sorunu çözer. Ayrıca oluşturduğunuz profili Adrenalin yazılımından `.xml` olarak dışa aktarıp (export) saklamanız önerilir.