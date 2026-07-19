---
title: mangohud kurulumu
description: mangohud kurulumu hakkında detaylı optimizasyon ve donanım rehberi.
---

# Linux Performans İzleme: Adım Adım MangoHud Kurulumu ve Yapılandırması

Linux işletim sistemlerinde oyun oynarken veya grafik yoğunluklu uygulamaları çalıştırırken donanım kaynaklarının anlık durumunu izlemek, sistem optimizasyonu için kritik öneme sahiptir. **MangoHud**, Vulkan ve OpenGL uygulamaları için geliştirilmiş, özelleştirilebilir ve açık kaynaklı bir donanım izleme (overlay) katmanıdır. CPU/GPU sıcaklığı, yükü, VRAM/RAM kullanımı, FPS ve kare zamanlaması (frame time) gibi verileri gerçek zamanlı olarak ekrana yansıtır.

Bu rehberde, kıdemli bir sistem mimarı ve donanım uzmanı perspektifiyle, farklı Linux dağıtımlarında **MangoHud kurulumu** adımlarını, yapılandırma detaylarını ve performans optimizasyonlarını inceleyeceğiz.

---

## MangoHud Nedir ve Neden Kullanılmalıdır?

MangoHud, MSI Afterburner/RivaTuner Statistics Server (RTSS) yazılımının Linux ekosistemindeki en güçlü ve kararlı alternatifidir. C++ ile geliştirilen bu araç, doğrudan grafik sürücüleri ve Vulkan API katmanı ile entegre çalışarak sistem üzerinde minimum ek yük (overhead) oluşturur.

**Temel Avantajları:**
*   **Düşük Gecikme:** Doğrudan Vulkan katmanına (layer) entegre olduğu için CPU döngülerini gereksiz yere meşgul etmez.
*   **Geniş Donanım Desteği:** AMD, NVIDIA ve Intel grafik işlemcileriyle tam uyumludur.
*   **Kapsamlı Metrikler:** Kare zamanlaması grafiği (frame time graph), minimum/maksimum/ortalama FPS, RAM/VRAM kullanımı ve işlemci çekirdeklerinin tekil sıcaklık takibini yapabilir.

---

## Farklı Linux Dağıtımlarında MangoHud Kurulumu

MangoHud kurulumu, kullandığınız Linux dağıtımının paket yöneticisine ve uygulamanın (örneğin Steam) Flatpak veya yerel (native) olarak kurulup kurulmadığına göre değişiklik gösterir.

### Arch Linux ve Tabanlı Dağıtımlar (Manjaro, EndeavourOS)

Arch Linux kullanıcıları, MangoHud paketlerine resmi depolardan ve AUR (Arch User Repository) üzerinden erişebilirler. Hem 64-bit hem de 32-bit (eski oyunlar için) kütüphanelerin kurulması zorunludur.

Terminali açın ve aşağıdaki komutu çalıştırın:

```bash
sudo pacman -S mangohud lib32-mangohud
```

Eğer en güncel geliştirme sürümünü (Git) kurmak istiyorsanız, bir AUR yardımcısı (örneğin `yay`) kullanarak şu komutu çalıştırabilirsiniz:

```bash
yay -S mangohud-git lib32-mangohud-git
```

### Ubuntu, Debian ve Linux Mint

Ubuntu 20.04 LTS ve üzeri sürümlerde MangoHud, resmi depolarda yer almaktadır. Ancak en güncel donanım destekleri için PPA deposunu kullanmak veya doğrudan GitHub üzerinden derlemek önerilir.

**Resmi Depodan Kurulum:**

```bash
sudo apt update
sudo apt install mangohud
```

**En Güncel Sürüm İçin (GitHub Üzerinden Manuel Derleme):**

Eğer dağıtımınızdaki paket eskiyse, aşağıdaki bağımlılıkları yükleyip kaynak koddan derleme yapabilirsiniz:

```bash
# Bağımlılıkların yüklenmesi
sudo apt install dbus-user-session git python3-pip python3-setuptools python3-wheel ninja-build meson libx11-dev libxnvctrl-dev

# Kaynak kodun çekilmesi ve derlenmesi
git clone --recurse-submodules https://github.com/flightlessmango/MangoHud.git
cd MangoHud
./build.sh install
```

### Fedora ve RHEL Tabanlı Dağıtımlar

Fedora depolarında MangoHud paketlenmiş olarak sunulmaktadır. Kurulum için `dnf` paket yöneticisi kullanılır:

```bash
sudo dnf install mangohud
```

### Evrensel Kurulum: Flatpak (Steam ve Heroic Launcher İçin)

Eğer Steam veya Heroic Games Launcher gibi oyun istemcilerini **Flatpak** olarak kullanıyorsanız, sistem genelinde kurulu olan MangoHud bu uygulamalar tarafından algılanmayacaktır. Flatpak sandbox (yalıtılmış alan) mimarisi nedeniyle MangoHud'ı Flatpak çalışma zamanı (runtime) olarak kurmanız gerekir.

Aşağıdaki komutla Flatpak için MangoHud kurulumunu gerçekleştirebilirsiniz:

```bash
flatpak install flathub org.freedesktop.Platform.VulkanLayer.MangoHud
```

---

