---
title: "windows 11 gereksiz servisler kapatma"
description: "windows 11 gereksiz servisler kapatma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Gereksiz Servisleri Kapatma Rehberi: Performans ve Hız Optimizasyonu

Windows 11, arka planda varsayılan olarak gelen onlarca servis (hizmet) çalıştırır. Bu servislerin birçoğu ortalama bir ev kullanıcısı veya oyuncu için gereksizdir. Arka planda çalışan lüzumsuz servislerin kapatılması; CPU kullanımını düşürür, RAM (bellek) tüketimini azaltır ve sistemin tepki süresini hızlandırır.

Bu rehberde, Windows 11 sistem kararlılığını bozmadan güvenle kapatabileceğiniz veya "Elle" moduna alabileceğiniz servisler teknik detaylarıyla listelenmiştir.

---

## Windows Hizmetler Yöneticisine Erişim

İşlemleri gerçekleştirmek için Windows Hizmetler arabirimini açmanız gerekir:

1. `Win + R` tuş kombinasyonu ile **Çalıştır** penceresini açın.
2. `services.msc` yazın ve **Enter** tuşuna basın.
3. Değiştirmek istediğiniz hizmete çift tıklayarak **Başlangıç türü** seçeneğini **Devre Dışı** veya **Elle** olarak değiştirin.

---

## Güvenle Kapatılabilecek Windows 11 Servisleri

Aşağıdaki servisler, kullanım senaryonuza bağlı olarak sistem performansını artırmak için kapatılabilir.

### 1. Telemetri ve Veri Toplama Servisleri
Microsoft'a kullanım verilerini gönderen ve arka planda sürekli I/O (Disk) işlemi yapan servislerdir.

*   **Bağlanmış Kullanıcı Deneyimleri ve Telemetri (Connected User Experiences and Telemetry - DiagTrack):**
    *   *Açıklama:* Sistem kullanım verilerini toplar.
    *   *Öneri:* **Devre Dışı**
*   **dmwappushservice:**
    *   *Açıklama:* WAP Anında İletme Mesaj Yönlendirme Hizmetidir, telemetri ile ilişkilidir.
    *   *Öneri:* **Devre Dışı**
*   **Tanılama İlkesi Hizmeti (Diagnostic Policy Service):**
    *   *Açıklama:* Windows bileşenlerindeki sorunları tespit eder. Genellikle çözümsüz raporlar oluşturur ve kaynak tüketir.
    *   *Öneri:* **Devre Dışı**

### 2. Oyun ve Xbox Servisleri (Xbox / Game Pass Kullanmayanlar İçin)
Bilgisayarınızda Xbox uygulaması veya Xbox Game Pass kullanmıyorsanız bu servislerin tamamını kapatabilirsiniz.

*   **Xbox Accessory Management Service**
*   **Xbox Live Auth Manager**
*   **Xbox Live Game Save**
*   **Xbox Live Networking Service**
    *   *Öneri:* Xbox platformunu kullanmıyorsanız tümünü **Devre Dışı** yapın. Oyun oynuyorsanız **Elle** modunda bırakın.

### 3. Donanım ve Cihaz Özel Servisleri
Kullanmadığınız donanımlara ait servislerin çalışması gereksiz kaynak tüketimidir.

*   **Dokunmatik Klavye ve El Yazısı Paneli Hizmeti (Touch Keyboard and Handwriting Panel Service):**
    *   *Açıklama:* Dokunmatik ekranı olmayan masaüstü ve standart laptoplar için gereksizdir.
    *   *Öneri:* **Devre Dışı**
*   **Yazdırma Biriktiricisi (Print Spooler):**
    *   *Açıklama:* Yazıcı ve tarayıcı işlemlerini yönetir.
    *   *Öneri:* Fiziksel bir yazıcı kullanmıyorsanız **Devre Dışı**. (PDF yazdırma özelliğini etkileyebilir).
*   **Bluetooth Destek Hizmeti (Bluetooth Support Service):**
    *   *Açıklama:* Bluetooth cihazlarını yönetir.
    *   *Öneri:* Bilgisayarınızda Bluetooth adaptörü yoksa veya kullanmıyorsanız **Devre Dışı**.
