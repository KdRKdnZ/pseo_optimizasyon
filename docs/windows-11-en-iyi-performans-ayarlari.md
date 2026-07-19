---
title: windows 11 en iyi performans ayarları
description: windows 11 en iyi performans ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 En İyi Performans Ayarları: Derinlemesine Optimizasyon Rehberi

Windows 11, modern mimarisi ve gelişmiş güvenlik özellikleriyle öne çıksa da, varsayılan ayarları arka planda yüksek CPU döngüsü, RAM tüketimi ve disk I/O (Giriş/Çıkış) yükü yaratır. Bir yazılım mimarı ve donanım uzmanı gözüyle, işletim sisteminin çekirdek (kernel) seviyesinden grafik alt katmanına kadar optimize edilmesi, gecikme sürelerini (latency) düşürür ve donanım verimliliğini maksimuma çıkarır.

Aşağıda, sistem kararlılığını bozmadan uygulayabileceğiniz, kanıta dayalı **Windows 11 en iyi performans ayarları** adım adım listelenmiştir.

---

## 1. Donanım Seviyesinde Grafik ve GPU Optimizasyonları

Grafik işlemcinizin (GPU) işletim sistemiyle olan iletişimini optimize etmek, darboğazları (bottleneck) engellemenin en doğrudan yoludur.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) Aktifleştirme
HAGS (Hardware-Accelerated GPU Scheduling), Windows'un önceliklendirme görevlerini CPU yerine doğrudan GPU'nun kendi özel zamanlama işlemcisine devretmesini sağlar. Bu, CPU üzerindeki bağlam geçişi (context switching) yükünü azaltır ve kare hızlarında (FPS) kararlılık sağlar.

1. **Ayarlar > Sistem > Monitör > Grafik** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin.
4. Bilgisayarı yeniden başlatın.

### Resizable BAR (ReBAR) Kontrolü
Resizable BAR, CPU'nun PCIe veri yolu üzerinden GPU'nun tüm VRAM (Video RAM) çerçeve arabelleğine tek seferde erişmesini sağlayan bir PCI Express teknolojisidir. 

* **Nasıl Yapılır?** Bu ayar anakartınızın BIOS/UEFI ekranından (genellikle *Advanced > PCIe Subsystem Settings* altında) **Enable** edilmelidir. Windows içinde aktif olup olmadığını GPU-Z programından veya NVIDIA Kontrol Paneli > Sistem Bilgisi altından doğrulayabilirsiniz.

---

## 2. İşletim Sistemi ve Çekirdek (Kernel) Optimizasyonları

Windows 11'in güvenlik katmanları, özellikle eski nesil işlemcilerde ve oyun senaryolarında %5 ila %15 arasında performans kaybına yol açabilir.

### VBS (Sanal Tabanlı Güvenlik) ve HVCI Devre Dışı Bırakılması
VBS (Virtualization-Based Security), donanım sanallaştırma özelliklerini kullanarak güvenli bir bellek bölgesi oluşturur. HVCI (Çekirdek Yalıtımı / Bellek Bütünlüğü) ise bu alanı kötü amaçlı kodlardan korur. Ancak bu işlem, CPU üzerinde sürekli bir sanallaştırma yükü (overhead) yaratır. Maksimum oyun ve render performansı için bu özelliği kapatabilirsiniz:

1. Başlat menüsüne **Çekirdek Yalıtım** (Core Isolation) yazın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** duruma getirin.
3. Bilgisayarı yeniden başlatın.

### Nihai Performans (Ultimate Performance) Güç Planını Etkinleştirme
Standart "Yüksek Performans" modu, mikro saniyeler düzeyindeki güç geçişlerinde CPU çekirdeklerini park edebilir (core parking). "Nihai Performans" modu ise işletim sisteminin donanım üzerindeki tüm güç tasarrufu kısıtlamalarını kaldırır.

