# Linux MangoHud Kurulumu ve Yapılandırma Rehberi

MangoHud, Linux işletim sistemlerinde Vulkan ve OpenGL tabanlı oyunlar ile uygulamalar için geliştirilmiş açık kaynaklı, yüksek performanslı bir sistem izleme Katmanıdır (Overlay). CPU/GPU sıcaklıkları, FPS, kare süreleri (frametime), RAM ve VRAM kullanımı gibi kritik donanım verilerini oyun ekranı üzerinde gerçek zamanlı olarak gösterir.

Bu rehberde, farklı Linux dağıtımlarında MangoHud kurulumunu, Steam entegrasyonunu ve yapılandırma adımlarını bulabilirsiniz.

---

## 1. Dağıtıma Göre MangoHud Kurulumu

MangoHud, çoğu popüler Linux dağıtımının resmi depolarında yer almaktadır. Sisteminiz için uygun olan komut setini terminalde çalıştırarak kurulumu gerçekleştirebilirsiniz.

### Arch Linux / Manjaro / EndeavourOS
Arch tabanlı sistemlerde MangoHud hem 64-bit hem de 32-bit (multilib) desteğiyle resmi depoda mevcuttur:

```bash
sudo pacman -S mangohud lib32-mangohud
```

### Ubuntu / Debian / Linux Mint
Ubuntu 20.04 LTS ve üzeri sürümlerde MangoHud apt depolarında bulunur:

```bash
sudo apt update
sudo apt install mangohud
```

*Not: 32-bit oyunlarda destek sağlamak için 32-bit kütüphaneyi de ekleyebilirsiniz:*
```bash
sudo apt install mangohud:i386
```

### Fedora
Fedora depolarında paket doğrudan mevcuttur. Hem 64-bit hem de 32-bit sürümlerini yüklemek için:

```bash
sudo dnf install mangohud mangohud.i686
```

### Flatpak (Steam Flatpak Kullanıcıları İçin)
Eğer Steam uygulamasını Flatpak olarak kullanıyorsanız, MangoHud'ı Flatpak bağımlılığı olarak yüklemeniz gerekir:

```bash
flatpak install flathub org.freedesktop.Platform.VulkanLayer.MangoHud
```

---

## 2. MangoHud Çalışma Testi

Kurulumun başarılı olduğunu doğrulamak için Vulkan test küpünü MangoHud parametresi ile çalıştırabilirsiniz:

```bash
mangohud vkcube
```
Ekranda dönen küpün sol üst köşesinde sistem bilgilerini ve FPS değerini görüyorsanız kurulum başarıyla tamamlanmıştır.

---

## 3. MangoHud Kullanımı ve Oyunlara Entegre Edilmesi

MangoHud'ı oyunlarda aktif etmek için uygulamanın veya oyun istemcisinin başlatma komutlarına ekleme yapmanız gerekir.

### Steam Başlatma Seçenekleri (Steam Launch Options)
1. Steam kütüphanenizden bir oyuna sağ tıklayın ve **Özellikler (Properties)** seçeneğine girin.
2. **Genel (General)** sekmesindeki **Başlatma Seçenekleri (Launch Options)** kutusuna şu kodu ekleyin:

```bash
mangohud %command%
```

### Lutris / Heroic Games Launcher
* **Lutris:** Oyunun ayarlarına girin -> *Runner options* sekmesi -> *Enable MangoHud* anahtarını aktif edin.
* **Heroic Games Launcher:** *Game Settings* -> *Other* bölümünden *Enable MangoHud* seçeneğini işaretleyin.

### Terminal Üzerinden Çalıştırma
Bağımsız bir oyunu veya uygulamayı doğrudan terminalden çalıştırmak için:

```bash
mangohud ./oyun_dosyasi
```

---

## 4. MangoHud Yapılandırması (Configuration)

MangoHud'ın ekrandaki boyutunu, gösterilecek verileri ve kısayol tuşlarını özelleştirmek için konfigürasyon dosyası kullanılır.

### Yapılandırma Dosyasını Oluşturma
Varsayılan yapılandırma şablonunu kendi kullanıcı dizininize kopyalayın:

```bash
mkdir -p ~/.config/MangoHud
cp /usr/share/doc/mangohud/MangoHud.conf.example ~/.config/MangoHud/MangoHud.conf
```

### Örnek Konfigürasyon Dosyası Düzenlemesi
`~/.config/MangoHud/MangoHud.conf` dosyasını bir metin editörü (nano, gedit vb.) ile açarak aşağıdaki örnek ayarları uygulayabilirsiniz:

```ini
# Performans ve Görünüm Ayarları
legacy_layout=false
gpu_stats
gpu_temp
gpu_core_clock
cpu_stats
cpu_temp
cpu_core_clock
fps
frametime=1
ram
vram

# Ekranda Duracağı Konum (top-left, top-right, bottom-left, bottom-right)
position=top-left

# Yazı Boyutu ve Şeffaflık
font_size=24
background_alpha=0.5
round_corners=10

# FPS Sınırlayıcı (Örn: Shift_L + F2 ile geçiş yapılır)
fps_limit=144,60,0

# Kısayol Tuşları
toggle_hud=Shift_R+F12
toggle_fps_limit=Shift_L+F2
```

---

## 5. Grafik Arayüz ile Yapılandırma: GOverlay

Kodlarla uğraşmak istemiyorsanız, MangoHud ayarlarını görsel bir arayüz üzerinden yönetmek için **GOverlay** aracını kullanabilirsiniz.

* **Arch Linux:** `sudo pacman -S goverlay`
* **Ubuntu/Debian:** `sudo apt install goverlay`
* **Fedora:** `sudo dnf install goverlay`
* **Flatpak:** `flatpak install flathub io.github.benjamimgois.goverlay`

GOverlay uygulamasını açarak yazı tiplerini, renkleri, gösterilecek donanım bilgilerini ve konumlandırmayı canlı önizleme ile kolayca ayarlayabilirsiniz.

---

## 6. Sık Karşılaşılan Sorunlar ve Çözümleri

### MangoHud Oyunlarda Görünmüyor
* **OpenGL Oyunları:** Bazı eski OpenGL oyunlarında `mangohud` yerine `mangohud --dlsym` komutunu kullanmanız gerekebilir.
* **32-Bit Oyunlar:** Sisteminizde `lib32-mangohud` (Arch) veya `mangohud:i386` (Ubuntu) paketinin kurulu olduğundan emin olun.

### Vulkan Katman Hatası (Vulkan Layer Error)
Eğer Vulkan katmanı algılanmıyorsa, ortam değişkenini manuel olarak tanımlayabilirsiniz:

```bash
export VK_INSTANCE_LAYERS=VK_LAYER_MANGOHUD_overlay
```