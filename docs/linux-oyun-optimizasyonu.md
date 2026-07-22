---
title: "linux oyun optimizasyonu"
description: "linux oyun optimizasyonu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Linux Oyun Optimizasyonu: Maksimum Performans ve FPS Artırma Rehberi

Linux işletim sistemlerinde oyun performansı, doğru sürücü yapılandırmaları, kernel (çekirdek) özelleştirmeleri ve katman yazılımlarının optimizasyonu ile Windows seviyesine hatta bazı durumlarda üzerine çıkarılabilir. Bu rehber; Vulkan, Proton, CPU/GPU optimizasyonları ve sistem parametrelerini kapsayan teknik bir kılavuzdur.

---

## 1. Ekran Kartı Sürücülerinin Yapılandırılması

Oyun performansındaki en kritik faktör ekran kartı sürücüleridir. Açık kaynak ve kapalı kaynak sürücülerin doğru ayarlanması gerekir.

### Nvidia GPU Optimizasyonu
Nvidia kullanıcıları mutlaka güncel **Sahipli (Proprietary)** sürücüleri kullanmalıdır.

* **Sürücü Kurulumu:** Dağıtımınızın paket yöneticisini kullanarak en son kararlı sürücüyü (örn. `nvidia-driver-550` veya üstü) yükleyin.
* **PowerMizer Ayarı:** Ekran kartının sürekli yüksek frekansta çalışmasını sağlamak için Terminal üzerinden veya `nvidia-settings` GUI paneli ile PowerMizer modunu "Prefer Maximum Performance" olarak ayarlayın.
  ```bash
  nvidia-settings -a "[gpu:0]/PowerMizerEnable=01" -a "[gpu:0]/NV20ControlXvDisableBackendScaling=1" -a "[gpu:0]/GPUPowerMizerMode=1"
  ```
* **DRM KMS Etkinleştirme:** Ekran yırtılmalarını önlemek ve Wayland uyumluluğunu artırmak için Kernel parametrelerine `nvidia-drm.modeset=1` ekleyin.

### AMD GPU Optimizasyonu
AMD kartlar için çekirdeğe entegre **MESA (RADV)** sürücüleri en iyi performansı verir.

* **MESA Sürücülerini Güncel Tutun:** PPA veya Arch (AUR) depolarından en güncel MESA paketlerini kullanın.
* **RADV Kullanımı:** AMDVLK yerine varsayılan Vulkan sürücüsü olarak MESA'nın RADV sürücüsünü zorlamak için şu ortam değişkenini kullanın:
  ```bash
  export AMD_VULKAN_ICD=RADV
  ```

---

## 2. Kernel (Çekirdek) ve CPU Optimizasyonu

Standart Linux çekirdekleri genel kullanım için tasarlanmıştır. Oyunlarda düşük gecikme (latency) ve yüksek FPS için optimize edilmiş çekirdekler tercih edilmelidir.

### Özel Kernel Kullanımı
Oyun odaklı özelleştirilmiş çekirdekler, **fsync (futex2)** ve düşük gecikmeli zamanlayıcılar (scheduler) içerir:
* **XanMod Kernel:** Yüksek yük altında düşük gecikme sağlar.
* **Liquorix Kernel:** Masaüstü ve oyun tepkiselliğine odaklanır.
* **CachyOS / Zen Kernel:** AMD ve Intel işlemciler için ek derleme optimizasyonları sunar.

### CPU Governor (Güç Modu) Ayarı
İşlemci frekansının oyun esnasında düşmesini engellemek için `performance` moduna geçilmelidir.

```bash
# cpupower aracını kullanarak tüm çekirdekleri performans moduna alın
sudo cpupower frequency-set -g performance
```

*Alternatif olarak `auto-cpufreq` veya `gamemode` servisleri bu işlemi otomatikleştirir.*

---

## 3. Wine, Proton ve DXVK/VKD3D Yapılandırması

Windows oyunlarının Linux'ta çalışmasını sağlayan çeviri katmanlarının güncelliği ve konfigürasyonu hayati önem taşır.

### Custom Proton: Proton-GE (GloriousEggroll)
Valve'ın standart Proton sürümüne kıyasla daha fazla yaması, güncel DXVK bileşeni ve medya kod çözücü desteği barındırır.
* **Kurulum:** `ProtonUp-Qt` GUI aracını kullanarak en güncel **Proton-GE** sürümünü indirin ve Steam'e entegre edin.

### DXVK ve Vulkan Shader Önbelleği
DirectX 9/10/11 çağrılarını Vulkan'a çeviren DXVK ve DirectX 12'yi çeviren VKD3D, takılmaları (stutter) önlemek için shader'ları önceden işlemelidir.

