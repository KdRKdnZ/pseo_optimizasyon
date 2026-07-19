---
title: rtx 4060 undervolt ayarları
description: rtx 4060 undervolt ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# RTX 4060 Undervolt Ayarları: Adım Adım Sıcaklık ve Güç Tüketimi Optimizasyon Rehberi

Nvidia'nın Ada Lovelace mimarisi üzerine inşa edilen RTX 4060, TSMC 4N (5nm) üretim süreci sayesinde halihazırda yüksek verimliliğe sahip bir grafik işlemcidir (GPU). Ancak, fabrikasyon çıkışlı voltaj-frekans eğrileri (V-F Curve), silikon kalitesindeki değişkenlikler (silikon piyangosu) göz önünde bulundurularak oldukça güvenli ve yüksek voltaj değerlerinde rezerve edilir. 

Bu rehberde, **RTX 4060 undervolt ayarları** ile kartınızın performansından ödün vermeden güç tüketimini nasıl %20-25 oranında azaltacağınızı, sıcaklık değerlerini nasıl 5-10°C düşüreceğinizi ve fan gürültüsünü nasıl minimize edeceğinizi teknik detaylarıyla açıklıyoruz.

---

## RTX 4060 İçin Neden Undervolt Yapılmalı?

Undervolt işlemi, GPU çekirdeğine giden voltajı düşürürken, çekirdeğin bu düşük voltajda kararlı bir şekilde çalışabileceği maksimum frekansı (Core Clock) manuel olarak ayarlama işlemidir. RTX 4060 özelinde bu işlemin avantajları şunlardır:

*   **Termal Kısıtlama (Thermal Throttling) Önleme:** Kartın daha serin çalışmasını sağlayarak boost frekanslarında daha uzun süre stabil kalmasına olanak tanır.
*   **Güç Tüketimi Optimizasyonu:** Ortalama 115W olan TDP değerini, performans kaybı olmaksızın 85W - 90W seviyelerine çekebilirsiniz.
*   **Akustik İyileşme:** Düşen sıcaklıklar, fan devir hızını (RPM) düşürür ve daha sessiz bir sistem elde edilir.
*   **Donanım Ömrü:** Düşük voltaj ve sıcaklık, GPU üzerindeki elektromigrasyonu azaltarak bileşen ömrünü uzatır.

---

## Undervolt İşlemi İçin Gerekli Araçlar

İşleme başlamadan önce aşağıdaki yazılımların güncel sürümlerini sisteminize kurun:

1.  **MSI Afterburner:** Voltaj ve frekans eğrisini düzenlemek için kullanılacak ana yazılım.
2.  **GPU-Z:** Sensör verilerini (Sıcaklık, Voltaj, Güç Tüketimi) anlık izlemek için.
3.  **Superposition Benchmark** veya **3DMark Time Spy:** Kararlılık testleri ve performans karşılaştırması için.
4.  **HWMonitor** veya **HWiNFO64:** Detaylı telemetri takibi için.

---

## Adım Adım RTX 4060 Undervolt Nasıl Yapılır?

### Adım 1: Mevcut Durum Analizi (Baseline Test)
Herhangi bir değişiklik yapmadan önce kartınızın fabrika çıkış değerlerini kaydetmeniz gerekir.

1.  **Superposition Benchmark** uygulamasını çalıştırın (1080p Extreme veya 4K Optimized preset önerilir).
2.  Test esnasında GPU-Z üzerinden **GPU Temperature**, **GPU Voltage (VDDC)**, **Board Power Draw** ve **GPU Clock** değerlerini not edin.
3.  *Örnek Referans Değerler:* Stok bir RTX 4060 genellikle ~1.025V - 1.050V voltajda, 2600 MHz - 2700 MHz frekans aralığında çalışır ve ~115W güç tüketir.

### Adım 2: MSI Afterburner Ayarlarını Yapılandırma
1.  MSI Afterburner'ı açın ve **Ayarlar (Gear simgesi)** menüsüne girin.
2.  "Genel" sekmesinde **"Voltaj kontrolünü aç"** ve **"Voltaj takibini aç"** seçeneklerini işaretleyin.
3.  Uygulamayı yeniden başlatın.

### Adım 3: Voltaj-Frekans (V-F) Eğrisini Düzenleme
Bu aşama, undervolt işleminin çekirdeğini oluşturur.

```
[Stok Eğri]     : Voltaj arttıkça frekans doğrusal yükselir (Örn: 1.050V -> 2650 MHz)
[Undervolt]     : Belirlenen hedef voltajda frekans sabitlenir (Örn: 0.900V -> 2550 MHz)
```

