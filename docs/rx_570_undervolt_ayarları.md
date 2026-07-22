# AMD Radeon RX 570 Undervolt Ayarları Rehberi: Sıcaklık Düşürme ve Performans Artışı

AMD Radeon RX 570, Polaris mimarisinin en popüler ekran kartlarından biridir. Ancak fabrikasyon çıkışlı voltaj değerleri (stock değerler) gereğinden yüksek belirlendiği için kart yüksek sıcaklıklara ulaşır, fazla güç tüketir ve aşırı fan gürültüsü üretir. **Undervolt (voltaj düşürme)** işlemi; ekran kartının çekirdek frekansını düşürmeden (veya çok az artırarak) GPU'ya verilen voltajı azaltma işlemidir.

Bu rehberde, RX 570 ekran kartınızın sıcaklık değerlerini 10-15°C düşürecek, güç tüketimini azaltacak ve performans kaybı yaşamadan daha sessiz çalışmasını sağlayacak en ideal undervolt ayarlarını bulacaksınız.

---

## RX 570 Undervolt Yapmanın Avantajları

* **Daha Düşük Sıcaklık:** GPU sıcaklığında ortalama **10°C - 15°C** düşüş.
* **Düşük Güç Tüketimi:** Kartın çektiği güçte **30W - 50W** arası tasarruf.
* **Kararlı Performans (No Thermal Throttling):** Kart ısınmadığı için frekans düşürmez (throttling yaşanmaz), FPS dalgalanmaları engellenir.
* **Sessiz Çalışma:** Fanlar daha düşük devirde döneceği için kasa içi gürültü ciddi oranda azalır.
* **Donanım Ömrü:** Düşük sıcaklık ve voltaj, GPU çipinin ve VRM'lerin ömrünü uzatır.

---

## Gerekli Yazılımlar

Undervolt işlemine başlamadan önce aşağıdaki programların güncel sürümlerini indirin:

1. **AMD Software: Adrenalin Edition** (Gpu sürücüsü ve voltaj ayarı için)
2. **HWInfo64** veya **GPU-Z** (Voltaj, sıcaklık ve güç tüketimi takibi için)
3. **FurMark** veya **Unigine Heaven / Superposition** (Kararlılık/Stres testi için)

---

## Adım Adım AMD Software ile RX 570 Undervolt Ayarları

Her ekran kartının silikon kalitesi (Silikon Şansı / Silicon Lottery) farklıdır. Aşağıdaki değerler **RX 570 4GB ve 8GB** modellerinin %90'ında sorunsuz çalışan **en stabil referans değerleridir**.

### 1. Ayar Menüsüne Erişim
1. Masaüstüne sağ tıklayıp **AMD Software: Adrenalin Edition** uygulamasını açın.
2. Üst menüden **Performans** > **Ayarlanıyor (Tuning)** sekmesine gidin.
3. Manuel Ayar seçeneğini **Özel (Custom)** olarak işaretleyin.

### 2. Ekran Kartı (GPU) Voltaj Ayarları
GPU Ayarı (GPU Tuning) bölümünü aktif edin ve **Gelişmiş Kontrol (Advanced Control)** butonunu açın. Voltaj kontrolünü **Manuel** duruma getirin.

* **P-State 1 - 5:** Varsayılan bırakılabilir.
* **P-State 6 (1145 MHz):** `1000 mV` veya `980 mV`
* **P-State 7 (1244 MHz - Stok Hız):** `1010 mV` (Varsayılan değer genelde 1150 mV - 1200 mV civarıdır)

> **Not:** Eğer kartınız fabrikasyon olarak overclocklu bir model ise (Örn: 1300 MHz), P-State 7 frekansını **1244 MHz - 1260 MHz** seviyesine çekmek voltajı çok daha fazla düşürmenize olanak tanır.

### 3. Bellek (VRAM) Ayarları
VRAM Ayarı (Bellek Tuning) bölümünü aktif edin.

