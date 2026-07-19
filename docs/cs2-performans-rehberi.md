---
title: cs2 performans rehberi
description: cs2 performans rehberi hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 Performans Rehberi: Source 2 Motoru İçin Donanım ve Yazılım Optimizasyonu

Counter-Strike 2 (CS2), emektar Source motorundan **Source 2** motoruna geçiş yaparak oyunun render pipeline (görüntü oluşturma hattı), fizik ve ağ protokolü mimarisini tamamen değiştirdi. Bu rehber, CS2'de maksimum FPS, en düşük gecikme süresi (latency) ve kararlı kare süreleri (frametimes) elde etmeniz için kıdemli yazılım mimarisi ve donanım perspektifiyle hazırlanmış en güncel optimizasyon kılavuzudur.

---

## Source 2 Mimarisini Anlamak: CS:GO'dan Ne Değişti?

CS:GO, DirectX 9 tabanlı ve büyük oranda tek çekirdek CPU performansına (single-thread) bağımlı bir oyundu. CS2 ise **DirectX 11** (ve Vulkan) API'lerini kullanır. Bu değişim, donanım kaynaklarının tüketim şeklini kökten değiştirmiştir.

### CPU Darboğazı ve Çoklu Çekirdek Kullanımı
Source 2, modern çok çekirdekli işlemcileri (multi-core) CS:GO'ya kıyasla çok daha verimli kullanır. İşlem parçacıkları (threads) artık render, fizik (özellikle dinamik sis bombaları) ve ses işleme için optimize edilmiş şekilde dağıtılır. CS2'de ortalama FPS değerinden ziyade **%1 Low** ve **%0.1 Low** FPS değerleri oyun akıcılığını belirler. Bu değerlerin düşük olması, mikro takılmalara (stuttering) neden olur.

### Sub-Tick Sistemi ve Ağ Gecikmesi (Network Latency)
CS2, geleneksel 64 veya 128 tick rate yerine **Sub-Tick** mimarisini kullanır. Sunucu, girdilerinizi (input) milisaniyelik hassasiyetle kaydeder. Bu sistemin pürüzsüz çalışması, yerel sisteminizdeki kare sürelerinin (frametime) stabil olmasına doğrudan bağlıdır. Dalgalı bir FPS, sub-tick kaydında tutarsızlıklara yol açar.

---

## En İyi CS2 Grafik Ayarları (FPS ve Görünürlük Dengesi)

CS2'de grafik ayarlarını tamamen en düşüğe getirmek her zaman en yüksek performansı vermez. GPU kullanımını çok fazla düşürmek, yükü CPU'ya bindirerek darboğaza (bottleneck) neden olabilir.

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama & Performans Etkisi |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır (Boost Player Contrast)** | **Etkin (Enabled)** | Karakterlerin gölgelik alanlarda görünürlüğünü artırır. CPU'ya hafif yük bindirir ancak rekabetçi avantaj için zorunludur. |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı (Disabled)** | Giriş gecikmesini (input lag) ciddi oranda artırır. Kesinlikle kapatılmalıdır. |
| **Çoklu Örnekleme Kenar Yumuşatma Modu (MSAA)** | **4x MSAA** veya **2x MSAA** | CMAA2 performansı artırsa da piksellenmeye yol açar. MSAA, Source 2'de kenar titremelerini önlemek ve düşman piksellerini ayırt etmek için idealdir. |
| **Evrensel Gölge Kalitesi (Global Shadow Quality)** | **Yüksek (High)** | CS2'de gölgeler dinamiktir ve rakiplerin konumunu ele verir. "Düşük" ayar gölgeleri tamamen kapatabilir veya bozabilir. En az "Orta" veya "Yüksek" kullanılmalıdır. |
| **Model / Doku Detayı (Model / Texture Detail)** | **Düşük (Low)** veya **Orta (Medium)** | VRAM kapasitenize bağlıdır. 6GB ve üzeri VRAM için "Orta" ayar performansı etkilemez. |
| **Gölgelendirici Detayı (Shader Detail)** | **Düşük (Low)** | Işık yansımalarını ve materyal kalitesini belirler. GPU hesaplama (compute) yükünü azaltmak için düşükte tutulmalıdır. |
| **Parçacık Detayı (Particle Detail)** | **Düşük (Low)** | El bombası patlamaları ve sis efektlerinin yoğunluğunu belirler. Çatışma anında FPS düşüşlerini (drop) önlemek için en düşükte olmalıdır. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı (Disabled)** | Köşelerdeki gerçekçi gölgelendirmeleri yapar. Rekabetçi oyunda gereksizdir ve GPU'ya yüksek yük bindirir. |
| **Yüksek Dinamik Aralık (HDR)** | **Performans (Performance)** | Renk derinliğini optimize eder. "Kalite" modu özellikle eski GPU'larda kare hızını düşürür. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Disabled - En Yüksek Kalite)** | FSR, görüntüyü upscale ederek çamurlaştırır ve gecikmeye yol açar. Sadece çok düşük donanımlarda FPS kurtarmak için "Ultra Kalite" modunda açılabilir. |

