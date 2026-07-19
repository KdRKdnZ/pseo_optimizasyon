---
title: valorant en iyi ayarlar
description: valorant en iyi ayarlar hakkında detaylı optimizasyon ve donanım rehberi.
---

# Valorant En İyi Ayarlar: FPS Artırma ve En Düşük Gecikme (Input Lag) Rehberi

Valorant, Unreal Engine 4 motoru üzerinde geliştirilmiş, CPU (İşlemci) bağımlı ve tick-rate hassasiyeti yüksek bir taktiksel nişancı oyunudur. Rekabetçi avantaj elde etmek, yalnızca yüksek kare hızına (FPS) ulaşmakla değil, aynı zamanda kare oluşturma sürelerini (frametimes) stabilize etmek ve giriş gecikmesini (input lag) en aza indirmekle mümkündür. 

Bu rehber; donanım mimarisi, yazılım optimizasyonu ve oyun içi motor parametreleri göz önünde bulundurularak hazırlanmış en optimize **Valorant en iyi ayarlar** listesini sunmaktadır.

---

## Donanım ve İşletim Sistemi Optimizasyonu

Oyun içi ayarlara geçmeden önce, Windows işletim sisteminin ve grafik kartı sürücülerinin donanım kaynaklarını doğrudan oyuna aktarmasını sağlamak gerekir.

### Windows Grafik Ayarları ve HAGS
Windows 10 ve 11 ile gelen Donanım Hızlandırmalı GPU Zamanlaması (HAGS), GPU belleğini yönetme görevini CPU'dan alarak doğrudan GPU'ya verir.
*   **Arama çubuğuna** "Grafik Ayarları" yazın.
*   **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** konuma getirin.
*   Aşağıdaki listeden "Valorant"ı seçip (yoksa `VALORANT-Win64-Shipping.exe` dosyasını göz at seçeneğiyle ekleyin) **Seçenekler** kısmından **Yüksek Performans** olarak ayarlayın.

### NVIDIA Denetim Masası Ayarları
NVIDIA grafik işlemcilerinde sürücü seviyesinde gecikmeyi azaltmak için aşağıdaki parametreleri uygulayın:
*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra (CPU'nun kareleri önceden hazırlamasını engelleyerek doğrudan GPU'ya gönderir).
*   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et (GPU çekirdek saat hızlarının dalgalanmasını önler).
*   **Doku Süzme - Kalite:** Yüksek Performans.
*   **Dikey Senkronizasyon (V-Sync):** Kapalı.

---

## Valorant En İyi Grafik Ayarları (Video Settings)

Valorant'ta grafik kalitesini düşürmek, sadece FPS'i artırmakla kalmaz; ekrandaki görsel gürültüyü (visual clutter) azaltarak rakipleri daha hızlı tespit etmenizi sağlar.

### Genel Grafik Ayarları

| Ayar | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | Windows Masaüstü Pencere Yöneticisi'ni (DWM) devre dışı bırakarak en düşük giriş gecikmesini sağlar. |
| **Çözünürlük** | Monitörün Doğal Çözünürlüğü (Örn: 1920x1080 240Hz) | Piksel eşleşmesi sağlayarak gecikmeyi önler ve netliği maksimuma çıkarır. |
| **En Boy Oranı Yöntemi** | Doldur (Fill) | Görüş açısını (FOV) bozmadan ekranı kaplar. |
| **Pil Gücünde FPS'yi Sınırla** | Kapalı | Performans dalgalanmalarını önler. |
| **Menüde FPS'yi Sınırla** | Açık (60 FPS) | Menüdeyken GPU'nun gereksiz yere ısınmasını engeller. |
| **Arka Planda FPS'yi Sınırla** | Açık (30 FPS) | Alt-Tab durumunda sistem kaynaklarını serbest bırakır. |
| **Her Zaman FPS'yi Sınırla** | Kapalı | Monitör yenileme hızının (Hz) üzerindeki FPS değerleri, giriş gecikmesini daha da düşürür. |

### Grafik Kalitesi (Graphics Quality)

```
[Çoklu Çekirdek Oluşturma] ---> AÇIK (Modern CPU'lar için zorunlu)
[Materyal / Doku Kalitesi] ---> DÜŞÜK (VRAM darboğazını önler)
[Ayrıntı / Arayüz Kalitesi] -> DÜŞÜK (Görsel gürültüyü azaltır)
[Vignette / V-Sync] ---------> KAPALI (Gecikmeyi ve kenar kararmasını önler)
```

