---
title: "windows 11 ram kullanımı azaltma"
description: "windows 11 ram kullanımı azaltma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 RAM Kullanımı Azaltma: Teknik Optimizasyon Rehberi

Windows 11, gelişmiş grafik arayüzü, arka plan servisleri ve entegre yapay zeka araçları nedeniyle Windows 10'a kıyasla daha yüksek miktarda sistem belleği (RAM) tüketir. Boşta %50'nin üzerine çıkan RAM kullanımı, özellikle 8 GB ve 16 GB RAM'e sahip sistemlerde oyun ve ağır yazılım performansını doğrudan olumsuz etkiler. 

Bu rehberde, Windows 11'in bellek yönetim mimarisini bozmadan RAM kullanımını optimize etmek için uygulayabileceğiniz teknik yöntemler adım adım açıklanmıştır.

---

## 1. Başlangıç Uygulamalarını ve Arka Plan İşlemlerini Kısıtlama

Sistem açılışında otomatik başlayan uygulamalar, siz onları kullanmasanız bile bellekte yer kaplamaya devam eder.

### Başlangıç Programlarını Devre Dışı Bırakma
1. `Ctrl + Shift + Esc` kısayolu ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç Uygulamaları** sekmesine gelin.
3. Durumu "Etkin" olan ve yüksek etki gösteren uygulamalara (Spotify, Discord, Teams, OneDrive vb.) sağ tıklayıp **Devre Dışı Bırak** seçeneğini işaretleyin.

### Arka Plan Uygulama İzinlerini Kapatma
1. `Win + I` tuşlarına basarak **Ayarlar**'ı açın.
2. **Uygulamalar > Yüklü Uygulamalar** bölümüne gidin.
3. Listelenen uygulamaların yanındaki üç noktaya tıklayıp **Gelişmiş Seçenekler**'i seçin.
4. **Arka plan uygulamaları izinleri** başlığı altındaki ayarı **Hiçbir zaman** olarak değiştirin.

---

## 2. SysMain (SuperFetch) Hizmetini Yapılandırma

`SysMain` (eski adıyla SuperFetch), sık kullanılan uygulamaları önceden RAM'e yükleyerek açılış sürelerini hızlandırmayı amaçlar. Ancak NVMe SSD kullanan sistemlerde bu süreç gereksiz bellek yükü oluşturur ve RAM kullanımını %10-20 oranında artırabilir.

### SysMain Hizmetini Kapatma:
1. `Win + R` tuşlarına basın, `services.msc` yazıp **Enter**'a basın.
2. Listeden **SysMain** hizmetini bulun ve çift tıklayın.
3. **Başlangıç türü** seçeneğini **Devre Dışı** olarak değiştirin.
4. **Hizmet durumu** altındaki **Durdur** butonuna tıklayın ve **Uygula/Tamam** diyerek kaydedin.

*Alternatif olarak Komut İstemi (CMD) üzerinden yönetici olarak:*
```cmd
sc config "SysMain" start=disabled
sc stop "SysMain"
```

---

## 3. Windows 11 Widget'ları ve Copilot'u Devre Dışı Bırakma

Windows 11 Widget paneli ve Copilot, arka planda WebView2 süreçlerini çalıştırarak 300 MB ile 1 GB arasında RAM tüketebilir.

### Registry (Kayıt Defteri) Üzerinden Widget'ları Kapatma:
1. `Win + R` kombinasyonu ile `regedit` komutunu çalıştırın.
2. Aşağıdaki yola gidin:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft`
3. **Microsoft** anahtarına sağ tıklayıp **Yeni > Anahtar** deyin ve adını `DWM` koyun.
4. `DWM` içine sağ tıklayıp **Yeni > DWORD (32 bit) Değeri** oluşturun, adını `DisallowAnimations` yapın ve değerini `1` yapın.
5. `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced` yoluna gidin.
6. `TaskbarDa` DWORD değerini bulun ve verisini `0` yapın (Widget simgesini görev çubuğundan kaldırır).

---

## 4. NDU (Network Data Usage) RAM Sızıntısını Önleme

Windows 11'deki NDU sürücüsü, ağ kullanımını izlerken bazı sistemlerde **Non-Paged Pool (Sayfalanmayan Havuz)** bellek sızıntısına (Memory Leak) neden olur. Bu durum, RAM kullanımının zamanla durduk yere %90'lara ulaşmasına yol açar.

### NDU Sürücüsünü Devre Dışı Bırakma:
1. `Win + R` yapıp `regedit` yazın.
2. Yol: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Ndu`
3. Sağ taraftaki **Start** değerine çift tıklayın.
4. Değeri **2** (Otomatik) yerine **4** (Devre Dışı) olarak değiştirin.
5. Bilgisayarı yeniden başlatın.

