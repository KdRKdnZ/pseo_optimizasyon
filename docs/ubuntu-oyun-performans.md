---
title: "ubuntu oyun performansı"
description: "ubuntu oyun performansı hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Ubuntu Oyun Performansı: Teknik İnceleme, Sürücü Mimarisi ve Optimizasyon Rehberi

Son yıllarda Linux çekirdeğindeki gelişmeler, grafik sürücülerindeki olgunlaşma ve Valve'ın Proton projesine yaptığı yatırımlar sayesinde Ubuntu, oyun konusunda Windows'a doğrudan rakip hale gelmiştir. Ubuntu'nun oyun performansı; grafik API'lerinin çevirisi, ekran kartı sürücülerinin çalışma mimarisi ve çekirdek (kernel) seviyesindeki zamanlayıcı (scheduler) optimizasyonlarına doğrudan bağlıdır.

Bu makalede Ubuntu'nun oyun mimarisi, GPU sürücü yapılandırmaları, performans artırma teknikleri ve Windows ile olan teknik farkları detaylandırılmıştır.

---

## 1. Ubuntu Oyun Altyapısı ve Mimarisi

Linux üzerinde bir Windows oyununun çalışması sanallaştırma (virtualization) veya öykünme (emulation) ile gerçekleşmez. Çalışma mantığı, **POSIX uyumluluk katmanları** ve **API çeviricileri** üzerinden doğrudan Donanım Hızlandırmalı (Hardware Accelerated) komut setlerine dönüştürülmesidir.

### Katman Dizilimi:
1. **Oyun (Executable - .exe):** DirectX 9/11/12 veya Vulkan çağrıları yapar.
2. **Proton / Wine:** Windows API çağrılarını (`Kernel32.dll`, `User32.dll` vb.) Linux sistem çağrılarına (syscalls) çevirir.
3. **DXVK / VKD3D-Proton:** 
   * **DXVK:** DirectX 9, 10 ve 11 çağrılarını **Vulkan API**'sine anlık olarak dönüştürür.
   * **VKD3D-Proton:** DirectX 12 çağrılarını Vulkan API'sine dönüştürür.
4. **Mesa / NVIDIA Sürücüsü:** Vulkan komutlarını işler ve GPU'ya iletir.
5. **Linux Çekirdeği (Kernel):** GPU komut kuyruklarını ve bellek yönetimini (VRAM/RAM) üstlenir.

```
[Windows Oyunu (.exe)]
         │
  (DirectX 11/12)
         ▼
  [DXVK / VKD3D] ────► [Vulkan API]
         │                   │
         └───────► [Proton] ◄┘
                     │
         (Linux Syscalls)
                     ▼
             [Linux Kernel]
                     ▼
               [GPU Hardware]
```

---

## 2. Ekran Kartı Sürücüsü Mimarisi ve Performans Etkisi

Ubuntu'da grafik performansı, kullanılan GPU mimarisine ve sürücü türüne göre değişiklik gösterir.

### AMD (Radeon) ve Intel
AMD ve Intel, açık kaynaklı **Mesa** sürücü ailesini kullanır. 
* **Mesa RADV (AMD Vulkan Sürücüsü):** AMD’nin resmi kapalı kaynak sürücüsünden (AMDGPU-PRO) genellikle daha yüksek FPS ve daha düşük gecikme sunar.
* **ACO Shader Derleyicisi:** Valve tarafından geliştirilen ve Mesa RADV içerisinde yer alan ACO, oyun içi takılmaları (stuttering) önlemek için gölgelendirici (shader) derleme sürelerini milisaniyeler seviyesine indirir.

### NVIDIA
NVIDIA, kapalı kaynaklı (proprietary) sürücü modeliyle çalışır.
* Ubuntu deposundaki varsayılan `nouveau` (açık kaynak) sürücüsü oyun için yetersizdir.
* **Proprietary NVIDIA Sürücüsü (DKMS):** En yüksek performansı almak için sahipli sürücü kurulmalıdır.
* **X11 vs Wayland:** NVIDIA kartlarda Wayland protokolü son sürümlerde (555+ sürücüleri ve Explicit Sync desteği ile) gelişmiş olsa da, en kararlı FPS ve Değişken Yenileme Hızı (G-Sync) performansı halen **Xorg (X11)** oturumunda elde edilir.

