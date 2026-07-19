---
title: wine performans artırma
description: wine performans artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Wine Performans Artırma: Linux Üzerinde Windows Uygulamalarını En Yüksek Hızda Çalıştırma Rehberi

Wine (Wine Is Not an Emulator), Windows API çağrılarını POSIX (Linux, macOS) sistem çağrılarına anlık olarak çeviren bir uyumluluk katmanıdır. Bu çeviri işlemi, doğası gereği CPU ve GPU üzerinde ek bir yük oluşturur. Ancak doğru optimizasyonlar, doğru kernel yapılandırmaları ve donanım hızlandırma teknikleri ile Wine üzerinde çalışan uygulamaların ve oyunların performansını yerel (native) Windows seviyesine, hatta bazı durumlarda daha üzerine çıkarmak mümkündür.

Bu teknik rehberde, sistem mimarisi seviyesinde **wine performans artırma** yöntemlerini, kanıta dayalı parametreleri ve donanım optimizasyonlarını inceleyeceğiz.

---

## 1. Grafik ve Sürücü Optimizasyonları

Wine performansını doğrudan etkileyen en kritik darboğaz (bottleneck) grafik API çevrimleridir. Windows uygulamalarının kullandığı DirectX çağrılarının, Linux'un anlayabileceği Vulkan veya OpenGL çağrılarına en az kayıpla dönüştürülmesi gerekir.

### DXVK ve VKD3D-Proton Entegrasyonu
Geleneksel Wine, DirectX kodlarını OpenGL'e çevirir (wined3d). Bu işlem ciddi CPU yükü yaratır. **DXVK**, DirectX 9, 10 ve 11 çağrılarını doğrudan **Vulkan** API'sine çevirerek GPU tabanlı donanım hızlandırması sağlar. DirectX 12 için ise **VKD3D-Proton** kullanılmalıdır.

*   **Uygulama:** Manuel kurulum yerine Lutris, Bottles veya Steam (Proton) gibi modern Wine ön yüzleri kullanılarak DXVK aktif edilmelidir.
*   **Performans Kazanımı:** Kare hızlarında (FPS) %50 ila %200 arasında artış, CPU darboğazlarında ciddi azalma.

### Grafik Sürücüsü ve Vulkan Yapılandırması
Ekran kartı sürücülerinin güncelliği ve doğru Vulkan kütüphanelerinin kullanımı kritik önem taşır.

*   **NVIDIA Kullanıcıları:** Sahipli (proprietary) güncel sürücüleri kullanmalıdır. Açık kaynaklı Nouveau sürücüleri Wine performansı için yetersizdir. Ek olarak, çoklu iş parçacığı (multithreading) desteği için şu ortam değişkeni (environment variable) sisteme tanımlanmalıdır:
    ```bash
    __GL_THREADED_OPTIMIZATIONS=1
    ```
*   **AMD Kullanıcıları:** Mesa sürücüleri içerisindeki **RADV** Vulkan sürücüsünü tercih etmelidir. AMDVLK yerine RADV, shader derleme sürelerinde (stuttering/takılma önleme) daha başarılıdır.

---

## 2. Çekirdek (Kernel) ve İşlemci Seviyesinde İyileştirmeler

Wine, Windows'un çoklu iş parçacığı (multi-threading) yönetimini Linux süreçlerine (processes) eşler. Standart Linux çekirdeği bu senkronizasyonu `wineserver` üzerinden yapar ve bu durum yüksek gecikmeye (latency) yol açar.

### Esync ve Fsync Aktivasyonu
`wineserver` darboğazını aşmak için geliştirilen iki temel teknoloji mevcuttur:

*   **Esync (Eventfd-based synchronization):** Sistem kaynaklarındaki dosya tanımlayıcı (file descriptor) limitlerini kullanarak senkronizasyonu hızlandırır. Esync kullanabilmek için sistemdeki limitlerin artırılması gerekir. `/etc/security/limits.conf` dosyasına şu satırlar eklenmelidir:
    ```text
    * hard nofile 1048576
    * soft nofile 1048576
    ```
*   **Fsync (Futex-based synchronization):** Linux Kernel 5.16 ile ana çekirdeğe dahil edilen `futex_waitv` sistem çağrısını kullanır. Doğrudan çekirdek seviyesinde senkronizasyon sağladığı için Esync'ten daha hızlıdır ve CPU yükünü minimize eder.
    *   **Kullanımı:** Fsync destekli bir kernel (örn: Zen Kernel, Liquorix veya Proton-GE) kullanırken şu değişken ile aktif edilir:
        ```bash
        WINEFSYNC=1
        ```

