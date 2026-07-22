---
title: "mangohud kurulumu"
description: "mangohud kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# MangoHud Kurulumu ve Yapılandırma Rehberi: Linux Performans İzleme

MangoHud, Linux işletim sistemlerinde Vulkan ve OpenGL tabanlı uygulamalar ile oyunlar için geliştirilmiş açık kaynaklı bir performans izleme (overlay) katmanıdır. MSI Afterburner / RivaTuner (RTSS) yazılımlarının Linux ekosistemindeki karşılığı olan MangoHud; kare hızını (FPS), kare süresini (frametime), CPU/GPU sıcaklıklarını, RAM/VRAM kullanımını ve sistem kaynaklarını gerçek zamanlı olarak ekranda görüntüler.

Bu rehberde, farklı Linux dağıtımlarında MangoHud kurulumu, Steam ve bağımsız oyunlarda kullanımı ve konfigürasyon detayları adım adım ele alınmaktadır.

---

## Sistem Gereksinimleri ve Ön Koşullar

MangoHud'ın sorunsuz çalışabilmesi için sisteminizde aşağıdaki bileşenlerin yüklü olması gerekir:

*   **Grafik Sürücüleri:** Güncel Nvidia (Proprietary) veya Mesa (AMD/Intel) sürücüleri.
*   **Vulkan Desteği:** Sistemde Vulkan sürücülerinin ve `vulkan-tools` paketinin aktif olması.
*   **Grafik Mimarisi:** 64-bit ve (eski oyunlar için) 32-bit kütüphane desteği.

---

## Linux Dağıtımlarına Göre MangoHud Kurulumu

Dağıtımınıza uygun komut satırı talimatlarını takip ederek kurulumu gerçekleştirin.

### 1. Arch Linux / Manjaro / EndeavourOS

Arch tabanlı sistemlerde MangoHud resmi depolarda (`extra`) mevcuttur. Hem 64-bit hem de 32-bit (multilib) kütüphanelerinin kurulması önerilir.

```bash
sudo pacman -S mangohud lib32-mangohud
```

### 2. Ubuntu / Debian / Linux Mint

Ubuntu 22.04 LTS ve daha yeni sürümlerde MangoHud ana depolarda yer alır:

```bash
sudo apt update
sudo apt install mangohud
```

*Not: 32-bit oyunlarda destek sağlamak için multiarch yapısı aktifse `mangohud:i386` paketini de yükleyebilirsiniz.*

### 3. Fedora

Fedora 33 ve üzeri sürümlerde resmi depolar üzerinden tek komutla yüklenebilir:

```bash
sudo dnf install mangohud
```

32-bit Steam oyunları için ek kütüphane:

```bash
sudo dnf install mangohud.i686
```

### 4. Flatpak (Evrensel Kurulum)

Eğer Steam veya oyunlarınızı Flatpak formatında kullanıyorsanız, MangoHud'ı Flatpak bağımlılığı olarak kurmanız gerekir:

```bash
flatpak install flathub org.freedesktop.Platform.VulkanLayer.MangoHud
```

---

## MangoHud Kullanımı ve Çalıştırma Yöntemleri

MangoHud kurulum tamamlandıktan sonra arka planda bir servis olarak çalışmaz; istenen uygulama başlatılırken çağrılır.

### Steam Üzerinde Kullanım

Steam kütüphanenizdeki bir oyunda MangoHud'ı aktif etmek için:

1.  Steam'i açın ve oyuna sağ tıklayıp **Özellikler (Properties)** seçeneğine girin.
2.  **Genel (General)** sekmesindeki **Başlatma Seçenekleri (Launch Options)** kutusuna şu kodu ekleyin:

```bash
mangohud %command%
```

*Proton (DXVK/VKD3D) kullanan tüm Windows oyunlarında otomatik olarak Vulkan katmanı tetiklenecektir.*

### Terminal Üzerinden Kullanım (OpenGL ve Vulkan)

Herhangi bir Linux uygulamasını veya oyununu terminalden MangoHud ile başlatmak için komutun önüne `mangohud` ekleyin:

```bash
# Vulkan Örneği (vkcube)
mangohud vkcube

# OpenGL Örneği (glxgears)
mangohud --dlsym glxgears
```

### Lutris ve Heroic Games Launcher

*   **Lutris:** System Options > Command prefix alanına `mangohud` yazın veya "Enable MangoHud" anahtarını aktif edin.
*   **Heroic Games Launcher:** Game Settings > Other > Enable MangoHud seçeneğini işaretleyin.

---

## MangoHud Yapılandırması (Configuration)

MangoHud varsayılan ayarlarıyla gelir ancak tamamen özelleştirilebilir. Yapılandırma dosyası kullanıcı dizininde saklanır.

### Konfigürasyon Dosyası Oluşturma

Varsayılan konfigürasyon şablonunu kullanıcı dizininize kopyalayın:

```bash
mkdir -p ~/.config/MangoHud
cp /usr/share/doc/mangohud/MangoHud.conf.example ~/.config/MangoHud/MangoHud.conf
```

`~/.config/MangoHud/MangoHud.conf` dosyasını herhangi bir metin düzenleyici (`nano`, `gedit`) ile açarak düzenleyebilirsiniz.

### Örnek Konfigürasyon Parametreleri

Aşağıda optimize edilmiş bir `MangoHud.conf` içeriği bulunmaktadır:

```ini
### Görünüm Ayarları
legacy_layout=false
position=top-left
round_corners=10
background_alpha=0.5
font_size=24

### Donanım İzleme
cpu_stats
cpu_temp
gpu_stats
gpu_temp
ram
vram

### Performans ve Metrikler
fps
frametime=1
frame_timing=1

### Kısayol Tuşları
toggle_hud=Shift_R+F12
toggle_logging=Shift_L+F11
```

---

## Görsel Arayüz ile Yapılandırma: GGOverlay

Kod yazmadan metrikleri, renkleri ve konumlandırmayı düzenlemek istiyorsanız **GGOverlay** adlı GUI aracını kullanabilirsiniz.

*   **Arch Linux:** `sudo pacman -S ggoverlay`
*   **Flatpak:** `flatpak install flathub io.github.benjamimgois.goverlay`

GGOverlay, oluşturduğunuz değişiklikleri anlık olarak önizlemenizi sağlar ve doğrudan `MangoHud.conf` dosyasına işler.

---

## Sorun Giderme (Troubleshooting)

### 1. Overlay Oyunda Görünmüyor
*   Oyunun Vulkan veya OpenGL kullandığından emin olun.
*   Nvidia kullanıcısıysanız `nvidia-drm.modeset=1` parametresinin GRUB üzerinde aktif olduğunu doğrulayın.
*   OpenGL oyunlarında `mangohud --dlsym %command%` komutunu deneyin.

### 2. Flatpak Steam İçinde Çalışmıyor
Flatpak Steam kullanıyorsanız MangoHud Flatpak katmanının Steam ile aynı mimaride (Flatpak) kurulu olduğundan emin olun:
```bash
flatpak list | grep MangoHud
```

### 3. Sıcaklık Değerleri Yanlış veya Görünmüyor
AMD işlemcilerde `k10temp`, Intel işlemcilerde `coretemp` çekirdek modüllerinin yüklü olduğunu kontrol edin:
```bash
sensors
```