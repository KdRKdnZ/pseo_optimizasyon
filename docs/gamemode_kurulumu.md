# Linux GameMode Kurulumu ve Yapılandırma Rehberi

GameMode, Feral Interactive tarafından geliştirilen ve Linux işletim sistemlerinde oyun performansını geçici olarak optimize eden açık kaynaklı bir sistem daemon'ıdır (arka plan hizmeti). Oyun başladığında işlemci yöneticisini (CPU Governor) "performance" moduna alır, I/O önceliklerini düzenler, GPU saat hızlarını artırır ve ekran koruyucuyu devre dışı bırakır. Oyun kapatıldığında ise sistemi otomatik olarak varsayılan ayarlara döndürür.

Bu rehberde, farklı Linux dağıtımlarında GameMode kurulumu, Steam/Lutris entegrasyonu ve gelişmiş konfigürasyon adımları teknik detaylarıyla açıklanmaktadır.

---

## 1. Dağıtıma Göre Paket Kurulumu

GameMode, çoğu ana akım Linux dağıtımının resmi depolarında yer almaktadır. 32-bit oyunlarda da performans artışı sağlamak için hem 64-bit hem de 32-bit (multilib) kütüphanelerinin kurulması kritik önem taşır.

### Ubuntu / Debian / Pop!_OS
```bash
sudo apt update
sudo apt install gamemode libgamemodeauto0 libgamemode1 gamemode-daemon
# 32-bit desteği için (Steam oyunları için gereklidir)
sudo apt install libgamemodeauto0:i386 libgamemode1:i386
```

### Arch Linux / Manjaro / EndeavourOS
```bash
sudo pacman -S gamemode lib32-gamemode
```

### Fedora
```bash
sudo dnf install gamemode gamemode-devel
# 32-bit desteği için
sudo dnf install gamemode.i686
```

### Kaynak Koddan Derleyerek Kurulum (Opsiyonel)
En güncel sürümü kullanmak veya özel bir dağıtım üzerinde derlemek için:

```bash
# Gerekli bağımlılıkları yükleyin (Debian/Ubuntu örneği)
sudo apt install meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev

# Depoyu klonlayın ve derleyin
git clone https://github.com/FeralInteractive/gamemode.git
cd gamemode
git checkout 1.8.1 # En son kararlı sürüm
./bootstrap.sh
```

---

## 2. GameMode Kullanımı ve Oyun Entegrasyonu

GameMode kurulduktan sonra arka planda D-Bus üzerinden tetiklenmeyi bekler. Oyunları GameMode ile çalıştırmak için başlatma parametrelerine `gamemoderun` komutu eklenmelidir.

### Steam Entegrasyonu
1. Steam kütüphanenizi açın.
2. Oyuna sağ tıklayıp **Özellikler (Properties)** seçeneğine girin.
3. **Genel (General)** sekmesindeki **Başlatma Seçenekleri (Launch Options)** kutusuna aşağıdaki kodu ekleyin:

```bash
gamemoderun %command%
```

### Lutris Entegrasyonu
1. Lutris ayarlarını açın (veya oyuna sağ tıklayıp *Configure* deyin).
2. **System options** sekmesine gelin.
3. **Enable GameMode** seçeneğini aktif konuma getirin.

### Heroic Games Launcher Entegrasyonu
1. Oyun ayarlarına veya genel ayarlara gidin.
2. **Other** sekmesi altındaki **Enable GameMode** anahtarını açın.

### Komut Satırından (CLI) Çalıştırma
Herhangi bir bağımsız uygulamayı veya oyunu GameMode ile başlatmak için terminalde şu komutu çalıştırın:

```bash
gamemoderun ./oyun_dosyasi
```

---

## 3. Gelişmiş Konfigürasyon (`gamemode.ini`)

GameMode'un Varsayılan yapılandırma dosyası `/usr/share/gamemode/gamemode.ini` dizinindedir. Özel ayarlar yapmak için bu dosyayı kullanıcı dizininize kopyalamanız gerekir.

```bash
mkdir -p ~/.config
cp /usr/share/gamemode/gamemode.ini ~/.config/gamemode.ini
nano ~/.config/gamemode.ini
```

### Kritik Yapılandırma Parametreleri

#### CPU Ayarları
İşlemci frekans yöneticisini performans moduna zorlar:
```ini
[custom]
; Oyun başladığında ve bittiğinde çalışacak özel scriptler
start=notify-send "GameMode" "Oyun modu aktif edildi."
end=notify-send "GameMode" "Oyun modu kapatıldı."

[cpu]
governor=performance
; İşlemci çekirdek park etmeyi (core parking) devre dışı bırakır
park_cores=no
```

#### GPU Ayarları (NVIDIA / AMD)
Ekran kartı performans profillerini optimize eder:

```ini
[gpu]
; NVIDIA için Güç Yönetim Modu (1 = Prefer Maximum Performance)
apply_gpu_optimisations=accept-responsibility
gpu_device=0
nv_powermode=1

; AMD için Güç Seviyesi (high, low, auto)
amd_performance_level=high
```

#### Sistem Öncelikleri (Renice & Scheduling)
Oyun sürecine (process) daha yüksek işlemci zamanı ve I/O önceliği atar:

```ini
[general]
renice=10
ioprio=0
inhibit_screensaver=1
```

---

## 4. Kurulum ve Çalışma Doğrulaması (Testing)

GameMode'un doğru kurulduğunu ve arka planda sorunsuz çalıştığını doğrulamak için aşağıdaki adımları uygulayın.

### 1. Servis Durumu Kontrolü
GameMode'un aktif olup olmadığını ve hata verip vermediğini doğrulayın:

```bash
gamemoded -s
```
*Çıktı `gamemode is inactive` şeklinde olmalıdır (oyun çalışmıyorken).*

### 2. Test Modu Çalıştırma
GameMode simülasyonu başlatarak sistem optimizasyonlarının devreye girip girmediğini test edin:

```bash
gamemoded -t
```
*Tüm test adımlarının `PASSED` olarak sonuçlanması gerekir.*

### 3. Oyun Esnasında Anlık Durum Sorgulama
Bir oyun açıkken (ve `gamemoderun` ile başlatılmışken) terminalden durum kontrolü yapın:

```bash
gamemoded -s
```
*Oyun esnasında çıktı `gamemode is active` olarak değişmelidir.*

---

## 5. Sorun Giderme (Troubleshooting)

### Polkit İzin Hataları
GameMode, CPU governor değiştirmek için `polkit` yetkilerine ihtiyaç duyar. Eğer erişim engellendi hatası alıyorsanız, kullanıcınızın `gamemode` grubunda veya sudo yetkisine sahip olduğundan emin olun.

### Proton / Wine Oyunlarında Çalışmama Sorunu
Steam Proton oyunlarında GameMode tetiklenmiyorsa, `lib32-gamemode` (veya ilgili dağıtımın 32-bit kütüphanesi) eksiktir. Dağıtımınıza uygun 32-bit paketleri yükleyip sistemi yeniden başlatın.