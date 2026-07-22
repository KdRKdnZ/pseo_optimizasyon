# Windows 11 Gereksiz Uygulamaları (Bloatware) Kaldırma Rehberi

Windows 11, varsayılan kurulumla birlikte sistem kaynaklarını (RAM, CPU, Disk) arka planda tüketen ve her kullanıcı için gerekli olmayan birçok önceden yüklenmiş uygulama (bloatware) ile gelir. Bu teknik rehberde, Windows 11 işletim sistemindeki gereksiz uygulamaları Grafik Kullanıcı Arayüzü (GUI), PowerShell ve Windows Package Manager (Winget) kullanarak sistem kararlılığını bozmadan kaldırma yöntemleri açıklanmaktadır.

---

## 1. Windows Ayarları Üzerinden Standart Kaldırma (GUI)

Kullanıcı arayüzü izin veren temel bloatware bileşenleri için en güvenli yöntem dahili ayarlar menüsüdür.

1. **Win + I** kısayolu ile **Ayarlar** panelini açın.
2. Sol menüden **Uygulamalar** > **Yüklü Uygulamalar** sekmesine gidin.
3. Kaldırmak istediğiniz uygulamanın yanındaki **üç nokta (...)** simgesine tıklayın.
4. **Kaldır (Uninstall)** seçeneğini belirleyin.

*Bu yöntemle silinebilen yaygın uygulamalar: Spotify, Disney+, Instagram, Solitaire Collection, Prime Video.*

---

## 2. PowerShell ile Gelişmiş AppX Paketlerini Silme

Windows'un GUI üzerinden silinmesine izin vermediği yerleşik AppX paketleri için Administrator (Yönetici) yetkileriyle çalıştırılan PowerShell komutları kullanılır.

### Hazırlık
1. **Windows + X** tuşlarına basın ve **Terminal (Yönetici)** veya **PowerShell (Yönetici)** seçeneğini başlatın.

### Sistemdeki Tüm Uygulama Paketlerini Listeleme
Sistemde yüklü olan tüm AppX paketlerinin tam adını görmek için:

```powershell
Get-AppxPackage | Select Name, PackageFullName
```

### Tekil Uygulama Kaldırma Komut Yapısı
```powershell
Get-AppxPackage *uygulama_adi* | Remove-AppxPackage
```

Sistemdeki **tüm kullanıcı hesaplarından** kaldırmak için `-AllUsers` parametresi eklenir:
```powershell
Get-AppxPackage -AllUsers *uygulama_adi* | Remove-AppxPackage
```

Yeni açılacak kullanıcı hesaplarına da bu uygulamaların otomatik yüklenmesini engellemek için **Provisioned Package** kaydı silinmelidir:
```powershell
Get-AppxProvisionedPackage -Online | Where-Object {$_.DisplayName -like "*uygulama_adi*"} | Remove-AppxProvisionedPackage -Online
```

---

### En Çok Silinmek İstenen Windows 11 Uygulamaları ve Komutları

Aşağıdaki komut satırlarını PowerShell penceresine doğrudan yapıştırarak ilgili uygulamaları tamamen kaldırabilirsiniz:

#### 1. Cortana'yı Kaldırma
```powershell
Get-AppxPackage *549981C3F5F10* | Remove-AppxPackage
```

#### 2. Xbox Bileşenlerini Kaldırma (Oyun oynamayanlar için)
```powershell
Get-AppxPackage *xbox* | Remove-AppxPackage
```

#### 3. Windows Haritalar (Maps) Kaldırma
```powershell
Get-AppxPackage *WindowsMaps* | Remove-AppxPackage
```

#### 4. Microsoft Weather (Hava Durumu) Kaldırma
```powershell
Get-AppxPackage *bingweather* | Remove-AppxPackage
```