Bu gizli planı etkinleştirmek için:
1. Başlat'a sağ tıklayıp **Terminal (Yönetici)** veya **PowerShell (Yönetici)** seçeneğini açın.
2. Aşağıdaki kodu yapıştırın ve Enter tuşuna basın:
   ```powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Donanım ve Ses > Güç Seçenekleri** bölümüne gidin ve yeni eklenen **Nihai Performans** planını seçin.

---

## 3. Bellek (RAM) ve Depolama Yönetimi

Disk I/O operasyonlarının optimize edilmesi, sistemin genel tepki süresini (responsiveness) doğrudan etkiler.

### Sanal Bellek (Paging File) Statik Yapılandırması
Windows varsayılan olarak sanal belleği dinamik olarak yönetir. Disk üzerinde sürekli olarak sanal bellek boyutunun büyütülüp küçültülmesi, özellikle NVMe SSD'lerde bile gereksiz yazma/okuma döngülerine ve anlık takılmalara (stuttering) neden olur. Sanal belleği statik hale getirmek bu yükü ortadan kaldırır.

1. **Gelişmiş sistem ayarlarını görüntüle** menüsünü açın.
2. **Gelişmiş** sekmesinde, Performans altındaki **Ayarlar** butonuna tıklayın.
3. **Gelişmiş** sekmesine geçip Sanal Bellek altındaki **Değiştir** butonuna tıklayın.
4. "Tüm sürücüler için disk belleği dosyası boyutunu otomatik yönet" seçeneğinin işaretini kaldırın.
5. İşletim sisteminin kurulu olduğu diski seçip **Özel Boyut** deyin.
6. **Başlangıç boyutu** ve **En büyük boyut** değerlerini birbirine eşit olacak şekilde ayarlayın (Örn: 16 GB RAM için her iki kutuya da `8192` MB veya `16384` MB yazın). Bu, diskin parçalanmasını (fragmentation) önler.

### Depolama Alanı Sensörü ve Geçici Dosya Temizliği
Windows 11 arka planda eski güncelleme kalıntılarını ve geçici dosyaları tarar. Bunu otomatikleştirmek ancak arka plan tarama sıklığını azaltmak gerekir.

* **Ayarlar > Sistem > Depolama** yolundan **Depolama Algısı**'nı açın, ancak yapılandırma ayarlarından tarama sıklığını "Her ay" veya "Disk alanı azaldığında" olarak değiştirin.

---

## 4. Arka Plan Hizmetleri ve Telemetri Optimizasyonu

Windows 11, Microsoft sunucularına sürekli veri gönderen telemetri servisleri ve gereksiz arka plan uygulamalarıyla birlikte gelir. Bu servislerin kapatılması CPU'nun "Context Switch" (bağlam geçişi) oranını düşürür.

### Arka Plan Uygulamalarının Devre Dışı Bırakılması
Windows 11'de klasik "Arka Plan Uygulamaları" menüsü kaldırılmıştır. Ancak uygulamaların arka planda çalışmasını engellemek için şu adımlar izlenmelidir:

1. **Ayarlar > Uygulamalar > Yüklü Uygulamalar** bölümüne gidin.
2. Arka planda çalışmasını istemediğiniz uygulamanın yanındaki üç noktaya tıklayıp **Gelişmiş Seçenekler** deyin.
3. **Arka plan uygulama izinleri** menüsünü **Hiçbir zaman** olarak ayarlayın.

### Başlangıç Programlarının Temizlenmesi
Sistem açılış süresini ve RAM kullanımını optimize etmek için:
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç Uygulamaları** sekmesine gelin.
3. Microsoft OneDrive, Microsoft Teams, Spotify gibi sistem başlangıcında çalışması gerekmeyen tüm üçüncü taraf uygulamaları **Devre Dışı Bırak** olarak işaretleyin.

---

## 5. Ağ ve Gecikme (Latency) Ayarları

Çevrimiçi oyunlarda ve veri transferlerinde paket gecikmesini (ping) azaltmak için Windows'un ağ yığınını (network stack) optimize edebilirsiniz.

### Nagle Algoritmasını Devre Dışı Bırakma (TCP No Delay)
Nagle algoritması, küçük veri paketlerini birleştirerek ağ trafiğini azaltmayı amaçlar. Ancak bu durum, gerçek zamanlı veri akışlarında ve oyunlarda paketlerin bekletilmesine (gecikmeye) yol açar.

1. `Win + R` tuşlarına basıp `regedit` yazarak Kayıt Defteri Düzenleyicisi'ni açın.
2. Şu yola gidin:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\`
3. Alt klasörler arasından aktif internet bağlantınızın IP adresini içeren klasörü bulun.
4. Sağ tıklayıp **Yeni > DWORD (32-bit) Değeri** oluşturun. Adını `TcpAckFrequency` yapın ve değerini `1` olarak ayarlayın.
5. Aynı klasörde bir tane daha DWORD (32-bit) oluşturup adını `TCPNoDelay` yapın ve değerini `1` olarak ayarlayın.

Bu ayarlar, ağ kartınızın paketleri bekletmeden doğrudan iletmesini sağlayarak ağ tabanlı gecikmeleri minimize eder.