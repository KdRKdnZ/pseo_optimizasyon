---
title: linux oyun optimizasyonu
description: linux oyun optimizasyonu hakkında detaylı optimizasyon ve donanım rehberi.
---

# Linux Oyun Optimizasyonu: Maksimum FPS ve Düşük Gecikme İçin Kapsamlı Rehber

Linux, açık kaynaklı yapısı sayesinde oyun performansını donanım seviyesinde optimize etmek için eşsiz bir esneklik sunar. Doğru yapılandırılmış bir Linux dağıtımı, Windows'a kıyasla daha düşük sistem gecikmesi (latency), daha verimli RAM yönetimi ve daha kararlı kare hızları (FPS) sağlayabilir. Bu rehber, çekirdek (kernel) seviyesinden grafik API'lerine kadar uygulayabileceğiniz en etkili **linux oyun optimizasyonu** adımlarını teknik detaylarıyla ele almaktadır.

---

## Çekirdek (Kernel) ve Zamanlayıcı (Scheduler) Optimizasyonları

Linux çekirdeği, sistem kaynaklarının nasıl dağıtılacağını belirler. Varsayılan çekirdekler genellikle genel kullanım (sunucu/ofis) için optimize edilmiştir. Oyunlar gibi gerçek zamanlı (real-time) performans gerektiren senaryolar için özel çekirdekler tercih edilmelidir.

### Zen Kernel ve XanMod Kullanımı

Oyunlarda milisaniyelik gecikmeleri önlemek için "preemption" (öncelikleme) modeli agresif olan çekirdekler kullanılmalıdır.

*   **Zen Kernel:** Arch Linux tabanlı sistemlerde varsayılan olarak sunulan, masaüstü ve oyun performansına odaklanan bir çekirdektir. Düşük gecikmeli zamanlama (low-latency scheduling) algoritmaları içerir.
*   **XanMod:** Debian/Ubuntu tabanlı sistemler için mükemmel bir alternatiftir. FQ-CoDel paket zamanlayıcısı ve optimize edilmiş ham güç yönetimi ile oyunlarda daha kararlı %1 ve %0.1 minimum FPS değerleri sunar.

**Kurulum (Ubuntu/Debian için XanMod):**

```bash
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg
echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-kernel.list
sudo apt update && sudo apt install linux-xanmod-x64v3
```

### CPU Governor ve Enerji Yönetimi

İşlemcinizin (CPU) oyun esnasında güç tasarrufu moduna geçmesi anlık takılmalara (stuttering) neden olur. CPU ölçekleyiciyi "Performance" moduna almak, çekirdeklerin sürekli en yüksek frekansta çalışmasını sağlar.

