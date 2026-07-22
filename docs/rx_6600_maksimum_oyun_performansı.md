# AMD Radeon RX 6600 Maksimum Oyun Performansı Rehberi: Donanım, BIOS ve Sürücü Optimizasyonu

AMD Radeon RX 6600, RDNA 2 mimarisi ve 8 GB GDDR6 bellek yapısıyla 1080p çözünürlükte en yüksek fiyat/performans oranını sunantran ekran kartlarından biridir. Ancak fabrika çıkışı (stock) ayarlarda kart, tam potansiyelinin %10 ila %20 altında çalışır. Bu rehberde; doğru BIOS yapılandırması, undervolt/overclock değerleri, AMD Adrenalin yazılım optimizasyonu ve sistem bileşenleri entegrasyonu ile RX 6600’den alınabilecek **maksimum oyun performansını** teknik detaylarıyla inceliyoruz.

---

## 1. Donanım Mimari Özellikleri ve Limitler

RX 6600'ün sınırlarını zorlamadan önce mimari yapısını anlamak gerekir:

*   **Grafik Çekirdeği:** Navi 23 XL
*   **İşlem Birimi (CU):** 28
*   **Akış İşlemcisi (Stream Processors):** 1792
*   **Sonsuz Önbellek (Infinity Cache):** 32 MB
*   **Veri Yolu Genişliği:** 128-bit (PCIe 4.0 x8 şeridi)
*   **TDP / TBP:** 132 Watt

> **Teknik Kritik:** Kartın PCIe 4.0 x8 veri yolunu kullanması, PCIe 3.0 anakartlarda bant genişliği sınırına takılmasına neden olabilir. Maksimum performans için anakart ve işlemci tarafında PCIe 4.0 desteği kritik rol oynar.

---

## 2. BIOS Seviyesinde Optimizasyon: Smart Access Memory (SAM)

RX 6600’ün karesel performansını (FPS) doğrudan %5-15 artıran en önemli teknoloji **Smart Access Memory (SAM)**'dir. İşlemcinin (CPU) VRAM’in tamamına tek seferde erişmesini sağlayan bu özelliği aktif etmek için BIOS adımları:

1.  Anakart BIOS’una girin (DEL veya F2 tuşu ile).
2.  **Advanced / PCI Subsystem Settings** menüsüne gidin.
3.  **Above 4G Decoding** seçeneğini `Enabled` yapın.
4.  **Re-Size BAR Support** seçeneğini `Auto` veya `Enabled` konuma getirin.
5.  CSM (Compatibility Support Module) modunu kapatıp **UEFI** modunu etkinleştirin.

---

## 3. AMD Software: Adrenalin Edition İdeal Ayarları

Sürücü ayarlarının yanlış yapılandırılması, giriş gecikmesine (input lag) ve kare hızı düşüşlerine yol açar. Maksimum performans için aşağıdaki ayarları uygulayın:

### Ekran Kartı (Graphics) Sekmesi
*   **Radeon Anti-Lag:** `Etkin` (Giriş gecikmesini düşürür).
*   **Radeon Chill:** `Devre Dışı` (Performansı kısıtlamaması için).
*   **Radeon Boost:** `Devre Dışı` (Dinamik çözünürlük ölçekleme görüntü kalitesini bozar).
*   **Radeon Image Sharpening (RIS):** `Etkin` (%80 netlik - FSR kullanıldığında oluşan bulanıklığı giderir).
*   **Dikey Yenileme İçin Bekleyin (VSync):** `Her Zaman Devre Dışı`.
*   **Doku Süzme Kalitesi:** `Performans`.
*   **Yüzey Biçim Eniyilemesi:** `Etkin`.

---

## 4. RX 6600 Undervolt ve Overclock (Maksimum Saat Hızı)