### NVIDIA Reflex Düşük Gecikme (NVIDIA Reflex Low Latency)
*   **Önerilen:** **Etkin + Takviye (Enabled + Boost)**
*   **Teknik Detay:** "Enabled", CPU render kuyruğunu GPU ile senkronize ederek gecikmeyi azaltır. "+ Boost" seçeneği ise GPU çekirdek frekanslarının (clock speeds) CPU darboğazı anlarında bile maksimumda kalmasını sağlayarak gecikmeyi en aza indirir.

---

## Donanım Seviyesinde Optimizasyon ve İşletim Sistemi Ayarları

Yazılımsal optimizasyon, donanımınızın kararlı çalışmadığı senaryolarda yetersiz kalır. CS2 performans rehberi kapsamında işletim sistemi ve donanım seviyesinde yapılması gerekenler şunlardır:

### Windows Güç Planı ve Çekirdek Park Etme (Core Parking)
Windows varsayılan olarak enerji tasarrufu amacıyla CPU çekirdeklerini park edebilir (uyku moduna alabilir). Bu durum CS2 gibi anlık CPU gücü isteyen oyunlarda mikro takılmalara yol açar.

1.  **Nihai Performans (Ultimate Performance)** modunu aktif edin. (CMD'yi yönetici olarak açın ve şu kodu girin: `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`).
2.  **Oyun Modu (Game Mode):** Windows Ayarları > Oyun > Oyun Modu seçeneğini **Açık** konuma getirin. Bu, Windows arka plan işlemlerinin CPU önceliğini CS2'ye vermesini sağlar.

### RAM Frekansı ve XMP/EXPO Profilleri
Source 2 motoru, bellek gecikmesine (RAM latency) karşı son derece hassastır.
*   BIOS ekranına girerek **XMP (Intel)** veya **EXPO (AMD)** profilinin aktif olduğundan emin olun.
*   Belleklerinizin **Dual-Channel (Çift Kanal)** modunda çalıştığını CPU-Z gibi bir yazılımla doğrulayın. Tek kanal RAM kullanımı, CS2'de %1 Low FPS değerlerini yarı yarıya düşürebilir.

### Ekran Kartı Sürücü Ayarları (NVIDIA Denetim Masası)
*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık.
*   **Güç Yönetimi Modu (Power Management Mode):** Maksimum performansı tercih et (Prefer maximum performance).
*   **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** **Sınırsız (Unlimited)** veya **10GB**. (Source 2, shader derlemesini dinamik olarak yapar. Önbellek sınırını kaldırmak, harita yüklenirken ve ilk kez sis/bomba atıldığında oluşan takılmaları engeller).

---

## CS2 Başlatma Seçenekleri (Launch Options) ve Konsol Komutları

CS:GO'dan kalma birçok başlatma seçeneği (örneğin `-threads`, `-high`, `-nod3d9ex`) CS2'de kararsızlığa veya çökmelere neden olmaktadır. CS2 için optimize edilmiş güncel parametreler şunlardır:

### Doğrulanmış Başlatma Seçenekleri
Steam kütüphanenizden CS2'ye sağ tıklayıp Özellikler > Başlatma Seçenekleri kısmına aşağıdaki kodları ekleyin:

```text
-novid -nojoy -vulkan (Sadece AMD ekran kartlarında DX11'e kıyasla daha stabil FPS veriyorsa kullanılmalıdır, aksi takdirde silin)
```

*   `-novid`: Giriş videosunu atlar, oyunun daha hızlı açılmasını sağlar.
*   `-nojoy`: Denetleyici (joystick) desteğini kapatarak RAM ve CPU thread tüketimini azaltır.

### Performans Artıran Konsol Kodları (Autoexec.cfg)
Oyun içi konsolu (`~` tuşu) açarak veya bir `autoexec.cfg` dosyası oluşturarak aşağıdaki komutları uygulayın:

```clf
fps_max 0 // FPS sınırını kaldırır. Ancak sisteminiz çok ısınıyorsa monitör yenileme hızınızın (Hz) 2 katına sabitlemek (örn: fps_max 400) kare süresi kararlılığını artırır.
cl_updaterate 128 // Sunucu ile veri alışveriş sıklığını maksimuma çıkarır.
cl_interp_ratio 1 // Ağ interpolasyonunu optimize eder, mermilerin daha tutarlı gitmesini sağlar.
cl_interp 0.015625 // Düşük ping değerleri için ideal interpolasyon süresi.
```

---

## Sonuç ve Donanım Tavsiyeleri

CS2, GPU mimarisindeki yeniliklerden (özellikle mimari düzeyindeki gölgelendirici iyileştirmelerinden) yüksek oranda yararlanır. Eğer bu rehberdeki tüm adımlara rağmen hedeflediğiniz FPS değerlerine ulaşamıyorsanız, sisteminizde darboğaza neden olan bileşeni tespit etmelisiniz:

1.  **CPU Tercihi:** CS2 için tek çekirdek hızı ve L3 önbellek boyutu kritiktir. AMD'nin **3D V-Cache** teknolojisine sahip işlemcileri (örn: *Ryzen 7 7800X3D*), Source 2 motorunda en yüksek %1 Low FPS değerlerini sunmaktadır.
2.  **Depolama:** Oyunun mutlaka bir **NVMe M.2 SSD** üzerine kurulu olması gerekir. Yavaş HDD veya SATA SSD'ler, harita içi dinamik doku yüklemelerinde anlık takılmalara (stutter) yol açar.