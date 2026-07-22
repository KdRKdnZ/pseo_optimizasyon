---
title: "RX 6600 Linux sürücü kurulumu"
description: "RX 6600 Linux sürücü kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# AMD Radeon RX 6600 Linux Sürücü Kurulum Rehberi

AMD Radeon RX 6600 (RDNA 2 mimarisi), Linux ekosisteminde en sorunsuz çalışan ekran kartlarından biridir. AMD'nin açık kaynaklı sürücü politikası sayesinde, RX 6600 için gerekli sürücüler Linux çekirdeğine (**AMDGPU**) ve grafik kütüphanesine (**Mesa**) doğrudan entegre olarak gelir. 

Bu rehberde, RX 6600 ekran kartınızdan maksimum performans almak için Ubuntu, Arch Linux ve Fedora üzerinde güncel grafik sürücülerinin (Mesa/Vulkan) nasıl kurulacağını ve optimize edileceğini teknik detaylarıyla inceleyeceğiz.

---

## Linux Grafik Sürücü Mimarisi: Açık Kaynak vs. AMDGPU-PRO

AMD grafik kartları Linux ortamında iki farklı sürücü yapısına sahiptir:

1. **Açık Kaynak Yığını (Önerilen):** `amdgpu` çekirdek modülü ve `Mesa` (RADV Vulkan + Gallium3D OpenGL) kütüphanelerinden oluşur. Oyun, günlük kullanım ve genel performans için en yüksek verimi sunar.
2. **AMDGPU-PRO (Mülk Sürücü):** AMD tarafından sağlanan kapalı kaynaklı sürücüdür. Yalnızca belirli endüstriyel yazılımlar (örneğin eski CAD araçları veya özel DaVinci Resolve sürümleri) için gereklidir. **Oyun performansı açık kaynaklı Mesa sürücülerinden daha düşüktür.**

---

## 1. Dağıtımlara Göre Sürücü Kurulumu ve Güncelleme

RX 6600 kartınız sistem tarafından varsayılan olarak tanınır. Ancak yeni çıkan oyunlarda yüksek FPS ve düşük gecikme süresi için **Mesa ve Vulkan** paketlerinin güncel tutulması kritiktir.

### A. Ubuntu / Pop!_OS / Linux Mint (Debian Tabanlı)

Ubuntu tabanlı sistemlerde varsayılan depolardaki Mesa sürümü eski kalabilir. En güncel kararlı Mesa sürücüsünü yüklemek için **Kisak PPA** kullanılması tavsiye edilir.

1. **Sistemi Güncelleyin:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Kisak Mesa PPA Deposunu Ekleleyin:**
   ```bash
   sudo add-apt-repository ppa:kisak/kisak-mesa -y
   sudo apt update
   ```

3. **Mesa ve Vulkan Paketlerini Yükleyin/Güncelleyin:**
   ```bash
   sudo apt install -y mesa-vulkan-drivers mesa-vulkan-drivers:i386 libgl1-mesa-dri libgl1-mesa-dri:i386
   ```

4. **Sistemi Yeniden Başlatın:**
   ```bash
   sudo reboot
   ```

---

### B. Arch Linux / Manjaro / EndeavourOS

Arch Linux, her zaman en güncel çekirdek ve Mesa sürümlerini sunar. RX 6600 için 32-bit (Steam oyunları için gerekli) ve 64-bit kütüphanelerin tamamını yüklemek için aşağıdaki adımları izleyin.

1. **/etc/pacman.conf** dosyasında `[multilib]` deposunun etkin olduğundan emin olun.
2. **Sürücü ve Vulkan Paketlerini Yükleyin:**
   ```bash
   sudo pacman -Syu
   sudo pacman -S --needed mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon xf86-video-amdgpu
   ```

---

### C. Fedora

Fedora, varsayılan olarak güncel açık kaynak sürücülerle gelir. Oyun performansı ve video kod çözme (VA-API) desteğini artırmak için RPM Fusion depolarını etkinleştirmek önerilir.

