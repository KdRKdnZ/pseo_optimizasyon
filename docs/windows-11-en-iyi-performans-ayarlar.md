---
title: "windows 11 en iyi performans ayarları"
description: "windows 11 en iyi performans ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 En İyi Performans Ayarları: Adım Adım Hızlandırma Rehberi

Windows 11, gelişmiş bir görsel arayüz ve yeni özelliklerle gelse de, varsayılan ayarları sistem kaynaklarını (CPU, RAM, Disk) yoğun şekilde tüketebilir. Donanımınızdan maksimum verim almak, oyunlarda FPS değerlerini artırmak ve sistem gecikmesini (latency) en aza indirmek için uygulanması gereken teknik performans optimizasyonları aşağıda sıralanmıştır.

---

## 1. Güç ve Performans Modunu Yapılandırma

Windows 11 varsayılan olarak "Dengeli" güç planı ile gelir. Bu mod, işlemci frekansını dinamik olarak kısar.

### Nihai Performans Modunu Etkinleştirme
Gelişmiş güç yönetimi için gizli olan "Nihai Performans" (Ultimate Performance) modunu komut satırı ile aktif edin:

1. **Windows Arama** çubuğuna `cmd` yazın, sağ tıklayıp **Yönetici olarak çalıştır**'ı seçin.
2. Şu komutu girin ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Ayarlar > Sistem > Güç ve Pil** yolunu izleyin.
4. **Güç Modu** seçeneğini **En iyi performans** olarak değiştirin.
5. Denetim Masası üzerinden **Güç Seçenekleri**'ne girerek yeni eklenen **Nihai Performans** planını işaretleyin.

---

## 2. Görsel Efektleri ve Animasyonları Optimize Etme

Windows 11'in gölge, pencere animasyonları ve saydamlık efektleri GPU ve RAM üzerinde ek yük oluşturur.

1. `Win + R` tuşlarına basarak **Çalıştır** penceresini açın.
2. `sysdm.cpl` yazıp Enter'a basın.
3. **Gelişmiş** sekmesinde, **Performans** başlığı altındaki **Ayarlar** butonuna tıklayın.
4. **En iyi performans için ayarla** seçeneğini işaretleyin.
5. Okunabilirliği bozmamak için yalnızca şu iki seçeneği açık bırakın:
   * *Ekran yazı tipi kenarlarını düzelt*
   * *Simgeler yerine küçük resimler göster*
6. **Ayarlar > Kişiselleştirme > Renkler** bölümünden **Saydamlık efektleri** seçeneğini **Kapalı** duruma getirin.

---

## 3. Oyun ve Grafik Ayarlarını Optimize Etme

Oyun performansını artırmak ve kare hızını (FPS) sabitlemek için Windows 11'in çekirdek grafik ayarları düzenlenmelidir.

### Oyun Modu ve Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
1. **Ayarlar > Oyun > Oyun Modu** sekmesine gidin ve **Açık** konuma getirin.
2. Aynı sayfada **İlgili Ayarlar** altındaki **Grafikler** bölümüne tıklayın.
3. **Varsayılan grafik ayarlarını değiştir** bağlantısına tıklayın.
4. **Donanım hızlandırmalı GPU zamanlaması (HAGS)** seçeneğini **Açık** duruma getirin.
5. **Değişken Yenileme Hızı (VRR)** seçeneğini aktif edin (Destekleyen monitörler için).

### Uygulama Bazlı GPU Ataması
Grafikler sekmesinde listede yer alan veya manuel eklediğiniz oyunların/yazılımların üzerine tıklayarak **Seçenekler**'den yüksek performanslı harici grafik kartınızı (NVIDIA/AMD) manuel olarak atayın.

---

## 4. Arka Plan Uygulamaları ve Başlangıç Programlarını Kapatma

Sistem açılış süresini ve boşta RAM kullanımını düşürmek için gereksiz servisleri devre dışı bırakın.

### Başlangıç Uygulamalarını Kısıtlama
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç uygulamaları** sekmesine gelin.
3. Sistem için kritik olmayan (Discord, Spotify, Steam, OneDrive vb.) tüm uygulamalara sağ tıklayıp **Devre Dışı Bırak** deyin.

