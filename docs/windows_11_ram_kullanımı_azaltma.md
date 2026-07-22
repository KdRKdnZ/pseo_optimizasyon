# Windows 11 RAM Kullanımı Azaltma Rehberi: Teknik ve Etkili Yöntemler

Windows 11, gelişmiş görsel efektleri, varsayılan arka plan hizmetleri ve akıllı bellek yönetimi (SysMain/SuperFetch) nedeniyle boştayken bile ortalama 3.5 GB ile 5.5 GB arasında RAM tüketebilir. Düşük veya orta segment belleğe (8 GB veya 16 GB) sahip sistemlerde bu durum oyunlarda drop sorunlarına ve uygulama geçişlerinde yavaşlamalara yol açar.

Aşağıdaki adımlar, Windows 11'in sistem kararlılığını bozmadan bellek ayak izini (RAM footprint) en aza indirmek için hazırlanmış teknik optimizasyon protokolleridir.

---

## 1. Başlangıç Uygulamalarını ve Microsoft Dışı Hizmetleri Kısıtlama

Sistem açılışında yüklenen yazılımlar, kullanıcı arayüzü görünmese dahi RAM'de yer kaplar.

### Başlangıç Uygulamalarını Kapatma:
1. `Ctrl + Shift + Esc` tuş kombinasyonu ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç Uygulamaları** (Start-up apps) sekmesine gidin.
3. Microsoft Edge, OneDrive, Discord, Spotify, Steam gibi arka planda çalışması zorunlu olmayan uygulamalara sağ tıklayıp **Devre Dışı Bırak** seçeneğini işaretleyin.

### Microsoft Dışı Hizmetleri Gizleme ve Kapatma:
1. `Win + R` tuşlarına basıp `msconfig` yazın ve Enter'a basın.
2. **Hizmetler** sekmesine gelin.
3. Alt kısımda bulunan **"Tüm Microsoft hizmetlerini gizle"** kutucuğunu **mutlaka** işaretleyin.
4. Kalan üçüncü taraf hizmetlerden (Örn: Google Update, Adobe Update Service) gereksiz olanların tikini kaldırın ve **Uygula**'ya tıklayın.

---

## 2. SysMain (SuperFetch) ve Telemetri Hizmetlerini Devre Dışı Bırakma

Windows 11, sık kullanılan uygulamaları RAM önbelleğine yüklemek için **SysMain** hizmetini kullanır. SSD kullanan sistemlerde bu özellik RAM'i gereksiz yere doldurabilir.

### SysMain Hizmetini Durdurma:
1. `Win + R` tuşlarına basıp `services.msc` yazın.
2. Listeden **SysMain** hizmetini bulun ve çift tıklayın.
3. **Başlangıç türü** seçeneğini **Devre Dışı** olarak değiştirin.
4. **Hizmet durumu** altındaki **Durdur** butonuna basın ve **Uygula** deyin.

### Windows Telemetri ve Tanılama Hizmetlerini Kapatma:
1. Aynı hizmetler penceresinde **Bağlı Kullanıcı Deneyimleri ve Telemetri** (*Connected User Experiences and Telemetry*) hizmetini bulun.
2. Başlangıç türünü **Devre Dışı** yapın ve hizmeti durdurun.

---

## 3. Windows 11 Araç Takımlarını (Widgets) ve Web Aramasını Kaldırma

Windows 11 Widgets süreci (`Widgets.exe`), arka planda WebView2 süreçlerini çalıştırarak 300 MB ile 1 GB arasında RAM tüketebilir.

### Windows Widgets'ı PowerShell ile Tamamen Silme:
1. Başlat menüsüne sağ tıklayıp **Terminal (Yönetici)** veya **PowerShell (Yönetici)** modunu açın.
2. Aşağıdaki komutu yapıştırın ve Enter'a basın:
   ```powershell
   winget uninstall "Windows web experience pack"
   ```
3. İşlem tamamlandıktan sonra Widgets sistemi tamamen kaldırılacak ve RAM yükü azalacaktır.

---

## 4. Arka Plan Uygulama İzinlerini Düzenleme

Windows 11'de Microsoft Store uygulamalarının arka planda çalışması standart olarak açıktır.

