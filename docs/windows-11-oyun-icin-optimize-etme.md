---
title: windows 11 oyun için optimize etme
description: windows 11 oyun için optimize etme hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Oyun İçin Optimize Etme: Maksimum FPS ve Düşük Gecikme Süresi Rehberi

Windows 11, modern hibrit işlemci mimarileri (Intel Thread Director gibi) ve DirectStorage gibi yeni nesil API'ler için optimize edilmiş bir çekirdeğe (kernel) sahip olsa da, varsayılan yapılandırmasında arka planda çalışan güvenlik katmanları ve telemetri servisleri nedeniyle oyun performansında darboğazlar yaratabilir. 

Bu rehberde, **Windows 11 oyun için optimize etme** sürecini işletim sistemi mimarisi, donanım etkileşimi ve sürücü seviyesinde ele alarak, sisteminizi kararlı ve en yüksek FPS değerini verecek şekilde yapılandıracağız.

---

## Çekirdek Seviyesinde Optimizasyon: VBS ve HVCI Kapatma

Windows 11'de varsayılan olarak açık gelen Sanallaştırma Tabanlı Güvenlik (VBS - Virtualization-Based Security) ve Hipervizör Korumalı Kod Bütünlüğü (HVCI - Hypervisor-Protected Code Integrity), sistemi kötü amaçlı yazılımlardan korumak için donanım sanallaştırmasını kullanır. Ancak bu güvenlik katmanı, CPU üzerinde ek bir yük (overhead) oluşturarak oyunlarda %5 ile %15 arasında performans kaybına yol açar.

### Bellek Bütünlüğünü (HVCI) Devre Dışı Bırakma

1. Windows Arama çubuğuna **Cihaz Güvenliği** (Device Security) yazın ve uygulamayı açın.
2. **Çekirdek Yalıtım** (Core Isolation) detaylarına tıklayın.
3. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
4. Bilgisayarınızı yeniden başlatın.

*Kanıt:* Yapılan bağımsız donanım testleri (özellikle CPU limitli senaryolarda ve 1080p çözünürlükte), HVCI kapatıldığında minimum FPS (1% Low) değerlerinde ciddi bir kararlılık artışı olduğunu göstermektedir.

---

## Windows 11 Grafik ve Zamanlama Ayarlarını Yapılandırma

Windows 11, grafik işlemci (GPU) kaynaklarını yönetmek ve CPU üzerindeki zamanlama yükünü azaltmak için gelişmiş API'lere sahiptir. Bu ayarların doğru yapılandırılması, doğrudan kare hızına (FPS) ve giriş gecikmesine (input lag) etki eder.

### Oyun Modu (Game Mode) Aktifleştirme

Windows 11'deki Oyun Modu, eski Windows sürümlerinin aksine oldukça kararlı çalışmaktadır. Bu mod aktifken Windows, arka plan güncellemelerini askıya alır, CPU iş parçacığı (thread) önceliğini oyuna verir ve RAM üzerindeki gereksiz önbelleği temizler.

1. **Ayarlar > Oyun > Oyun Modu** yolunu izleyin.
2. Oyun Modu seçeneğini **Açık** hale getirin.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) ve VRR

HAGS (Hardware-Accelerated GPU Scheduling), bellek yönetimini CPU'dan alarak doğrudan GPU'nun kendi özel zamanlama işlemcisine devreder. Bu işlem, özellikle NVIDIA DLSS 3 Frame Generation teknolojisinin çalışması için zorunludur.

1. **Ayarlar > Sistem > Monitör > Grafik** bölümüne gidin.
2. **Varsayılan grafik ayarlarını değiştirin** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini aktif edin.
4. Varsa **Değişken yenileme hızı (VRR)** seçeneğini de aktif hale getirin (ekran yırtılmalarını önler ve gecikmeyi azaltır).

---

## Donanım ve Sürücü Seviyesinde Performans Artışı

Yazılımsal optimizasyonların donanım katmanıyla doğrudan iletişim kurabilmesi için PCIe veri yolu ve güç yönetimi ayarlarının optimize edilmesi gerekir.

### Resizable BAR (ReBAR) ve Smart Access Memory (SAM) Aktivasyonu

Resizable BAR, CPU'nun PCIe veri yolu üzerinden GPU'nun tüm VRAM (Video RAM) kapasitesine tek seferde erişmesini sağlar. Varsayılan olarak bu erişim 256 MB'lık bloklarla sınırlıdır.

