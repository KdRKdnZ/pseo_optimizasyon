# Windows 11 Gereksiz Servisleri Kapatma ve Performans Optimizasyon Rehberi

Windows 11, varsayılan kurulumda arka planda çalışan yüzlerce farklı sistem hizmeti (service) ile gelir. Bu hizmetlerin bir kısmı işletim sisteminin temel işlevselliği için hayati önem taşırken, önemli bir kısmı ortalama bir kullanıcının ihtiyaç duymadığı telemetri, eski donanım desteği veya özel yazılım servislerinden oluşur. 

Gereksiz arka plan servislerini kapatmak; **RAM kullanımını düşürür, CPU yükünü azaltır, disk G/Ç (I/O) işlemlerini rahatlatır ve sistem açılış süresini hızlandırır.**

Bu rehberde, Windows 11'de performans artışı sağlamak amacıyla güvenle kapatılabilecek servisleri, bu servislerin işlevlerini ve işlem adımlarını teknik detaylarıyla inceleyebilirsiniz.

---

## Önemli Uyarı ve Ön Hazırlık

Hizmetleri değiştirmeden önce mutlaka bir **Sistem Geri Yükleme Noktası** oluşturulmalıdır. Yanlış bir kritik servisin kapatılması sistem kararsızlığına yol açabilir.

1. `Win + R` tuşlarına basın, `sysdm.cpl` yazıp **Enter**'a basın.
2. **Sistem Koruması** sekmesine geçin.
3. **Oluştur...** butonuna tıklayarak "Servis Optimizasyonu Öncesi" adıyla bir geri yükleme noktası oluşturun.

---

## Windows Hizmetler Yöneticisine (services.msc) Erişim

Hizmetleri yönetmek için Windows'un yerleşik araçları kullanılır:

* **Klavye Kısayolu:** `Win + R` tuş bileşimine basın.
* **Komut:** Açılan Çalıştır penceresine `services.msc` yazın ve **Enter** tuşuna basın.

Açılan pencerede her hizmet için üç temel Başlangıç Türü (Startup Type) bulunur:
* **Otomatik (Automatic):** Sistem açılışında kendiliğinden başlar.
* **Elle (Manual):** Sadece bir uygulama veya sistem bileşeni ihtiyaç duyduğunda tetiklenir (Önerilen moddur).
* **Devre Dışı (Disabled):** Hizmet hiçbir koşulda çalışmaz.

---

## Güvenle Devre Dışı Bırakılabilecek Windows 11 Servisleri

Aşağıdaki listede, sistemin kararlılığını bozmadan kapatılabilecek hizmetler kategorize edilmiştir. Hizmet adları hem Türkçe arayüz hem de parantez içinde teknik sistem adları (Service Name) ile belirtilmiştir.

### 1. Telemetri ve Veri Toplama Servisleri
Microsoft'a kullanım verilerini gönderen ve arka planda sürekli kaynak tüketen servislerdir.

* **Bağlı Kullanıcı Deneyimleri ve Telemetri (DiagTrack / Connected User Experiences and Telemetry):** Kullanım verilerini toplayıp Microsoft sunucularına gönderir.
  * *Önerilen Ayar:* **Devre Dışı**
* **Tanılama Yürütme Hizmeti (diagsvc / Diagnostic Execution Service):** Sistem sorunlarını teşhis etmek için arka planda çalışır.
  * *Önerilen Ayar:* **Devre Dışı**

### 2. Oyun ve Xbox Servisleri
Bilgisayarınızda Xbox Game Pass kullanmıyorsanız veya Microsoft Store oyunları oynamıyorsanız bu servislerin tamamı kapatılabilir.

* **Xbox Aksesuar Yönetimi Hizmeti (XboxGipSvc)**
* **Xbox Live Auth Manager (XblAuthManager)**
* **Xbox Live Game Save (XblGameSave)**
* **Xbox Live Ağ Hizmeti (XboxNetApiSvc)**
  * *Önerilen Ayar:* Xbox platformunu kullanmıyorsanız **Devre Dışı**, kullanıyorsanız **Elle**.

### 3. Donanım ve Çevre Birimleri Servisleri
Kullanmadığınız donanımlara ait servislerin çalışması gereksiz kaynak tüketimidir.

* **Yazdırma Biriktiricisi (Spooler / Print Spooler):** Yazıcı veya tarayıcı kullanmıyorsanız (PDF olarak yazdırma dahil ihtiyacınız yoksa) kapatılabilir.
  * *Önerilen Ayar:* Yazıcınız yoksa **Devre Dışı**.
* **Bluetooth Destek Hizmeti (bthserv / Bluetooth Support Service):** Masaüstü bilgisayarınızda Bluetooth adaptörü yoksa veya Bluetooth cihaz kullanmıyorsanız.
  * *Önerilen Ayar:* Bluetooth yoksa **Devre Dışı**.
