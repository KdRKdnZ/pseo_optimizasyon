---
title: "windows 11 oyun optimizasyon rehberi"
description: "windows 11 oyun optimizasyon rehberi hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Oyun Optimizasyon Rehberi: Maksimum FPS ve Düşük Gecikme

Windows 11, gelişmiş bellek yönetimi ve yeni nesil donanım desteği ile güçlü bir işletim sistemidir. Ancak, varsayılan kurulumda gelen birçok güvenlik, arka plan hizmeti ve görsel efekt, oyun performansını ve girdi gecikmesini (input lag) olumsuz etkiler. 

Bu rehber, Windows 11 işletim sistemini minimum sistem kaynağı tüketimi, maksimum FPS ve en düşük kare zamanı (frametime) dalgalanması için optimize edecek teknik adımları içermektedir.

---

## 1. Çekirdek İşletim Sistemi ve Güvenlik Ayarları

### VBS (Virtualization-based Security) ve HVCI'yi Devre Dışı Bırakma
Windows 11'de varsayılan olarak açık gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Bellek Bütünlüğü (HVCI), işlemci komut setlerine ek yük getirerek oyunlarda %5 ile %15 arasında FPS kaybına neden olur.

1. **Başlat** menüsüne `Çirdek Yalıtımı` (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Sistemi yeniden başlatın.

> **Teknik Not:** Bu ayar, çekirdek düzeyindeki güvenlik katmanını esnetir. Yalnızca güvenilir yazılımlar kullanan oyuncu bilgisayarları için kapatılması önerilir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) ve Pencereli Oyun Optimizasyonu
HAGS, VRAM yönetim yükünü CPU'dan alarak doğrudan GPU'ya devreder. Windows 11 ile gelen Pencereli Oyun Optimizasyonu ise DirectX 11 oyunlarının DirectX 12 benzeri düşük gecikmeli çalışmasını sağlar.

1. **Ayarlar > Sistem > Ekran > Grafik** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** yapın.
4. **Pencereli oyunlar için optimizasyonlar** seçeneğini **Açık** konuma getirin.

---

## 2. Windows Oyun Modu ve Güç Planı Optimizasyonu

### Oyun Modu (Game Mode) Yapılandırması
Windows 11'in Oyun Modu, Windows 10'a kıyasla daha kararlıdır. Arka plan işlemlerinin thread önceliğini düşürür ve oyun işlemine yüksek öncelikli CPU çekirdekleri atar.

* **Ayarlar > Oyun > Oyun Modu** adımlarını takip edin ve ayarı **Açık** hale getirin.
* **Yakalama (Captures)** sekmesine giderek **Arka planda kaydet** özelliğini **Kapalı** yapın.

### "Nihai Performans" (Ultimate Performance) Güç Planını Etkinleştirme
Yüksek performans güç planı, CPU çekirdeklerinin park edilmesini (core parking) önler ve işlemci frekansının anlık düşüşlerini engeller.

1. **Komut İstemi'ni (CMD)** Yönetici olarak çalıştırın.
2. Aşağıdaki kodu yapıştırın ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Güç Seçenekleri** bölümüne gidin.
4. Yeni eklenen **Nihai Performans** planını seçin.

---

## 3. Donanım ve Sürücü Seviyesinde Yapılandırma

### BIOS/UEFI Ayarları: XMP/EXPO ve ReBAR
Yazılımsal optimizasyonların etkili olabilmesi için donanımın tam kapasitede çalışması gerekir.

* **XMP / EXPO:** BIOS'a girerek RAM'lerinizin üretici tarafından vaat edilen frekans ve gecikme değerlerinde (CL) çalıştığından emin olun (Varsayılan JEDEC frekansında kalmamalıdır).
* **Resizable BAR (AMD Smart Access Memory):** CPU'nun GPU VRAM'inin tamamına tek seferde erişmesini sağlar. BIOS üzerinden `Re-Size BAR Support` ve `Above 4G Decoding` seçeneklerini **Enabled** yapın.