1. **Ayarlar > Uygulamalar > Yüklü Uygulamalar** yolunu izleyin.
2. Arka planda çalışmasını istemediğiniz uygulamanın yanındaki **üç noktaya** tıklayıp **Gelişmiş Seçenekler**'i seçin.
3. **Arka plan uygulamaları izinleri** başlığı altındaki seçeneği **Hiçbir zaman** olarak ayarlayın.

---

## 5. Görsel Efektleri ve Saydamlığı Optimize Etme

Fluent Design mimarisi, GPU ve sistem RAM'i üzerinde ek yük oluşturur.

### Saydamlık Efektlerini Kapatma:
* **Ayarlar > Erişilebilirlik > Görsel Efektler** bölümüne gidin.
* **Saydamlık efektleri** seçeneğini **Kapalı** duruma getirin.

### Performans İçin Görsel Ayarları Düzenleme:
1. `Win + R` tuşlarına basıp `sysdm.cpl` yazın.
2. **Gelişmiş** sekmesine gelin ve **Performans** altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini seçin veya yalnızca şu iki seçeneği açık bırakarak diğerlerini kapatın:
   * *Ekran yazı tipi kenarlarını düzelt*
   * *Simgeler yerine küçük resimler göster*

---

## 6. Windows Sıkıştırılmış Bellek (RAM Compression) Ayarı

Windows 11, RAM dolmaya başladığında verileri disk yerine RAM'in özel sıkıştırılmış bir bölümüne yazar. Yüksek RAM'li sistemlerde bu durum CPU yüküne neden olabilir; ancak düşük RAM'li sistemlerde hayat kurtarır.

RAM miktarınız **8 GB ve altıysa** RAM Sıkıştırma açık kalmalıdır. **16 GB ve üzeri** RAM'iniz varsa ve CPU kullanımını düşürmek istiyorsanız PowerShell (Yönetici) üzerinden kapatabilirsiniz:

* **RAM Sıkıştırmayı Kapatmak İçin (PowerShell Yönetici):**
  ```powershell
  Disable-MMAgent -MemoryCompression
  ```
* **RAM Sıkıştırmayı Tekrar Açmak İçin:**
  ```powershell
  Enable-MMAgent -MemoryCompression
  ```
*(Değişikliklerin etkili olması için bilgisayarı yeniden başlatın.)*

---

## 7. Sanal Bellek (Pagefile) Boyutunu Manuel Yapılandırma

Windows'un sanal belleği otomatik yönetmesi, bellek şişmelerine yol açabilir. Sanal belleği sabitlemek performansı artırır ve RAM yönetimini rahatlatır.

1. `sysdm.cpl` > **Gelişmiş** > **Performans Ayarları** > **Gelişmiş** sekmesine gidin.
2. **Sanal Bellek** alanındaki **Değiştir** butonuna tıklayın.
3. **"Tüm sürücülerde döküm dosyası boyutunu otomatik yönet"** seçeneğinin tikini kaldırın.
4. Sisteminizin kurulu olduğu diski (genelde C:) seçip **Özel boyut**'u işaretleyin.
5. Değerleri sistem RAM'inize göre ayarlayın:
   * **8 GB RAM için:** Başlangıç: `4096 MB`, En Yüksek: `8192 MB`
   * **16 GB RAM için:** Başlangıç: `8192 MB`, En Yüksek: `12288 MB`
6. **Ayarla** butonuna basıp sistemi yeniden başlatın.

---

## Özet: Optimizasyon Sonrası Beklenen Değerler

| Donanım Yapılandırması | Optimizasyon Öncesi Boşta RAM | Optimizasyon Sonrası Boşta RAM |
| :--- | :--- | :--- |
| **8 GB RAM Sistem** | ~4.2 GB (%52) | ~2.1 GB (%26) |
| **16 GB RAM Sistem** | ~5.8 GB (%36) | ~2.8 GB (%17) |

Bu teknik adımlar uygulandığında Windows 11, arka plan yüklerinden arındırılarak oyunlar ve ağır yazılımlar (Render, sanallaştırma vb.) için maksimum kullanılabilir bellek alanını serbest bırakacaktır. Third-party (Bölüm 3 temizleme araçları) "RAM Cleaner" yazılımlarını sürekli arka planda çalıştırmaktan kaçının; bu yazılımlar anlık boşaltma yapsa da Windows'un bellek mimarisini bozarak uzun vadede sistem kararsızlığına (BSOD) yol açabilir.