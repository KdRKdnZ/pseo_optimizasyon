---
title: gamemode kurulumu
description: gamemode kurulumu hakkında detaylı optimizasyon ve donanım rehberi.
---

# Gamemode Kurulumu: Linux Oyun Performansını En Üst Düzeye Çıkarma Rehberi

Linux işletim sistemlerinde oyun performansı, arka plan servislerinin ve CPU/GPU güç yönetim politikalarının doğru yapılandırılmasına doğrudan bağlıdır. Feral Interactive tarafından geliştirilen **GameMode**, Linux çekirdeğinin (kernel) ve donanım bileşenlerinin oyunlar sırasında dinamik olarak optimize edilmesini sağlayan açık kaynaklı bir arka plan programıdır (daemon). 

Bu rehberde, Linux sisteminizde oyun performansını optimize etmek için **gamemode kurulumu**, yapılandırılması ve entegrasyon süreçlerini teknik detaylarıyla ele alacağız.

---

## GameMode Nedir ve Nasıl Çalışır?

GameMode, oyun başladığında tetiklenen ve oyun kapandığında sistemi eski haline getiren geçici optimizasyonlar bütünüdür. Sistem kaynaklarını statik olarak yüksek performansa ayarlamak yerine, yalnızca ihtiyaç anında (on-demand) müdahale ederek donanım ömrünü ve enerji tasarrufunu korur.

### CPU Governor ve Zamanlama (Scheduling) Optimizasyonu
GameMode aktif olduğunda, CPU governor modunu otomatik olarak `powersave` veya `schedutil` konumundan `performance` konumuna getirir. Bu işlem, işlemci çekirdeklerinin maksimum frekansta kalmasını sağlayarak oyun içi anlık FPS düşüşlerini (stuttering) engeller. Ayrıca, oyun sürecinin (process) CPU önceliğini (`renice` ve `SCHED_ISO` kullanarak) artırır.

### GPU Güç Yönetimi ve I/O Önceliği
*   **NVIDIA:** GPU saat hızlarını ve fan profillerini en yüksek performans seviyesine (PowerMizer Performance Mode) çeker.
*   **AMD:** `power_dpm_force_performance_level` değerini `high` olarak ayarlayarak GPU'nun agresif bir şekilde frekans yükseltmesini sağlar.
*   **I/O Önceliği:** Disk okuma/yazma önceliğini (`ionice`) optimize ederek harita yükleme sürelerini kısaltır.

---

## Dağıtımlara Göre GameMode Kurulumu

GameMode, modern Linux dağıtımlarının resmi depolarında yer almaktadır. Kurulum sırasında hem 64-bit hem de 32-bit kütüphanelerinin kurulması, özellikle Steam ve Wine/Proton tabanlı oyunların uyumluluğu için kritiktir.

### Ubuntu, Debian ve Linux Mint Üzerinde Kurulum
Debian tabanlı sistemlerde kurulum için aşağıdaki komutu terminalde çalıştırın:

```bash
sudo apt update
sudo apt install gamemode libgamemodeauto0-dev libgamemode-dev
```

*Not: 32-bit oyun desteği için çoklu mimari (multi-arch) etkinleştirilmişse, `libgamemodeauto0:i386` paketinin de kurulması önerilir.*

### Arch Linux ve Manjaro Üzerinde Kurulum
Arch Linux depolarında GameMode ana paket ve 32-bit kütüphanesi olarak ikiye ayrılmıştır:

```bash
sudo pacman -S gamemode lib32-gamemode
```

### Fedora ve RHEL Tabanlı Dağıtımlarda Kurulum
Fedora kullanıcıları aşağıdaki `dnf` komutu ile kurulumu tamamlayabilir:

```bash
sudo dnf install gamemode gamemode-devel
```

---

## GameMode Nasıl Kullanılır ve Yapılandırılır?

Kurulum tamamlandıktan sonra GameMode arka planda bir `systemd` kullanıcı servisi olarak çalışmaya hazır hale gelir. Ancak oyunların bu servisi tetiklemesi için başlatma parametrelerinin ayarlanması gerekir.

