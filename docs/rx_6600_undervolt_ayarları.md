# AMD Radeon RX 6600 Undervolt Rehberi: Optimal Voltaj ve Performans Ayarları

AMD Radeon RX 6600, RDNA 2 mimarisinin en verimli kartlarından biridir. Stok halde 132W TDP değerine sahip olan bu kart, fabrikasyon olarak güvenli marjlar sebebiyle gerekenden fazla voltaj (genellikle 1150 mV) ile gelir. **RX 6600 undervolt işlemi**, performanstan ödün vermeden (veya mimari izin verirse performansı artırarak) güç tüketimini 90-100W seviyelerine çekmeyi, sıcaklıkları 5-10°C düşürmeyi ve fan gürültüsünü en aza indirmeyi sağlar.

Bu rehberde, AMD Software: Adrenalin Edition üzerinden adım adım RX 6600 undervolt ayarlarını ve kararlılık testlerini bulabilirsiniz.

---

## Undervolt Öncesi Gereksinimler ve Araçlar

İşleme başlamadan önce aşağıdaki yazılımların güncel olduğundan emin olun:

1. **AMD Software: Adrenalin Edition:** Güncel GPU sürücüsü.
2. **HWiNFO64:** Detaylı sıcaklık (GPU Core, Hotspot/Sıcak Nokta, Memory) ve güç çekişi takibi için.
3. **Stress Testi Yazılımları:** 
   * *3DMark (Time Spy)* veya *Unigine Superposition* (Sentetik testler).
   * *FurMark* (Maksimum güç ve sıcaklık testi).
   * Ağır grafikli oyunlar (örneğin *Cyberpunk 2077*, *Red Dead Redemption 2*).

---

## Adım Adım RX 6600 Undervolt Ayarları

Undervolt ayarlarını yapmak için sürücü arayüzünü açın:  
`AMD Software -> Performans -> Ayarlanıyor (Tuning)` sekmesine gidin. Buradan **Özel (Custom)** seçeneğini işaretleyin.

```
+-------------------------------------------------------------------+
| NOT: Silikon kalitesi (Silicon Lottery) her kartta farklıdır.    |
| Aşağıdaki değerler RX 6600 çiplerinin %90'ında kararlı çalışan   |
| "Sweet Spot" (En Optimum) referans değerlerdir.                   |
+-------------------------------------------------------------------+
```

### 1. GPU Ayarları (GPU Tuning)
* **GPU Ayarlaması:** Etkin (Enabled)
* **Gelişmiş Kontrol:** Etkin (Enabled)
* **Minimum Frekans (MHz):** `2300` *(Stokta çok düşük olan min. frekansı yükseltmek takılmaları/stuttering engeller).*
* **Maksimum Frekans (MHz):** `2491` *(Stok değerde bırakabilir veya 2500-2550 MHz'e esnetebilirsiniz).*
* **Voltaj (mV):** **`1075`** *(Stok değer 1150 mV'dur. Adım adım düşüreceğiz).*

### 2. Bellek Ayarları (VRAM Tuning)
* **VRAM Ayarlaması:** Etkin (Enabled)
* **Gelişmiş Kontrol:** Etkin (Enabled)
* **Bellek Zamanlaması:** `Hızlı Zamanlama (Fast Timing)`
* **Maksimum Frekans (MHz):** `1850` veya `1900` *(Stok varsayılan 1750 MHz'dir. GDDR6 bellekler bu artışı rahatlıkla kaldırır ve bant genişliğini artırır).*

### 3. Fan Ayarları (Fan Tuning)
* **Fan Ayarlaması:** Etkin (Enabled)
* **Gelişmiş Kontrol:** Etkin (Enabled)
* **Zero RPM:** İsteğe bağlı (Boşta fanların durmasını istiyorsanız açık bırakın).
* **Fan Eğrisi:** Sıcak Nokta (Hotspot) 80°C'yi geçmeyecek şekilde ayarlanmalıdır. 
  * *Örnek Eğri:* 50°C -> %35 Fan | 65°C -> %45 Fan | 75°C -> %60 Fan.

### 4. Güç Ayarları (Power Tuning)
* **Güç Ayarlaması:** Etkin (Enabled)
* **Güç Limiti (%):** `+10%` veya `+15%` *(Voltajı düşürdüğümüz için güç limitini artırmak kartın fazla güç çekmesine sebep olmaz, aksine kilitlenen yüksek frekanslarda kartın güç limitine takılmasını önler).*

---

## Özet: Önerilen Başlangıç ve İleri Seviye Profil Tablosu

| Ayar Parametresi | Stok Değer | Güvenli Undervolt (Başlangıç) | Agresif Undervolt (Maksimum Verim) |
| :--- | :--- | :--- | :--- |
| **Min Çekirdek Hızı** | ~500 MHz | 2300 MHz | 2350 MHz |
| **Maks Çekirdek Hızı**| 2491 MHz | 2491 MHz | 2550 MHz |
| **Voltaj (mV)** | 1150 mV | **1075 mV** | **1025 mV - 1050 mV** |
| **VRAM Frekansı** | 1750 MHz | 1850 MHz (Fast Timing) | 1900 MHz (Fast Timing) |
| **Güç Limiti** | %0 | +%10 | +%15 |

---

## Kararlılık Testi ve İnce Ayar Prosedürü

Ayarları uyguladıktan sonra profilinizi sağ üstteki ikon üzerinden `.xml` formatında **kaydedin**. Sürücü çökmesi durumunda ayarlar varsayılana döner.

1. **Test 1 (Sentetik Yük):** *FurMark* uygulamasını açın ve 15 dakika boyunca 1080p çözünürlükte çalıştırın. 
   * **Kontrol:** HWiNFO64 üzerinden *GPU Temp* (hedef < 65°C) ve *GPU Hotspot Temp* (hedef < 80°C) değerlerini izleyin.
2. **Test 2 (Oyun Testi):** *Cyberpunk 2077* veya *RDR 2* gibi ekran kartını %100 kullanan bir oyuna girin. 1 saatlik kullanımda çökme, siyah ekran veya WattMan hatası yoksa işlem başarılıdır.

### Çökme veya WattMan Hatası Alırsanız:
* Sistem çökerse voltajı çok düşürmüşsünüz demektir. Voltajı **+10 mV** artırın (Örn: 1050 mV çöktüyse 1060 mV yapın).
* Bellek kaynaklı artifact (ekranda renkli kareler/çizgiler) görürseniz VRAM frekansını 1800 MHz seviyesine geri çekin.

---

## Beklenen Sonuçlar ve Performans Kazanımı

Başarılı bir RX 6600 undervolt işlemi sonrasında elde edilecek ortalama değerler:

* **Sıcaklık Düşüşü:** Çekirdek sıcaklığında 5-8°C, Hotspot sıcaklığında 10-12°C azalma.
* **Güç Tüketimi:** Stok halde 130-132W çeken kart, yük altında **90W - 105W** aralığına geriler (%25-30 güç tasarrufu).
* **FPS Değişimi:** Hızlı VRAM zamanlaması ve kararlı boost frekansları sayesinde FPS düşmez, aksine **%2 ila %5 arasında artış** gösterir.
* **Ses Seviyesi:** Fan devri düştüğü için sistem belirgin şekilde daha sessiz çalışır.