* **Steam Shader Pre-compilation:** Steam ayarlarından *"Enable Shader Pre-caching"* seçeneğini aktif tutun.
* **Görsel Takılmaları Engelleme (Gelişmiş):** DXVK Async özelliğini destekleyen bir yapılandırmada takılmaları minimuma indirmek için başlangıç seçeneğine ekleyin:
  ```bash
  DXVK_ASYNC=1 %command%
  ```

---

## 4. Feral GameMode Kullanımı

Feral Interactive tarafından geliştirilen **GameMode**, bir oyun başladığında arka planda sistem ayarlarını anlık olarak oyuna göre optimize eder (CPU governor, I/O önceliği, GPU aşırı hızlandırma vb.).

### Kurulum ve Kullanım
Dağıtımınıza göre `gamemode` paketini yükleyin. Oyunları GameMode ile başlatmak için başlatma parametrelerine aşağıdaki komutu ekleyin:

```bash
gamemoderun %command%
```

---

## 5. Steam ve Oyun Başlatma Seçenekleri (Launch Options)

Steam üzerindeki oyunların özellikler menüsüne girerek "Başlatma Seçenekleri" (Launch Options) kısmına eklenen komutlar doğrudan performansa etki eder.

### Örnek Optimizasyon Dizesi (AMD Sürücüleri İçin):
```bash
gamemoderun mangohud RADV_PERFTEST=nggc %command%
```

### Örnek Optimizasyon Dizesi (Nvidia Sürücüleri İçin):
```bash
gamemoderun mangohud __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia %command%
```

### Parametrelerin Anlamları:
* `gamemoderun`: Feral GameMode'u tetikler.
* `mangohud`: FPS, sıcaklık, RAM/VRAM kullanımını ekranda gösterir ve FPS limitleme imkanı tanır.
* `PROTON_NO_ESYNC=1` / `PROTON_NO_FSYNC=1`: Eski sistemlerde veya belirli oyunlarda çökme sorunlarını çözer.

---

## 6. Masaüstü Ortamı (Compositor) Optimizasyonu

Masaüstü ortamının pencere yöneticisi (Compositor), oyunlar üzerinde **Girdi Gecikmesine (Input Lag)** ve FPS düşüşlerine neden olabilir.

### X11 Kullanıcıları İçin:
Oyun tam ekrana geçtiğinde Compositor'ün devre dışı kalması gerekir (Bypass Compositor).
* **KDE Plasma:** Ayarlar > Ekran ve Monitör > İşleyici bölümünden "Tam ekran pencerelerinin işleyiciyi devre dışı bırakmasına izin ver" seçeneğini işaretleyin.
* **XFCE:** `xfwm4-tweaks-settings` altından pencere yöneticisi bileşik oluşturmayı tam ekranda kapatın.

### Wayland Kullanıcıları İçin:
* Wayland, geleneksel compositor mantığını değiştirmiştir.
* VRR (Variable Refresh Rate / G-Sync / FreeSync) desteğinin aktif olduğundan emin olun.
* Nvidia 555 ve üzeri sürücülerde **Explicit Sync** desteği geldiği için Wayland üzerindeki takılmalar tamamen çözülmüştür.

---

## 7. Bellek (RAM) ve Swap (Sanal Bellek) Ayarları

Bellek yönetimi, özellikle 16 GB ve altı RAM'e sahip sistemlerde oyunların aniden kapanmasını ve takılmasını engeller.

### Swappiness Değerini Düşürme
Sistemin RAM varken diski (Swap) kullanmasını engellemek için `swappiness` değerini 10'a düşürün.

1. `/etc/sysctl.d/99-swappiness.conf` dosyasını oluşturun veya düzenleyin:
   ```text
   vm.swappiness=10
   ```
2. Değişikliği uygulayın:
   ```bash
   sudo sysctl -p /etc/sysctl.d/99-swappiness.conf
   ```

### zRAM Kullanımı
Fiziksel RAM yetersiz kaldığında diske yazmak yerine RAM'in bir bölümünü sıkıştırarak kullanan `zram-generator` paketini aktif edin. Bu işlem, diske erişim gecikmesini ortadan kaldırarak oyunların çökmesini engeller.

---

## Özet Performans Kontrol Listesi

1. **GPU Sürücüsü:** Güncel mi? (Nvidia için Proprietary, AMD için MESA/RADV).
2. **CPU Governor:** `performance` modunda mı?
3. **GameMode:** Yüklü ve Steam başlatma seçeneğine `gamemoderun %command%` eklendi mi?
4. **Proton:** Oyun için en uygun `Proton-GE` sürümü seçildi mi?
5. **Compositor:** Tam ekranda devre dışı bırakılıyor mu?
6. **Esync/Fsync:** Kernel destekliyor mu? (`fsync` destekli kernel önerilir).