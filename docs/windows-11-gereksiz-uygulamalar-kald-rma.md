---
title: "windows 11 gereksiz uygulamalar kaldırma"
description: "windows 11 gereksiz uygulamalar kaldırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Gereksiz Uygulamalar Kaldırma Rehberi: PowerShell ve Winget ile Bloatware Temizliği

Windows 11 işletim sistemi, varsayılan olarak kullanıcıların çoğunun ihtiyaç duymadığı birçok önceden yüklenmiş uygulama (bloatware) ve arka plan servisi ile birlikte gelir. Bu uygulamalar sistem kaynaklarını (RAM, CPU), depolama alanını tüketir ve telemetri veri trafiğine neden olur. 

Bu rehberde, Windows 11'deki gereksiz uygulamaları standart arayüz, **PowerShell**, **Winget (Windows Package Manager)** ve **Grup İlkesi** yöntemlerini kullanarak kalıcı olarak kaldırmanın teknik adımları yer almaktadır.

---

## 1. Ön Hazırlık: Sistem Geri Yükleme Noktası Oluşturma

Sistem bileşenlerine müdahale etmeden önce bir geri yükleme noktası oluşturulması önerilir.

1. `Win + R` tuşlarına basın, `sysdm.cpl` yazıp **Enter**'a basın.
2. **Sistem Koruması** sekmesine geçin.
3. Yerel Disk (C:) seçiliyken **Oluştur** butonuna tıklayın ve bir isim vererek işlemi tamamlayın.

---

## 2. Windows Ayarları Arayüzü ile Standart Kaldırma

Bazı temel dâhili uygulamalar Grafik Kullanıcı Arayüzü (GUI) üzerinden kaldırılabilir:

1. `Win + I` tuş kombinasyonu ile **Ayarlar** menüsünü açın.
2. **Uygulamalar** > **Yüklü Uygulamalar** sekmesine gidin.
3. Kaldırmak istediğiniz uygulamanın sağ tarafındaki **üç nokta (...)** simgesine tıklayın.
4. **Kaldır** seçeneğini işaretleyin.

> **Not:** Xbox, Cortana, Haritalar ve OneDrive gibi bazı sistem uygulamalarında "Kaldır" seçeneği pasif durumdadır. Bu uygulamalar için PowerShell kullanılmalıdır.

---

## 3. PowerShell ile Derinlemesine Bloatware Temizliği

Windows 11 yerleşik paketlerini (AppX) kaldırmanın en etkili yolu PowerShell komut satırını kullanmaktır.

### PowerShell'i Yönetici Olarak Çalıştırma
`Win + X` menüsünden veya Arama çubuğuna **PowerShell** yazarak **Yönetici olarak çalıştır** seçeneğini seçin.

### Yüklü Tüm Uygulama Paketlerini Listeleme
Sisteminizde yüklü olan tüm AppX paketlerinin tam adını görmek için:

```powershell
Get-AppxPackage | Select-Object Name, PackageFullName
```

### Tekil Uygulama Kaldırma Komutu
Genel kaldırma sözdizimi şu şekildedir:

```powershell
Get-AppxPackage *uygulama_adi* | Remove-AppxPackage
```

### En Çok Silinen Gereksiz Windows 11 Uygulamaları İçin PowerShell Komutları

Aşağıdaki komutları doğrudan PowerShell terminaline yapıştırarak ilgili uygulamaları silebilirsiniz:

*   **Cortana:**
    ```powershell
    Get-AppxPackage *Microsoft.5499817D141F1* | Remove-AppxPackage
    ```
*   **3D Viewer:**
    ```powershell
    Get-AppxPackage *3dviewer* | Remove-AppxPackage
    ```
*   **Get Help (Yardım Alın):**
    ```powershell
    Get-AppxPackage *GetHelp* | Remove-AppxPackage
    ```
*   **Microsoft News (Haberler):**
    ```powershell
    Get-AppxPackage *bingnews* | Remove-AppxPackage
    ```
*   **Microsoft Solitaire Collection:**
    ```powershell
    Get-AppxPackage *solitairecollection* | Remove-AppxPackage
    ```
*   **Windows Haritalar:**
    ```powershell
    Get-AppxPackage *windowsmaps* | Remove-AppxPackage
    ```
*   **Geri Bildirim Merkezi (Feedback Hub):**
    ```powershell
    Get-AppxPackage *WindowsFeedbackHub* | Remove-AppxPackage
    ```
*   **Xbox Uygulamaları (Xbox Bar, Game Overlay vb.):**
    ```powershell
    Get-AppxPackage *xbox* | Remove-AppxPackage
    ```
*   **Windows Kamera:**
    ```powershell
    Get-AppxPackage *windowscamera* | Remove-AppxPackage
    ```
*   **Posta ve Takvim (Mail and Calendar):**
    ```powershell
    Get-AppxPackage *communicationsapps* | Remove-AppxPackage
    ```

