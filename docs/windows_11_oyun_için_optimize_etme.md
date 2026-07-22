# Windows 11 Oyun Optimizasyon Rehberi: FPS Artırma ve Minimum Gecikme (Latency) Ayarları

Windows 11, modern mimarisi ve DirectX 12 Ultimate desteği ile güçlü bir oyun platformudur. Ancak varsayılan sistem ayarları, güvenlik ve arka plan hizmetlerine öncelik verdiği için maksimum oyun performansını engeller. Bu rehberde, Windows 11 işletim sistemini donanım seviyesinde oyunlar için optimize edecek teknik adımları bulacaksınız.

---

## 1. Çekirdek Sistem ve Güvenlik Ayarlarının Yapılandırılması

Windows 11'in sanallaştırma tabanlı güvenlik özellikleri, işlemci üzerinde ek yük oluşturarak kare hızlarında (FPS) %5 ila %15 arasında kayıplara neden olabilir.

### VBS (Virtualization-Based Security) ve Bellek Bütünlüğünü Devre Dışı Bırakma
Oyun odaklı bir sistemde maksimum işlemci verimi için bu özelliğin kapatılması önerilir.

1. **Başlat** menüsüne `Çekirdek Yalıtımı` (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Sistemi yeniden başlatın.

> **Teknik Not:** Bu ayar, virüslere karşı bir koruma katmanını kaldırır. Yalnızca güvenli yazılımlar kullanan oyuncular için önerilir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS, grafik belleği (VRAM) yönetimini işletim sisteminden alıp doğrudan GPU'ya devreder. Bu işlem gecikmeyi düşürür ve FPS kararlılığı sağlar.

1. `Ayarlar > Sistem > Ekran > Grafik Ayarları` yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** hale getirin.
4. Bilgisayarı yeniden başlatın.

---

## 2. Windows 11 Oyun Modu ve Grafik Tercihleri

### Oyun Modunu (Game Mode) Aktifleştirme
Windows 11'deki Oyun Modu, arka plan güncellemelerini durdurur ve CPU çekirdeklerini doğrudan çalışan oyuna atar.

* `Ayarlar > Oyun > Oyun Modu` sekmesine gidin ve ayarı **Açık** yapın.

### Harici Grafik Kartını Zorunlu Kılma (GPU Preference)
Özellikle çift ekran kartlı (Laptop) sistemlerde oyunların dahili GPU (Intel HD/AMD Radeon Vega) yerine harici GPU (Nvidia/AMD) kullanmasını sağlayın.

1. `Ayarlar > Sistem > Ekran > Grafik` bölümüne gidin.
2. Listeden oyununuzu seçin (Yoksa "Göz at" ile `.exe` dosyasını ekleyin).
3. **Seçenekler** butonuna tıklayıp **Yüksek Performans** (Harici GPU) modunu işaretleyin.

---

## 3. Güç Planı ve İşlemci Performans Yönetimi

Varsayılan "Dengeli" güç planı, işlemci frekansını sürekli değiştirerek oyunlarda anlık takılmalara (stuttering) yol açabilir.

### "Nihai Performans" (Ultimate Performance) Modunu Açma
Bu mod, sistemdeki tüm enerji tasarrufu kısıtlamalarını kaldırır.

1. **Komut İstemi'ni (CMD)** Yönetici olarak çalıştırın.
2. Şu kodu yapıştırın ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Denetim Masası > Güç Seçenekleri` bölümüne gidin ve yeni eklenen **Nihai Performans** planını seçin.

---

## 4. Ağ ve Gecikme (Ping / Latency) Optimizasyonu

Çevrimiçi oyunlarda veri paketlerinin iletim hızını artırmak için Windows ağ kısıtlamalarını kaldırın.

### Ağ Bağlantısı Kısıtlamasını Devre Dışı Bırakma (Registry Tweak)
1. `Win + R` tuşlarına basıp `regedit` yazın.
2. Şu yola gidin:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile`
3. **NetworkThrottlingIndex** değerine çift tıklayın ve değerini `ffffffff` (Hexadecimal) yapın.
4. **SystemResponsiveness** değerini `0` yapın.

### Nagle Algoritmasını Kapatma (TCP Ack Frequency)
Veri paketlerinin biriktirilerek gönderilmesini engelleyip, anlık iletilmesini sağlar.

1. `regedit` üzerinden şu yola gidin:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\`
2. Ağ kartınızın ID'sine ait klasörü bulun ve sağ taraftaki boşluğa sağ tıklayıp iki adet **DWORD (32-bit)** değeri oluşturun:
   * `TcpAckFrequency` -> Değer: `1`
   * `TCPNoDelay` -> Değer: `1`

---

## 5. Görsel Efektler ve Arka Plan Hizmetlerinin Temizliği

### Görsel Performans Ayarları
Windows 11'in animasyonları GPU ve RAM üzerinde ek yük oluşturur.

1. `Win + R` basıp `sysdm.cpl` yazın.
2. **Gelişmiş** sekmesinden Performans altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini seçin. (İsteğe bağlı olarak sadece "Ekran yazı tipi kenarlarını düzelt" seçeneğini açık bırakabilirsiniz).

### Başlangıç Uygulamalarını Devre Dışı Bırakma
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. **Başlangıç Uygulamaları** sekmesine gelin.
3. Oyun esnasında gerekli olmayan tüm uygulamaları (Spotify, Discord, OneDrive vb.) **Devre Dışı Bırakın**.

---

## 6. Sürücü ve Temel Güncellemeler

* **DDU (Display Driver Uninstaller) Kullanımı:** Grafik kartı sürücülerinizi güncellerken eski kalıntıları temizlemek için güvenli modda DDU kullanın ve en güncel WHQL sertifikalı sürücüyü kurun.
* **Chipset Sürücüleri:** Özellikle AMD Ryzen işlemcilerde, 3D V-Cache mimarisinden tam verim almak için güncel AMD Chipset sürücülerinin kurulması kritiktir.
* **Oyun İçi Kaplamaları (Overlay) Kapatın:** Discord Overlay, GeForce Experience In-Game Overlay ve Xbox Game Bar özelliklerini kullanmıyorsanız devre dışı bırakın.

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Beklenen Etki | Risk / Yan Etki |
| :--- | :--- | :--- |
| **VBS / Bellek Bütünlüğü Kapatma** | Yüksek FPS Artışı (%10+) | Düşük Güvenlik Seviyesi |
| **HAGS Aktifleştirme** | Düşük Gecikme, Stuttering Azalması | Yok (Modern GPU'larda) |
| **Nihai Performans Güç Planı** | Kararlı FPS, Sabit İşlemci Frekansı | Artan Güç Tüketimi / Sıcaklık |
| **Nagle Algoritması Kapatma** | Düşük Oyun İçi Ping (MS) | Yok |
| **Görsel Efekt Kapatma** | %1% ve %0.1 Low FPS İyileşmesi | Görsel Kalite Kaybı |