* **Bellek Frekansı:** `1750 MHz` (Varsayılan) veya stabilse `1850 MHz - 1900 MHz`
* **Voltaj Durumu (Voltaj Durumu 3 / State 2):** `950 mV` veya `1000 mV` (Varsayılan: 1000 mV)

### 4. Güç Limiti ve Fan Eğrisi
* **Güç Limiti (Power Limit):** **+%10** ile **+%20** arasında bir değere getirin. Bu işlem, kartın güç limitine takılıp frekans düşürmesini engeller (Fazla voltaj çekmez, sadece kararlılık sağlar).
* **Fan Eğrisi:** Fan kontrolünü manuel yaparak %60 sıcaklıkta fan hızının %50-55 civarında çalışmasını sağlayacak tatlı bir eğri oluşturun.

---

## RX 570 İçin Örnek Referans Tablosu

| Durum (State) | Frekans (MHz) | Stok Voltaj (mV) | **Önerilen Undervolt Voltajı (mV)** |
| :--- | :--- | :--- | :--- |
| **State 4** | 1045 MHz | 1050 mV | **950 mV** |
| **State 5** | 1100 MHz | 1100 mV | **970 mV** |
| **State 6** | 1145 MHz | 1150 mV | **990 mV** |
| **State 7** | 1244 MHz | 1150 - 1200 mV | **1000 - 1020 mV** |

---

## Kararlılık (Stres) Testi Nasıl Yapılır?

Ayarları kaydettikten sonra sisteminizin stabil çalışıp çalışmadığını test etmeniz gerekir:

1. **FurMark Testi:** FurMark uygulamasını başlatın ve 1080p çözünürlükte **15-20 dakika** çalıştırın.
2. **Sıcaklık Kontrolü:** Test sırasında GPU sıcaklığının ve "GPU VRM (Mofset)" sıcaklığının 75°C'yi geçmediğinden emin olun.
3. **Oyun Testi:** *Red Dead Redemption 2, Cyberpunk 2077, GTA V* veya *The Witcher 3* gibi GPU'yu %99 kullanan oyunlarda en az 30 dakika oynayın.

### Test Sonucuna Göre İnce Ayar (Troubleshooting):
* **Sistem Kilitlenirse / Siyah Ekran Verirse / Oyun Çökerse:** Voltaj gereğinden fazla düşürülmüştür. P-State 7 voltajını **+15 mV** artırın (Örn: 1000 mV yaptıysanız 1015 mV deneyin).
* **Sistem Sorunsuz Çalışırsa:** Dilerseniz voltajı **-10 mV** daha düşürerek (Örn: 990 mV) kartınızın sınırlarını zorlayabilirsiniz.

---

## Undervolt Öncesi ve Sonrası Karşılaştırma

| Değer | Stok (Fabrika) Ayarları | Undervolt Yapılmış Ayarlar |
| :--- | :--- | :--- |
| **GPU Çekirdek Voltajı** | ~1150 mV - 1200 mV | **1000 mV** |
| **GPU Ortam Sıcaklığı** | 78°C - 85°C | **63°C - 68°C** |
| **Güç Tüketimi (TDP)** | ~135W - 150W | **90W - 105W** |
| **Fan Devri / Gürültü** | %75 - %90 (Yüksek) | **%45 - %55 (Sessiz)** |
| **Ortalama FPS** | Dalgalı (Throttling sebebiyle) | **Sabit ve Kararlı** |

---

## Önemli İpuçları ve Uyarılar

* **Radeon WattMan Sıfırlandı Hatası:** Bilgisayar beklenmedik şekilde kapanırsa AMD sürücüsü güvenlik amacıyla stok ayarlara döner. Kararlı ayarlarınızı bulduğunuzda AMD yazılımı içinden **"Profili Kaydet"** seçeneği ile ayarlarınızı `.xml` olarak yedekleyin.
* **MSI Afterburner Kullanımı:** Eğer AMD Software yerine MSI Afterburner kullanıyorsanız, `Core Voltage (mV)` kısmını kilit açma ayarlarından aktif edip **-50 mV ile -100 mV** arasında bir değer vererek aynı sonucu elde edebilirsiniz.