*   **Akıllı Kart (Smart Card) Servisleri:**
    *   *Açıklama:* Fiziksel akıllı kart okuyucuları için gereklidir.
    *   *Öneri:* **Devre Dışı**

### 4. Ağ ve Uzaktan Erişim Servisleri
Güvenlik açıklarını kapatmak ve ağı rahatlatmak için önerilen ayarlar:

*   **Uzak Kayıt Defteri (Remote Registry):**
    *   *Açıklama:* Uzaktaki kullanıcıların Windows Kayıt Defterini değiştirmesine izin verir.
    *   *Öneri:* Güvenlik ve performans için **Devre Dışı**.
*   **Uzak Masaüstü Hizmetleri (Remote Desktop Services):**
    *   *Açıklama:* RDP bağlantılarını sağlar.
    *   *Öneri:* AnymDesk/TeamViewer gibi 3. taraf yazılımlar kullanıyorsanız veya uzaktan bağlantı yapmıyorsanız **Devre Dışı**.
*   **İndirilen Haritalar Yöneticisi (Downloaded Maps Manager):**
    *   *Açıklama:* Windows Haritalar uygulamasının harita indirmesini sağlar.
    *   *Öneri:* **Devre Dışı**

### 5. Diğer İkincil Servisler

*   **Faks (Fax):**
    *   *Öneri:* **Devre Dışı**
*   **Perakende Gösteri Hizmeti (Retail Demo Service):**
    *   *Açıklama:* Mağazalarda sergilenen cihazlar içindir.
    *   *Öneri:* **Devre Dışı**
*   **Kurumsal Uygulama Yönetimi (Enterprise App Management):**
    *   *Öneri:* Şirket ağına bağlı olmayan kişisel bilgisayarlarda **Devre Dışı**.

---

## Gelişmiş Kullanıcılar İçin PowerShell İle Servis Kapatma

Aşağıdaki komutları **Yönetici olarak çalıştırılan PowerShell** üzerinden girerek en çok kaynak tüketen telemetri servislerini tek seferde devre dışı bırakabilirsiniz:

```powershell
# Telemetri ve Tanılama Servislerini Kapatma
Stop-Service -Name "DiagTrack" -Force
Set-Service -Name "DiagTrack" -StartupType Disabled

Stop-Service -Name "dmwappushservice" -Force
Set-Service -Name "dmwappushservice" -StartupType Disabled

# Akıllı Kart ve Perakende Gösteri Servislerini Kapatma
Set-Service -Name "SCardSvr" -StartupType Disabled
Set-Service -Name "RetailDemo" -StartupType Disabled

# Uzak Kayıt Defterini Kapatma
Set-Service -Name "RemoteRegistry" -StartupType Disabled
```

---

## Kritik Uyarı: Asla Kapatılmaması Gereken Servisler

Sistem kararsızlığına, mavi ekran (BSOD) hatalarına veya internet/ses kesintilerine yol açabileceğinden aşağıdaki servisleri **kesinlikle kapatmayın**:

*   **DHCP İstemcisi (DHCP Client):** İnternet IP adresinizi alır.
*   **DNS İstemcisi (DNS Client):** Web sitelerinin IP çözünürlüğünü sağlar.
*   **Windows Defender Servisleri:** Temel güvenlik korumasıdır.
*   **Windows Audio / Windows Audio Bitişik Düzeni:** Sistem seslerini yönetir.
*   **Tak ve Çalıştır (Plug and Play):** Yeni takılan donanımları tanır.
*   **Kullanıcı Profili Hizmeti (User Profile Service):** Kullanıcı oturumu açmayı sağlar.

---

## Özet ve En İyi Uygulama Stratjeisi

Servis optimizasyonu yapmadan önce mutlaka bir **Sistem Geri Yükleme Noktası** oluşturun. Bir servisin işlevinden emin değilseniz, onu direkt "Devre Dışı" bırakmak yerine **"Elle" (Manual)** moduna getirin. "Elle" modundaki servisler sistem tarafından ihtiyaç anında otomatik başlatılır, varsayılan çalışmada ise RAM kapsamaz.