## MangoHud Yapılandırması (Configuration) Nasıl Yapılır?

MangoHud, varsayılan olarak temel metrikleri gösterir. Ancak arayüzü özelleştirmek, renkleri değiştirmek veya gösterilecek donanım parametrelerini seçmek için bir yapılandırma dosyası oluşturmanız gerekir.

### Manuel Yapılandırma Dosyası Oluşturma

MangoHud, yapılandırma dosyasını kullanıcı dizini altındaki belirli bir yolda arar. İlk olarak bu dizini ve dosyayı oluşturalım:

```bash
mkdir -p ~/.config/MangoHud
nano ~/.config/MangoHud/MangoHud.conf
```

Aşağıda, donanım uzmanları tarafından optimize edilmiş, hem GPU hem de CPU limitlerini analiz etmenize olanak tanıyan **örnek bir `MangoHud.conf` şablonu** yer almaktadır. Bu içeriği oluşturduğunuz dosyaya yapıştırın:

```text
# MangoHud Optimize Edilmiş Yapılandırma Dosyası

# Performans Metrikleri
fps
frame_timing=1
frametime_color=00FF00

# CPU İzleme
cpu_temp
cpu_mhz
cpu_power
cpu_stats

# GPU İzleme
gpu_temp
gpu_core_clock
gpu_mem_clock
gpu_power
gpu_stats

# Bellek İzleme
ram
vram

# Görsel Özelleştirmeler
legacy_layout=0
horizontal=0
round_corners=10
background_alpha=0.5
background_color=020202
font_size=24

# Kısayollar
toggle_hud=Shift_R+F12
```

Dosyayı kaydedip çıkın (Nano için `CTRL+O`, `Enter`, `CTRL+X`).

### GOverlay ile Grafiksel Arayüz (GUI) Kullanımı

Kodlarla uğraşmak istemiyorsanız, MangoHud yapılandırmasını görsel olarak yapmanızı sağlayan **GOverlay** aracını kurabilirsiniz.

*   **Arch Linux:** `sudo pacman -S goverlay`
*   **Debian/Ubuntu:** `sudo apt install goverlay`
*   **Fedora:** `sudo dnf install goverlay`

GOverlay arayüzü üzerinden yaptığınız tüm değişiklikler otomatik olarak `~/.config/MangoHud/MangoHud.conf` dosyasına yazılır.

---

## MangoHud Nasıl Çalıştırılır?

Kurulum ve yapılandırma tamamlandıktan sonra, MangoHud'ı oyunlarda aktif etmenin farklı yolları vardır.

### 1. Steam Başlatma Seçenekleri Entegrasyonu

Steam kütüphanenizdeki bir oyunda MangoHud'ı aktif etmek için:

1.  Steam'i açın ve kütüphanenizden bir oyuna sağ tıklayıp **Özellikler (Properties)** seçeneğine tıklayın.
2.  **Genel (General)** sekmesinde bulunan **Başlatma Seçenekleri (Launch Options)** alanına şu komutu ekleyin:

```bash
mangohud %command%
```

Eğer oyun Proton (Windows uyumluluk katmanı) kullanıyorsa komut yine aynı kalacaktır.

### 2. Lutris ve Heroic Games Launcher Entegrasyonu

*   **Lutris:** Oyunun üzerine sağ tıklayın -> *Configure* -> *System options* sekmesine gelin. Aşağı kaydırarak **MangoHud** seçeneğini aktif (Enable) hale getirin.
*   **Heroic Games Launcher:** Oyun ayarlarına girin ve *Alternative Launchers* veya *Sistem* sekmesinden **Enable MangoHud** seçeneğini işaretleyin.

### 3. Terminal Üzerinden Doğrudan Çalıştırma

Yerel bir OpenGL veya Vulkan uygulamasını terminalden MangoHud ile başlatmak için uygulamanın önüne `mangohud` parametresini eklemeniz yeterlidir:

```bash
mangohud ./oyun_dosyasi
```

---

## Sık Karşılaşılan Sorunlar ve Çözümleri

### Sorun 1: MangoHud Ekranı Görünmüyor (Özellikle 32-bit Oyunlarda)
**Çözüm:** Genellikle 32-bit kütüphanelerin eksikliğinden kaynaklanır. Arch Linux kullanıyorsanız `lib32-mangohud` paketinin, Ubuntu kullanıyorsanız ilgili 32-bit sürücülerin kurulu olduğundan emin olun.

### Sorun 2: Flatpak Steam'de MangoHud Çalışmıyor
**Çözüm:** Flatpak izinlerinin MangoHud'ın donanım bilgilerine erişmesini engellemediğinden emin olun. Terminalde şu komutu çalıştırarak gerekli izinleri tanımlayabilirsiniz:

```bash
flatpak override --user --filesystem=xdg-config/MangoHud:ro org.valvesoftware.Steam
```

### Sorun 3: OpenGL Oyunlarında FPS Sayacı Kilitleniyor veya Çöküyor
**Çözüm:** OpenGL oyunlarında MangoHud bazen `ld_preload` mekanizmasına ihtiyaç duyar. Bu durumda başlatma seçeneğini şu şekilde değiştirin:

```bash
mangohud --dlsym %command%
```