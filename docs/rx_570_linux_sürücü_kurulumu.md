# AMD Radeon RX 570 Linux Sürücü Kurulum Rehberi

AMD Radeon RX 570, Polaris mimarisine dayanan ve Linux ekosisteminde mükemmel açık kaynak sürücü desteğine sahip bir grafik kartıdır. Linux çekirdeğinde (Kernel) entegre olarak gelen **AMDGPU** sürücüsü ve kullanıcı alanındaki **Mesa** grafik kütüphaneleri sayesinde, RX 570 için harici kapalı kaynak sürücü yüklemeye gerek kalmadan yüksek performans elde edilir.

Bu rehberde, RX 570 ekran kartınız için Linux dağıtımlarında en güncel açık kaynak sürücülerin (Mesa/Vulkan) nasıl kurulacağı, yapılandırılacağı ve doğrulanacağı adım adım açıklanmaktadır.

---

## 1. Temel Sürücü Mimarisi: Açık Kaynak vs. AMDGPU-PRO

*   **Mesa / AMDGPU (Tavsiye Edilen):** Linux çekirdeğine entegre açık kaynak sürücüdür. Oyun performansı, Steam/Proton uyumluluğu ve sistem kararlılığı açısından AMDGPU-PRO'dan çok daha üstündür.
*   **AMDGPU-PRO (Kapalı Kaynak):** Yalnızca profesyonel kurumsal yazılımlar (DaVinci Resolve, CAD vb.) ve spesifik OpenCL gereksinimleri için gereklidir. Günlük kullanım ve oyun için kesinlikle önerilmez.

---

## 2. Mevcut Sürücü Durumunu Kontrol Etme

Terminali açın ve RX 570 kartınızın sistem tarafından tanınıp tanınmadığını ve hangi sürücünün aktif olduğunu kontrol edin:

```bash
lspci -k | grep -A 3 -E "(VGA|3D)"
```

Çıktıda aşağıdaki satırları görmelisiniz:
*   `Kernel driver in use: amdgpu`
*   `Kernel modules: amdgpu`

---

## 3. Dağıtıma Göre RX 570 Sürücü Kurulumu

Açık kaynak sürücüler ve Vulkan kütüphaneleri dağıtım paket yöneticileri aracılığıyla yüklenir.

### A. Ubuntu / Linux Mint / Pop!_OS Kurulumu

1. **Sistemi Güncelleyin:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Güncel Mesa Sürücülerini Ekleyin (İsteğe Bağlı ama Önerilir):**
   En son oyun performans iyileştirmelerini almak için Kisak-Mesa PPA depolamasını ekleyebilirsiniz:
   ```bash
   sudo add-apt-repository ppa:kisak/kisak-mesa -y
   sudo apt update && sudo apt upgrade -y
   ```

3. **Vulkan ve 32-bit (Steam Uyumlu) Paketleri Yükleyin:**
   ```bash
   sudo dpkg --add-architecture i386
   sudo apt update
   sudo apt install mesa-vulkan-drivers mesa-vulkan-drivers:i386 libgl1-mesa-dri libgl1-mesa-dri:i386
   ```

### B. Fedora Kurulumu

Fedora, varsayılan olarak güncel Mesa paketleriyle gelir.

1. **Paketleri Güncelleyin ve Vulkan Desteğini Yükleyin:**
   ```bash
   sudo dnf upgrade --refresh
   sudo dnf install mesa-dri-drivers mesa-vulkan-drivers mesa-vulkan-drivers.i686 mesa-dri-drivers.i686
   ```

### C. Arch Linux / Manjaro Kurulumu

1. **Sistemi Güncelleyin:**
   ```bash
   sudo pacman -Syu
   ```

2. **Sürücü ve Vulkan Paketlerini Yükleyin:**
   *(32-bit paketler için `/etc/pacman.conf` dosyasında `multilib` deposunun açık olduğundan emin olun.)*
   ```bash
   sudo pacman -S xf86-video-amdgpu mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon libva-mesa-driver mesa-vdpau
   ```

---

## 4. Vulkan ve Sürücü Doğrulaması

Kurulumun başarılı olduğunu ve 3D hızlandırmanın çalıştığını doğrulamak için aşağıdaki araçları kullanın.

### OpenGL Doğrulaması
```bash
glxinfo | grep "OpenGL renderer"
```
*Beklenen çıktı:* `OpenGL renderer string: AMD Radeon RX 570 Series (RADV POLARIS10 ...)`

### Vulkan Doğrulaması
Vulkan araç paketini yükleyin (`vulkan-tools`) ve testi çalıştırın:

```bash
vkcube
```
Ekranda dönen bir Vulkan küpü görünüyorsa Vulkan sürücüleri sorunsuz çalışıyor demektir.

---

## 5. RX 570 Performans ve Fan Ayarları (Gelişmiş)

AMD RX 570 ekran kartınızın fan profillerini, güç limitlerini (Power Limit) ve çekirdek saat hızlarını grafik arayüz üzerinden yönetmek için **CoreCtrl** yazılımını kullanabilirsiniz.

### CoreCtrl Kurulumu (Ubuntu/Debian):
```bash
sudo apt install corectrl
```

### CoreCtrl Kurulumu (Arch Linux):
```bash
sudo pacman -S corectrl
```

> **Not:** Tam voltaj ve fan kontrolünü aktif etmek için GRUB önyükleyicisine `amdgpu.ppfeaturemask=0xffffffff` parametresini eklemeniz gerekebilir.

---

## 6. Sık Karşılaşılan Sorunlar ve Çözümleri

### Ekran Yırtılması (Screen Tearing)
X11 oturumu kullanıyorsanız ve ekran yırtılması yaşıyorsanız, `/etc/X11/xorg.conf.d/20-amdgpu.conf` konfigürasyon dosyasını oluşturun ve aşağıdaki kodları ekleyin:

```Xorg
Section "Device"
     Identifier "AMD Graphics"
     Driver "amdgpu"
     Option "TearFree" "true"
EndSection
```

### Oyunlarda Düşük FPS Veya Vulkan Hatası
Sistemde birden fazla Vulkan sürücüsü tanımlıysa (örneğin amdvlk ve RADV), Mesa'nın yüksek performanslı **RADV** sürücüsünün aktif olduğundan emin olun. Başlatma seçeneği olarak şu parametreyi kullanabilirsiniz:

```bash
AMD_VULKAN_ICD=RADV %command%
```

## Özet

AMD Radeon RX 570, Linux ortamında sürücü kurulumu açısından en sorunsuz kartlardan biridir. AMD'nin resmi web sitesinden `.run` veya `.deb` uzantılı AMDGPU-PRO paketlerini indirip manuel kurulum yapmanıza gerek yoktur. Dağıtımınızın paket yöneticisi üzerinden **Mesa** ve **vulkan-radeon** paketlerini güncel tutmanız, maksimum oyun ve sistem performansı almanız için yeterlidir.