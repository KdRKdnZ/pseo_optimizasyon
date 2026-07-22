# RTX 4060 Linux Sürücü Kurulum Rehberi: Adım Adım Teknik Anlatım

NVIDIA GeForce RTX 4060 (Ada Lovelace mimarisi), Linux sistemlerde tam performans, CUDA desteği ve Ray Tracing özelliklerini kullanabilmek için en az **NVIDIA 535.xx** veya daha güncel (önerilen **550.xx** ve üzeri) sürücülere ihtiyaç duyar. Açık kaynaklı "Nouveau" sürücüleri RTX 4000 serisinde donanım ivmelendirmesini tam sunamadığı için mülk (proprietary) NVIDIA sürücülerinin kurulması zorunludur.

Bu rehberde; Ubuntu/Debian, Fedora ve Arch Linux dağıtımlarında RTX 4060 sürücülerinin doğru, çakışmasız ve performanslı kurulumu teknik adımlarla açıklanmıştır.

---

## 1. Ön Hazırlık ve Gereksinimler

Kuruluma başlamadan önce sistemde çakışmaları önlemek ve doğru modüllerin yüklendiğinden emin olmak için aşağıdaki adımlar uygulanmalıdır:

1. **Secure Boot Durumu:** Eğer BIOS/UEFI üzerinde **Secure Boot** açıksa, sürücü modüllerinin imzalanması gerekir. Kurulumu kolaylaştırmak için geçici olarak BIOS'tan Secure Boot'u kapatmanız önerilir.
2. **Sistem Güncellemesi:** Paket depolarını ve çekirdeği (kernel) güncelleyin.

```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade -y

# Fedora
sudo dnf upgrade --refresh -y

# Arch Linux
sudo pacman -Syu
```

---

## 2. Dağıtıma Göre RTX 4060 Sürücü Kurulumu

### A. Ubuntu / Debian / Linux Mint Kurulumu

Ubuntu tabanlı sistemlerde sürücüyü PPA depoları üzerinden veya CLI yardımıyla kurmak en güvenli yöntemdir.

#### Yöntem 1: Otomatik CLI Kurulumu (Önerilen)

Sisteminiz için en uygun sürücüyü tespit edip kurmak için:

```bash
sudo ubuntu-drivers install
```

 Veya doğrudan RTX 4060 için önerilen güncel sürücüyü elle belirtin:

```bash
sudo apt install nvidia-driver-550 nvidia-dkms-550 -y
```

#### Yöntem 2: Grafik Arayüzü (GUI) ile Kurulum

1. **Uygulamalar** menüsünden **Yazılım ve Güncellemeler (Software & Updates)** uygulamasını açın.
2. **Ek Sürücüler (Additional Drivers)** sekmesine gelin.
3. **NVIDIA driver metapackage from nvidia-driver-550 (proprietary)** seçeneğini işaretleyin.
4. **Değişiklikleri Uygula (Apply Changes)** butonuna tıklayın ve işlem bitince sistemi yeniden başlatın.

---

### B. Fedora Kurulumu

Fedora resmi depolarında mülk sürücüler yer almaz. **RPM Fusion** deposunu etkinleştirerek sürücü yüklenmelidir.