### CPU Governor ve Güç Yönetimi
İşlemcinin dinamik frekans ölçeklendirmesi (ondemand/schedutil), Wine altındaki ani yük değişimlerine hızlı tepki veremeyebilir. Performans kaybını önlemek için CPU çalışma modu "Performance" olarak ayarlanmalıdır.

```bash
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```
Alternatif olarak, Feral Interactive tarafından geliştirilen **GameMode** aracı kullanılabilir. Başlatma komutunun başına `gamemoderun` eklemek, CPU governor'ı otomatik olarak performans moduna alır.

---

## 3. WinePrefix ve Bellek Yönetimi

Her Windows uygulaması için izole bir çalışma alanı (WinePrefix) oluşturmak, hem kararlılık hem de performans açısından en iyi pratiklerden biridir.

### 64-bit ve 32-bit WinePrefix Ayrımı
Sadece 32-bit olan eski Windows uygulamaları için 64-bit bir WinePrefix kullanmak gereksiz kütüphane yükü ve bellek harcaması yaratır. Uygulamanın mimarisine uygun temiz bir prefix oluşturulmalıdır:

```bash
# Sadece 32-bit uygulamalar için:
WINEPREFIX=~/.wine32 WINEARCH=win32 winecfg

# 64-bit modern uygulamalar için:
WINEPREFIX=~/.wine64 WINEARCH=win64 winecfg
```

### Sanal Bellek (Swap) ve Hugepages Ayarları
Bellek yoğun uygulamalarda Linux çekirdeğinin agresif swap (sanal bellek) kullanımı performansı düşürür. `swappiness` değerini düşürmek, verilerin fiziksel RAM'de kalmasını sağlar.

`/etc/sysctl.conf` dosyasına ekleyin:
```text
vm.swappiness=10
```

Ayrıca, büyük bellek bloklarının daha hızlı adreslenmesi için **Hugepages** aktif edilebilir. Bu, özellikle yüksek RAM tüketen modern oyunlarda FPS düşüşlerini engeller.

---

## 4. Gelişmiş Wine Ortam Değişkenleri (Environment Variables)

Wine çalışma zamanı (runtime) davranışını optimize etmek için terminalden veya oyun başlatıcılardan (Steam/Lutris) parametreler geçilebilir. İşte en etkili **wine performans artırma** değişkenleri:

| Değişken | Değer | Açıklama |
| :--- | :--- | :--- |
| `STAGING_SHARED_MEMORY` | `1` | Wine Staging kullanıcıları için paylaşılan bellek kullanımını açarak performansı artırır. |
| `WINE_LARGE_ADDRESS_AWARE` | `1` | 32-bit uygulamaların 2 GB yerine 4 GB RAM adreslemesine izin vererek çökmeleri önler. |
| `DXVK_HUD` | `compiler` | DXVK shader derleme durumunu ekranda gösterir (Performans takibi için). |
| `WINE_NO_PRELOAD_RESERVE` | `1` | Bellek adresleme alanındaki kısıtlamaları kaldırarak bazı uygulamaların açılışını hızlandırır. |

Örnek bir optimize edilmiş çalıştırma komutu:
```bash
env WINEFSYNC=1 STAGING_SHARED_MEMORY=1 WINE_LARGE_ADDRESS_AWARE=1 gamemoderun wine uygulama.exe
```

---

## 5. Donanım ve Yazılım Uyumluluk Matrisi

Yapılan optimizasyonların donanım mimarisine göre beklenen etki düzeyleri aşağıdaki tabloda özetlenmiştir:

| Optimizasyon Yöntemi | Etkilenen Donanım | Beklenen Performans Artışı | Zorluk Derecesi |
| :--- | :--- | :--- | :--- |
| **DXVK / VKD3D** | GPU (NVIDIA/AMD/Intel) | %100 - %300 (Çok Yüksek) | Kolay |
| **Fsync Aktivasyonu** | CPU (Çok Çekirdekli) | %15 - %40 (Yüksek) | Orta (Kernel Desteği Gerekir) |
| **CPU Governor (Performance)** | CPU | %5 - %15 (Düşük Gecikme) | Çok Kolay |
| **Sürücü Optimizasyonu (RADV/NVIDIA)** | GPU | %20 - %50 (Yüksek) | Orta |
| **Swappiness Ayarı** | RAM / Depolama (SSD/HDD) | %10 (Daha Az Takılma) | Kolay |

Bu adımların doğru sırayla uygulanması, Wine üzerindeki emülasyon katmanının getirdiği yükü neredeyse sıfıra indirerek donanımınızdan maksimum verim almanızı sağlayacaktır.