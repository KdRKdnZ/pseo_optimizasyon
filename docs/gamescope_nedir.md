# Gamescope Nedir? Linux İçin Valve Tarafından Geliştirilen Mikro Kompozitör Rehberi

**Gamescope**, Valve tarafından Linux işletim sistemleri için geliştirilen, oyunların pencerelenmesi, ölçeklendirilmesi ve kare hızı yönetimi gibi süreçleri ana masaüstü ortamından izole ederek optimize eden açık kaynaklı bir **mikro kompozitör (micro-compositor)** mimarisidir. İlk olarak Steam Deck'in işletim sistemi olan SteamOS 3.0'ın temel taşlarından biri olarak piyasaya sürülmüş, ardından tüm Linux dağıtımlarında kullanılabilir hale gelmiştir.

Geleneksel pencereli mod (windowed mode) veya tam ekran (fullscreen) uygulamalarının aksine Gamescope, oyunu sanal bir ekran sunucusunda (nested Wayland compositor) çalıştırarak sürücü seviyesinde kontrol sağlar.

---

## Gamescope Nasıl Çalışır? Teknik Mimari

Gamescope, oyun ile mevcut masaüstü ortamınız (GNOME, KDE Plasma, XFCE vb.) arasında bir katman görevi görür. 

1. **İzolasyon (Sandboxing Display):** Oyun, masaüstünüzün X11 veya Wayland grafik sunucusuna doğrudan erişmek yerine Gamescope'un oluşturduğu korumalı alanda çalışır. Oyun masaüstü çözünürlüğünü değiştiremez.
2. **XWayland Entegrasyonu:** X11 mimarisi için yazılmış eski veya modern oyunları Wayland protokolüne dönüştürür.
3. **Direct Scanout:** Desteklenen donanımlarda Gamescope, kareleri doğrudan ekrana göndererek (Direct Scanout) masaüstü kompozitörünün getirdiği ekstra gecikmeyi (input lag) ortadan kaldırır.

```
[ Oyun (X11 / Native Wayland) ]
             │
             ▼
      [ GAMESCOPE ] ➔ (FSR, FPS Limiti, Latency Control, HDR)
             │
             ▼
[ Ana Masaüstü Sunucusu (Kwin, Mutter, Sway vb.) ]
             │
             ▼
       [ GPU Sürücüsü ]
```

---

## Gamescope’un Temel Özellikleri ve Avantajları

### 1. İşletim Sistemi Seviyesinde AMD FSR ve NIS
Gamescope, oyunun içinde FSR (FidelityFX Super Resolution) desteği olmasa bile **sürücü/kompozitör seviyesinde FSR 1.0** veya NVIDIA Image Scaling (NIS) uygulayabilir. 720p çözünürlükte çalışan bir oyunu, kalite kaybını minimize ederek 1080p veya 4K ekrana ölçekleyebilirsiniz.

### 2. Hassas Kare Hızı Limitleme (FPS Capping)
Oyun içi FPS kısıtlayıcılar genellikle tutarsız kare sürelerine (frame pacing) neden olur. Gamescope, kareleri ekran kartı sürücüsü seviyesinde yakalayarak mükemmel kare süresi kararlılığı sağlar.

### 3. Girdi Gecikmesini (Input Lag) Azaltma
Masaüstü ortamlarının (örneğin X11 VSync) yarattığı gecikmeleri bypass eder. Oyun kendi VSync ayarından bağımsız olarak Gamescope üzerinden en düşük gecikmeyle render edilir.

### 4. Esnek Çözünürlük ve En-Boy Oranı Yönetimi
Eski oyunların 4:3 formatındaki zorunlu çözünürlüklerini, ultra geniş (21:9) ekranlarda siyah bantlar (letterboxing) ekleyerek veya düzgün ölçekleyerek masaüstünüzü bozmadan çalıştırır.

### 5. HDR ve VRR (Variable Refresh Rate) Desteği
Gamescope, Linux ekosisteminde HDR (High Dynamic Range) oyunculuğun öncüsüdür. Destekleyen GPU ve ekranlarda HDR ve FreeSync/G-Sync teknolojilerini sorunsuz bir şekilde oyuna aktarır.

---

## Gamescope Kurulumu

Popüler Linux dağıtımlarında Gamescope paket yöneticileri üzerinden kolayca kurulabilir:

* **Arch Linux / Manjaro:**
  ```bash
  sudo pacman -S gamescope
  ```

* **Fedora:**
  ```bash
  sudo dnf install gamescope
  ```

* **Ubuntu / Debian (22.04+):**
  ```bash
  sudo apt install gamescope
  ```

---

## Gamescope Kullanımı ve Komut Parametreleri

Gamescope, komut satırından veya Steam başlatma seçenekleri üzerinden çalıştırılır. Temel sözdizimi şu şekildedir:

```bash
gamescope [seçenekler] -- [çalıştırılacak_oyun_veya_komut]
```

### Önemli Parametreler:

| Parametre | Açıklama |
| :--- | :--- |
| `-w` | Oyunun iç çözünürlük genişliği (Internal width) |
| `-h` | Oyunun iç çözünürlük yüksekliği (Internal height) |
| `-W` | Ekran çıktısının genişliği (Output width) |
| `-H` | Ekran çıktısının yüksekliği (Output height) |
| `-r` | Hedef Yenileme Hızı (FPS / Hz limiti) |
| `-F` | Ölçeklendirme türü (`fsr`, `nis`, `linear`, `nearest`) |
| `-f` | Tam ekran modunda başlatır |
| `--fsr-sharpness` | FSR keskinlik değeri (0-20 arası, varsayılan 2) |

---

## Kullanım Senaryoları ve Örnekler

### Örnek 1: FSR ile 720p Oyunu 1080p Tam Ekrana Ölçekleme
Oyunu 1280x720 çözünürlükte işleyip, FSR algoritması ile 1920x1080 tam ekran çıktısına yükseltmek için:

```bash
gamescope -w 1280 -h 720 -W 1920 -H 1080 -F fsr -f -- %command%
```

### Örnek 2: FPS Limitleme ve Pencere Modu
Oyunu 60 FPS'e sabitleyip 1080p boyutunda pencereli modda çalıştırmak için:

```bash
gamescope -w 1920 -h 1080 -r 60 -- %command%
```

### Örnek 3: Steam İçinde Başlatma Seçeneği Olarak Ekleme
Steam kütüphanenizdeki bir oyuna sağ tıklayıp **Özellikler > Başlatma Seçenekleri** kısmına şu satırı ekleyebilirsiniz:

```bash
gamescope -w 1440 -h 900 -W 2560 -H 1440 -F fsr -r 144 -f -- %command%
```
*(Bu komut: Oyunu 1400x900'de işler, FSR ile 2K'ya çeker, 144Hz/FPS ile kısıtlar ve tam ekran yapar.)*

---

## Neden Gamescope Kullanmalısınız?

* **Steam Deck Deneyimi:** Masaüstü PC'nizde Steam Deck akıcılığı elde etmek için.
* **Eski Oyun Uyumluluğu:** Çözünürlüğü bozulan veya alt-tab yapınca çöken oyunları izole etmek için.
* **Performans Artışı:** Düşük konfigürasyonlu sistemlerde donanım tabanlı FSR ile FPS kazanmak için.
* **Giriş Gecikmesi Hassasiyeti:** Rekabetçi oyunlarda Wayland veya X11 masaüstü gecikmelerinden kurtulmak için.

Gamescope, modern Linux oyunculuk ekosisteminin (Proton, Wine, DXVK) en kritik tamamlayıcı bileşenlerinden biridir.