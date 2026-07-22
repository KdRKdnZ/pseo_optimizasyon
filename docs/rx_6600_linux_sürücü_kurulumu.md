# AMD Radeon RX 6600 Linux Sürücü Kurulum Rehberi

AMD Radeon RX 6600 (RDNA2 / Navi 23 mimarisi), Linux işletim sistemlerinde **çekirdek seviyesinde (in-tree)** sürücü desteğine sahiptir. NVIDIA grafik kartlarının aksine, RX 6600 için harici bir kapalı kaynak sürücü kurmanız gerekmez. Sürücü altyapısı doğrudan Linux Çekirdeği (Kernel) ve **Mesa 3D Grafik Kütüphanesi** tarafından sağlanır.

Bu rehberde, RX 6600 ekran kartınızdan maksimum performans (OpenGL, Vulkan, OpenCL) almanız için gerekli sürücülerin ve bağımlılıkların popüler Linux dağıtımlarına kurulumu teknik detaylarıyla açıklanmıştır.

---

## 1. Gereksinimler ve Mimarinin Kontrolü

RX 6600'ün tam performansla çalışabilmesi için sisteminizin aşağıdaki minimum sürümleri karşılaması gerekir:

*   **Linux Kernel:** 5.11 veya üzeri (Önerilen: 6.x+)
*   **Mesa:** 21.1 veya üzeri (Önerilen: 23.x / 24.x)
*   **LLVM:** 12.0 veya üzeri

Ekran kartınızın çekirdek tarafından doğru algılanıp algılanmadığını kontrol etmek için terminalde şu komutu çalıştırın:

```bash
lspci -nnk | grep -A 3 -i vga
```

Çıktıda `Kernel driver in use: amdgpu` ifadesini görüyorsanız, temel sürücü aktif durumdadır.

---

## 2. Dağıtıma Göre Sürücü ve Vulkan Kurulumu

Oyun ve grafik performansı için **AMDGPU (Çekirdek Sürücüsü)** ile **Mesa RADV (Vulkan Sürücüsü)** bileşenlerinin kurulması gerekir.

### A. Ubuntu / Linux Mint / Pop!_OS (Debian Tabanlı)

Ubuntu tabanlı sistemler genellikle güncel Mesa sürümlerini içermez. En yüksek oyun performansı için PPA aracılığıyla Mesa'yı güncellemeniz önerilir.

1. **Güncel Mesa Depolarını (Kisak PPA) Ekleme:**
   ```bash
   sudo add-apt-repository ppa:kisak/kisak-mesa
   sudo apt update && sudo apt upgrade -y
   ```

2. **32-bit ve 64-bit Vulkan/Mesa Paketlerini Yükleme (Steam ve Proton İçin Şarttır):**
   ```bash
   sudo apt install mesa-vulkan-drivers mesa-vulkan-drivers:i386 libgl1-mesa-dri libgl1-mesa-dri:i386 libglx-mesa0 libglx-mesa0:i386
   ```

### B. Arch Linux / Manjaro / EndeavourOS

Arch Linux en güncel Mesa sürücülerini doğrudan resmi depolarında sunar.

1. **32-Bit (multilib) Deposunu Etkinleştirme:**
   `/etc/pacman.conf` dosyasını düzenleyin ve `[multilib]` bölümündeki yorum satırlarını (`#`) kaldırın. Ardından depoyu güncelleyin:
   ```bash
   sudo pacman -Syu
   ```

2. **Gerekli Paketlerin Kurulumu:**
   ```bash
   sudo pacman -S --needed lib32-mesa mesa vulkan-radeon lib32-vulkan-radeon xf86-video-amdgpu libva-mesa-driver lib32-libva-mesa-driver
   ```

### C. Fedora

Fedora varsayılan olarak güncel açık kaynak sürücülerle gelir. Oyunlarda Tam performans ve 32-bit desteği için şu adımları izleyin:

1. **RPM Fusion Depolarını Etkinleştirme:**
   ```bash
   sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
   ```

2. **Mesa ve Vulkan Sürücülerini Güncelleme/Yükleme:**
   ```bash
   sudo dnf install mesa-dri-drivers mesa-vulkan-drivers mesa-vulkan-drivers.i686 mesa-dri-drivers.i686
   ```

---

## 3. ROCm / OpenCL Kurulumu (Blender, DaVinci Resolve ve Yapay Zeka İçin)

Oyun oynamak için OpenCL gerekmez. Ancak Blender rendering, DaVinci Resolve veya PyTorch/TensorFlow kullanıyorsanız AMD'nin **ROCm** paketini yüklemeniz gerekir.

### ROCm OpenCL Kurulumu (Ubuntu Örneği)

1. AMD'nin resmi depolama aracını indirin ve kurun:
   ```bash
   wget https://repo.radeon.com/amdgpu-install/6.0/ubuntu/jammy/amdgpu-install_6.0.60000-1_all.deb
   sudo apt install ./amdgpu-install_6.0.60000-1_all.deb
   ```

2. Yalnızca OpenCL/ROCm bileşenlerini sisteme entegre edin (Açık kaynak Mesa sürücüsünü bozmadan):
   ```bash
   sudo amdgpu-install --usecase=rocm,opencl --no-dkms
   ```

3. Kullanıcınızı `render` ve `video` gruplarına ekleyin:
   ```bash
   sudo usermod -aG render $USER
   sudo usermod -aG video $USER
   ```
   *(Değişikliklerin geçerli olması için sistemi yeniden başlatın).*

---

## 4. Kurulum ve Performans Doğrulama

Sürücülerin doğru yüklendiğini ve Donanım Hızlandırmanın (Hardware Acceleration) aktif olduğunu doğrulamak için aşağıdaki araçları kullanabilirsiniz.

### OpenGL Doğrulaması
`mesa-utils` paketini yükledikten sonra:
```bash
glxinfo | grep "OpenGL renderer"
```
*Beklenen Çıktı:* `OpenGL renderer string: AMD Radeon RX 6600 (RADV NAVI23)` veya benzeri bir Mesa sürücü kimliği.

### Vulkan Doğrulaması
`vulkan-tools` paketini yükledikten sonra:
```bash
vulkaninfo | grep deviceName
```
*Beklenen Çıktı:* `deviceName = AMD Radeon RX 6600 (RADV NAVI23)`

---

## 5. RX 6600 İnce Ayarlar ve Sorun Giderme

### Oyunlarda Şader Derleme Kasılmalarını (Stutter) Engelleme
Mesa RADV sürücüsü varsayılan olarak **ACO (AMD Compiler)** kullanır. ACO, oyunlardaki gölgelendirici derleme sürelerini ciddi oranda düşürür. Etkin olup olmadığını kontrol etmek veya zorlamak için başlangıç parametrelerine şu değişkeni ekleyebilirsiniz:

```bash
RADV_PERFTEST=aco %command%
```

### Video Derleme / Çözme (VA-API) Desteği
RX 6600, h264, h265 ve VP9 donanımsal video kod çözme (hardware decoding) destekler. VA-API durumunu kontrol etmek için:

```bash
sudo apt install vainfo # Ubuntu/Debian
# veya
sudo pacman -S libva-utils # Arch
vainfo
```
Çıktıda `VAProfileH264...` ve `VAEntrypointVLD` ifadeleri görünmelidir.