*   **Çoklu Çekirdek Oluşturma (Multithreaded Rendering):** **Açık.** Valorant, CPU tabanlı bir oyundur. Bu ayar, oyun motorunun iş yükünü işlemcinizin mantıksal çekirdeklerine (threads) dağıtır. FPS'i doğrudan %20 ila %40 oranında artırır.
*   **Materyal Kalitesi:** **Düşük.** Yüksek ayarlar, silahlardaki ve haritadaki yansımaları artırarak GPU bütçesini tüketir.
*   **Doku Kalitesi:** **Düşük.** VRAM kullanımını minimumda tutarak kare geçiş sürelerini (frametimes) stabilize eder.
*   **Ayrıntı Kalitesi:** **Düşük.** Haritadaki gereksiz çim, yaprak ve küçük nesneleri kaldırarak görüşü netleştirir.
*   **Arayüz Kalitesi:** **Düşük.** HUD elemanlarının render maliyetini düşürür.
*   **Vignette:** **Kapalı.** Ekranın köşelerinde oluşan karanlık gölgeleri kaldırarak görüş açısını artırır.
*   **Dikey Senkronizasyon (V-Sync):** **Kapalı.** Monitör yırtılmalarını önlese de sisteme ciddi oranda giriş gecikmesi (input lag) ekler.
*   **Kenar Yumuşatma (Anti-Aliasing):** **MSAA 2x** veya **Hiçbiri**. MSAA, FXAA'ya göre daha keskin kenarlar sunar ve rakiplerin piksellerini ayırt etmeyi kolaylaştırır. Performans kaybı yaşanıyorsa tamamen kapatılmalıdır.
*   **Eşyönsüz Süzme (Anisotropic Filtering):** **2x** veya **4x**. Eğik açılardaki dokuların netliğini ayarlar. Performansa etkisi minimaldir, ancak en kararlı frametime için düşük tutulmalıdır.
*   **Netliği Artır (Improve Clarity):** **Kapalı.** Orta tonlardaki kontrastı artırır ancak CPU'ya ek yük bindirir.
*   **Deneysel Keskinleştirme (Experimental Sharpening):** **Kapalı.** Post-processing (sonradan işleme) filtresidir, gecikmeyi artırabilir.
*   **Bloom (Işık Patlaması):** **Kapalı.** Yeteneklerin (örn. Sage duvarı, Brimstone ultisi) yaydığı ışığı artırarak görüşü engeller.
*   **Bozulma (Distortion):** **Kapalı.** Patlamaların arkasındaki havayı bükerek hedef almayı zorlaştırır.
*   **Birinci Şahıs Gölgeler:** **Kapalı.** Sadece kendi karakterinizin gölgesini kapatır, rakiplerin gölgelerini etkilemez. Performans için kapatılmalıdır.

---

## Gecikmeyi Sıfırlayan NVIDIA Reflex Teknolojisi

NVIDIA Reflex, CPU ve GPU arasındaki iş hattını (render queue) dinamik olarak senkronize eder.

*   **NVIDIA Reflex Düşük Gecikme:** **Açık + Takviye (On + Boost).**
    *   *Teknik Açıklama:* "Açık" konumu gecikmeyi doğrudan azaltır. "+ Takviye" (Boost) ise GPU'nun saat hızlarını (core clocks) her zaman maksimumda tutarak, CPU darboğazı yaşanan anlarda bile ekran kartının uyku moduna geçmesini engeller.

---

## En İyi Valorant Mouse ve Hassasiyet (Sensitivity) Ayarları

Valorant gibi mikro-düzeltmelerin (micro-adjustments) kritik olduğu oyunlarda, mouse veri iletim hızı ve hassasiyeti hayati önem taşır.

### Ham Girdi Arabelleği (Raw Input Buffer)
*   **Ayar:** **Açık.**
*   **Teknik Gerekçe:** Windows'un kendi mouse ivmelendirme ve işleme algoritmalarını (APIs) tamamen devre dışı bırakarak, mouse sensöründen gelen verileri doğrudan oyun motoruna aktarır. Özellikle 1000Hz ve üzeri (2000Hz, 4000Hz, 8000Hz) tarama hızına (polling rate) sahip mouse'larda gecikmeyi milisaniyeler düzeyinde düşürür.

### DPI ve eDPI Dengesi
Profesyonel Valorant oyuncularının büyük çoğunluğu **200 ila 400 eDPI** aralığını kullanır. eDPI (Effective DPI), fiziksel hassasiyetinizin gerçek karşılığıdır.

$$\text{eDPI} = \text{Mouse DPI} \times \text{Oyun İçi Hassasiyet (Sensitivity)}$$

*   **Örnek Hesaplama:** 800 DPI ve 0.35 oyun içi hassasiyet kullanan bir oyuncunun eDPI değeri: $800 \times 0.35 = 280$'dir.
*   **Öneri:** Piksel atlamalarını (pixel skipping) önlemek için mouse donanımınızı **800 DPI** veya **1600 DPI** değerine ayarlayın ve oyun içi hassasiyetinizi buna göre düşürün.

---

## Ağ (Network) ve Ses Ayarları

### Ağ Arabelleğe Alma (Network Buffering)
*   **Ayar:** **Asgari (Minimum).**
*   **Teknik Gerekçe:** Bu ayar, sunucudan gelen paketlerin bilgisayarınızda ne kadar süreyle depolanıp işleneceğini belirler. "Asgari" ayarı, paketleri doğrudan işleyerek rakipleri sunucuda bulundukları en güncel konumda görmenizi sağlar. Sadece internet bağlantınızda aşırı paket kaybı (packet loss) varsa "Orta" konumuna getirilmelidir.

### HRTF (Head-Related Transfer Function)
*   **Ayar:** **Açık (Stereo kulaklıklar ile).**
*   **Teknik Gerekçe:** HRTF, insan kulağının ses dalgalarını algılama biçimini simüle eden 3 boyutlu bir ses algoritmasıdır. Rakiplerin ayak seslerinin sadece sağda veya solda değil; yukarıda, aşağıda, önünüzde veya arkanızda olduğunu milimetrik olarak tespit etmenizi sağlar. Bu ayarın aktif çalışabilmesi için Windows ses ayarlarından "Uzamsal Ses" (Spatial Sound) kapatılmalı ve kulaklık yazılımlarındaki sanal 7.1 özellikleri devre dışı bırakılmalıdır.