### Arka Plan İzinlerini Kapatma
1. **Ayarlar > Uygulamalar > Yüklü Uygulamalar** bölümüne gidin.
2. Arka planda çalışmasını istemediğiniz uygulamanın yanındaki üç noktaya tıklayıp **Gelişmiş Seçenekler**'i seçin.
3. **Arka plan uygulamaları izinleri** başlığı altından seçeneği **Hiçbir zaman** olarak ayarlayın.

---

## 5. Çekirdek Yalıtımı (VBS) Devre Dışı Bırakma (Oyun Performansı İçin)

Sanal tabanlı güvenlik (VBS) ve Çekirdek Yalıtımı, sistemi zararlı kodlardan korur ancak özellikle oyunlarda %5 ila %15 arasında performans kaybına yol açabilir.

> **Not:** Güvenlik seviyesini bir miktar düşürür. Sadece maksimum performans odaklı sistemlerde kapatılması önerilir.

1. Windows Arama çubuğuna **Çekirdek Yalıtımı** (Core Isolation) yazın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Değişikliğin uygulanması için bilgisayarı yeniden başlatın.

---

## 6. Sanal Bellek (Pagefile) ve Depolama Optimizasyonu

Sistem RAM'i yetersiz kaldığında kullanılan disk üzerindeki sanal belleğin boyutunu elle yapılandırmak kilitlenmeleri önler.

### Sanal Bellek Ayarı
1. `sysdm.cpl` > **Gelişmiş** > Performans **Ayarlar** > **Gelişmiş** sekmesine gidin.
2. Sanal Bellek altındaki **Değiştir** butonuna tıklayın.
3. **Tüm sürücülerde disk bellek dosyası boyutunu otomatik yönet** seçeneğindeki işareti kaldırın.
4. **Özel boyut** seçeneğini işaretleyin:
   * **Başlangıç boyutu (MB):** Mevcut RAM miktarınızın 1.5 katı (Örn: 16 GB RAM için 16384 x 1.5 = 24576 MB).
   * **En büyük boyut (MB):** Mevcut RAM miktarınızın 3 katı.
5. **Ayarla** butonuna basıp **Tamam**'ı tıklayın.

### Depolama Algılaması (Storage Sense)
1. **Ayarlar > Sistem > Depolama** yolunu izleyin.
2. **Depolama Algılaması** özelliğini **Açık** konuma getirin.
3. Otomatik geçici dosya temizliğini gün/hafta bazında yapılandırın.

---

## 7. Ağ ve İndirme Optimizasyonu (Gecikme Düşürme)

Windows Update'in arka planda diğer bilgisayarlarla veri paylaşmasını engelleyerek ağ gecikmesini (ping) düşürün.

1. **Ayarlar > Windows Update > Gelişmiş Seçenekler** sekmesine girin.
2. **Teslim İyileştirme** (Delivery Optimization) seçeneğine tıklayın.
3. **Diğer bilgisayarlardan indirmelere izin ver** seçeneğini **Kapalı** konuma getirin.

---

## 8. Gereksiz Windows Hizmetlerini Devre Dışı Bırakma

Kullanmadığınız Windows servislerini durdurarak CPU döngülerini ve bellek kullanımını rahatlatın.

1. `Win + R` tuşlarına basıp `services.msc` yazın.
2. Aşağıdaki hizmetleri bulun, sağ tıklayıp **Özellikler**'e girin, **Başlangıç türü**'nü **Devre Dışı** yapın ve hizmeti durdurun:
   * **SysMain** (Eğer SSD kullanıyorsanız kapatılabilir, HDD için açık kalmalıdır).
   * **Connected User Experiences and Telemetry** (Teşhis ve veri toplama hizmeti).
   * **Arama** / **Windows Search** (SSD kullanıyorsanız ve sistem içi aramayı az kullanıyorsanız kapatılabilir).
   * **Dokunmatik Klavye ve El Yazısı Paneli Hizmeti** (Dokunmatik ekran kullanmıyorsanız).

---

## Sonuç Kontrol Listesi

Yapılan ayarların etkinleşmesi için bilgisayarınızı **yeniden başlatın**. Bu optimizasyonlar sonucunda:
* Boşta RAM kullanımı gözle görülür şekilde düşecektir.
* İşlemci tabanlı gecikmeler (input lag) azalacaktır.
* Oyun içi ani FPS düşüşleri (stuttering) engellenecektir.
* Sistem açılış ve tepki süreleri kısalacaktır.