#### 5. Windows Kamera ve Ses Kaydedicisi Kaldırma
```powershell
Get-AppxPackage *windowscamera* | Remove-AppxPackage
Get-AppxPackage *soundrecorder* | Remove-AppxPackage
```

#### 6. Microsoft News (Haberler) ve Finance Kaldırma
```powershell
Get-AppxPackage *bingnews* | Remove-AppxPackage
Get-AppxPackage *bingfinance* | Remove-AppxPackage
```

#### 7. Feedback Hub (Geri Bildirim Merkezi) ve Yardım Alma
```powershell
Get-AppxPackage *WindowsFeedbackHub* | Remove-AppxPackage
Get-AppxPackage *GetHelp* | Remove-AppxPackage
```

#### 8. Windows Mail ve Takvim Kaldırma
```powershell
Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage
```

#### 9. 3D Viewer ve Paint 3D Kaldırma
```powershell
Get-AppxPackage *3d* | Remove-AppxPackage
```

---

## 3. Winget (Windows Package Manager) ile Toplu Temizlik

Windows 11 ile entegre gelen **Winget** komut satırı aracı, uygulama kaldırma işlemlerini hızlıca gerçekleştirir.

1. **PowerShell**'i Yönetici olarak açın.
2. Yüklü uygulamaların kimliklerini (ID) listelemek için:
   ```cmd
   winget list
   ```
3. Belirli bir uygulamayı kaldırmak için:
   ```cmd
   winget uninstall --id <Uygulama-ID>
   ```

**Örnekler:**
* Cortana silme: `winget uninstall --id Microsoft.549981C3F5F10_8wekyb3d8bbwe`
* Microsoft News silme: `winget uninstall --id Microsoft.BingNews_8wekyb3d8bbwe`
* Microsoft Teams (Kişisel) silme: `winget uninstall --id MicrosoftTeams_8wekyb3d8bbwe`

---

## 4. OneDrive'ı Tamamen Sistemden Kaldırma

Windows 11 ile entegre gelen OneDrive, sadece program ekle/kaldırdan silindiğinde kayıt defteri (Registry) kalıntıları bırakabilir.

1. OneDrive sürecini sonlandırın ve kaldırın:
   ```powershell
   taskkill /f /im OneDrive.exe
   %SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall
   ```
   *(32-bit sistemler için `SysWOW64` yerine `System32` yolunu kullanın).*

2. Dosya Gezgini sol panelinden OneDrive simgesini kaldırmak için PowerShell (Yönetici) komutu:
   ```powershell
   Remove-ItemProperty -Path "HKCR:\CLSID\{018D5C66-453A-4307-9B53-224DE2ED1FE6}" -Name "System.IsPinnedToNameSpaceTree" -ErrorAction SilentlyContinue
   ```

---

## 5. Yanlışlıkla Silinen Varsayılan Uygulamaları Geri Yükleme

PowerShell ile silinen tüm orijinal Windows 11 uygulamalarını fabrika ayarlarına döndürerek tekrar yüklemek için şu komut kullanılır:

```powershell
Get-AppxPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
```

---

## Kararlılık ve Güvenlik Uyarıları

* **Sistem Geri Yükleme Noktası Oluşturun:** Komut satırı üzerinden toplu silme işlemi yapmadan önce `sysdm.cpl` çalıştırılarak bir Sistem Geri Yükleme noktası oluşturulmalıdır.
* **Kritik Paketleri Silmeyin:** `Microsoft.WindowsStore` (Windows Mağazası), `Microsoft.Windows.Photos` (Fotoğraflar) veya VCLibs bağımlılık paketlerinin silinmesi, işletim sisteminin temel işlevlerinde bozulmalara yol açabilir.
* **Güncelleme Sonrası Kontrol:** Major Windows 11 güncellemeleri (Örn: 23H2, 24H2) kaldırılan bazı AppX paketlerini sisteme yeniden yükleyebilir. Bu durumda işlemlerin tekrarlanması gerekebilir.