---

## 5. Görsel Efektleri ve Animatik Arayüzü Optimize Etme

Görsel efektler doğrudan Masaüstü Pencere Yöneticisi (`dwm.exe`) tarafından RAM üzerinde işlenir.

1. `Win + R` yapıp `sysdm.cpl` yazın.
2. **Gelişmiş** sekmesine gelin ve **Performans** altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini seçin.
4. Okunabilirliği bozmamak için yalnızca şu iki seçeneği işaretleyin:
   - *Ekran yazı tipi kenarlarını düzelt*
   - *Simgeler yerine küçük resimler göster*
5. **Uygula** butonuna basarak çıkın.

---

## 6. Sanal Bellek (Paging File) Ayarlarını Optimize Etme

Sanal bellek, RAM dolduğunda verilerin diske yazılmasını sağlar. Yanlış yapılandırılmış bir sanal bellek, sistemin RAM üzerindeki yükü boşaltamamasına sebep olur.

1. `sysdm.cpl` > **Gelişmiş** > **Performans Ayarları** > **Gelişmiş** sekmesine gidin.
2. **Sanal Bellek** bölümündeki **Değiştir** butonuna tıklayın.
3. "Tüm sürücülerde disk bellek dosyası boyutunu otomatik yönet" seçeneğindeki işareti kaldırın.
4. Sistem sürücünüzü (C:) seçip **Özel boyut**'u işaretleyin:
   - **Başlangıç boyutu (MB):** Mevcut RAM miktarınızın 1.5 katı (Örn: 8 GB için 12288 MB)
   - **En büyük boyut (MB):** Mevcut RAM miktarınızın 3 katı (Örn: 8 GB için 24576 MB)
5. **Ayarla** ve ardından **Tamam** butonuna tıklayın.

---

## 7. Web Tarayıcılarında Bellek Tasarrufu Modunu Açma

Günlük kullanımda RAM tüketiminin en büyük sebebi web tarayıcılarıdır (Chrome, Edge, Brave).

- **Google Chrome:** `chrome://settings/performance` adresine gidin ve **Bellek Tasarrufu (Memory Saver)** özelliğini aktif edin.
- **Microsoft Edge:** `edge://settings/system` adresine gidin, **Verimlilik Modu** ve **Uykudaki Sekmeler** seçeneklerini etkinleştirin.

---

## Özet: Optimize Edilmiş Bellek Tüketim Değerleri

Yapılan optimizasyonların ardından Windows 11 boşta RAM kullanımı değerlerinin aşağıdaki aralıklarda olması beklenir:

| Toplam RAM | Optimizasyon Öncesi (Boşta) | Optimizasyon Sonrası (Boşta) |
| :--- | :--- | :--- |
| **8 GB RAM** | %60 - %75 (~5.0 GB) | %30 - %40 (~2.8 GB) |
| **16 GB RAM** | %35 - %50 (~6.5 GB) | %18 - %25 (~3.5 GB) |
| **32 GB RAM** | %20 - %30 (~8.0 GB) | %10 - %15 (~4.0 GB) |

> **Not:** Windows 11 NT mimarisi boşta duran RAM'i önbellekleme amacıyla kullanabilir. Bu durum sistemin normal çalışmasıdır; ancak yukarıdaki adımlar, aktif olarak işgal edilen (In-use) RAM miktarını düşürerek ağır yüklere alan açacaktır.