### Uygulamaları Tüm Kullanıcılardan (All Users) Kaldırma
Eğer bilgisayarda birden fazla kullanıcı hesabı varsa, uygulamayı tüm profillerden silmek için `-AllUsers` parametresi eklenmelidir:

```powershell
Get-AppxPackage -AllUsers *bingnews* | Remove-AppxPackage
```

### Yeni Açılan Kullanıcı Hesaplarında Otomatik Yüklenmeyi Engelleme (Provisioned Packages)
Sistemden bir AppX paketini silseniz bile, yeni bir kullanıcı profili oluşturulduğunda bu uygulamalar tekrar yüklenebilir. Bunu tamamen engellemek için hazırlık paketini sistem görüntüsünden silmek gerekir:

```powershell
Get-AppxProvisionedPackage -Online | Where-Object {$_.DisplayName -like "*bingnews*"} | Remove-AppxProvisionedPackage -Online
```

---

## 4. Winget (Windows Paket Yöneticisi) Kullanarak Kaldırma

Windows 11 ile entegre gelen **Winget** aracı, uygulamaları kimlik (ID) belirteçleri üzerinden hızlıca kaldırmaya olanak tanır.

1. Komut İstemi (CMD) veya PowerShell'i **Yönetici** olarak açın.
2. Yüklü uygulamaları ID'leri ile listelemek için:
   ```cmd
   winget list
   ```
3. Hedef uygulamayı silmek için `winget uninstall` komutunu ve uygulamanın Adını/ID'sini kullanın:

   *   **Microsoft OneDrive:**
       ```cmd
       winget uninstall "Microsoft OneDrive"
       ```
   *   **Microsoft Teams:**
       ```cmd
       winget uninstall "Microsoft Teams"
       ```
   *   **Web Experience Pack (Widgets / Araç Takımları):**
       ```cmd
       winget uninstall "Windows Web Experience Pack"
       ```
       *(Not: Bu paket silindiğinde Windows 11 Sol Alt köşedeki Hava Durumu ve Widgets paneli devre dışı kalır).*

---

## 5. Otomatik Windows Önerilerini ve Promosyon Uygulamalarını Engelleme

Windows 11, Başlat menüsünde veya bildirimlerde Disney+, Spotify, TikTok gibi uygulamaların kısayollarını otomatik olarak indirebilir. Bu durumu Kayıt Defteri (Registry) üzerinden kalıcı olarak kapatabilirsiniz.

### Registry (Kayıt Defteri) Düzenlemesi

1. `Win + R` basıp `regedit` yazın ve **Enter**'a basın.
2. Şu yola gidin:
   `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager`
3. Sağ panelde bulunan aşağıdaki `DWORD (32-bit)` değerlerini bulun (yoksa sağ tıklayıp Yeni > DWORD değeri oluşturun) ve değerlerini **`0`** yapın:
   *   `SilentInstalledAppsEnabled` -> **0**
   *   `SystemPaneSuggestionsEnabled` -> **0**
   *   `SoftLandingEnabled` -> **0**
   *   `SubscribedContent-338388Enabled` -> **0**

---

## 6. Açık Kaynaklı Otomatik Debloat Araçları (İleri Seviye)

Tüm bu komutları manuel yazmak yerine toplu temizlik sağlayan, topluluk tarafından geliştirilmiş açık kaynaklı ve güvenilir scriptler kullanılabilir.

### Chris Titus Tech - Windows Utility (WinUtil)
PowerShell'e şu komutu yapıştırarak gelişmiş debloat arayüzünü başlatabilirsiniz:

```powershell
iwr -useb https://christitus.com/win | iex
```
*   **İşlev:** Açılan arayüzdeki "Tweaks" sekmesinden "Desktop" profilini seçerek önerilen tüm gereksiz servis ve uygulamaları tek tıkla kaldırabilirsiniz.

---

## Özet ve Yan Etki Yönetimi

| Uygulama / Servis | Silinmeli mi? | Olası Etkisi |
| :--- | :--- | :--- |
| **Xbox App / Game Bar** | Oyun oynamıyorsanız evet | Oyun içi ekran kaydı ve Oyun Modu entegrasyonu kaybolur. |
| **Web Experience Pack** | Widget kullanmıyorsanız evet | Görev çubuğundaki Hava Durumu ve Haberler paneli çalışmaz. |
| **OneDrive** | Bulut depolama kullanmıyorsanız evet | Dosya eşitlemesi durur, yerel klasör yapısına dönülür. |
| **Microsoft Store** | **HAYIR** | Windows sistem güncellemeleri ve gerekli kütüphaneler (VCLibs vb.) bozulabilir. |

Gereksiz uygulamaların kaldırılması; sisteminizin açılış süresini hızlandırır, arka planda çalışan süreç sayısını (Process Count) azaltır ve sistem yanıt süresini (Latency) düşürür.