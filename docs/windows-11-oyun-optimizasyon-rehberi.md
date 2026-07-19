---
title: windows 11 oyun optimizasyon rehberi
description: windows 11 oyun optimizasyon rehberi hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Oyun Optimizasyon Rehberi: Maksimum FPS ve Düşük Gecikme İçin Gelişmiş Ayarlar

Windows 11, modern oyun mimarileri (DirectX 12 Ultimate, DirectStorage, Auto HDR) için optimize edilmiş bir çekirdeğe sahip olsa da, varsayılan işletim sistemi yapılandırması maksimum oyun performansı için tasarlanmamıştır. Arka plan servisleri, sanallaştırma tabanlı güvenlik katmanları ve agresif güç tasarrufu algoritmaları, donanımınızın tam potansiyeline ulaşmasını engeller.

Bu teknik rehber, Windows 11 işletim sisteminizi kernel (çekirdek) seviyesinden sürücü katmanına kadar optimize ederek donanım darboğazlarını (bottleneck) minimuma indirmeyi ve girdi gecikmesini (input lag) en alt düzeye düşürmeyi amaçlamaktadır.

---

## Çekirdek Seviyesinde Windows 11 Optimizasyonu

Windows 11'in güvenlik odaklı mimarisi, oyunlarda CPU ve bellek alt sistemine ek yük getirir. Bu yükü azaltmak, oyun içi minimum FPS (1% ve 0.1% low) değerlerini doğrudan artırır.

### Sanallaştırma Tabanlı Güvenlik (VBS) ve HVCI Kapatma
Virtualization-Based Security (VBS) ve Hypervisor-Protected Code Integrity (HVCI / Çekirdek Yalıtımı), Windows 11'de varsayılan olarak etkindir. Bu özellikler, belleğin güvenli bir bölgesini izole etmek için donanım sanallaştırmasını kullanır. Ancak, CPU'nun bellek yönetim birimine (MMU) ek yük bindirerek oyunlarda **%5 ile %15 arasında performans kaybına** yol açar.

**VBS ve HVCI'ı Devre Dışı Bırakma Adımları:**
1. Başlat menüsüne **Çekirdek Yalıtımı** (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini "Kapalı" konuma getirin.
3. Başlat'a sağ tıklayıp *Terminal (Yönetici)* seçeneğini açın ve şu komutu çalıştırarak sanallaştırma tabanlı güvenliği tamamen kapatın:
   ```cmd
   bcdedit /set hypervisorlaunchtype off
   ```
4. Bilgisayarınızı yeniden başlatın.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) Aktivasyonu
Hardware-Accelerated GPU Scheduling (HAGS), video belleği (VRAM) yönetimini CPU'dan alarak doğrudan GPU'nun kendi özel zamanlama işlemcisine devreder. Bu işlem, CPU üzerindeki sürücü yükünü (driver overhead) azaltır ve girdi gecikmesini düşürür. Ayrıca, NVIDIA DLSS 3 Frame Generation teknolojisinin çalışması için bu ayarın açık olması zorunludur.

**HAGS Nasıl Etkinleştirilir?**
1. **Ayarlar > Sistem > Monitör > Grafik** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini "Açık" duruma getirin.

### Windows Oyun Modu (Game Mode) Yapılandırması
Windows 11'deki "Oyun Modu", işletim sisteminin iş parçacığı zamanlayıcısını (Thread Scheduler) optimize eder. Oyun modu etkinken, oyun işlemi (process) CPU üzerinde en yüksek önceliğe (High Priority) sahip olur ve arka plan işlemleri (Windows Update, telemetri vb.) askıya alınır.

*   **Ayarlar > Oyun > Oyun Modu** bölümüne gidin ve bu özelliği **Açık** konuma getirin.

---

## Donanım ve Sürücü Seviyesinde Optimizasyon

Yazılımsal optimizasyonların donanımla tam uyumlu çalışması için veri yolları ve güç yönetim şemaları optimize edilmelidir.

### CPU Çekirdek Park Etme (Core Parking) ve Güç Planları
Windows, enerji tasarrufu sağlamak amacıyla boşta duran CPU çekirdeklerini "park" moduna alır. Bir oyun aniden işlem gücü talep ettiğinde, park edilmiş çekirdeklerin uyanması milisaniyeler mertebesinde gecikmelere ve dolayısıyla anlık takılmalara (stuttering) neden olur.

**Nihai Performans (Ultimate Performance) Güç Planını Aktif Etme:**
Bu plan, donanım gecikmelerini en aza indirmek için tasarlanmış gizli bir Windows şemasıdır.

1. *Terminal (Yönetici)* ekranını açın.
2. Aşağıdaki komutu yapıştırıp Enter tuşuna basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Donanım ve Ses > Güç Seçenekleri** bölümüne gidin ve yeni eklenen **Nihai Performans** planını seçin.

### GPU Sürücü Temizliği (DDU) ve Kontrol Paneli Ayarları
Eski sürücü kalıntıları, Windows 11'in grafik alt sisteminde çakışmalara yol açar. Temiz bir kurulum için **Display Driver Uninstaller (DDU)** kullanılmalıdır.

**NVIDIA Denetim Masası Optimizasyonu:**
*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** "Açık" veya "Ultra" (CPU darboğazı varsa Ultra seçilmelidir; bu ayar kare kuyruğunu sıfırlayarak gecikmeyi azaltır).
*   **Güç Yönetimi Modu:** "Maksimum performansı tercih et" (GPU saat hızlarının oyun esnasında düşmesini engeller).
*   **Doku Süzme - Kalite:** "Yüksek Performans".

