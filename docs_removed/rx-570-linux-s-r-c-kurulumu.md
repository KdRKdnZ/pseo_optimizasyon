---
title: "RX 570 Linux sürücü kurulumu"
description: "RX 570 Linux sürücü kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# AMD Radeon RX 570 Linux Sürücü Kurulum Rehberi

AMD Radeon RX 570, Polaris mimarisine dayanan ve Linux ekosisteminde mükemmel açık kaynak sürücü desteğine sahip bir ekran kartıdır. AMD'nin Linux sürücü stratejisi doğrultusunda, RX 570 için gerekli olan çekirdek modülü (`amdgpu`) ve kullanıcı alanı sürücüleri (`Mesa`), modern Linux dağıtımlarının birçoğunda varsayılan olarak yüklü gelir. 

Ancak en yüksek grafik performansını elde etmek, Vulkan desteğini aktif etmek ve Oyun/OpenCL süreçlerini optimize etmek için doğru paketlerin yapılandırılması gerekir. Bu rehberde, farklı Linux dağıtımlarında RX 570 sürücü kurulumu, Vulkan yapılandırması ve performans optimizasyonu adım adım anlatılmaktadır.

---

## 1. Açık Kaynak (Mesa) ve Kapalı Kaynak (AMDGPU-PRO) Sürücü Farkı

Kuruluma geçmeden önce iki ana sürücü yapısını anlamak önemlidir:

*   **Mesa (Açık Kaynak - Tavsiye Edilen):** AMD ve Linux topluluğu tarafından geliştirilir. Oyun performansı, Steam/Proton uyumluluğu ve sistem kararlılığı açısından kapalı kaynak sürücüden çok daha üstündür.
*   **AMDGPU-PRO (Kapalı Kaynak/Kurumsal):** Sadece belirli CAD yazılımları ve eski kurumsal OpenCL bağımlılıkları için gereklidir. **Günlük kullanım ve oyun için kesinlikle önerilmez.**

---

## 2. Mevcut Sürücü Durumunu Kontrol Etme

Sisteminizde ekran kartının doğru tanınıp tanınmadığını ve hangi sürücünün aktif olduğunu kontrol etmek için terminalde şu komutları çalıştırın:

```bash
# GPU'nun tespit edilip edilmediğini kontrol edin
lspci -k | grep -A 3 -E "(VGA|3D)"

# OpenGL sağlayıcısını ve Mesa sürümünü kontrol edin
glxinfo | grep "OpenGL vendor\|OpenGL renderer\|OpenGL version"
```

Eğer çıktı içerisinde `amdgpu` ve `Mesa` ifadelerini görüyorsanız temel sürücünüz çalışıyor demektir.

---

## 3. Dağıtıma Göre RX 570 Sürücü ve Vulkan Kurulumu

Oyunlarda DirectX 11/12 ve Vulkan çevirilerini (DXVK/VKD3D) sorunsuz çalıştırmak için hem 64-bit hem de 32-bit (multilib/i386) Vulkan kütüphanelerinin kurulması şarttır.

### A. Ubuntu / Linux Mint / Pop!_OS Kurulumu

Ubuntu tabanlı sistemlerde varsayılan Mesa sürücüleri güncellenebilir. En son performans yamalarını almak için Kisak PPA deposunu eklemek önerilir:

```bash
# En güncel kararlı Mesa PPA deposunu ekleyin
sudo add-apt-repository ppa:kisak/kisak-mesa
sudo apt update && sudo apt upgrade -y

# Vulkan ve 32-bit bağımlılıklarını kurun (Steam ve Wine için gereklidir)
sudo apt install libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386 vulkan-tools
```

### B. Fedora Kurulumu

Fedora, varsayılan olarak en güncel çekirdek ve Mesa sürücüleriyle gelir. Sadece 32-bit kütüphaneleri ve Vulkan paketlerini doğrulamak yeterlidir:

```bash
# Sistemi güncelleyin
sudo dnf upgrade --refresh

# Vulkan sürücülerini ve 32-bit desteğini yükleyin
sudo dnf install mesa-dri-drivers.i686 mesa-vulkan-drivers mesa-vulkan-drivers.i686 vulkan-tools
```

### C. Arch Linux / Manjaro Kurulumu

Arch Linux üzerinde multilib deposunun aktif olduğundan emin olun (`/etc/pacman.conf` içinde `[multilib]` satırları açık olmalıdır).

```bash
# Sistem paketlerini güncelleyin
sudo pacman -Syu

# RX 570 için Mesa, Vulkan ve 32-bit kütüphaneleri yükleyin
sudo pacman -S mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader vulkan-tools
```

---

## 4. OpenCL Kurulumu (Görüntü İşleme ve Blender İçin)

RX 570 üzerinde Blender, DaVinci Resolve veya Darktable gibi yazılımlarda GPU hızlandırma kullanmak istiyorsanız OpenCL desteğine ihtiyacınız vardır. Mesa'nın açık kaynak OpenCL sürücüsü olan `ROCm` veya `RUSTICL` kullanılabilir.

**Arch Linux için:**
```bash
sudo pacman -S rocm-opencl-runtime
```

**Ubuntu için (ROCm paketleri):**
```bash
sudo apt install libocl-icd-opencl-dev opencl-headers clinfo
```

OpenCL kurulumunu doğrulamak için:
```bash
clinfo
```

---

## 5. Doğrulama ve Test

Kurulumların ardından Vulkan'ın doğru çalışıp çalışmadığını test etmek için terminale şu komutu girin:

```bash
vkcube
```

Ekranda dönen bir 3D küp görünüyorsa, RX 570 Vulkan sürücüleri sorunsuz şekilde çalışıyor demektir.

---

## 6. RX 570 İçin Gelişmiş Performans ve Güç Yönetimi

RX 570 kartınızın saat hızlarını, fan profillerini ve voltaj ayarlarını (overclock/under-volt) Linux altında yönetmek için **CoreCtrl** aracını kullanabilirsiniz.

### CoreCtrl Kurulumu (Ubuntu/Debian):
```bash
sudo apt install corectrl
```

### CoreCtrl Kurulumu (Arch Linux):
```bash
sudo pacman -S corectrl
```

> **İpucu:** Tam GPU kontrolünü aktif etmek için GRUB konfigürasyonunuza (`/etc/default/grub`) `amdgpu.ppfeaturemask=0xffffffff` parametresini ekleyip `sudo update-grub` komutunu çalıştırın.

---

## 7. Olası Sorunlar ve Çözümleri

### Ekran Yırtılması (Screen Tearing) Sorunu
X11 oturumu kullanıyorsanız ve ekran yırtılması yaşıyorsanız, `/etc/X11/xorg.conf.d/20-amdgpu.conf` dosyasını oluşturun ve şu satırları ekleyin:

```Xorg
Section "Device"
     Identifier "AMD Graphics"
     Driver "amdgpu"
     Option "TearFree" "true"
EndSection
```

### Oyunlarda Düşük FPS Sorunu
Oyunların dahili grafik birimi (iGPU) yerine RX 570 ile çalıştırıldığından emin olun. Lutris veya Steam Başlatma Seçeneklerine şu komutu ekleyebilirsiniz:

```bash
DRI_PRIME=1 %command%
```