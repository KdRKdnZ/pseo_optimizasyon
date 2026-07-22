# Windows 11 Oyun Optimizasyon Rehberi: FPS Artırma ve Latency Düşürme

Windows 11, oyun içi performansı artırmak için tasarlanmış birçok yerleşik özellik sunar. Ancak varsayılan ayarlar her zaman maksimum kare hızını (FPS) ve en düşük girdi gecikmesini (input lag) hedeflemez. Bu rehber, Windows 11 işletim sisteminizi donanım seviyesinde oyunlar için optimize edecek teknik adımları içerir.

---

## 1. Çekirdek Yalıtımı (VBS / HVCI) Devre Dışı Bırakma

Windows 11'de güvenlik için varsayılan olarak açık gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Bellek Bütünlüğü (HVCI), CPU üzerinde yük oluşturarak oyunlarda %5 ila %15 arasında performans kaybına neden olabilir.

1. **BAŞLAT** menüsüne `Çekirdek Yalıtımı` (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Sistemi yeniden başlatın.

---

## 2. Windows Oyun Modu ve Donanım Hızlandırmalı GPU Zamanlaması (HAGS)

### Oyun Modunu Aktifleştirme
Oyun Modu, arka plan işlemlerini kısıtlayarak CPU ve RAM kaynaklarını doğrudan oyuna yönlendirir.

* `Ayarlar` > `Oyun` > `Oyun Modu` sekmesine gidin.
* **Oyun Modu** seçeneğini **Açık** konuma getirin.

### HAGS (Hardware-Accelerated GPU Scheduling)
HAGS, bellek yönetimini CPU'dan alıp doğrudan GPU'ya devreder. Bu işlem vRAM kullanımını optimize eder ve girdi gecikmesini azaltır.

1. `Ayarlar` > `Sistem` > `Ekran` > `Grafikler` yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** bağlantısına tıklayın.
3. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** hale getirin.
4. **Değişken Yenileme Hızı (VRR)** seçeneğini etkinleştirin.

---

## 3. "Nihai Performans" Güç Planını Etkinleştirme

Windows 11 varsayılan olarak "Dengeli" güç planı ile gelir. İşlemcinin çekirdek park etme (core parking) özelliğini kapatmak ve her an maksimum frekansta çalışmasını sağlamak için "Nihai Performans" (Ultimate Performance) modunu açın.

1. **Komut İstemi'ni (CMD)** Yönetici olarak çalıştırın.
2. Aşağıdaki kodu yapıştırın ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Denetim Masası` > `Donanım ve Ses` > `Güç Seçenekleri` sekmesine gidin.
4. Yeni eklenen **Nihai Performans** planını seçin.

---

## 4. Ekran Kartı Sürücüsü ve Kontrol Paneli Optimizasyonu

Sürücülerinizi DDU (Display Driver Uninstaller) ile güvenli modda temizleyip güncel tutmanız temel şarttır. Ardından GPU panellerinde aşağıdaki kritik ayarları uygulayın:

### NVIDIA Denetim Masası Ayarları
* **3D Ayarlarının Yönetilmesi** bölümüne gidin:
  * **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et
  * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra
  * **Doku Süzme - Kalite:** Yüksek Performans
  * **Dikey Senkronizasyon (V-Sync):** Kapalı (G-Sync kullanmıyorsanız)
  * **Maksimum Kare Hızı:** Monitör Hz değerinin 1-2 FPS altına sabitleyin (G-Sync aktifse).

### AMD Radeon Software Ayarları
* **Ekran Kartları** sekmesine gidin:
  * **Radeon Anti-Lag:** Etkin
  * **Radeon Boost:** Devre Dışı (Çözünürlük ölçekleme dalgalanmasını önlemek için)
  * **Doku Süzme Kalitesi:** Performans
  * **Yüzey Biçim Optimizasyonu:** Etkin

---

## 5. Ağ Latansı ve Ping Optimizasyonu (Nagle Algoritmasını Kapatma)

Online oyunlarda paketin gönderilmeden önce biriktirilmesini sağlayan Nagle algoritmasını Kayıt Defteri (Registry) üzerinden kapatmak gecikmeyi (ping) düşürür.

1. `Win + R` tuşlarına basıp `regedit` yazın.
2. Şu yola gidin: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\`
3. Alt klasörler arasından IP adresinizin bulunduğu doğru ağ bağdaştırıcısı GUID klasörünü bulun.
4. Boş bir yere sağ tıklayıp iki adet **DWORD (32 Bit) Değeri** oluşturun:
   * ad: `TcpAckFrequency` -> Değer: `1` (Hexadecimal)
   * ad: `TCPNoDelay` -> Değer: `1` (Hexadecimal)

---

## 6. Depolama ve DirectStorage Yapılandırması

Windows 11, NVMe SSD'ler için tasarlanmış DirectStorage teknolojisini destekler. Oyunların yükleme sürelerini ve render takılmalarını (stuttering) önlemek için depolama biriminizi optimize edin.

### TRIM Etkinleştirme
NVMe ve SATA SSD'lerin performansını korumak için TRIM komutunun aktif olduğunu doğrulayın:

1. CMD'yi Yönetici olarak açın.
2. Kodu çalıştırın:
   ```cmd
   fsutil behavior query DisableDeleteNotify
   ```
3. Sonuç `NTFS DisableDeleteNotify = 0` şeklinde görünmelidir. `1` ise aşağıdaki kodla aktifleştirin:
   ```cmd
   fsutil behavior set DisableDeleteNotify 0
   ```

---

## 7. Sistem Görsel Efektlerini ve Arka Plan Hizmetlerini Kısma

Görsel efektler GPU ve RAM üzerinde gereksiz iş yükü yaratır.

1. `Win + R` yapıp `sysdm.cpl` yazın.
2. **Gelişmiş** sekmesinden Performans altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini işaretleyin.
4. Sadece **Ekran yazı tipi kenarlarını düzelt** seçeneğini açık bırakarak uygulayın.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
Sık oynadığınız oyunların `.exe` dosyasına sağ tıklayın:
* `Özellikler` > `Uyumluluk` sekmesine gidin.
* **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
* **Yüksek DPI ayarlarını değiştir** butonuna basıp **Yüksek DPI ölçekleme davranışını geçersiz kıl** seçeneğini aktif edin.

---

## Özet Performans Kontrol Listesi

| Parametre | İdeal Durum | Etki Alanı |
| :--- | :--- | :--- |
| **Bellek Bütünlüğü (HVCI)** | Kapalı | CPU Performansı / FPS |
| **Oyun Modu & HAGS** | Açık | GPU Verimliliği / Latency |
| **Güç Planı** | Nihai Performans | Çekirdek Park Etme Engeli |
| **Nagle Algoritması** | Pasif (Registry tweak) | Ağ Ping / Ağ Paket İletimi |
| **Sürücüler** | DDU ile Güncel | Sistem Kararlılığı / FPS |