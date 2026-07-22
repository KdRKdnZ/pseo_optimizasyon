---
title: "RTX 4060 undervolt ayarları"
description: "RTX 4060 undervolt ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# RTX 4060 Undervolt Ayarları Rehberi: Düşük Sıcaklık ve Maksimum Verim

Nvidia’nın Ada Lovelace mimarisine sahip **GeForce RTX 4060**, varsayılan ayarlarında oldukça verimli bir ekran kartıdır. Ancak fabrika çıkışı voltaj haritaları (V-F Curve), silikon kalitesi fark etmeksizin tüm çipleri kararlı çalıştırmak adına gereğinden fazla voltaj çeker. **RTX 4060 undervolt (voltaj düşürme)** işlemi ile kartın performansını kaybetmeden (veya artırarak) sıcaklık değerlerini **8-15°C** düşürmek, güç tüketimini ise **%20-30** oranında azaltmak mümkündür.

Bu rehberde, masaüstü ve dizüstü (Mobile) RTX 4060 kartlar için adım adım en stabil undervolt parametrelerini ve uygulama yöntemlerini bulacaksınız.

---

## RTX 4060 için Neden Undervolt Yapılmalı?

*   **Düşük Güç Tüketimi:** Stok halde 115W-120W civarında çalışan masaüstü RTX 4060, undervolt sonrası **80W - 95W** seviyelerine iner.
*   **Düşük Sıcaklık ve Fan Sesi:** Voltaj azaldıkça GPU çekirdek sıcaklığı düşer, fan devri azalarak sistem daha sessiz çalışır.
*   **Sabit Çekirdek Hızı (Throttling Önleme):** Yüksek sıcaklık nedeniyle oluşan frekans düşmelerinin (Thermal Throttling) önüne geçilir ve minimum FPS değerleri iyileşir.

---

## Gerekli Yazılımlar

Undervolt işlemine başlamadan önce aşağıdaki araçları indirin:

1.  **MSI Afterburner:** Voltaj ve frekans eğrisini düzenlemek için.
2.  **HWiNFO64:** Voltaj, sıcaklık ve güç tüketimini anlık izlemek için.
3.  **Superposition Benchmark / FurMark / Cyberpunk 2077:** Stabilite testleri için.

---

## RTX 4060 Undervolt Ayarları (Adım Adım)

### Adım 1: MSI Afterburner Hazırlığı
1.  MSI Afterburner programını açın.
2.  `Settings` (Ayarlar) menüsünden **"Unlock Voltage Control"** (Voltaj Kontrolünü Aç) ve **"Unlock Voltage Monitoring"** seçeneklerini işaretleyin.
3.  Ana ekrana dönüp `Core Clock` değerini **0** konumuna getirin (Reset butonuna basın).

### Adım 2: Voltaj-Frekans Eğrisini (V-F Curve) Açma
1.  Klavyenizden **Ctrl + F** kombinasyonuna basarak **Voltage/Frequency Curve Editor** penceresini açın.
2.  Sol eksen çekirdek hızını (MHz), alt eksen ise milivolt (mV) cinsinden voltajı gösterir.

### Adım 3: Optimal Profil Ayarı (En Çok Tercih Edilen "Sweet Spot")

RTX 4060 için ortalama silikon kalitesinde en başarılı sonuç veren **"Tatlı Nokta" (Sweet Spot)** değerleri şunlardır:

> **Hedef:** 925 mV voltajda 2600 MHz - 2650 MHz Çekirdek Hızı.