1. RPM Fusion depolarını ekleyin:

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
```

2. Sürücü ve CUDA desteğini yükleyin:

```bash
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda -y
```

3. Çekirdek modüllerinin derlenmesi için **5-10 dakika** bekleyin ve ardından sistemi yeniden başlatın:

```bash
sudo reboot
```

---

### C. Arch Linux / Manjaro Kurulumu

Arch Linux kullanıcıları varsayılan Linux çekirdeği veya DKMS modülleri ile sürücüyü kurabilirler.

1. Varsayılan `linux` çekirdeği kullanıyorsanız:

```bash
sudo pacman -S nvidia nvidia-utils lib32-nvidia-utils nvidia-settings
```

2. Özel bir çekirdek (örneğin `linux-zen` veya `linux-lts`) kullanıyorsanız DKMS sürümünü seçin:

```bash
sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils nvidia-settings
```

3. `DRM Kernel Mode Setting` özelliğini aktif etmek için `/etc/default/grub` dosyasındaki `GRUB_CMDLINE_LINUX_DEFAULT` satırına `nvidia-drm.modeset=1` parametresini ekleyin ve GRUB'u güncelleyin:

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

---

## 3. Kurulumun Doğrulanması

Sistemi yeniden başlattıktan sonra RTX 4060 sürücüsünün aktif olup olmadığını ve Wayland/X11 üzerinde doğru çalışıp çalışmadığını kontrol edin.

### 1. CLI Üzerinden Kontrol

Terminalde aşağıdaki komutu çalıştırın:

```bash
nvidia-smi
```

**Başarılı Çıktı Örneği:**
Çıktıda ekran kartınızın modeli (**NVIDIA GeForce RTX 4060**), sürücü sürümü (**Driver Version: 550.xx**) ve CUDA sürümü görünmelidir.

```text
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|----------------------------------+------------------------+----------------------+
| GPU  Name        Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp Perf Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|==================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 Off | 00000000:01:00.0  On |                  N/A |
|  0%   42C    P8    12W / 115W |    350MiB /  8188MiB |      1%      Default |
+----------------------------------+------------------------+----------------------+
```

### 2. OpenGL İvmelendirme Kontrolü

Masaüstü işleyicisinin NVIDIA GPU'yu kullandığından emin olun:

```bash
glxinfo | grep -i vendor
```
*Çıktı `NVIDIA Corporation` olmalıdır.*

---

## 4. Sık Karşılaşılan Sorunlar ve Çözümleri

### A. Siyah Ekran Sorunu (Nouveau Çakışması)
Nouveau sürücüsü otomatik olarak karalisteye (blacklist) alınmadıysa sistem açılışta kilitlenebilir.

Çözüm için `/etc/modprobe.d/blacklist-nouveau.conf` dosyası oluşturun:

```bash
sudo bash -c "cat <<EOF > /etc/modprobe.d/blacklist-nouveau.conf
blacklist nouveau
options nouveau modeset=0
EOF"
```

Initramfs'yi güncelleyin:
* **Ubuntu/Debian:** `sudo update-initramfs -u`
* **Fedora:** `sudo dracut --force`
* **Arch Linux:** `sudo mkinitcpio -P`

### B. Laptop Kullanıcıları İçin Hibrit Grafik (Prime Select)
RTX 4060 bir dizüstü bilgisayarda bulunuyorsa, GPU geçişleri için `nvidia-prime` kullanabilirsiniz.

* Yalnızca NVIDIA GPU'yu aktif etmek için:
```bash
sudo prime-select nvidia
```
* Entegre GPU'ya (Intel/AMD) dönmek için:
```bash
sudo prime-select intel # veya 'amd'
```

### C. Wayland Performans ve Titreme Sorunları
RTX 4060 ve NVIDIA 550+ sürücüleri Wayland ile oldukça kararlıdır. Ancak titreme (flickering) yaşanıyorsa, `/etc/environment` dosyasına şu değişkeni ekleyin:

```env
GBM_BACKEND=nvidia-drm
__GLX_VENDOR_LIBRARY_NAME=nvidia
```

---

## 5. Özet

RTX 4060 kartının Linux üzerinde sorunsuz çalışması doğrudan sürücü sürümüne bağlıdır. Manuel `.run` dosyaları yerine dağıtımınızın paket yöneticisini (`apt`, `dnf`, `pacman`) kullanmak, çekirdek güncellemelerinde sistemin bozulmasını engeller. Kurulum sonrası `nvidia-smi` çıktısı alınıyorsa sürücünüz başarıyla yüklenmiştir.