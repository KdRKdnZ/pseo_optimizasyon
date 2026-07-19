---
title: windows 11 gereksiz servisler kapatma
description: windows 11 gereksiz servisler kapatma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Gereksiz Servisler Kapatma Rehberi: Performans ve RAM Optimizasyonu

Windows 11, modern donanımlar için optimize edilmiş bir işletim sistemi olsa da, arka planda çalışan ve birçok kullanıcı için hiçbir işlev ifade etmeyen onlarca servis (hizmet) barındırır. Bu servisler; CPU döngülerini tüketir, RAM (Rastgele Erişimli Bellek) üzerinde gereksiz "Commit Charge" (taahhüt edilen bellek) oluşturur ve disk G/Ç (Giriş/Çıkış) işlemlerini artırarak sistem gecikmesini (latency) yükseltir.

Bu teknik rehberde, Windows 11'in kararlılığını bozmadan, donanım kaynaklarınızı serbest bırakmak için kapatabileceğiniz gereksiz servisleri, risk analizleriyle birlikte inceliyoruz.

---

## Windows 11 Servis Yönetimi Neden Önemlidir?

İşletim sistemi mimarisinde her servis, arka planda bir `svchost.exe` işlemi altında veya bağımsız bir süreç olarak çalışır. Gereksiz servislerin açık kalması şu donanımsal ve yazılımsal maliyetlere yol açar:

*   **Bağlam Geçişi (Context Switching):** CPU çekirdekleri, aktif olmayan servislerin iş parçacıkları (threads) arasında sürekli geçiş yapmak zorunda kalır. Bu durum mikro gecikmelere yol açar.
*   **Bellek Ayak İzi (Memory Footprint):** Her aktif servis, RAM üzerinde fiziksel ve sanal bellek alanı işgal eder.
*   **Güç Tüketimi:** Arka plan aktiviteleri, CPU'nun daha yüksek güç durumlarında (C-states yerine P-states) kalmasına neden olarak özellikle dizüstü bilgisayarlarda pil ömrünü kısaltır.

---

## Güvenle Kapatılabilecek Windows 11 Servisleri

Aşağıdaki tabloda, genel kullanıcı senaryolarında kapatılması sistem kararlılığına zarar vermeyen, **windows 11 gereksiz servisler kapatma** listesinde yer alan kritik hizmetler ve işlevleri listelenmiştir.

| Servis Adı (Görünen Ad) | Sistem Adı (Service Name) | Varsayılan Durum | Kapatma Nedeni / Senaryosu |
| :--- | :--- | :--- | :--- |
| **Bağlı Kullanıcı Deneyimleri ve Telemetri** | `DiagTrack` | Otomatik | Microsoft'a kullanım verileri gönderir. Gizlilik ve CPU tasarrufu için kapatılmalıdır. |
| **SysMain** (Eski adıyla Superfetch) | `SysMain` | Otomatik | SSD kullanan sistemlerde gereksiz disk yazma işlemi yapar. SSD ömrü ve performansı için kapatılabilir. |
| **Yazdırma Biriktiricisi** | `Spooler` | Otomatik | Eğer bilgisayarınıza bağlı bir yazıcı yoksa tamamen gereksizdir. |
| **Dokunmatik Klavye ve El Yazısı Paneli** | `TabletInputService` | Elle | Dokunmatik ekran veya grafik tablet kullanmıyorsanız gereksiz kaynak tüketir. |
| **Windows Arama** (Windows Search) | `WSearch` | Otomatik | Arka planda sürekli disk indekslemesi yapar. Dosya aramalarını nadiren yapıyorsanız kapatabilirsiniz. |
| **İndirilen Haritalar Yöneticisi** | `MapsBroker` | Otomatik (Gecikmeli) | Çevrimdışı harita uygulamasını kullanmıyorsanız gereksizdir. |
| **Bluetooth Destek Hizmeti** | `bthserv` | Elle | Bilgisayarınızda Bluetooth adaptörü yoksa veya kullanmıyorsanız kapatın. |
| **Uzak Kayıt Defteri** | `RemoteRegistry` | Devre Dışı / Elle | Güvenlik açığı yaratabilir. Ağ üzerinden kayıt defteri düzenlemesi yapmıyorsanız kapatılmalıdır. |

---

## Adım Adım Windows 11 Gereksiz Servisleri Kapatma

Windows 11'de servisleri optimize etmek için iki ana yöntem mevcuttur: Grafiksel Arayüz (GUI) ve komut satırı (PowerShell).

### 1. Yöntem: Hizmetler (services.msc) Konsolu ile Kapatma

Bu yöntem, servisleri tek tek inceleyerek ve açıklamalarını okuyarak kapatmak isteyen kullanıcılar için en güvenli yoldur.

1.  Klavye üzerinden `Windows Tuşu + R` kombinasyonuna basarak **Çalıştır** penceresini açın.
2.  Arama kutusuna `services.msc` yazın ve `Enter` tuşuna basın.
3.  Açılan listeden kapatmak istediğiniz servisi bulun (Örneğin: *Bağlı Kullanıcı Deneyimleri ve Telemetri*).
4.  Servisin üzerine çift tıklayarak **Özellikler** penceresini açın.
5.  **Başlangıç türü** açılır menüsünü **Devre Dışı** olarak değiştirin.
6.  Eğer servis o an çalışıyorsa, **Hizmet durumu** altındaki **Durdur** butonuna tıklayın.
7.  **Uygula** ve **Tamam** butonlarına basarak değişiklikleri kaydedin.

