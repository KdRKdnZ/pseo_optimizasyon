---
title: "gamemode kurulumu"
description: "gamemode kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Linux GameMode Kurulumu ve Yapılandırma Rehberi

GameMode, Feral Interactive tarafından açık kaynak olarak geliştirilen, Linux işletim sistemlerinde oyun performansını artırmak amacıyla sistem kaynaklarını dinamik olarak optimize eden bir daemon (arka plan hizmeti) ve kitaplık birleşimidir. Oyun başladığında varsayılan sistem ayarlarını geçici olarak değiştirir ve oyun kapatıldığında sistemi eski durumuna döndürür.

Bu rehberde, GameMode'un teknik çalışma prensipleri, popüler Linux dağıtımları üzerindeki kurulum adımları, konfigürasyonu ve oyun istemcileriyle entegrasyonu detaylandırılmaktadır.

---

## GameMode Nasıl Çalışır? (Teknik Altyapı)

GameMode, bir oyun çalıştığında D-Bus protokolü üzerinden sinyal alır ve aşağıdaki sistem parametrelerini "Performans" moduna alır:

1. **CPU Governor:** İşlemci çekirdeklerini en yüksek frekansta çalışacak şekilde `performance` moduna zorlar (ondemand veya powersave modundan çıkarır).
2. **GPU Saat Hızları:** AMD ve NVIDIA ekran kartlarında güç tasarruf modlarını devre dışı bırakır, VRAM ve çekirdek hızlarını maksimuma kilitler.
3. **I/O ve Süreç Önceliği (Renice):** Oyun sürecine (process) yüksek CPU ve disk okuma/yazma önceliği atar.
4. **Kernel Scheduler:** `SCHED_ISO` (izokron zamanlama) veya gerçek zamanlı öncelik ayarlarını devreye sokar.
5. **Ekran Koruyucu İnhibisyonu:** Oyun esnasında ekran koruyucu ve güç yönetiminin devreye girmesini engeller.

---

## Dağıtımlara Göre GameMode Kurulumu

GameMode paketleri modern Linux dağıtımlarının resmi depolarında yer almaktadır. 64-bit sistemlerde hem 64-bit hem de 32-bit (multilib/multiarch) kütüphanelerinin kurulması, eski ve Proton/Wine tabanlı oyunlarda uyumluluk için şarttır.

### 1. Ubuntu / Debian / Pop!_OS Kurulumu
```bash
sudo apt update
sudo apt install gamemode libgamemode1 libgamemodeauto1
```
*32-bit oyun desteği için (Multiarch etkinse):*
```bash
sudo apt install libgamemode1:i386 libgamemodeauto1:i386
```

### 2. Arch Linux / Manjaro / EndeavourOS Kurulumu
```bash
sudo pacman -S gamemode lib32-gamemode
```

### 3. Fedora Kurulumu
```bash
sudo dnf install gamemode gamemode-32bit
```

### 4. openSUSE Kurulumu
```bash
sudo zypper install gamemode gamemode-32bit
```

---

## GameMode Hizmetinin Doğrulanması

Kurulum tamamlandıktan sonra arka plan hizmetinin doğru çalışıp çalışmadığı ve sistem uyumluluğu kontrol edilmelidir.

Aşağıdaki komut ile GameMode'un sisteminizdeki tüm bileşenleri (D-Bus, CPU Governor, GPU denetleyicileri) destekleyip desteklemediğini test edin:

```bash
gamemoded -t
```

Tüm test çıktılarının **PASSED** veya **SUCCESS** vermesi gerekir. Arka plan hizmetinin durumunu görmek için:

```bash
systemctl --user status gamemoded
```

---

## GameMode Yapılandırma Dosyası (`gamemode.ini`)

GameMode varsayılan ayarlarla sorunsuz çalışır; ancak özel GPU hız aşırtma (overclocking) veya özel betik tetiklemeleri için konfigüre edilebilir.

Örnek şablon dosyasını kullanıcı dizinine kopyalayın:

```bash
mkdir -p ~/.config/
cp /usr/share/doc/gamemode/gamemode.ini.template ~/.config/gamemode.ini
```

`~/.config/gamemode.ini` dosyasını bir metin düzenleyici ile açarak aşağıdaki teknik ayarları uygulayabilirsiniz:

```ini
[general]
# Oyun başladığında ve bittiğinde çalışacak özel shell komutları
desiredgov=performance
igpu_desiredgov=powersave
renice=10

[gpu]
# AMD GPU optimizasyonu (0: varsayılan, 1: performans)
apply_gpu_optimisations=accept-responsibility
gpu_device=0
amd_performance_level=high

# NVIDIA GPU güç sınırı ve overclock (NVreg_EnableGpuFirmware=0 gerekebilir)
nv_powermizer_mode=1

[cpu]
# Belirli CPU çekirdeklerini park etmek/kapatmak için (örnek: 0-3 arası)
# park_cores=no
```

---

## Oyunlarda GameMode Kullanımı ve Entegrasyonu

GameMode, LD_PRELOAD mekanizması veya D-Bus tetiklemeleri ile çalışır.

### Steam Entegrasyonu
Steam kütüphanenizdeki herhangi bir oyuna sağ tıklayın -> **Özellikler** -> **Genel** sekmesindeki **Başlatma Seçenekleri** (Launch Options) kısmına şu komutu ekleyin:

```bash
gamemoderun %command%
```

### Lutris Entegrasyonu
1. Lutris'i açın.
2. **Preferences** (Tercihler) > **System Options** (Sistem Seçenekleri) sekmesine gidin.
3. **Enable GameMode** seçeneğini aktif hale getirin.

### Heroic Games Launcher (Epic Games / GOG)
1. Heroic ayarlarından **Game Settings** bölümüne girin.
2. **Other** sekmesinde **Use GameMode** seçeneğini işaretleyin.

### Komut Satırından Çalıştırma (CLI / Bağımsız Oyunlar)
Yerel bir binary dosyasını veya betiği GameMode ile çalıştırmak için:

```bash
gamemoderun ./oyun_dosyasi
```

---

## GameMode Etkinlik Testi

Bir oyun çalışırken GameMode'un aktif olup olmadığını doğrulamak için uçbirimde şu komutu çalıştırın:

```bash
gamemoded -s
```

Çıktı aşağıdaki gibi olmalıdır:
* **GameMode is active** (GameMode aktif)
* **GameMode is inactive** (GameMode pasif)

GameMode aktifleştiğinde CPU frekanslarını anlık izlemek için:

```bash
watch -n 1 "cat /proc/cpuinfo | grep 'cpu MHz'"
```

Bu adımlar tamamlandığında Linux sisteminiz oyun esnasında minimum gecikme (latency), kararlı kare hızları (FPS) ve maksimum donanım performansı sunacak şekilde optimize edilmiş olur.