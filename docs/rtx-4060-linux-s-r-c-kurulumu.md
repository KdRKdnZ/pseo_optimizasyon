---
title: "RTX 4060 Linux sürücü kurulumu"
description: "RTX 4060 Linux sürücü kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# RTX 4060 Linux Sürücü Kurulum Rehberi: Adım Adım Teknik Anlatım

Nvidia GeForce RTX 4060 (Ada Lovelace mimarisi), yüksek performans sunabilmesi için Linux sistemlerde güncel ve kapalı kaynaklı (proprietary) resmi Nvidia sürücülerine ihtiyaç duyar. Açık kaynaklı `nouveau` sürücüleri, RTX 4000 serisinde donanım ivmelendirme ve güç yönetimi konularında yetersiz kalmaktadır.

Bu rehberde; Ubuntu/Debian, Fedora ve Arch Linux dağıtımlarında RTX 4060 için sürücü kurulumu, Secure Boot konfigürasyonu ve doğrulama adımları teknik detaylarıyla açıklanmaktadır.

---

## 1. Ön Hazırlık ve Sistem Kontrolü

Kuruluma başlamadan önce sistemin ekran kartını doğru algıladığından ve kernel başlıklarının (kernel headers) güncel olduğundan emin olunmalıdır.

### Donanım Tespiti
Terminali açın ve cihazın PCI otobüsünde görünüp görünmediğini kontrol edin:

```bash
lspci | grep -i nvidia
```

Çıktıda `NVIDIA Corporation AD107 [GeForce RTX 4060]` ifadesi görülmelidir.

### Secure Boot Uyarısı
Eğer BIOS/UEFI üzerinde **Secure Boot** aktif ise, üçüncü taraf sürücülerin (out-of-tree kernel modules) yüklenmesi engellenebilir. 
* **Tavsiye Edilen:** BIOS ayarlarına girerek Secure Boot seçeneğini `Disabled` konumuna getirmektir.
* **Alternatif:** Secure Boot açık kalacaksa, kurulum sırasında bir **MOK (Machine Owner Key)** şifresi belirleyip yeniden başlatmada bu anahtarı sisteme kaydetmeniz gerekir.

---

## 2. Dağıtımlara Göre RTX 4060 Sürücü Kurulumu

RTX 4060 için **Nvidia 535.xx** veya üzeri (tercihen **550.xx** ve üstü) sürücü sürümleri kullanılmalıdır.

### A. Ubuntu / Debian / Pop!_OS Tabanlı Sistemler

Ubuntu ve türevlerinde en kararlı sürücüler PPA depoları veya dahili araçlar üzerinden kurulur.

1. **Sistem Paketlerini Güncelleyin:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Graphics PPA Deposunu Ekleyin (En Güncel Sürücüler İçin):**
   ```bash
   sudo add-apt-repository ppa:graphics-drivers/ppa -y
   sudo apt update
   ```

3. **Önerilen Sürücüyü Tespit Edin:**
   ```bash
   ubuntu-drivers devices
   ```

4. **Sürücüyü Kurun:**
   RTX 4060 için güncel `nvidia-driver-550` veya en son kararlı sürümü yükleyin:
   ```bash
   sudo apt install nvidia-driver-550 nvidia-dkms-550 -y
   ```

5. **Sistemi Yeniden Başlatın:**
   ```bash
   sudo reboot
   ```

---

### B. Fedora / RHEL Tabanlı Sistemler

Fedora üzerinde kurulum yapmak için öncelikle RPM Fusion depolarının etkinleştirilmesi gerekir.

1. **RPM Fusion Depolarını Etkinleştirin:**
   ```bash
   sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
   sudo dnf update -y
   ```

2. **Gerekli Kernel Geliştirme Araçlarını ve Sürücüyü Yükleyin:**
   ```bash
   sudo dnf install kernel-devel kernel-headers akmod-nvidia xorg-x11-drv-nvidia-cuda -y
   ```

3. **Kernel Modüllerinin Derlenmesini Bekleyin:**
   Kurulum bittikten sonra hemen yeniden başlatmayın. Modüllerin arka planda derlenmesi için 2-3 dakika bekleyin ve ardından sistemi yeniden başlatın:
   ```bash
   sudo reboot
   ```

---

### C. Arch Linux / Manjaro

Arch Linux, çekirdek güncellemelerini hızlı aldığı için `nvidia-dkms` paketi kullanılması önerilir.

1. **Sistemi Güncelleyin:**
   ```bash
   sudo pacman -Syu
   ```

2. **Gerekli Paketleri ve Sürücüyü Kurun:**
   Kullandığınız çekirdeğe uygun Linux başlıkları ile birlikte sürücüyü yükleyin:
   ```bash
   sudo pacman -S nvidia-dkms nvidia-utils lib32-nvidia-utils linux-headers nvidia-settings
   ```

3. **DRM Modeset Ayarını Etkinleştirin (İsteğe Bağlı - Wayland Kararlılığı İçin):**
   `/etc/default/grub` dosyasındaki `GRUB_CMDLINE_LINUX_DEFAULT` satırına `nvidia_drm.modeset=1` parametresini ekleyin ve GRUB'u güncelleyin:
   ```bash
   sudo grub-mkconfig -o /boot/grub/grub.cfg
   ```

4. **Sistemi Yeniden Başlatın:**
   ```bash
   sudo reboot
   ```

---

## 3. Kurulum Doğrulama ve Performans Testi

Sistem yeniden başladıktan sonra Nvidia sürücülerinin aktif olup olmadığını denetlemek için terminalde aşağıdaki komutu çalıştırın:

```bash
nvidia-smi
```

**Başarılı Kurulum Göstergeleri:**
* **Driver Version:** 535.xx veya 550.xx (veya daha yüksek) olmalıdır.
* **CUDA Version:** Desteklenen CUDA sürümü görünmelidir.
* **GPU Name:** NVIDIA GeForce RTX 4060 doğru şekilde listelenmelidir.
* **Memory Usage:** VRAM kullanımı ve çalışan süreçler pencerede yer almalıdır.

Grafik Arayüzü (GUI) üzerinden ayar yapmak için:
```bash
nvidia-settings
```

---

## 4. Olası Sorunlar ve Çözümleri

### Siyah Ekran (Black Screen) Sorunu
Sistem boot ederken siyah ekranda kalıyorsa, dahili GPU (iGPU) ile Nvidia (dGPU) arasındaki çakışmadan veya `nouveau` sürücüsünün kara listeye (blacklist) alınmamasından kaynaklanabilir.

1. GRUB menüsünde `e` tuşuna basarak önyükleme parametrelerine gelin.
2. `quiet splash` ifadesinin sonuna `nomodeset` ekleyip `Ctrl + X` ile başlatın.
3. Sisteme girdikten sonra `/etc/modprobe.d/blacklist-nouveau.conf` adında bir dosya oluşturup içine şu satırları ekleyin:
   ```text
   blacklist nouveau
   options nouveau modeset=0
   ```
4. initramfs güncelleyin:
   * **Ubuntu/Debian:** `sudo update-initramfs -u`
   * **Fedora/Arch:** `sudo dracut --force`

### Wayland Altında Ekran Yırtılması veya Donma
Nvidia, Wayland üzerinde gelişme göstermiş olsa da tam kararlılık için X11 (Xorg) kullanımı tercih edilebilir. GDM (Gnome Display Manager) oturum açma ekranında dişli simgesine tıklayarak **"GNOME on Xorg"** seçeneğini işaretlemek sorunları çözebilir.