### Steam Üzerinde GameMode Aktifleştirme
Steam kütüphanenizdeki bir oyunda GameMode'u etkinleştirmek için:

1.  Steam'i açın ve oyununuza sağ tıklayıp **Özellikler (Properties)** seçeneğine gidin.
2.  **Genel (General)** sekmesindeki **Başlatma Seçenekleri (Launch Options)** alanına gelin.
3.  Aşağıdaki komutu ekleyin:

```bash
gamemoderun %command%
```

Bu komut, Steam'in oyunu başlatmadan önce GameMode daemon'ını tetiklemesini sağlar.

### Lutris ve Heroic Games Launcher Entegrasyonu
*   **Lutris:** Sağ üstteki menüden *Preferences > System options* yolunu izleyin. **Enable GameMode** seçeneğini aktif hale getirin.
*   **Heroic Games Launcher:** Oyun ayarlarına girin, *Alternative Launchers* veya *System* sekmesinden **Use GameMode** seçeneğini işaretleyin.

### Terminal ve Manuel Çalıştırma
Bağımsız bir oyunu veya emülatörü terminal üzerinden GameMode ile çalıştırmak için komutun başına `gamemoderun` eklemeniz yeterlidir:

```bash
gamemoderun ./oyun_dosyasi
```

---

## Gelişmiş Yapılandırma (`gamemode.ini`)

GameMode'un varsayılan davranışlarını özelleştirmek için bir yapılandırma dosyası oluşturabilirsiniz. Sistem genelindeki varsayılan şablon `/usr/share/gamemode/gamemode.ini` konumundadır. Kullanıcıya özel özelleştirme yapmak için bu dosyayı kendi ev dizininize kopyalayın:

```bash
mkdir -p ~/.config/
cp /usr/share/gamemode/gamemode.ini ~/.config/gamemode.ini
```

`~/.config/gamemode.ini` dosyasını favori metin editörünüzle açarak aşağıdaki gelişmiş ayarları uygulayabilirsiniz:

```ini
[general]
# GameMode aktif olduğunda çalışacak özel scriptler
start=notify-send "GameMode Aktif" "Performans modu başlatıldı."
end=notify-send "GameMode Pasif" "Normal moda dönüldü."

[gpu]
# GPU optimizasyonunu etkinleştirme (0: Kapalı, 1: Açık)
apply_gpu_optimisations=1
gpu_device=0

# NVIDIA için overclock ve güç limitleri (CoolBits gerektirir)
nv_core_clock_mhz_offset=100
nv_mem_clock_mhz_offset=250

# AMD için güç profili
amd_performance_level=high

[custom]
# Ekran koruyucuyu ve güç tasarrufu modunu engelle
inhibit_screensaver=1
```

---

## Kurulum Doğrulama ve Sorun Giderme

GameMode'un sisteminizde sorunsuz çalıştığını ve oyun sırasında aktif olduğunu doğrulamak için aşağıdaki yöntemleri kullanabilirsiniz.

### Servis Durumunu Kontrol Etme
GameMode'un aktif olup olmadığını sorgulamak için terminale şu komutu yazın:

```bash
gamemoded -s
```

Eğer çıktı **"gamemode is active"** ise servis başarıyla çalışıyor demektir. **"gamemode is inactive"** çıktısı, servisin kurulu olduğunu ancak şu anda herhangi bir oyun tarafından tetiklenmediğini gösterir.

### Log Analizi ve Hata Ayıklama
Eğer performans artışı hissetmiyorsanız veya servis tetiklenmiyorsa, `systemd` günlüklerini inceleyebilirsiniz:

```bash
journalctl --user -u gamemoded.service
```

Bu komut, GPU sürücüsü uyumsuzlukları veya yetki hataları (örneğin, NVIDIA CoolBits eksikliği) gibi sorunları tespit etmenizi sağlar.