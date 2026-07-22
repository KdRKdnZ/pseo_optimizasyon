---
title: "gamescope nedir"
description: "gamescope nedir hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Gamescope Nedir? Linux Oyun Deneyimini Değiştiren Micro-Compositor Rehberi

**Gamescope**, Valve tarafından geliştirilen, özellikle Linux işletim sistemlerinde oyun performansını, görüntü kalitesini ve pencere yönetimini optimize etmek için kullanılan **Wayland tabanlı bir micro-compositor (bileşik görüntü yöneticisi)** mimarisidir. 

İlk olarak Valve'ın Steam Deck cihazında kullandığı ve temelini `steamcompmgr` projesinden alan Gamescope, oyunu çalıştıran sanal bir ekran sunucusu oluşturur. Bu sayede oyun, işletim sisteminin ana masaüstü ortamından (GNOME, KDE vb.) izole edilir ve doğrudan grafik sürücüsüne işlenir.

---

## Gamescope Nasıl Çalışır? (Teknik Mimarisi)

Geleneksel Linux mimarisinde oyunlar, X11 veya Wayland masaüstü yöneticisi üzerinde diğer pencerelerle aynı görüntü işleme hattını (rendering pipeline) paylaşır. Bu durum gecikmeye (input lag), kare yırtılmalarına (screen tearing) ve ölçekleme sorunlarına yol açabilir.

Gamescope bu mimariyi şu şekilde dönüştürür:

1. **İzolasyon (Nested Compositing):** Gamescope, oyun için özel bir **Xwayland** veya **Vulkan** sunucusu başlatır. Oyun kendisini tamamen bağımsız bir ekranda çalışıyor zanneder.
2. **Kare Oluşturma (Rendering):** Oyunun ürettiği kareler doğrudan Gamescope tarafından yakalanır.
3. **Piksel İşleme ve Ölçekleme:** Gamescope, yakalanan kareleri ekran kartının Donanım Düzlemlerini (Hardware Planes) ve Vulkan katmanlarını kullanarak yeniden ölçeklendirir (Upscale/Downscale), HDR işler veya kare hızını sınırlar.
4. **Ekrana Sunum (Direct Scanout):** Hazırlanan nihayi görüntü, masaüstü yöneticisi baypas edilerek **DRM/KMS (Direct Rendering Manager / Kernel Mode Setting)** aracılığıyla doğrudan monitöre gönderilir. Bu işlem gecikmeyi minimuma indirir.

---

## Gamescope'un Temel Teknik Özellikleri

### 1. Gelişmiş Ölçekleme Teknolojileri (Upscaling)
Gamescope, donanım düzeyinde veya GPU tabanlı Vulkan shader'ları kullanarak düşük çözünürlükteki oyunları yüksek çözünürlüklü ekranlara kaliteden ödün vermeden taşır. Desteklenen ölçekleme algoritmaları:
* **AMD FSR (FidelityFX Super Resolution):** Sürücü seviyesinde tüm oyunlara uygulanabilir.
* **NVIDIA NIS (Nvidia Image Scaling):** NVIDIA kartlar için keskinleştirme ve ölçekleme.
* **Bilinear & Nearest Neighbor:** Piksel grafikli veya retro oyunlar için performans odaklı ölçekleme.

### 2. Düşük Gecikme ve Kare Zamanlaması (Frame Pacing)
Gamescope, ekran kartının `Vulkan Present` katmanı üzerinden çalışarak oyun içi kısıtlayıcılardan daha kararlı bir **Frame Limiter (FPS Sınırlayıcı)** sunar. Kare sunum zamanlamasını mükemmelleştirerek "micro-stuttering" (mikro takılma) sorunlarını ortadan kaldırır.

### 3. Esnek Çözünürlük Sanallaştırması
Pencereli modu desteklemeyen veya eski çözünürlük standartlarına (örneğin 4:3) sahip oyunları, monitörünüzün yerel çözünürlüğüne veya oranına zorlamadan sanal bir pencere içerisinde çalıştırır.

### 4. Gelişmiş Renk Yönetimi ve HDR
Linux üzerinde native HDR (High Dynamic Range) desteğinin öncüsüdür. Oyunların ürettiği SDR görüntüleri HDR'a dönüştürebilir veya oyunun native HDR sinyallerini doğrudan monitöre iletebilir.

---

## Gamescope Kurulumu

Popüler Linux dağıtımlarında Gamescope paket yöneticileri üzerinden kolayca kurulabilir:

### Arch Linux / Manjaro
```bash
sudo pacman -S gamescope
```

