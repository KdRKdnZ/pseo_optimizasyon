# Linux Oyun Optimizasyonu Rehberi: Performans ve FPS Artırma Yöntemleri

Linux işletim sistemlerinde oyun performansı, doğru yapılandırmalar ve optimizasyon araçları kullanıldığında Windows ile yarışır hatta bazı senaryolarda Windows'u geride bırakır seviyeye ulaşmıştır. Bu rehber, Linux üzerinde girdi gecikmesini (input lag) düşürmek, FPS değerlerini artırmak ve kare takılmalarını (stuttering) engellemek için uygulanması gereken teknik adımları içermektedir.

---

## 1. Çekirdek (Kernel) Seçimi ve Sistem Ayarları

Standart Linux çekirdekleri (kernel) genel kullanım ve sunucu kararlılığı odaklıdır. Düşük gecikme süresi ve yüksek oyun performansı için özelleştirilmiş çekirdekler tercih edilmelidir.

### Performans Odaklı Kernel Alternatifleri
*   **Zen Kernel:** Masaüstü ve oyun yükleri için girdi gecikmesini en aza indiren gecikme odaklı (latency-focused) çekirdektir. (Arch tabanlı sistemlerde: `sudo pacman -S linux-zen`)
*   **XanMod Kernel:** Yüksek yenileme hızlı monitörler ve ağır iş yükleri için özel zamanlayıcı (scheduler) yamalarına sahip çekirdektir.
*   **Linux-TKG:** PDS veya BORE zamanlayıcılarını kullanarak oyunlarda maksimum FPS ve kararlılık sağlar.

### CPU Governor (İşlemci Güç Yönetimi)
Varsayılan olarak Linux, güç tasarrufu sağlayan `powersave` veya `ondemand` modunu kullanır. Oyun sırasında işlemcinin sürekli maksimum frekansta çalışması için `performance` moduna geçilmelidir.

Terminal üzerinden anlık değişim için:
```bash
sudo cpupower frequency-set -g performance
```

Sistem başlangıcında otomatikleşmesi için **Feral GameMode** entegrasyonu önerilir.

---

## 2. GPU Sürücüleri ve Vulkan Optimizasyonları

Grafik kartı sürücülerinin güncelliği ve Vulkan katmanının doğru yapılandırılması, DirectX - Vulkan dönüşümündeki (DXVK / VKD3D) verimliliği doğrudan etkiler.

### AMD (Mesa) Grafik Kartı Optimizasyonu
AMD kartlar için açık kaynaklı **Mesa RADV** sürücüleri kullanılmalıdır. AMDGPU-PRO sürücüleri oyun için tavsiye edilmez.

*   **ACO Shader Derleyicisi:** Mesa varsayılan olarak ACO derleyicisini kullanır. Bu derleyici, gölgelendirici (shader) derleme sürelerini kısaltarak oyundaki anlık takılmaları engeller.
*   **Değişken Renk Desteği (VRS):** Destekleyen AMD GPU'larda FPS artışı için ortam değişkenlerine ekleyin:
    ```bash
    RADV_PERFTEST=vrs
    ```

### NVIDIA Grafik Kartı Optimizasyonu
NVIDIA kullanıcıları kapalı kaynaklı resmi sürücüleri kullanmalıdır.

1.  **NVIDIA KMS Etkinleştirme:** `/etc/default/grub` dosyasına Kernel parametresi olarak `nvidia-drm.modeset=1` ekleyin ve GRUB'u güncelleyin.
2.  **PowerMizer Performans Modu:** NVIDIA X Server Settings üzerinden PowerMizer ayarını "Prefer Maximum Performance" olarak değiştirin.
3.  **G-Sync / FreeSync:** Kompozitör kaynaklı gecikmeyi önlemek için tam ekran modlarında "Allow G-SYNC/G-SYNC Compatible" seçeneğini aktif edin.

---

## 3. Bellek (RAM) ve Swap (Sanal Bellek) Yapılandırması

Ağır oyunlarda bellek yetersizliği nedeniyle oluşan kilitlenmeleri önlemek için kernel parametreleri düzenlenmelidir.

### vm.max_map_count Artırımı
*Hogwarts Legacy*, *DayZ* veya *Starfield* gibi yoğun bellek alanı adresi talep eden oyunların çökmesini engellemek için `max_map_count` değeri artırılmalıdır.

`/etc/sysctl.d/99-game-performance.conf` dosyasını oluşturun ve aşağıdaki satırları ekleyin:

```ini
# Oyunlarda bellek haritalama limitini yükseltir (Proton/Wine için zorunlu)
vm.max_map_count=16777216

# Swappiness değerini düşürerek sistemin RAM bitmeden disk Swap'ını kullanmasını engeller
vm.swappiness=10

# Bellek temizleme sıklığını optimize eder
vm.vfs_cache_pressure=50
```

