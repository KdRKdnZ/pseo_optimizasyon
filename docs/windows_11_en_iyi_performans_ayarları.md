# Windows 11 En İyi Performans Ayarları: Eksiksiz Optimizasyon Rehberi

Windows 11, gelişmiş görsel öğeleri ve arka plan hizmetleriyle varsayılan ayarlarda yüksek sistem kaynağı (CPU, RAM, Disk) tüketebilir. Donanımınızdan maksimum verim almak, gecikmeyi (latency) düşürmek ve özellikle oyun veya ağır iş yüklerinde sistem hızını artırmak için aşağıdaki teknik optimizasyon adımlarını uygulayabilirsiniz.

---

## 1. Görsel Efektleri ve Saydamlığı Devre Dışı Bırakma

Windows 11'in "Fluent Design" arayüzü GPU ve RAM üzerinde ekstra yük oluşturur. Görsel efektlerin kapatılması, özellikle arayüz tepki süresini anında hızlandırır.

### Performans İçin Görsel Efekt Ayarı:
1. `Win + R` tuşlarına basın, **`sysdm.cpl`** yazıp `Enter` tuşuna basın.
2. Açılan pencerede **Gelişmiş** sekmesine gelin ve **Performans** başlığı altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini işaretleyin.
4. Okunabilirliği korumak adına yalnızca şu iki seçeneği açık bırakın:
   * *Ekran yazı tipi kenarlarını düzelt*
   * *Simgeler yerine küçük resimler göster*
5. **Uygula** ve **Tamam** butonlarına tıklayın.

### Saydamlık Efektlerini Kapatma:
* **Ayarlar > Erişilebilirlik > Görsel Efektler** yolunu izleyin.
* **Saydamlık efektleri** ve **Animasyon efektleri** seçeneklerini **Kapalı** konuma getirin.

---

## 2. "Nihai Performans" Güç Planını Etkinleştirme

Windows 11 varsayılan olarak "Dengeli" güç planı ile gelir. Bu durum işlemci frekansında dalgalanmalara yol açabilir. Maksimum işlemci gücü için "Nihai Performans" (Ultimate Performance) modunu aktif edin.