1. Bilgisayarınızı yeniden başlatarak **BIOS/UEFI** ekranına girin.
2. **Advanced** veya **PCI Subsystem Settings** menüsünü bulun.
3. **Above 4G Decoding** ve **Re-Size BAR Support** seçeneklerini **Enabled** (Etkin) yapın.
4. Ayarları kaydedip Windows'u başlatın. GPU-Z programı üzerinden aktif olup olmadığını doğrulayabilirsiniz.

### Güç Planı Optimizasyonu: Nihai Performans (Ultimate Performance)

Windows 11'in standart "Yüksek Performans" planı, CPU çekirdeklerinin park edilmesini (core parking) tamamen engellemez. "Nihai Performans" modu ise mikrosaniyeler düzeyindeki gecikmeleri önlemek için donanım geçiş durumlarını (C-states) en aza indirir.

Bu gizli planı aktif etmek için:
1. Başlat menüsüne sağ tıklayıp **Terminal (Yönetici)** seçeneğini açın.
2. Aşağıdaki komutu yapıştırın ve Enter tuşuna basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Donanım ve Ses > Güç Seçenekleri** bölümüne giderek yeni eklenen **Nihai Performans** planını seçin.

---

## Arka Plan Süreçleri ve Gecikme (Latency) Optimizasyonu

İşletim sisteminin ağ yığını (network stack) ve arka plan servisleri, çevrimiçi oyunlarda paket kaybına (packet loss) ve yüksek ping değerlerine neden olabilir.

### Nagle Algoritmasını Devre Dışı Bırakarak Ping Süresini Düşürme

Nagle Algoritması, ağ üzerindeki küçük paketleri birleştirerek bant genişliğini optimize etmeye çalışır. Ancak bu durum, rekabetçi oyunlarda paketlerin gecikmeli gönderilmesine (yüksek ping) yol açar.

1. `Win + R` tuşlarına basıp `regedit` yazarak Kayıt Defteri Düzenleyicisi'ni açın.
2. Aşağıdaki dizine gidin:
   ```text
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\
   ```
3. Sol taraftaki alt klasörlerden (Interface ID'leri) aktif internet bağlantınızın IP adresini içeren klasörü bulun (sağ taraftaki `DhcpIPAddress` değerinden kontrol edebilirsiniz).
4. Bu klasörün içine sağ tıklayıp **Yeni > DWORD (32-bit) Değeri** oluşturun. Adını `TcpAckFrequency` yapın ve değerini `1` olarak ayarlayın.
5. Aynı yerde bir adet daha DWORD (32-bit) oluşturun, adını `TCPNoDelay` yapın ve değerini `1` olarak ayarlayın.
6. Değişikliklerin geçerli olması için sistemi yeniden başlatın.

### Başlangıç Uygulamalarını ve Telemetriyi Sınırlandırma

Windows 11 arka planda sürekli olarak Microsoft sunucularına veri (telemetri) gönderir. Bu durum hem CPU döngülerini tüketir hem de ağ trafiğinde anlık dalgalanmalara yol açar.

*   **Görev Yöneticisi (Ctrl + Shift + Esc) > Başlangıç Uygulamaları** sekmesine gidin. Discord, Steam, Spotify gibi uygulamaların Windows açılışında otomatik başlamasını engelleyin.
*   **Ayarlar > Gizlilik ve Güvenlik > Teşhis ve Geri Bildirim** menüsünden **İsteğe bağlı teşhis verilerini gönder** seçeneğini kapatın.

---

## Sonuç ve Performans Analizi

**Windows 11 oyun için optimize etme** adımları tamamlandığında, sisteminiz donanım kaynaklarını doğrudan oyun motoruna aktaracak şekilde yapılandırılmış olur. VBS/HVCI'nin kapatılması işlemci darboğazını azaltırken, HAGS ve ReBAR optimizasyonları ekran kartınızın veri işleme hızını maksimize eder. 

Bu optimizasyonların ardından, özellikle rekabetçi oyunlarda (Valorant, CS2, Apex Legends) %1 ve %0.1 Low FPS değerlerinizde (anlık takılmalar/stuttering) gözle görülür bir iyileşme ve daha akıcı bir oyun deneyimi elde edeceksiniz.