RX 6600, güç limitine (Power Limit) çabuk takılan bir karttır. **Undervolt (Voltaj Düşürme)** işlemi, kartın çekirdek sıcaklığını düşürerek *Throttling* (ısıya bağlı frekans kısma) yaşanmasını engeller ve yüksek frekanslarda stabil kalmasını sağlar.

AMD Adrenalin > Performance > Tuning sekmesinden "Manual" moda geçerek şu değerleri uygulayın:

### Stabil Overclock / Undervolt Profili:

| Parametre | Stok Değer | Maksimum Performans Değeri |
| :--- | :--- | :--- |
| **GPU Minimum Frekans** | 500 MHz | **2350 MHz** |
| **GPU Maksimum Frekans** | 2491 MHz | **2650 - 2700 MHz** |
| **GPU Voltajı** | 1150 mV | **1050 - 1075 mV** |
| **VRAM Zamanlaması** | Standart | **Fast Timing (Hızlı Zamanlama)** |
| **VRAM Maks Frekans** | 1750 MHz | **1880 - 1900 MHz** |
| **Güç Limiti (Power Limit)**| %0 | **+%20** |

> **Uyarı:** Her silikon kalitesi farklıdır. Değerleri uyguladıktan sonra *3DMark Time Spy* veya *FurMark* testleri ile stabiliteyi kontrol edin. Çökme durumunda voltajı 10'ar mV artırın.

---

## 5. 1080p Maksimum Oyun Performansı Verileri (Benchmark)

Optimizasyonlar (SAM + Overclock + Undervolt) uygulandıktan sonra elde edilen ortalama FPS değerleri:

| Oyun | Çözünürlük ve Grafik Ayarı | Stok FPS | Optimizasyonlu FPS | FSR 2/3 / AFMF Etkin FPS |
| :--- | :--- | :--- | :--- | :--- |
| **Cyberpunk 2077** | 1080p / High (RT Kapalı) | 62 FPS | **74 FPS** | **105 FPS (FSR Quality)** |
| **Red Dead Redemption 2**| 1080p / Ultra | 58 FPS | **69 FPS** | **84 FPS (FSR Quality)** |
| **Call of Duty: Warzone 3**| 1080p / Competitive | 105 FPS | **128 FPS** | **175 FPS (AFMF Açık)** |
| **CS2** | 1080p / High | 210 FPS | **255 FPS** | - |
| **Starfield** | 1080p / Medium | 48 FPS | **57 FPS** | **82 FPS (FSR3 + FG)** |

---

## 6. Maksimum Performansı Engelleyen Sistem Darboğazları

RX 6600 ekran kartından %100 verim almak için sistemin geri kalanının şu şartları karşılaması gerekir:

1.  **İşlemci (CPU):** RX 6600, 1080p'de işlemciye yük bindirir. Minimum Ryzen 5 3600 veya i5-10400F gereklidir. Tam performans için **Ryzen 5 5600** veya **i5-12400F** idealdir.
2.  **Bellek (RAM):** Çift kanal (Dual Channel) 2x8 GB 3200 MHz/3600 MHz RAM kullanımı şarttır. Tek kanal (Single Channel) RAM kullanımı minimum FPS (1% Low FPS) değerlerini düşürerek anlık takılmalara (stutter) yol açar.
3.  **Depolama:** NVMe M.2 SSD kullanımı, oyunlarda kaplama yükleme (texture streaming) takılmalarını engeller.

---

## Özet Performans Kontrol Listesi

* [x] BIOS üzerinden **Smart Access Memory (SAM)** açıldı.
* [x] PCIe modu anakart üzerinden **Gen 4** olarak doğrulandı.
* [x] Windows Ayarları > Grafik Ayarları > **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** kapatıldı/açıldı (Oyuna göre test edilmeli).
* [x] AMD Adrenalin üzerinden **1060 mV / 2650 MHz** Undervolt + OC yapıldı.
* [x] VRAM **Fast Timing** moduna alındı.
* [x] FSR 2.0/3.0 destekleyen oyunlarda **Quality** mod eklendi.