---
title: windows 11 gereksiz uygulamalar kaldırma
description: windows 11 gereksiz uygulamalar kaldırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Gereksiz Uygulamalar Kaldırma: Sistem Optimizasyonu ve Bloatware Temizleme Rehberi

Windows 11 işletim sistemi, temiz bir kurulumla gelse dahi arka planda çalışan, RAM, CPU ve disk G/Ç (I/O) kaynaklarını tüketen birçok önceden yüklenmiş uygulama (bloatware) barındırır. Bu uygulamalar, sistem mimarisinde gereksiz bağlam geçişlerine (context switching) ve telemetri trafiğine neden olarak donanım verimliliğini düşürür. 

Bu rehberde, Windows 11'deki gereksiz uygulamaları (bloatware) sistem kararlılığını bozmadan, yerleşik araçlar, PowerShell ve paket yöneticileri kullanarak kalıcı olarak kaldırmanın en güvenli ve efektif yöntemlerini inceleyeceğiz.

---

## Windows 11 Bloatware'in Donanım ve Sistem Mimarisine Etkileri

Windows 11 ile entegre gelen gereksiz uygulamalar, yalnızca disk alanı kaplamakla kalmaz; işletim sisteminin çekirdek (kernel) ve kullanıcı modu (user mode) kaynaklarını da meşgul eder.

### 1. CPU ve RAM Tüketimi
Arka planda çalışan UWP (Universal Windows Platform) uygulamaları, askıya alınmış (suspended) modda olsalar dahi RAM üzerinde yer kaplar. Özellikle düşük ve orta segment donanımlarda, bu durum sayfalama dosyası (paging file) kullanımını artırarak disk üzerinde gereksiz yazma/okuma döngülerine yol açar.

### 2. Disk G/Ç (I/O) ve NVMe Ömrü
Sürekli arka planda çalışan telemetri ve güncelleme servisleri, SSD ve NVMe sürücülerinizde rastgele yazma (random write) işlemleri gerçekleştirir. Bu durum, sürücünün TBW (Terabytes Written) ömrünü doğrudan etkiler.

### 3. Ağ Bant Genişliği ve Gecikme (Latency)
Hava Durumu, Haberler, Xbox servisleri ve üçüncü taraf sponsorlu uygulamalar (TikTok, Instagram vb.), canlı kutucuklar (live tiles) ve arka plan senkronizasyonları için sürekli olarak Microsoft sunucuları ile iletişim kurar. Bu durum, oyunlarda ve gerçek zamanlı veri akışlarında mikro gecikmelere (jitter) neden olabilir.

---

## Yöntem 1: Windows Package Manager (Winget) ile Güvenli Temizlik

Windows Package Manager (`winget`), Microsoft tarafından geliştirilen ve sistem bütünlüğünü bozmadan uygulama yönetimi sağlayan en güvenli komut satırı aracıdır.

### Winget ile Uygulama Listeleme ve Kaldırma

1. **Başlat** menüsüne sağ tıklayın ve **Terminal (Yönetici)** seçeneğini seçin.
2. Sisteminizde yüklü olan tüm uygulamaları listelemek için aşağıdaki komutu çalıştırın:
   ```powershell
   winget list
   ```