### Resizable BAR (ReBAR) ve DirectStorage Yapılandırması
*   **Resizable BAR:** CPU'nun PCIe veri yolu üzerinden GPU belleğinin (VRAM) tamamına tek seferde erişmesini sağlar. BIOS üzerinden *Above 4G Decoding* ve *ReBAR* seçenekleri etkinleştirilmelidir.
*   **DirectStorage:** NVMe SSD'nizdeki oyun varlıklarının (asset), CPU'yu bypass ederek doğrudan GPU'ya aktarılmasını sağlar. Bu teknolojiden tam yararlanmak için oyunların kurulu olduğu diskin **PCIe Gen3 veya üzeri bir NVMe SSD** olması ve dosya sisteminin **NTFS** olarak biçimlendirilmesi gerekir.

---

## Gelişmiş Kayıt Defteri (Registry) ve Sistem İnce Ayarları

İşletim sisteminin ağ ve işlem önceliklendirme algoritmalarını Kayıt Defteri üzerinden değiştirerek daha kararlı bir oyun deneyimi elde edebilirsiniz.

> **Önemli Uyarı:** Kayıt defterinde değişiklik yapmadan önce ilgili anahtarların yedeğini alınız.

### Network Throttling Index ve Ağ Gecikmesini (Ping) Azaltma
Windows, multimedya dışı ağ trafiğini sınırlayarak ağ kartı kaynaklarını korumaya çalışır. Çevrimiçi oyunlarda bu durum paket kaybına (packet loss) ve ping dalgalanmalarına yol açar.

1. `Win + R` tuşlarına basıp `regedit` yazarak Kayıt Defteri'ni açın.
2. Şu yola gidin:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile`
3. **NetworkThrottlingIndex** değerine çift tıklayın, taban değerini *Onaltılık (Hexadecimal)* yapın ve değer verisini `ffffffff` olarak değiştirin (bu işlem sınırlamayı devre dışı bırakır).
4. Aynı konumdaki **SystemResponsiveness** değerini `0` yapın (arka plan işlemlerine ayrılan CPU rezervasyonunu sıfırlar).

### FSE (Full-Screen Optimizations) ve Gecikme Yönetimi
Windows 11, klasik tam ekran modu yerine "Pencereli Tam Ekran" modunu optimize eden hibrit bir sunum modeli kullanır. Ancak bazı DirectX 11 ve eski oyunlarda bu durum girdi gecikmesine yol açar.

**Gecikmeyi Azaltmak İçin:**
1. Oyunun `.exe` dosyasına sağ tıklayıp **Özellikler** seçeneğini seçin.
2. **Uyumluluk** sekmesine gelin.
3. **Tam ekran iyileştirmelerini devre dışı bırak** (Disable full-screen optimizations) seçeneğini işaretleyin.

---

## Windows 11 "Debloat" İşlemleri: Gereksiz Servisleri Devre Dışı Bırakma

Windows 11, arka planda RAM ve CPU döngülerini tüketen birçok telemetri ve widget servisiyle birlikte gelir. Bu servislerin kapatılması, sistem kaynaklarını tamamen oyuna tahsis eder.

### Devre Dışı Bırakılması Gereken Windows Servisleri
`services.msc` konsolu üzerinden aşağıdaki servisleri bulup başlangıç türlerini **Devre Dışı** olarak ayarlayın:

| Servis Adı | Teknik Açıklama | Devre Dışı Bırakma Nedeni |
| :--- | :--- | :--- |
| **Connected User Experiences and Telemetry** | Kullanım verilerini Microsoft'a gönderir. | CPU ve disk G/Ç (I/O) kaynaklarını tüketir. |
| **SysMain (Eski adıyla Superfetch)** | Sık kullanılan uygulamaları RAM'e önceden yükler. | Oyun esnasında RAM tahsisatını kararsızlaştırır. |
| **Windows Arama (Windows Search)** | Arka planda dosya indekslemesi yapar. | Oyun sırasında ani disk okuma/yazma takılmalarına sebep olur. |

### Telemetri ve Widget'ların Kapatılması
Windows 11 Widget altyapısı, arka planda sürekli olarak `WebView2` süreçlerini çalıştırır.

*   **Ayarlar > Kişiselleştirme > Görev Çubuğu** yolunu izleyin ve **Widget'lar** seçeneğini kapatın.
*   Gizlilik ve Güvenlik sekmesinden tüm **Tanılama ve Geri Bildirim** gönderimlerini devre dışı bırakın.

---

## Sonuç ve Performans Analizi

Bu rehberde uygulanan optimizasyonların başarısı, donanım konfigürasyonunuza bağlı olarak değişkenlik gösterecektir. Yapılan değişikliklerin kararlılığını ve performans üzerindeki etkisini ölçmek için aşağıdaki adımları takip etmeniz önerilir:

1. **Sentetik Testler:** Değişiklikler öncesinde ve sonrasında **3DMark Time Spy** veya **Cinebench R23** testleri ile sistem kararlılığını ölçün.
2. **Oyun İçi Metrikler:** **MSI Afterburner** ve **RTSS (RivaTuner Statistics Server)** kullanarak oyun içi %1 ve %0.1 Low FPS değerlerini takip edin. Bu değerlerdeki artış, anlık takılmaların (stuttering) azaldığının en büyük kanıtıdır.
3. **Gecikme Analizi:** NVIDIA LDAT veya yazılımsal olarak **PresentMon** aracıyla kare oluşturma sürelerini (Frame Time) analiz ederek girdi gecikmesindeki düşüşü gözlemleyin.