### GPU Sürücü Yapılandırması (NVIDIA Control Panel)
Grafik kartı panelindeki optimizasyonlar kare süresi kararlılığını doğrudan etkiler.

* **Bağlantılı Optimizasyon (Threaded Optimization):** Açık
* **Güç Yönetimi Modu:** Maksimum performansı tercih et
* **Düşük Gecikme Oranı Modu (Low Latency Mode):** On veya Ultra (NVIDIA Reflex desteklemeyen oyunlar için)
* **Doku Süzme - Kalite:** Yüksek Performans

---

## 4. Arka Plan Hizmetleri ve Ağ Gecikmesi (Ping) Optimizasyonu

### Gereksiz Hizmetleri ve Başlangıç Uygulamalarını Kapatma
Sistem kaynaklarını tüketen arka plan süreçlerini minimize edin.

1. **Görev Yöneticisi (Ctrl + Shift + Esc) > Başlangıç Uygulamaları** sekmesine gidin. Discord, Spotify, Steam gibi oyun esnasında şart olmayan tüm uygulamaları devre dışı bırakın.
2. `services.msc` komutu ile Hizmetler penceresini açın.
   * **SysMain (Superfetch):** SSD kullanan sistemlerde devre dışı bırakılabilir. RAM kullanımını düşürür.
   * **Connected User Experiences and Telemetry:** Devre dışı bırakın (Gizlilik ve CPU yükünü azaltır).

### Ağ Gecikmesini (Nagle Algoritması) Devre Dışı Bırakma
Nagle Algoritması, küçük veri paketlerini birleştirerek gönderir. Bu durum web gezintisinde verimlilik sağlasa da online oyunlarda ping süresini artırır.

1. **Win + R** basıp `regedit` yazın.
2. Aşağıdaki dizine gidin:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\`
3. İlgili ağ bağdaştırıcınızın GUID klasörünü bulun (içinde IP adresinizin olduğu klasör).
4. Sağ tıklayıp iki adet yeni **DWORD (32 bit) Değeri** oluşturun:
   * Isim: `TcpAckFrequency` -> Değer: `1` (Hexadecimal)
   * Isim: `TCPNoDelay` -> Değer: `1` (Hexadecimal)

---

## 5. Görsel Efektler ve Disk Temizliği

### Windows Görsel Efektlerini Minimuma İndirme
Windows 11'in akıcı pencere animasyonları GPU/CPU işleme kuyruğuna yük getirir.

1. **Win + R** tuşlarına basıp `sysdm.cpl` yazın.
2. **Gelişmiş** sekmesinden **Performans** altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini seçin.
4. Sadece **Ekran yazı tipi kenarlarını düzelt** ve **Simgeler yerine küçük resimler göster** seçeneklerini işaretleyip kaydedin.

### Geçici Dosyaları Temizleme (Storage Sense)
Oyun güncellemeleri ve Windows derlemeleri sonrası biriken önbellek dosyaları disk I/O performansını düşürür.

1. **Ayarlar > Sistem > Depolama** bölümüne gidin.
2. **Depolama Mantığı (Storage Sense)** özelliğini **Açık** konuma getirin.
3. **Geçici Dosyalar** sekmesine girerek `Windows Update Temizleme` ve `Gölgeli Kopya` verilerini silin.

---

## Özet Performans Kontrol Listesi

| Yapılandırılan Ayar | Hedef Etki | Risk / Yan Etki |
| :--- | :--- | :--- |
| **VBS / HVCI Kapatma** | +%5-15 FPS, Düşük Frametime | Çekirdek düzeyde güvenlik azalır |
| **HAGS & Pencereli Opt.** | VRAM yükü azalır, Düşük Input Lag | Yok |
| **Nihai Performans Planı** | CPU Throttle ve Stuttering önlenir | Güç tüketimi artar |
| **ReBAR / XMP** | Yüksek veri aktarım hızı, Yüksek FPS | BIOS müdahalesi gerektirir |
| **Nagle Algoritması Pasif** | Ağ paket gecikmesi (Ping) düşer | Yok |