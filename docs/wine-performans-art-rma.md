---
title: "wine performans artırma"
description: "wine performans artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Wine Performans Artırma Rehberi: Linux Üzerinde Windows Başarımını Optimize Etme

Wine (Wine Is Not an Emulator), Windows API çağrılarını POSIX standartlarına anlık olarak çeviren bir uyumluluk katmanıdır. Doğru konfigüre edilmediğinde işlemci (CPU) ve grafik kartı (GPU) üzerinde ciddi bir yük oluşturarak FPS düşüşlerine, gecikmelere (input lag) ve takılmalara neden olur. 

Bu rehberde, Wine ortamında maksimum grafik ve işlemci performansı elde etmek için uygulanması gereken teknik adımlar, ortam değişkenleri (environment variables) ve sistem düzeyindeki optimizasyonlar yer almaktadır.

---

## 1. Grafik Çeviri Katmanlarını Güncelleyin: DXVK ve VKD3D-Proton

Wine'ın yerel DirectX-to-OpenGL çeviricisi performans açısından yetersizdir. Bunun yerine DirectX çağrılarını Vulkan API'sine çeviren katmanlar kullanılmalıdır.

*   **DXVK (DirectX 9, 10, 11 -> Vulkan):** CPU darboğazını azaltır ve GPU kullanım verimliliğini artırır.
*   **VKD3D-Proton (DirectX 12 -> Vulkan):** Valve tarafından geliştirilen, DX12 performansını doğrudan Vulkan pipeline'ına aktaran kütüphanedir.

### Kurulum ve Etkinleştirme:
DXVK paketini indirdikten sonra ilgili Wine prefix'ine entegre etmek için:

```bash
export WINEPREFIX=~/.wine_custom
./setup_dxvk.sh install
```

Oyun veya uygulama başlatılırken Vulkan gölgelendirici (shader) derlemesini hızlandırmak için şu ortam değişkenlerini ekleyin:

```bash
export DXVK_STATE_CACHE=1
export DXVK_ASYNC=1 # (Geliştirici derlemelerinde takılmaları önler)
```

---

## 2. Çekirdek Düzeyinde Senkronizasyon: Esync ve Fsync

Wine, varsayılan olarak Windows iş parçacığı (thread) senkronizasyonunu taklit etmek için yavaş bir yöntem olan Windows Server (wineserver) iletişimini kullanır. Bu durum CPU kullanımı tavan yaptırır.

### Esync (Eventfd Synchronization)
Wineserver yükünü ortadan kaldırarak dosya tanımlayıcıları (file descriptors) üzerinden senkronizasyon sağlar.
*   **Kullanım:** `export WINEESYNC=1`
*   **Gereksinim:** Açık dosya limitinin artırılması gerekir (`/etc/security/limits.conf` içinde `nofile 1048576`).

### Fsync (Futex Synchronization)
Esync'ten daha verimlidir. Linux çekirdeğindeki `futex` sistem çağrılarını doğrudan kullanır.
*   **Kullanım:** `export WINEFSYNC=1`
*   **Gereksinim:** Linux Kernel 5.16+ veya Valve Fsync yamalı bir çekirdek (Zen, XanMod vb.).

---

## 3. Özel Wine Yapılandırmaları (Proton-GE ve Wine-GE)

Ana hat (vanilla) Wine sürümleri genel uyumluluğa odaklanır. Oyun ve ağır grafik uygulamaları için optimize edilmiş özel derlemeleri kullanmak performans artışı sağlar.

*   **Wine-GE (GloriousEggroll):** Oyunlar için özel patch setleri, güncel DXVK/VKD3D entegrasyonu ve Media Foundation düzeltmeleri içerir.
*   **Staging Sürümleri:** `wine-staging`, deneysel performans yamalarını (CSMT, Raw Input, GPU Passthrough geliştirmeleri) varsayılan olarak barındırır.

---

## 4. CPU Zamanlayıcısı ve GameMode Entegrasyonu

İşlemcinin güç tasarrufu modundan çıkıp sürekli yüksek frekansta (Boost Clock) çalışması sağlanmalıdır.

### CPU Governor Ayarı:
Sistem işlemci yönetimini "performance" moduna alın:

```bash
sudo cpupower frequency-set -g performance
```

### Feral GameMode Kullanımı:
Feral Interactive tarafından geliştirilen `gamemode`, uygulama başladığında GPU bellek frekansını, CPU zamanlayıcısını ve I/O önceliğini otomatik olarak en yüksek seviyeye çeker.

Wine uygulamasını GameMode ile çalıştırma:

```bash
gamemoderun wine uygulama.exe
```

---

## 5. Wine Registry (Kayıt Defteri) İnce Ayarları

`regedit` komutu ile Wine kayıt defterine erişerek grafik işlemci sınırlarını optimize edin.

Komut satırından `wine regedit` çalıştırın ve `HKEY_CURRENT_USER\Software\Wine\Direct3D` dizinine gidin (Yoksa oluşturun):

| Anahtar (Dword) | Değer | Açıklama |
| :--- | :--- | :--- |
| `csmt` | `0x00000001` | Multi-threaded Command Stream'i zorla açar (CPU yükünü böler). |
| `StrictDrawOrdering` | `disabled` | Çizim sırası kontrolünü gevşeterek FPS artışı sağlar. |
| `OffscreenRenderingMode` | `fbo` | Ekran dışı render işlemlerini Framebuffer Object ile hızlandırır. |
| `VideoMemorySize` | *GPU VRAM MB* | Ekran kartınızın bellek miktarını elle girin (Örn: `8192`). |

---

## 6. Sürücüye Özel Optimizasyonlar (Nvidia / AMD)

### Nvidia
Nvidia sürücülerinde GLX kütüphanesi yerine Vulkan bellek yönetimini agresifleştirmek için:

```bash
export __NV_PRIME_RENDER_OFFLOAD=1
export __GL_SHADER_DISK_CACHE=1
export __GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1
```

### AMD (MESA / RADV)
AMD kullanıcıları için varsayılan LLVM derleyicisi yerine Valve'ın geliştirdiği ACO shader derleyicisini kullanmak derleme sürelerini ve oynanış sırasındaki takılmaları (stuttering) engeller:

```bash
export RADV_PERFTEST=aco
```

---

## 7. Bellek ve Prefiks (Prefix) Temizliği

*   **64-Bit Prefiks Kullanımı:** Gereksiz 32-bit kitaplık karmaşasını önlemek için temiz bir 64-bit mimari oluşturun:
    ```bash
    export WINEARCH=win64
    export WINEPREFIX=~/.wine64_perf
    wineboot -u
    ```
*   **Hata Ayıklama (Debug) Günlüklerini Kapatın:** Wine, varsayılan olarak arka planda yoğun bir log kaydı tutar. Bu durum disk I/O ve CPU kullanımını etkiler. Tüm logları kapatmak için:
    ```bash
    export WINEDEBUG=-all
    ```

---

## Özet: Maksimum Performans Başlatma Komutu dizilimi

Bir oyunu veya uygulamayı en yüksek performans konfigürasyonu ile başlatmak için terminal çıktısı veya script içeriği şu şekilde olmalıdır:

```bash
#!/bin/bash
export WINEPREFIX="/home/kullanici/wine_prefixes/oyun"
export WINEDEBUG=-all
export WINEESYNC=1
export WINEFSYNC=1
export DXVK_STATE_CACHE=1
export RADV_PERFTEST=aco

gamemoderun wine "/path/to/game.exe"
```