1.  Curve Editor penceresindeyken klavyeden `Shift` tuşuna basılı tutarak tüm eğriyi seçin ve farenizle eğriyi biraz aşağı çekin (veya Core Clock alanına **-150 MHz** yazıp Enter'a basın).
2.  Eğri üzerinde **925 mV** noktasına denk gelen dikey çizgiyi bulun.
3.  925 mV üzerindeki noktayı tıklayıp yukarı doğru çekerek **2610 MHz** (veya kartınızın stok boost frekansı neyse o seviyeye) getirin.
4.  925 mV noktasını seçtikten sonra `Shift + Enter` basarak sabitleyin veya üst menüden **"Apply" (Uygula - Tik işareti)** ikonuna tıklayın.
5.  925 mV seviyesinden sonraki tüm voltaj noktalarının düz bir çizgi halinde sabitlendiğini göreceksiniz.

---

## RTX 4060 için Önerilen Undervolt Profil Seçenekleri

Her GPU çipinin silikon kalitesi (Silicon Lottery) farklıdır. Aşağıdaki tablodan kartınıza en uygun profili deneyerek seçebilirsiniz:

| Profil Türü | Hedef Voltaj (mV) | Çekirdek Hızı (MHz) | VRAM Clock (Memory) | Kullanım Amacı |
| :--- | :--- | :--- | :--- | :--- |
| **Dengeli (Önerilen)** | **925 mV** | **2550 - 2625 MHz** | +800 MHz | Maksimum verimlellik, düşük sıcaklık. |
| **Agresif Tasarruf** | **875 mV - 900 mV** | **2400 - 2500 MHz** | +500 MHz | Laptoplar ve mini-ITX kasalar için. |
| **Performans Odaklı** | **950 mV - 975 mV** | **2700 - 2750 MHz** | +1000 MHz | Stok performansı aşıp sıcaklığı koruma. |

*Not: Ada Lovelace mimarisinde GDDR6 bellekler yüksek hız aşırtma potansiyeline sahiptir. Voltajı düşürdükten sonra `Memory Clock` değerine **+500 MHz ile +1000 MHz** arasında ekleme yapmak, düşen bant genişliğini telafi eder ve FPS artışı sağlar.*

---

## Stabilite Testi ve Hata Giderme

Yapılan ayarların oyunlarda çökme yapmayacağından emin olmak için test adımları:

1.  **Benchmarking:** *Unigine Superposition* testini 1080p Extreme ayarlarında çalıştırın.
2.  **Oyun Testi:** Ray Tracing ve DLSS 3 açık şekilde *Cyberpunk 2077* veya *Alan Wake 2* gibi ağır bir oyunu en az 30 dakika oynayın.

### Karşılaşılabilecek Durumlar ve Çözümleri:
*   **Oyun Donuyor / Masaüstüne Atıyor (Crash):** Seçilen voltaj (örneğin 925 mV), belirlenen frekans (2610 MHz) için yetersizdir.
    *   *Çözüm:* Frekansı **20-30 MHz düşürün** (Örn: 2580 MHz yapın) veya voltajı **935 mV** seviyesine çekin.
*   **Ekranda Renk Bozulmaları (Artifact):** VRAM (Memory Clock) fazla zorlanmıştır.
    *   *Çözüm:* Memory Clock değerini 100-200 MHz aşağı çekin.

---

## Sonuç: Stok Değerler vs Undervolt Karşılaştırması

Ortalama bir masaüstü RTX 4060 sistemde elde edilen test verileri:

```text
STOK AYARLAR:
- Voltaj: ~1.035 mV
- Çekirdek Hızı: 2530 MHz (Dalgalı)
- GPU Sıcaklığı: 69°C - 72°C
- Güç Tüketimi: 115W

UNDERVOLT (925 mV @ 2610 MHz + +800 Memory):
- Voltaj: 0.925 mV (Sabit)
- Çekirdek Hızı: 2610 MHz (Kilitli/Sabit)
- GPU Sıcaklığı: 58°C - 61°C (-11°C Düşüş)
- Güç Tüketimi: 88W (%23 Tasarruf)
- FPS Değişimi: +%2 ile +%4 (Artış)
```

Testler sonucunda başarılı olduğunuz profili MSI Afterburner üzerindeki kilit simgesine basıp **Profile 1** olarak kaydedin ve "Apply at Windows Startup" seçeneğini aktif edin.