Değişiklikleri uygulamak için: `sudo sysctl --system`

---

## 4. Feral GameMode Entegrasyonu

Feral Interactive tarafından geliştirilen **GameMode**, bir oyun başladığında arka planda otomatik olarak aşağıdaki optimizasyonları uygular:
*   CPU governor ayarını `performance` yapar.
*   GPU'yu yüksek performans moduna alır.
*   I/O önceliğini artırır.
*   Ekran koruyucuyu devre dışı bırakır.
*   RAM ve VRAM temizleme süreçlerini önceliklendirir.

### Kurulum ve Kullanım
Ubuntu/Debian: `sudo apt install gamemode`  
Arch Linux: `sudo pacman -S gamemode`

Steam oyun başlatma seçeneklerine entegrasyonu:
```bash
gamemoderun %command%
```

---

## 5. Wine, Proton ve Çeviri Katmanları (DXVK / VKD3D)

Steam dışı veya Steam üzerindeki Windows oyunlarını çalıştırmak için kullanılan çeviri katmanlarının doğru yapılandırılması hayati önem taşır.

### Proton GE (GloriousEggroll) Kullanımı
Valve'ın standart Proton katmanına ek olarak topluluk tarafından geliştirilen Proton GE; ek codec destekleri, performans yamaları ve güncel DXVK/VKD3D sürümlerini içerir. **ProtonUp-Qt** aracı ile kolayca kurulabilir.

### Esync ve Fsync Kullanımı
Wine üzerindeki senkronizasyon yükünü azaltarak CPU darboğazını engeller.
*   **Fsync:** Modern Linux kernel'larında varsayılan olarak desteklenen `futex2` mimarisini kullanır. En düşük CPU kullanımını sağlar.
*   Başlatma komutu parametresi: `WINEFSYNC=1 %command%`

---

## 6. Oyun İçin Masaüstü Ortamı (DE) ve Kompozitör Yönetimi

GNOME (Mutter) ve KDE Plasma (KWin) gibi masaüstü ortamlarının grafik işleyicileri (compositor), oyunlarda dikey eşitleme (V-Sync) gecikmesine ve FPS düşüşlerine yol açabilir.

*   **Wayland:** Wayland protokolü, oyunlarda "Tearing" olmadan düşük gecikme sunar. KDE Plasma Wayland oturumunda "Allow applications to block compositing" seçeneği aktif edilmelidir.
*   **X11 (Xorg):** X11 kullanılıyorsa, oyun başlatıldığında kompozitör kapatılmalıdır (KDE'de `Alt + Shift + F12`).

---

## 7. Örnek Steam Başlatma Seçenekleri (Launch Options)

Oyun performansını tek bir komutla en üst düzeye çıkarmak için Steam kütüphanesindeki bir oyuna sağ tıklayıp *Özellikler > Başlatma Seçenekleri* alanına aşağıdaki yapılandırma eklenebilir:

### Standart Yüksek Performans Konfigürasyonu:
```bash
gamemoderun DXVK_ASYNC=1 WINEFSYNC=1 %command%
```

### AMD Kartlar İçin Ekstra Performans Konfigürasyonu:
```bash
RADV_PERFTEST=aco gamemoderun WINEFSYNC=1 %command%
```

### NVIDIA Kartlar İçin Düşük Gecikme Konfigürasyonu:
```bash
__GL_THREADED_OPTIMIZATIONS=1 gamemoderun WINEFSYNC=1 %command%
```

---

## 8. Performans İzleme Araçları

Yapılan optimizasyonların etkisini ölçmek için en gelişmiş izleme aracı **MangoHud**'dır.

*   **MangoHud Kurulumu:** Vulkan ve OpenGL oyunlarında FPS, frametime (kare süresi), sıcaklık, CPU/GPU kullanımı ve VRAM tüketimini ekranda gösterir.
*   Kullanım: `mangohud gamemoderun %command%`
*   Arayüz özelleştirmesi için **GOverlay** grafik aracı kullanılabilir.

---

## Özet Check-list

1.  [ ] **Kernel:** Zen veya XanMod kernel kuruldu mu?
2.  [ ] **Sürücü:** AMD için Mesa (RADV), NVIDIA için güncel proprietary sürücü aktif mi?
3.  [ ] **System Limits:** `vm.max_map_count` en az 16777216 olarak ayarlandı mı?
4.  [ ] **GameMode:** Feral GameMode kuruldu ve Steam komutuna `gamemoderun` eklendi mi?
5.  [ ] **Proton:** Oyun için güncel Proton GE sürümü seçildi mi?
6.  [ ] **Kompozitör:** Oyun sırasında masaüstü kompozitörü devre dışı bırakıldı mı?