* **Dokunmatik Klavye ve El Yazısı Paneli Hizmeti (TabletInputService):** Dokunmatik ekrana sahip olmayan standart masaüstü ve laptoplarda gereksizdir.
  * *Önerilen Ayar:* **Devre Dışı**
* **Akıllı Kart (SCardSvr / Smart Card):** Kurumsal kimlik doğrulama kartları kullanmıyorsanız gereksizdir.
  * *Önerilen Ayar:* **Devre Dışı**

### 4. Diğer Gereksiz Sistem Servisleri

| Hizmet Adı (Görünen) | Sistem Adı (Service Name) | Açıklama | Önerilen Durum |
| :--- | :--- | :--- | :--- |
| **Uzaktan Kayıt Defteri** | `RemoteRegistry` | Güvenlik riski oluşturur. Dışarıdan kayıt defteri erişimini sağlar. | **Devre Dışı** |
| **Faks** | `Fax` | Faks donanımı kullanımı içindir. | **Devre Dışı** |
| **İndirilen Haritalar Yöneticisi** | `MapsBroker` | Windows Haritalar uygulamasının arka plan güncellemelerini yönetir. | **Devre Dışı** |
| **Perakende Gösteri Hizmeti** | `RetailDemo` | Mağazalardaki teşhir ürünleri içindir. | **Devre Dışı** |
| **Cüzdan Hizmeti** | `WalletService` | Microsoft Wallet kart ve ödeme işlemlerini yürütür. | **Devre Dışı** |
| **Windows Müşteri Deneyimini Geliştirme Programı** | `WerSvc` | Hata raporlarını Microsoft'a gönderir. | **Elle** veya **Devre Dışı** |
| **SysMain (Eski adıyla Superfetch)** | `SysMain` | SSD kullanan sistemlerde yüksek disk/RAM kullanımına sebep olabilir. | SSD'de **Elle / Devre Dışı**, HDD'de **Otomatik** |

---

## PowerShell ile Otomatik Hizmet Kapatma (İleri Düzey)

Grafik arayüzü tek tek kullanmak yerine, yönetici yetkileriyle açılmış bir **PowerShell** penceresinde aşağıdaki komut bloklarını çalıştırarak gereksiz servisleri toplu halde kapatabilirsiniz.

```powershell
# Telemetri ve Teşhis Servislerini Kapatma
Stop-Service -Name "DiagTrack" -Force
Set-Service -Name "DiagTrack" -StartupType Disabled

Stop-Service -Name "diagsvc" -Force
Set-Service -Name "diagsvc" -StartupType Disabled

# Xbox Servislerini Kapatma
Stop-Service -Name "XblAuthManager", "XblGameSave", "XboxNetApiSvc", "XboxGipSvc" -Force -ErrorAction SilentlyContinue
Set-Service -Name "XblAuthManager", "XblGameSave", "XboxNetApiSvc", "XboxGipSvc" -StartupType Disabled

# Gereksiz İkincil Servisleri Kapatma
Stop-Service -Name "RemoteRegistry", "MapsBroker", "RetailDemo", "Fax" -Force -ErrorAction SilentlyContinue
Set-Service -Name "RemoteRegistry", "MapsBroker", "RetailDemo", "Fax" -StartupType Disabled
```

---

## Kapatılmaması Gereken Kritik Windows 11 Servisleri

Aşağıdaki servisler işletim sisteminin temel ağ, güvenlik ve grafik mimarisini oluşturur. Bu servislerin kapatılması sistemin çökmesine veya internet erişiminin kesilmesine neden olur:

* **DHCP İstemcisi (DHCP):** Ağ üzerinden IP adresi almanızı sağlar.
* **DNS İstemcisi (Dnscache):** Alan adlarının (URL) çözümlenmesini sağlar.
* **Windows Defender Hizmeti (WinDefend):** Temel güvenlik katmanıdır.
* **Windows Ses (AudioSrv):** Ses kartının çalışmasını sağlar.
* **Tak ve Çalıştır (Plug and Play - PlugPlay):** Donanım tanılama sistemidir.
* **Windows Olay Günlüğü (EventLog):** Sistem hatalarının kaydedilmesi ve uygulama kararlılığı için zorunludur.

---

## Sonuç ve Doğrulama

Servis değişikliklerini uyguladıktan sonra bilgisayarınızı yeniden başlatın. Performance optimizasyonunun durumunu kontrol etmek için `Ctrl + Shift + Esc` kısayolu ile **Görev Yöneticisi**'ni açıp **Performans** sekmesinden boştaki RAM ve CPU kullanımını değişiklik öncesi değerlerle karşılaştırabilirsiniz. 

Herhangi bir uygulama hatasıyla karşılaşılması durumunda ilgili servisin başlangıç türü `services.msc` üzerinden tekrar **Elle (Manual)** konumuna getirilmelidir.