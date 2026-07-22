# RTX 4060 Undervolt Rehberi: Detaylı Ayarlar, Adım Adım Uygulama ve Performans Testleri

Nvidia’nın Ada Lovelace mimarisine sahip **GeForce RTX 4060** ekran kartı, varsayılan ayarlarında oldukça verimli çalışsa da üreticiler sistem kararlılığını garanti altına almak için karta gereğinden fazla voltaj (sıkça 1.025V - 1.050V arası) verir. **RTX 4060 undervolt ayarları** ile kartın performansından ödün vermeden (hatta bazen performans artışı sağlayarak) güç tüketimini düşürmek, sıcaklıkları 5-10°C arası azaltmak ve fan sesini minimuma indirmek mümkündür.

Bu makalede, RTX 4060 için en ideal voltaj-frekans değerlerini, adım adım undervolt yapma sürecini ve kararlılık testlerini bulacaksınız.

---

## Undervolt Nedir ve RTX 4060 için Neden Gereklidir?

Undervolt; ekran kartının grafik çekirdeğine (GPU) sağlanan voltajı, çekirdek saat hızlarını (Core Clock) koruyarak düşürme işlemidir. 

**RTX 4060’ta Undervolt Yapmanın Avantajları:**
* **Düşük Güç Tüketimi:** Stok halde 115W TGP değerine ulaşan kart, undervolt sonrası 80W - 90W bandında çalışır.
* **Daha Az Isınma:** Sıcaklıklar yüke bağlı olarak ortalama **6-10°C** düşer.
* **Daha Sessiz Fanlar:** Isı düştüğü için fan devir hızları azalır, sistem sessizleşir.
* **Sabit Saat Hızları (Termal Throttling Önleme):** Isınma azaldığı için GPU boost frekansını düşürmez ve daha kararlı bir FPS eğrisi sunar.

---

## Gerekli Yazılımlar

İşleme başlamadan önce aşağıdaki ücretsiz yazılımları indirin:

1. **MSI Afterburner:** Voltaj ve frekans eğrisini (VF Curve) düzenlemek için temel araç.
2. **GPU-Z / HWiNFO64:** Voltaj, sıcaklık ve güç tüketimi değerlerini anlık izlemek için.
3. **FurMark veya 3DMark (Time Spy):** Sistem kararlılığını ve yük altındaki değerleri test etmek için.
4. **Ağır Bir Oyun:** (Örn: *Cyberpunk 2077*, *Red Dead Redemption 2* veya *Control*) Realistik testler için.

---

## En İdeal RTX 4060 Undervolt Değerleri (Profil Tavsiyeleri)

Silikon kalitesi (Silicon Lottery) her kartta farklılık gösterse de, RTX 4060 çiplerinin büyük çoğunluğu belirli voltaj aralıklarında son derece kararlı çalışır.

> **Not:** Stok RTX 4060 modelleri genellikle **2500 MHz - 2700 MHz** arası boost frekansına sahiptir.

### 1. Denge Profili (Önerilen - Sweet Spot)
* **Hedef Frekans:** 2650 MHz - 2700 MHz
* **Hedef Voltaj:** 950 mV (0.950V)
* **Sonuç:** Stok performans veya %1-2 performans artışı, ~85W güç tüketimi, ~60°C sıcaklık.

### 2. Maksimum Verimlilik Profili (Ultra Düşük Sıcaklık)
* **Hedef Frekans:** 2500 MHz - 2550 MHz
* **Hedef Voltaj:** 900 mV (0.900V)
* **Sonuç:** %2-3 performans kaybı karşılığında ultra düşük güç tüketimi (~75W-80W) ve buz gibi çalışan GPU (~55°C).

---

## Adım Adım RTX 4060 Undervolt Nasıl Yapılır?

### Adım 1: Mevcut Stok Değerleri Belirleyin
1. **MSI Afterburner** ve **GPU-Z** programlarını açın.
2. Arka planda **FurMark** veya bir oyun çalıştırarak kartı %100 yüke sokun.
3. Kartın stok halde ulaştığı **maksimum çekirdek frekansını (MHz)** ve **voltaj değerini (mV)** not edin. (Örn: 2715 MHz @ 1035 mV).

### Adım 2: Voltaj/Frekans Eğrisini (VF Curve) Açın
1. MSI Afterburner arayüzünü sıfırlayın (Reset butonuna basın).
2. Klavyenizden **`CTRL + F`** tuşlarına basarak **Curve Editor** (Eğri Düzenleyici) penceresini açın.