1. **Başlat** menüsüne `cmd` yazın, sağ tıklayıp **Yönetici olarak çalıştır**'ı seçin.
2. Aşağıdaki komutu yapıştırın ve `Enter` tuşuna basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Win + R` basıp **`powercfg.cpl`** yazın.
4. Açılan Güç Seçenekleri penceresinde **Nihai Performans** modunu seçin.

---

## 3. Oyun Modu ve Donanım Hızlandırmalı GPU Zamanlaması (HAGS)

Oyunlarda kare hızını (FPS) artırmak ve sistem kaynaklarını oyuna önceliklendirmek için bu iki ayar kritik önem taşır.

* **Oyun Modunu Açma:**
  * **Ayarlar > Oyun > Oyun Modu** bölümüne gidin ve **Açık** konuma getirin.
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):**
  * **Ayarlar > Sistem > Ekran > Grafik** sekmesine gidin.
  * **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
  * **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin ve bilgisayarı yeniden başlatın.

---

## 4. Arka Plan Uygulamalarını ve Başlangıç Programlarını Sınırlandırma

Açılışta çalışan ve arka planda veri tüketen uygulamalar RAM ve CPU kaynaklarını işgal eder.

### Başlangıç Uygulamalarını Devre Dışı Bırakma:
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç Uygulamaları** sekmesine gelin.
3. Gereksiz tüm uygulamalara (OneDrive, Spotify, Steam, Edge vb.) sağ tıklayıp **Devre Dışı Bırak** deyin.

### Arka Plan İzinlerini Kapatma:
* **Ayarlar > Uygulamalar > Yüklü Uygulamalar** sekmesine gidin.
* Arka planda çalışmasını istemediğiniz uygulamanın yanındaki üç noktaya tıklayıp **Gelişmiş Seçenekler**'i seçin.
* **Arka plan uygulama izinleri** bölümünü **Hiçbir zaman** olarak değiştirin.

---

## 5. Telemetri ve Gereksiz Hizmetleri (Services) Kapatma

Microsoft'a veri gönderen telemetri hizmetleri ve kullanılmayan sistem servisleri diski ve ağı meşgul eder.

### Gereksiz Hizmetlerin Devre Dışı Bırakılması:
1. `Win + R` tuşlarına basıp **`services.msc`** yazın.
2. Aşağıdaki hizmetleri bulun, sağ tıklayıp **Özellikler** deyin, **Başlangıç türü**nü **Devre Dışı** yapın ve hizmeti durdurun:
   * **Connected User Experiences and Telemetry** (Teşhis ve Veri Toplama)
   * **SysMain** (SSD kullanıyorsanız kapatabilirsiniz; NVMe SSD'lerde devre dışı bırakılması diski rahatlatır).
   * **Windows Search** (Arama indekslemesi yapmıyorsanız ve SSD kullanıyorsanız kapatılabilir).

---

## 6. Çekirdek Yalıtımını (VBS / HVCI) Kapatma (Oyun Performansı İçin)

Windows 11 ile varsayılan olarak gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Bellek Bütünlüğü, işlemciye ek yük bindirir. Özellikle oyunlarda %5 ila %15 arasında performans kaybına neden olabilir. *(Not: Güvenlik öncelikli sistemlerde açık kalması önerilir).*

1. Başlat menüsüne **Cihaz Güvenliği** yazın ve açın.
2. **Çekirdek Yalıtımı ayrıntıları** bağlantısına tıklayın.
3. **Bellek Bütünlüğü** seçeneğini **Kapalı** duruma getirin.
4. Sisteminizi yeniden başlatın.

---

## 7. Kayıt Defteri (Registry) Üzerinden Hızlandırma Tweaks

*Önemli: Kayıt defteri değişikliklerinden önce geri yükleme noktası oluşturun.*

### MenuShowDelay (Arayüz Tepki Süresini Hızlandırma):
1. `Win + R` basıp `regedit` yazın.
2. `HKEY_CURRENT_USER\Control Panel\Desktop` yoluna gidin.
3. **`MenuShowDelay`** dizesini bulun ve değerini `400` yerine **`0`** yapın.

### Otomatik Kapanmayan Uygulamaları Hızla Sonlandırma:
1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` yoluna gidin.
2. **`WaitToKillServiceTimeout`** değerini `5000` (5 saniye) yerine **`2000`** (2 saniye) olarak değiştirin.

---

## 8. Disk Temizliği ve Trim Optimizasyonu

Geçici dosyalar (Temp) ve sistem kalıntıları diskin okuma/yazma performansını düşürür.

* **Depolama Mantığını Etkinleştirme:**
  * **Ayarlar > Sistem > Depolama** yolunu izleyin.
  * **Depolama Mantığı** (Storage Sense) ayarını **Açık** konuma getirin.
  * **Geçici Dosyalar** sekmesine girerek eski Windows güncellemelerini ve önbellek dosyalarını temizleyin.

* **SSD TRIM Komutunu Çalıştırma:**
  * CMD'yi yönetici olarak açın ve şu komutu girin:
    ```cmd
    defrag C: /O
    ```
  * Bu komut SSD sürücünüze TRIM komutu göndererek hücrelerin yeniden optimize edilmesini sağlar.

---

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Etki Alanı | Kazanç |
| :--- | :--- | :--- |
| **Görsel Efektleri Kapatmak** | RAM & GPU | Düşük gecikme, hızlı arayüz |
| **Nihai Performans Modu** | CPU | Sabit yüksek saat hızı |
| **HAGS ve Oyun Modu** | GPU / Sistem | Oyunda daha yüksek ve kararlı FPS |
| **VBS / Bellek Bütünlüğü Kapatma** | CPU | %5 - %15 İşlemci performans artışı |
| **Gereksiz Hizmetleri Durdurmak** | RAM & Disk | Arka plan yükünün azalması |