1.  MSI Afterburner ana ekranında **Core Clock (MHz)** değerini `-150 MHz` olarak ayarlayın ve "Uygula" (Apply) butonuna basın. (Bu işlem tüm eğriyi aşağı kaydırarak stabilite payı bırakır).
2.  Klavyeden **Ctrl + F** tuş kombinasyonuna basarak **Curve Editor (Eğri Düzenleyici)** penceresini açın.
3.  Yatay eksende (X) **Voltage** değerini, dikey eksende (Y) **Frequency** değerini göreceksiniz.
4.  X ekseninde **900 mV (0.900V)** noktasını bulun.
5.  Bu noktadaki kareyi dikey olarak **2550 MHz** (veya kartınızın stok boost frekansı ne ise) seviyesine kadar yukarı sürükleyin.
6.  Klavyeden **Shift** tuşuna basılı tutarak, 900 mV noktasının sağında kalan tüm alanı farenizle seçin.
7.  Seçili alandaki herhangi bir noktayı aşağı doğru sürükleyip ardından MSI Afterburner ana ekranındaki **"Apply" (Tik işareti)** butonuna basın.
8.  Eğri editörüne geri döndüğünüzde, 900 mV noktasından sonraki tüm çizginin düz bir hat (flat line) haline geldiğini göreceksiniz. Bu, GPU'nun 900 mV üzerine çıkmayacağını ve bu voltajda 2550 MHz frekansta çalışacağını gösterir.

---

## Kanıta Dayalı RTX 4060 Undervolt Profil Önerileri

Silikon kalitenize bağlı olarak uygulayabileceğiniz, test edilmiş iki farklı kararlı profil aşağıda tablolaştırılmıştır:

| Profil Türü | Hedef Voltaj (mV) | Hedef Frekans (MHz) | Güç Tüketimi (Ortalama) | Sıcaklık Değişimi | Performans Etkisi |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Profil 1: Sweet Spot (Önerilen)** | 900 mV | 2550 MHz | ~85W - 90W | -6°C ile -8°C | %0 (Eşit Performans) |
| **Profil 2: Maksimum Tasarruf** | 850 mV | 2460 MHz | ~75W - 80W | -10°C ile -12°C | -%2 ile -%3 Kayıp |

*Not: Bellek hızını (Memory Clock) +500 MHz ile +1000 MHz arasında artırmak, undervolt kaynaklı oluşabilecek minimal performans kayıplarını tamamen absorbe eder ve stok performansın üzerine çıkmanızı sağlar.*

---

## Kararlılık (Stability) Testi ve Sorun Giderme

Undervolt ayarlarının kararlılığını doğrulamak, sistemin oyun ortasında çökmesini (Crash-to-Desktop) önlemek için kritik öneme sahiptir.

### Kararlılık Testi Protokolü
1.  **Superposition Benchmark'ı** ardışık 3 kez çalıştırın. Eğer test esnasında ekranda yırtılma (artifact), donma veya doğrudan masaüstüne atma gerçekleşirse voltaj yetersiz demektir.
2.  **Cyberpunk 2077** veya **Alan Wake 2** gibi ağır Ray Tracing yükü barındıran oyunlarda 30 dakika test gerçekleştirin. Ray Tracing, voltaj hassasiyetini en çok tetikleyen unsurdur.

### Olası Sorunlar ve Çözümleri
*   **Sistem Dondu veya Siyah Ekran Verdi:** Bilgisayarı yeniden başlatın. MSI Afterburner ayarları henüz başlangıçta çalışacak şekilde kaydedilmediği için sistem stok ayarlarla açılacaktır. 
*   **Çözüm:** Voltajı aynı frekansta tutarak 15 mV artırın (Örn: 900 mV -> 915 mV) veya frekansı 30 MHz düşürün (Örn: 2550 MHz -> 2520 MHz).
*   **Performans Düştü (Clock Stretching):** Eğer voltajı çok fazla düşürürseniz, GPU çökmeden çalışabilir ancak dahili hata düzeltme mekanizmaları devreye girerek efektif saat hızını düşürür. Bunu GPU-Z üzerinden "Effective Clock" değerini takip ederek kontrol edin. Eğer efektif saat hızı, ayarladığınız saat hızından belirgin şekilde düşükse voltajı artırın.

Ayarların kararlılığından emin olduktan sonra, MSI Afterburner ana ekranındaki **"Startup"** (Windows logosu) butonuna basarak ayarların her sistem açılışında otomatik olarak uygulanmasını sağlayabilirsiniz.