### Adım 3: Frekans Offset Değerini Ayarlayın
1. Ana MSI Afterburner ekranındaki **Core Clock (MHz)** değerini **`-150 MHz`** veya **`-200 MHz`** olarak değiştirip "Apply" (Onayla) butonuna basın. 
2. Bu işlem tüm eğriyi aşağı çekecektir.

### Adım 4: Hedef Voltaj Noktasını Sabitleyin
1. Eğri ekranında (Curve Editor) yatay eksende **`950 mV`** noktasını bulun.
2. `950 mV` üzerindeki kare noktayı fare ile tutarak dikey eksende **`2650 MHz`** (veya kartınızın stok frekansı ne ise ona) seviyesine kadar yukarı sürükleyin.
3. MSI Afterburner ana ekranındaki **"Apply" (Tık/Onay)** butonuna basın.
4. **Önemli:** Onayladıktan sonra `950 mV` noktasından sonraki tüm çizginin düz bir yatay çizgi haline geldiğini göreceksiniz. Bu, GPU'nun 950 mV voltajı ve 2650 MHz frekansını aşmayacağı anlamına gelir.

```text
Grafik Görünümü (Temsili):
Frekans (MHz)
  |
2650 |               /-------------------- (Düz Çizgi)
  |              /
  |             /
  +------------+--------------------------
             950 mV                   Voltaj
```

### Adım 5: Bellek Owerclock (Memory Clock) Ekleme (Opsiyonel)
RTX 4060'ın bellek bant genişliğini artırmak undervolt işleminden kazanılan performansı pekiştirir:
* **Memory Clock (MHz):** `+1000 MHz` veya `+1200 MHz` ekleyebilirsiniz. Micron/Samsung bellekler bu artışı rahatlıkla kaldırır.

---

## Kararlılık Testi ve İnce Ayar (Stability Testing)

Ayarları uyguladıktan sonra sistemin çöküp çökmediğini doğrulamanız gerekir.

1. **FurMark Testi:** 15-20 dakika boyunca FurMark stress testini çalıştırın.
2. **Oyun Testi:** Ağır bir oyunda (Örn: Cyberpunk 2077 Ray Tracing açık şekilde) en az 30 dakika oynayın.

### Muhtemel Senaryolar ve Çözümleri:
* **Sistem Kilitleniyor / Oyun Kapanıyor (Crash):** Seçilen voltaj (950mV), belirlenen frekans (2650MHz) için yetersiz gelmiştir. 
  * *Çözüm:* Frekansı 2600 MHz'e düşürün veya voltajı 965 mV seviyesine çıkarın.
* **Ekranda Görüntü Bozulmaları (Artifact) Oluşuyor:** Memory Clock fazla yükseltilmiştir.
  * *Çözüm:* Memory Clock değerini +1000 MHz'den +750 MHz seviyesine çekin.
* **Sistem Sorunsuz Çalışıyor:** İşlem başarılıdır. İsterseniz voltajı adım adım (935 mV -> 925 mV) düşürerek sınırları zorlayabilirsiniz.

---

## Sonuçların Karşılaştırılması (Stok vs Undervolt)

Ortalama bir RTX 4060 modelinde elde edilen tipik test verileri şu şekildedir:

| Parametre | Stok Ayarlar | Undervolt (950mV @ 2650MHz) | Fark / Kazanç |
| :--- | :--- | :--- | :--- |
| **Çekirdek Voltajı** | ~1.035 V | 0.950 V | **-0.085 V** |
| **Güç Tüketimi (TGP)**| 115 W | 88 W | **~%23 Tasarruf** |
| **GPU Sıcaklığı** | 69°C - 72°C | 60°C - 62°C | **7-10°C Düşüş** |
| **Fan Devri (RPM)** | ~1800 RPM | ~1200 RPM | **Belirgin Ses Azalması** |
| **3DMark Time Spy** | ~10.400 Puan | ~10.550 Puan | **+%1.4 Performans** |

---

## Özet ve Profili Kaydetme

Ayarın kalıcı olması için MSI Afterburner ekranındaki **Disket** simgesine basıp bir profil numarasına (örneğin 1) kaydedin. Ardından sol üstteki **"Windows logosu"** simgesini aktif hale getirin. Böylece bilgisayar her açıldığında RTX 4060 undervolt ayarlarınız otomatik olarak yüklenecektir.