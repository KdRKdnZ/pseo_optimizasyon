# Ubuntu Oyun Performansı: Teknik Analiz ve Optimizasyon Rehberi

Ubuntu ve genel olarak Linux ekosistemi, Valve'ın Proton katmanı ve Vulkan API'sine yaptığı yatırımlar sayesinde modern oyunlarda Windows ile yarışabilecek, hatta bazı senaryolarda onu geçebilecek bir performansa ulaşmıştır. Ancak Ubuntu üzerinde maksimum FPS ve düşük sistem gecikmesi (latency) elde etmek; grafik sürücülerinin mimarisine, kullanılan çeviri katmanlarına ve çekirdek (kernel) seviyesindeki optimizasyonlara doğrudan bağlıdır.

---

## 1. Donanım Mimari Katmanı ve Grafik Sürücüleri

Ubuntu'da oyun performansını belirleyen ana unsur, GPU üreticisinin sunduğu sürücü mimarisi ve çekirdek modülleridir.

### AMD (Mesa / RADV)
AMD ekran kartları, Linux çekirdeğine entegre açık kaynaklı **AMDGPU** sürücüsü ve **Mesa RADV** Vulkan sürücüsü sayesinde Ubuntu'da en yüksek kararlılığı ve performansı sunar.
* **Mesa Sürücü Avantajı:** Shader derleme süreleri (shader compilation stutters) Windows'a kıyasla ACO (AMD Compiler) sayesinde daha düşüktür.
* **Güncelleme:** Sürücüler doğrudan Linux çekirdeği ve Mesa paketleriyle güncellenir.

### NVIDIA (Proprietary / Kapalı Kaynak)
NVIDIA, Linux tarafında proprietry (mülk) sürücüler kullanır. Açık kaynaklı `nouveau` sürücüleri 3D oyun performansı için yetersizdir.
* **X11 vs Wayland:** NVIDIA GPU'larda G-Sync ve kare hızı kararlılığı için şu anki en iyi performans **X11** oturumunda alınır. Wayland desteği `555+` sürücü sürümleri ve "Explicit Sync" ile gelişmekle birlikte henüz bazı konfigürasyonlarda takılmalara (stuttering) neden olabilir.
* **DKMS:** Çekirdek güncellemelerinde sürücü modüllerinin otomatik derlenmesi için `nvidia-dkms` kullanılmalıdır.

---

## 2. Çeviri Katmanları: Proton, DXVK ve VKD3D

Linux üzerinde çalışan Windows tabanlı (DirectX) oyunlar, komutları çalışma zamanında (runtime) Vulkan API çağrılarına dönüştürür.

```
[Oyun (DirectX 9/10/11/12)] ➔ [DXVK / VKD3D-Proton] ➔ [Vulkan API] ➔ [GPU Sürücüsü]
```

* **DXVK (DirectX 9/10/11 -> Vulkan):** CPU üzerindeki yükü azaltır. Çoğu DX11 oyunu Ubuntu üzerinde, Windows'taki yerel DirectX 11 performansından daha yüksek FPS verebilir.
* **VKD3D-Proton (DirectX 12 -> Vulkan):** DX12 komutlarını Vulkan'a çevirir. Yüksek GPU bellek yönetimi gerektirir. Donanım tespiti ve Vulkan yaygınlaşması doğru yapılandırılmışsa performans kaybı %2-5 aralığındadır.

---

## 3. Ubuntu Performans Optimizasyonu (Adım Adım)

Varsayılan Ubuntu kurulumu genel kullanım için tasarlanmıştır. Oyun performansını en üst seviyeye çıkarmak için aşağıdaki teknik düzenlemeler yapılmalıdır.

### A. Güncel Grafik Sürücülerinin Yüklenmesi

**AMD için Güncel Mesa PPA Eklenmesi:**
```bash
sudo add-apt-repository ppa:kisak/kisak-mesa
sudo apt update && sudo apt upgrade -y
```