### 2. Yöntem: PowerShell ile Gelişmiş Servis Yönetimi (Hızlı Yöntem)

Yazılım mimarları ve sistem yöneticileri için en efektif yöntem PowerShell betikleri kullanmaktır. Bu işlem için PowerShell'i yönetici olarak çalıştırmanız gerekir.

Aşağıdaki komut bloğu, yukarıda listelenen en yaygın gereksiz servisleri tek bir hamleyle durdurur ve başlangıç türünü "Devre Dışı" (Disabled) olarak ayarlar:

```powershell
# Yönetici yetkisiyle çalıştırıldığından emin olun
$services = @(
    "DiagTrack",      # Bağlı Kullanıcı Deneyimleri ve Telemetri
    "MapsBroker",      # İndirilen Haritalar Yöneticisi
    "RemoteRegistry",  # Uzak Kayıt Defteri
    "TabletInputService" # Dokunmatik Klavye ve El Yazısı Paneli
)

foreach ($service in $services) {
    if (Get-Service -Name $service -ErrorAction SilentlyContinue) {
        Stop-Service -Name $service -Force -ErrorAction SilentlyContinue
        Set-Service -Name $service -StartupType Disabled
        Write-Host "$service servisi başarıyla devre dışı bırakıldı." -ForegroundColor Green
    }
}
```

---

## Koşullu Olarak Kapatılabilecek Servisler (Kullanım Senaryosuna Göre)

Bazı servisler, bilgisayarı kullanım amacınıza göre tamamen gereksiz olabilir. Aşağıdaki senaryoları inceleyerek donanımınıza uygun optimizasyonu yapabilirsiniz.

### Oyuncular İçin Kapatılabilecek Servisler
Eğer bilgisayarınızda Xbox ekosistemini kullanmıyorsanız ve sadece Steam, Epic Games gibi platformlardan oyun oynuyorsanız, aşağıdaki servisleri kapatabilirsiniz:

*   **Xbox Accessory Management Service** (`XboxGipSvc`)
*   **Xbox Live Auth Manager** (`XblAuthManager`)
*   **Xbox Live Game Save** (`XblGameSave`)
*   **Xbox Live Networking Service** (`XboxNetApiSvc`)

### Sanallaştırma Kullanmayanlar İçin (Hyper-V)
Eğer bilgisayarınızda sanal makine (Hyper-V, WSL2) çalıştırmıyorsanız, aşağıdaki servisleri devre dışı bırakabilirsiniz:

*   **Hyper-V Sanal Makine Oturumu Hizmeti** (`vmicvmsession`)
*   **Hyper-V Zaman Sincronizasyonu Hizmeti** (`vmictimesync`)
*   **Hyper-V Konuk Hizmet Arabirimi** (`vmicguestinterface`)

---

## Kesinlikle Dokunulmaması Gereken Kritik Sistem Servisleri

Performans artırma amacıyla yapılan en büyük hata, işletim sisteminin çekirdek (kernel) işlevlerini yerine getiren servisleri kapatmaktır. Aşağıdaki servislere kesinlikle müdahale edilmemelidir:

*   **RPC (Remote Procedure Call - `RpcSs`):** Windows'un neredeyse tüm iç iletişim mimarisi bu servise bağlıdır. Kapatılması durumunda sistem çöker ve mavi ekran (BSOD) alırsınız.
*   **DCOM Sunucusu İşlem Başlatıcısı (`DcomLaunch`):** Sistem bileşenlerinin başlatılması için kritiktir.
*   **Windows Defender / Güvenlik Merkezi (`WinDefend`):** Üçüncü taraf bir antivirüs kullanmıyorsanız, sistemi zararlı yazılımlara karşı tamamen savunmasız bırakır.
*   **Windows Update (`wuauserv`):** Güvenlik yamalarının alınmasını engeller. Geçici olarak durdurulabilse de tamamen devre dışı bırakılması uzun vadede ciddi güvenlik açıklarına yol açar.

---

## Servis Optimizasyonunun Donanım Üzerindeki Etkileri (Kanıtlar ve Metrikler)

Doğru yapılandırılmış bir **windows 11 gereksiz servisler kapatma** işlemi sonrasında sisteminizde şu somut değişiklikler gözlemlenir:

1.  **RAM Kullanımında Azalma:** Boştaki RAM kullanımı, sistem donanımına bağlı olarak **300 MB ile 1 GB arasında** azalır. Bu durum, özellikle 8 GB veya daha az RAM'e sahip sistemlerde darboğazı (bottleneck) önler.
2.  **Daha Düşük İşlemci Sıcaklığı:** Arka plan thread sayısının azalmasıyla birlikte CPU çekirdekleri daha sık "Deep Sleep" (C-States) moduna geçer. Bu, boştaki işlemci sıcaklığını 2-4°C düşürebilir.
3.  **Düşük Gecikme Süresi (DPC Latency):** Ses üretimi, video kurgu ve rekabetçi oyunlarda kritik önem taşıyan DPC gecikmeleri, gereksiz sürücü ve servis çağrılarının engellenmesiyle minimize edilir.