1. **RPM Fusion Depolarını Etkinleştirin:**
   ```bash
   sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
   ```

2. **Mesa ve Donanım Hızlandırma Paketlerini Güncelleyin:**
   ```bash
   sudo dnf upgrade --refresh
   sudo dnf install mesa-dri-drivers mesa-vulkan-drivers mesa-va-drivers-freeworld
   ```

---

## 2. Kurulum Doğrulama ve Sürücü Durum Kontrolü

Sürücülerin doğru yüklendiğini, RX 6600 kartınızın aktif olduğunu ve Vulkan desteğini doğrulamak için terminalde aşağıdaki komutları çalıştırın:

### Çekirdek Modülünü Kontrol Etme:
```bash
lspci -k | grep -A 3 -E "(VGA|3D)"
```
*Çıktıda `Kernel driver in use: amdgpu` ifadesini görmelisiniz.*

### OpenGL ve Mesa Sürümünü Kontrol Etme:
```bash
glxinfo | grep -i "OpenGL renderer"
```
*Çıktı: `OpenGL renderer string: AMD Radeon RX 6600 (RADV NAVI23)...` şeklinde olmalıdır.*

### Vulkan Desteğini Doğrulama:
```bash
vulkaninfo | grep deviceName
```
*Çıktıda `RADV NAVI23` veya `AMD Radeon RX 6600` ibaresi yer almalıdır.*

---

## 3. RX 6600 İçin Performans Optimizasyonları

### A. CoreCtrl ile Fan ve Güç Yönetimi
RX 6600'ün fan eğrisini ayarlamak ve güç limitini (Power Limit) değiştirmek için MSI Afterburner benzeri bir araç olan **CoreCtrl** kullanabilirsiniz.

1. **CoreCtrl Yükleme (Ubuntu için):**
   ```bash
   sudo apt install corectrl
   ```
2. **Gelişmiş Denetimi Etkinleştirme:**
   Çekirdek parametrelerine `amdgpu.ppfeaturemask=0xffffffff` değerini ekleyerek voltaj ve saat hızı kontrolünü açabilirsiniz. GRUB yapılandırma dosyanıza (`/etc/default/grub`) şu parametreyi ekleyin:
   ```text
   GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.ppfeaturemask=0xffffffff"
   ```
   Ardından GRUB'u güncelleyin (`sudo update-grub`) ve sistemi yeniden başlatın.

### B. Ray Tracing (Işın İzleme) Etkinleştirme
RX 6600, Mesa RADV sürücüsü üzerinden Ray Tracing destekler. Oyun bazlı Ray Tracing desteğini zorlamak için başlatma seçeneğine şu çevresel değişkeni ekleyebilirsiniz:

```bash
VKD3D_CONFIG=dxr %command%
# veya Mesa Vulkan için
RADV_PERFTEST=rt %command%
```

---

## Sıkça Sorulan Sorular (SSS)

**1. AMD'nin resmi sitesinden `.deb` veya `.rpm` uzantılı sürücüyü indirmeli miyim?**  
Hayır. AMD'nin web sitesindeki sürücüler ticari dağıtımlar (RHEL, Ubuntu LTS) ve profesyonel iş yükleri içindir. Masaüstü ve oyun kullanımı için Linux çekirdeğindeki ve Mesa'daki açık kaynak sürücüler çok daha güncel ve performanslıdır.

**2. RX 6600 için En uygun Vulkan Sürücüsü Hangisidir (RADV vs AMDVLK)?**  
Linux üzerinde en yüksek performans ve oyun uyumluluğunu **RADV** (Mesa'nın Vulkan sürücüsü) sunar. AMDVLK (AMD'nin resmi açık kaynak sürücüsü) genellikle tercih edilmez.

**3. Oyunlarda Düşük FPS Alıyorum, Ne Yapmalıyım?**  
`gamemode` paketini yükleyerek CPU ve GPU'nun performans moduna geçmesini sağlayabilirsiniz.
- Ubuntu/Debian: `sudo apt install gamemode`
- Steam Başlatma Seçeneği: `gamemoderun %command%`