#### NVIDIA Sürücü Kurulumu (CLI):
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-driver-555 nvidia-dkms-555
```

---

## 3. Ubuntu'da Oyun Performansını Artırma Teknikleri

### A. Feral GameMode Kullanımı
Feral Interactive tarafından geliştirilen `GameMode`, oyun başladığında sistem kaynaklarını otomatik olarak optimize eden bir arka plan hizmetidir (daemon).

**GameMode Yapılandırmasının Yaptığı İşlemler:**
* CPU zamanlayıcısını `performance` moduna alır (Power Save modunu kapatır).
* GPU saat frekanslarını maksimuma sabitler.
* I/O önceliğini oyuna yönlendirir.
* Ekran koruyucuyu devre dışı bırakır.

**Kurulum:**
```bash
sudo apt install gamemode
```
**Steam Başlatma Seçeneği:**
```bash
gamemoderun %command%
```

### B. Özel Çekirdek (Kernel) Kullanımı: XanMod veya Zen Kernel
Ubuntu’nun varsayılan Linux çekirdeği genel kullanım amaçlıdır. Oyunlarda komut gecikmesini (latency) azaltmak ve kare hızlarını stabilize etmek için **XanMod** gibi düşük gecikmeli (low-latency) çekirdekler tercih edilebilir.

* **Futex2 (futex_waitv):** CPU üzerindeki iş parçacığı (thread) senkronizasyon yükünü azaltır, CPU sınırına takılan oyunlarda FPS artışı sağlar.

**XanMod Kurulumu:**
```bash
echo 'deb http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-kernel.list
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/xanmod-archive-keyring.gpg
sudo apt update && sudo apt install linux-xanmod-x64v3
```

### C. Gelişmiş Proton Sürümleri: Proton-GE (GloriousEggroll)
Steam'in resmi Proton sürümlerine ek olarak, topluluk tarafından geliştirilen **Proton-GE**, ek video kodlayıcıları (MF/Media Foundation), özel DXVK yamaları ve ek performans iyileştirmeleri içerir.

* ProtonUp-Qt aracı ile kolayca yönetilebilir:
```bash
flatpak install flathub net.davidotek.pupgui2
```

---

## 4. Ubuntu vs. Windows Performans Karşılaştırması

| Kriter | Ubuntu (Linux) | Windows 11 |
| :--- | :--- | :--- |
| **Vulkan Yerel Oyunlar** | %5 - %15 daha yüksek FPS | Standart performans |
| **DirectX 11 Oyunları** | DXVK sayesinde eşdeğer veya daha yüksek FPS | Standart performans |
| **DirectX 12 Oyunları** | VKD3D yükü nedeniyle %2 - %8 FPS kaybı olabilir | Yerel API desteği (En yüksek performans) |
| **Arka Plan Kaynak Kullanımı** | Düşük RAM (~1.5 - 2.5 GB) ve düşük CPU kullanımı | Yüksek RAM (~4 - 6 GB) ve arka plan servisleri |
| **Gölgelendirici (Shader) Takılmaları** | Mesa ACO ve Steam Shader Pre-compilation ile minimum | Oyun içinde anlık derleme takılmaları yaşanabilir |
| **Anti-Cheat (Hile Karşıtı) Desteği** | EAC ve BattlEye desteklenir. Kernel seviyesi (Vanguard vb.) **çalışmaz**. | Tüm anti-cheat yazılımları çalışır. |

---

## 5. Sistem Optimizasyon Kontrol Listesi

1. **Vulkan Kurulumunu Doğrulayın:**
   ```bash
   vulkaninfo | grep deviceName
   ```
2. **ESync ve FSync Kontrolü:** Sisteminizde `ulimit -n` değerinin yüksek olduğunu (örn: 1048576) doğrulayın. Bu, iş parçacığı sınırını kaldırarak oyun içi çökmeleri engeller.
3. **Masaüstü Ortamı Kompozitörünü Kapatın:** XFCE veya KDE Plasma kullanıyorsanız, oyun oynarken tam ekran pencere kompozitörünü (Unredirect Fullscreen Windows) kapatmak girdi gecikmesini (input lag) düşürür. GNOME bu işlemi otomatik yapar.

## Özet
Ubuntu, doğru grafik sürücüleri (NVIDIA için sahipli sürücüler, AMD için Mesa RADV), güncel Vulkan bileşenleri ve **GameMode** gibi optimizasyon araçları kullanıldığında Windows ile başa baş bir oyun performansı sunar. Özellikle Vulkan tabanlı ve DirectX 11 oyunlarda Ubuntu, daha hafif işletim sistemi mimarisi sayesinde kare sürelerinde (frame time) daha kararlı bir çizgi çizer.