3. Belirli bir gereksiz uygulamayı kaldırmak için şu sözdizimini kullanın:
   ```powershell
   winget uninstall --name "Uygulama Adı"
   ```
   *Örnek (Cortana'yı kaldırmak için):*
   ```powershell
   winget uninstall --name "Cortana"
   ```

---

## Yöntem 2: PowerShell (AppXPackage) ile Derinlemesine Sistem Temizliği

Windows 11'de bazı sistem uygulamaları GUI (Arayüz) üzerinden kaldırılamaz. Bu durumda PowerShell'in `AppX` modüllerini kullanmak gerekir. Burada iki kavramı birbirinden ayırmak kritik önem taşır:
* **AppxPackage:** Mevcut kullanıcı için yüklü olan uygulamalar.
* **ProvisionedAppxPackage:** Yeni açılacak kullanıcı hesapları ve sistem güncellemeleri için imajda hazır bekletilen uygulamalar.

### 1. Mevcut Kullanıcı İçin Gereksiz Uygulamaları Kaldırma
Aşağıdaki PowerShell komut bloğu, sistemde en sık karşılaşılan gereksiz uygulamaları mevcut kullanıcı profilinden temizler:

```powershell
# Kaldırılacak uygulamaların listesi
$BloatwareList = @(
    "*Microsoft.549981C3F5F10*" # Cortana
    "*Microsoft.3DBuilder*"
    "*Microsoft.BingNews*"
    "*Microsoft.BingWeather*"
    "*Microsoft.GetHelp*"
    "*Microsoft.Getstarted*"
    "*Microsoft.Messaging*"
    "*Microsoft.MicrosoftSolitaireCollection*"
    "*Microsoft.People*"
    "*Microsoft.SkypeApp*"
    "*Microsoft.YourPhone*"
    "*Microsoft.ZuneVideo*"
    "*Microsoft.ZuneMusic*"
    "*Microsoft.WindowsFeedbackHub*"
    "*Microsoft.XboxApp*"
    "*Microsoft.XboxGamingOverlay*"
)

foreach ($App in $BloatwareList) {
    Get-AppxPackage -Name $App -AllUsers | Remove-AppxPackage -ErrorAction SilentlyContinue
}
```

### 2. Yeni Kullanıcılar ve Güncellemeler İçin Uygulamaları İmajdan Silme
Uygulamaların Windows güncellemelerinden sonra geri gelmesini engellemek için "Provisioned" paketlerinin de silinmesi gerekir:

```powershell
foreach ($App in $BloatwareList) {
    Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like $App} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
}
```

---

## Yöntem 3: Kayıt Defteri (Registry) ile Otomatik Uygulama Yüklemelerini Engelleme

Windows 11, temiz kurulum sonrasında dahi "Tüketici Deneyimi" (Consumer Experience) kapsamında arka planda üçüncü taraf sponsorlu uygulamaları (Disney+, Spotify, Candy Crush vb.) otomatik olarak indirir. Bunu engellemek için Kayıt Defteri üzerinde mimari bir değişiklik yapılması gerekir.

### Adım Adım Otomatik Yüklemeleri Kapatma:

1. `Win + R` tuşlarına basın, `regedit` yazın ve Enter'a basın.
2. Aşağıdaki yola gidin:
   ```text
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager
   ```
3. Sağ taraftaki boş alana sağ tıklayın, **Yeni > DWORD (32-bit) Değeri** seçeneğini seçin.
4. Adını `SilentInstalledAppsEnabled` yapın.
5. Değerini `0` olarak ayarlayın.
6. Bilgisayarınızı yeniden başlatın.

---

## Kaldırılması Güvenli Olan ve Olmayan Windows 11 Uygulamaları

Sistem kararlılığını korumak adına hangi paketlerin silinebileceğini, hangilerinin ise kesinlikle sistemde kalması gerektiğini bilmek kritik bir donanım uzmanlığı gerektirir.

| Uygulama Adı | Paket Kimliği (Package ID) | Kaldırılması Güvenli mi? | Açıklama |
| :--- | :--- | :--- | :--- |
| **Cortana** | `Microsoft.549981C3F5F10` | **Evet** | Artık desteklenmeyen yapay zeka asistanı. |
| **Xbox Game Bar** | `Microsoft.XboxGamingOverlay` | **Evet** | Oyun oynamıyorsanız arka planda RAM tüketir. |
| **Hava Durumu** | `Microsoft.BingWeather` | **Evet** | Web üzerinden takip edilebilir, arka plan trafiği üretir. |
| **Microsoft Store** | `Microsoft.WindowsStore` | **HAYIR** | **Kesinlikle silinmemeli.** Sistem güncellemeleri ve uygulama kütüphanesi bozulur. |
| **Windows Güvenliği** | `Microsoft.SecHealthUI` | **HAYIR** | **Kesinlikle silinmemeli.** Windows Defender arayüzünü devre dışı bırakır. |
| **Hesap Makinesi** | `Microsoft.WindowsCalculator` | **Evet** | Alternatif LTSC hesap makinesi veya üçüncü taraf yazılımlar kullanılabilir. |

---

## Temizlik Sonrası Sistem Performans Analizi

Windows 11 gereksiz uygulamalar kaldırma işlemlerini tamamladıktan sonra, sisteminizdeki optimizasyonu doğrulamak için aşağıdaki adımları uygulayın:

1. **Görev Yöneticisi (Task Manager):** `Ctrl + Shift + Esc` kombinasyonu ile Görev Yöneticisi'ni açın. İşlemler (Processes) sekmesinde arka planda çalışan işlem sayısının düştüğünü ve boşta RAM kullanımının azaldığını gözlemleyin.
2. **Olay Görüntüleyicisi (Event Viewer):** `eventvwr.msc` komutu ile sistem günlüklerini kontrol ederek, kaldırılan uygulamalardan kaynaklanan herhangi bir servis hatası (DCOM veya Service Control Manager hatası) olup olmadığını denetleyin.
3. **Sistem Dosyası Denetleyicisi (SFC):** Kaldırma işlemlerinin sistem bütünlüğüne zarar vermediğinden emin olmak için terminalde şu komutu çalıştırın:
   ```cmd
   sfc /scannow
   ```

Bu adımlarla optimize edilmiş bir Windows 11, donanım kaynaklarınızı doğrudan işletim sisteminin kendisine ve çalıştırdığınız profesyonel yazılımlara/oyunlara tahsis ederek daha kararlı, düşük gecikmeli ve yüksek performanslı bir kullanıcı deneyimi sunar.