**Geçici olarak etkinleştirme:**
```bash
echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

**Kalıcı hale getirmek için (cpupower aracı ile):**
```bash
sudo systemctl enable --now cpupower.service
```

---

## Grafik Sürücüleri ve API Yapılandırması

Donanımınızdan tam performans almak, doğru grafik sürücülerinin seçilmesine ve Vulkan API'sinin doğru yapılandırılmasına bağlıdır.

### NVIDIA ve AMD Sürücü Seçimi

*   **AMD (Radeon):** AMD kullanıcıları kesinlikle kapalı kaynak kodlu sürücüler yerine açık kaynaklı **Mesa** sürücülerini kullanmalıdır. Mesa içindeki **RADV** Vulkan sürücüsü, AMD'nin resmi sürücüsünden çok daha yüksek oyun performansı sunar.
*   **NVIDIA:** NVIDIA kullanıcıları ise açık kaynaklı "Nouveau" sürücüsü yerine en güncel **proprietary (sahipli)** resmi sürücüleri kullanmalıdır.

**Mesa Sürücülerini Güncelleme (Ubuntu için Kisak PPA):**
```bash
sudo add-apt-repository ppa:kisak/kisak-mesa
sudo apt update && sudo apt upgrade -y
```

### Vulkan ve DXVK Entegrasyonu

Windows oyunları DirectX (9/10/11/12) API'lerini kullanır. Linux üzerinde bu oyunları çalıştırmak için DirectX çağrılarını Vulkan çağrılarına dönüştüren **DXVK** (DirectX 9/10/11) ve **VKD3D-Proton** (DirectX 12) katmanları kullanılır.

*   **Shader Pre-compilation (Gölgelendirici Ön Derlemesi):** Oyun içi takılmaların en büyük sebebi gölgelendiricilerin anlık derlenmesidir. Steam ayarlarından "Shader Pre-Caching" özelliğini mutlaka aktif hale getirin.
*   **Graphics Pipeline Library (GPL):** Mesa 23.0 ve NVIDIA 525.80 sürümleriyle gelen Vulkan GPL desteği, shader derleme takılmalarını neredeyse tamamen ortadan kaldırır. Bu özelliğin aktif olduğundan emin olun.

---

## Oyun Çalışma Zamanı (Runtime) ve Katman Optimizasyonları

Oyunların Linux üzerinde yerel performansa yakın çalışmasını sağlayan uyumluluk katmanlarının optimize edilmesi kritik önem taşır.

### Proton ve Wine Yapılandırması

Steam üzerinde oyun oynarken Valve'ın geliştirdiği **Proton** kullanılır. Ancak topluluk tarafından geliştirilen **Proton GE (GloriousEggroll)**, resmi Proton sürümlerine kıyasla birçok performans yaması, güncel DXVK kodları ve video kod çözücü iyileştirmeleri barındırır.

**Proton GE Kurulumu (ProtonUp-Qt aracı ile kolayca yapılabilir):**
1. `ProtonUp-Qt` uygulamasını Flatpak veya paket yöneticinizden indirin.
2. En güncel "GE-Proton" sürümünü seçip yükleyin.
3. Steam oyun özelliklerinden uyumluluk aracını yüklediğiniz GE-Proton sürümü olarak değiştirin.

### Feral GameMode ile Sistem Kaynaklarını Yönetme

Feral Interactive tarafından geliştirilen **GameMode**, oyun başladığında arka planda çalışan servisleri optimize eden bir daemon'dır.

**GameMode'un gerçekleştirdiği optimizasyonlar:**
*   CPU governor'ı otomatik olarak "performance" moduna alır.
*   I/O (Giriş/Çıkış) önceliğini oyuna verir.
*   Ekran koruyucuyu ve güç tasarrufu modlarını devre dışı bırakır.
*   NVIDIA GPU'lar için otomatik hız aşırtma (overclock) profillerini uygular.

**Kullanımı:**
Steam başlatma seçeneklerine (Launch Options) şu komutu ekleyin:
```bash
gamemoderun %command%
```

---

## Bellek (RAM) ve Depolama Optimizasyonları

Linux'un bellek yönetimi son derece gelişmiştir, ancak oyunlar gibi yoğun bellek kullanan uygulamalar için bazı parametrelerin optimize edilmesi gerekir.

### Esync ve Fsync (Dosya Tanımlayıcı Limitleri)

Windows oyunları çoklu iş parçacığı (multi-threading) senkronizasyonu için belirli API'ler kullanır. Linux'ta bunu simüle etmek için **Esync** (eventfd tabanlı) ve daha modern olan **Fsync** (futex_waitv tabanlı, kernel seviyesinde) kullanılır. Fsync, CPU kullanımını azaltarak FPS düşüşlerini engeller.

Fsync'in çalışabilmesi için sistemdeki maksimum dosya tanımlayıcı limitinin (file descriptor limit) yüksek olması gerekir.

**Limit kontrolü:**
```bash
ulimit -Hn
```
Eğer bu değer `1048576` veya daha yüksek değilse, `/etc/security/limits.conf` dosyasına şu satırları ekleyin:

```text
* hard nofile 1048576
* soft nofile 1048576
```

### VRAM ve Swap (Takas Alanı) Yönetimi

Sistem belleği dolduğunda Linux verileri diskteki Swap (Takas) alanına yazar. Bu durum oyunlarda ani FPS düşüşlerine (stutter) yol açar. `swappiness` değerini düşürerek sistemin diske yazma eğilimini azaltabilirsiniz.

**Swappiness değerini 10'a düşürmek için:**
```bash
sudo sysctl vm.swappiness=10
```
Bu ayarı kalıcı yapmak için `/etc/sysctl.d/99-sysctl.conf` dosyasına `vm.swappiness=10` satırını ekleyin.

---

## Sonuç ve Performans Karşılaştırması

Doğru yapılandırılmış bir Linux sistemi, oyunlarda Windows 11 ile başa baş veya bazı senaryolarda (özellikle CPU darboğazı olan oyunlarda) daha yüksek performans sunar.

| Optimizasyon Adımı | Etkilediği Alan | Beklenen Performans Artışı |
| :--- | :--- | :--- |
| **Zen/XanMod Kernel** | Sistem Gecikmesi & %1 Low FPS | %5 - %10 daha kararlı kare hızları |
| **Fsync & Esync** | CPU Çoklu Çekirdek Verimliliği | Yüksek CPU kullanan oyunlarda %15'e varan FPS artışı |
| **Mesa (RADV) / NVIDIA Proprietary** | Grafik İşleme Gücü | Maksimum GPU kullanımı ve kararlılık |
| **GameMode** | Arka Plan Kaynak Yönetimi | Anlık takılmaların (stuttering) önlenmesi |

Yukarıdaki adımları donanımınıza uygun şekilde uygulayarak, Linux işletim sisteminizi profesyonel bir oyun platformuna dönüştürebilirsiniz.