### Fedora
```bash
sudo dnf install gamescope
```

### Ubuntu / Debian (PPA veya Kaynak Koddan)
Ubuntu 23.10 ve üzeri sürümlerde Universe deposunda yer alır:
```bash
sudo apt install gamescope
```

---

## Gamescope Kullanımı ve Komut Parametreleri

Gamescope, komut satırından veya Steam başlatma seçeneklerinden (Launch Options) çalıştırılır. 

### Temel Sözdizimi
```bash
gamescope [GAMESCOPE SEÇENEKLERİ] -- [ÇALIŞTIRILACAK OYUN/UYGULAMA]
```

### Sık Kullanılan Parametreler

| Parametre | Açıklama |
| :--- | :--- |
| `-w [genişlik]` | Oyunun render edileceği çözünürlük genişliği |
| `-h [yükseklik]` | Oyunun render edileceği çözünürlük yüksekliği |
| `-W [genişlik]` | Pencerelerin/Pencere Yöneticisinin sunulacağı ekran genişliği |
| `-H [yükseklik]` | Pencerelerin/Pencere Yöneticisinin sunulacağı ekran yüksekliği |
| `-r [fps]` | Ekran tazeleme hızını/FPS limitini belirler (Örn: `-r 144`) |
| `-f` | Tam ekran (Fullscreen) modunda başlatır |
| `-b` | Sınırlandırılmamış pencereli (Borderless) modda başlatır |
| `-F [tür]` | Ölçekleme türü (`fsr`, `nis`, `linear`, `nearest`) |
| `--fsr-sharpness [0-20]`| FSR keskinleştirme seviyesi (0 en keskin) |

---

## Pratik Kullanım Örnekleri

### Örnek 1: Steam Üzerinde FSR ile 1080p Oyunu 4K Ekranına Ölçekleme
Steam kütüphanenizdeki bir oyuna sağ tıklayıp **Özellikler > Başlatma Seçenekleri** kısmına şu kodu ekleyebilirsiniz:

```bash
gamescope -w 1920 -h 1080 -W 3840 -H 2160 -f -F fsr -- %command%
```
*Bu komut oyunu içerde 1080p çalıştırır, GPU'yu yormaz ancak ekrana FSR ile 4K kalitesinde basar.*

### Örnek 2: Eski Bir Oyunu 60 FPS'e Sabitlenmiş 1440p Tam Ekran Yapma
```bash
gamescope -w 2560 -h 1440 -r 60 -f -- ./oyun_dosyasi
```

### Örnek 3: Lutris veya Heroic Games Launcher Üzerinde Kullanım
Masaüstü kısayolu veya başlatıcı içine yerel yürütülebilir dosya komutu olarak:
```bash
gamescope -w 1280 -h 720 -W 1920 -H 1080 -F fsr -- mangohud %command%
```
*(Bu örnekte performans göstergesi olan MangoHud da sürece dahil edilmiştir.)*

---

## Gamescope Kullanmanın Avantajları ve Dezavantajları

### Avantajları
* **Çökme Koruması:** Oyun çöktüğünde masaüstü ortamınız (X11/Wayland) çökmez, sadece Gamescope penceresi kapanır.
* **Girdi Gecikmesi (Input Lag) Azalması:** Doğrudan donanım katmanına erişim sayesinde minimum gecikme.
* **Çoklu Monitör Hatalarının Çözümü:** Farenin oyundan dışarı kaçması veya ikinci monitörün çözünürlüğünün bozulması gibi sorunları engeller.
* **Sürücü Bağımsız FSR:** Oyunda FSR desteği olmasa bile FSR kullanabilme imkanı.

### Dezavantajları
* NVIDIA kapalı kaynak kodlu sürücülerinde Wayland/DRM-KMS kısıtlamaları nedeniyle zaman zaman performans kayıpları veya uyumluluk sorunları yaşanabilir (AMD GPU'larda mükemmel çalışır).
* Anti-Cheat (Hile Karşıtı) yazılımı kullanan bazı online oyunlarda sanallaştırma katmanı olarak algılanma riski çok düşük de olsa teorik olarak mevcuttur.

---

## Özet

Gamescope, Valve'ın Linux oyun ekosistemine sunduğu en kritik teknolojilerden biridir. Oyunları masaüstü ortamının yükünden kurtararak donanım seviyesinde kontrol sağlar. Özellikle düşük konfigürasyonlu sistemlerde FSR desteğiyle performans artışı sağlarken, üst düzey sistemlerde ise daha kararlı kare zamanlaması ve HDR deneyimi sunar.