**NVIDIA için En Güncel Sürücünün Kurulması:**
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-driver-555 nvidia-dkms-555 -y
```

### B. Feral GameMode Entegrasyonu
Feral GameMode, oyun başladığında Linux çekirdeğine ve CPU'ya geçici optimizasyon emirleri gönderir (CPU Governor'ı `performance` moduna alır, I/O önceliğini artırır, GPU saat hızlarını kilitler).

**Kurulum:**
```bash
sudo apt install gamemode -y
```

**Steam Başlatma Seçeneğine Eklenmesi:**
Oyun özelliklerinden "Başlatma Seçenekleri" (Launch Options) kısmına şu komut eklenmelidir:
```text
gamemodedrun %command%
```

### C. Çekirdek (Kernel) Değişimi: XanMod veya Liquorix
Varsayılan Ubuntu kernel'i (generic), sunucu ve günlük iş yükleri için yüksek milisaniyelik zaman dilimlerine (scheduling) sahiptir. Oyunlarda mikro takılmaları önlemek ve I/O gecikmesini düşürmek için **XanMod** veya **Liquorix** (low-latency/real-time patch içeren) çekirdeklere geçilmelidir.

**XanMod Kernel Kurulumu:**
```bash
wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg
echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list
sudo apt update && sudo apt install linux-xanmod-x64v3 -y
```

### D. Esnek Bellek Yönetimi (vm.max_map_count)
Modern oyunlar (örneğin *Hogwarts Legacy*, *Starfield* veya *DayZ*) çok sayıda bellek haritalaması yapar. Varsayılan değer oyunların çökmesine (crash) veya FPS düşüşlerine yol açar.

**Değeri Yükseltme:**
```bash
sudo sysctl -w vm.max_map_count=16777216
echo "vm.max_map_count=16777216" | sudo tee -a /etc/sysctl.d/99-game-performance.conf
```

---

## 4. Anti-Cheat (Hile Karşıtı) Yazılımların Durumu

Ubuntu oyun performansındaki en büyük kısıtlama donanımsal değil, yazılımsaldır.

| Anti-Cheat Yazılımı | Ubuntu/Linux Uyumluluğu | Örnek Oyunlar |
| :--- | :--- | :--- |
| **Easy Anti-Cheat (EAC)** | Destekleniyor (Geliştirici inisiyatifinde) | Apex Legends, Elden Ring, Rust |
| **BattEye** | Destekleniyor (Geliştirici inisiyatifinde) | Rainbow Six Siege, ARMA 3, DayZ |
| **Riot Vanguard** | **Çalışmıyor** (Çekirdek Seviyesi / Ring 0) | Valorant, League of Legends |
| **EA Anti-Cheat** | **Çalışmıyor** | FIFA 24 / EA FC 24 |
| **RICOCHET** | **Çalışmıyor** | Call of Duty: Warzone |

---

## 5. Benchmarks: Windows 11 vs. Ubuntu (Karşılaştırmalı Analiz)

Doğru yapılandırılmış bir Ubuntu sistemi (Kernel 6.8+, Mesa 24.x/NVIDIA 555+, Proton-GE) ile Windows 11 arasındaki sentetik FPS oranları:

* **Cyberpunk 2077 (DirectX 12):** Windows 11 referans alındığında Ubuntu, VKD3D yükü nedeniyle **%95 - %98** başarım gösterir.
* **CS2 (Vulkan Native):** Ubuntu, daha iyi CPU çekirdek yönetimi ve azalan arka plan süreçleri sayesinde Windows 11'e kıyasla **%3 - %7 daha yüksek ortalama FPS** ve daha kararlı %1 LOW FPS değerleri sunar.
* **Doom Eternal (Vulkan Native):** Performans başa baş kalır, ancak Ubuntu üzerinde kare süreleri (frame times) daha düz bir çizgi izler.

---

## Teknik Özet ve Karar

Ubuntu, oyun performansı açısından doğru optimize edildiğinde Windows alternatifinden farksız bir deneyim sunar. 

* **Avantajlar:** Düşük arka plan RAM/CPU kullanımı, esnek çekirdek ve sürücü özelleştirmesi, DirectX 11 oyunlarında Vulkan dönüşümü sayesinde yüksek performans.
* **Dezavantajlar:** Çekirdek seviyesinde (Kernel-level) anti-cheat kullanan rekabetçi oyunların çalışmaması, NVIDIA tarafında Wayland altındaki konfigürasyon karmaşıklığı.