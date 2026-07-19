---
title: elden ring fps artırma
description: elden ring fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Elden Ring FPS Artırma Rehberi: Donanım ve Yazılım Optimizasyonu

FromSoftware tarafından geliştirilen Elden Ring, tescilli bir oyun motoru (proprietary engine) kullanır ve DirectX 12 API'si üzerine inşa edilmiştir. Bu mimari, görsel kaliteyi artırırken özellikle CPU-GPU arasındaki veri iletişiminde (draw calls) ve shader derleme (shader compilation) süreçlerinde ciddi darboğazlara yol açabilir. 

Bu rehber, Elden Ring'deki FPS düşüşlerini (FPS drop) ve kasma sorunlarını gidermek için donanım, işletim sistemi ve oyun içi motor seviyesinde uygulayabileceğiniz, teknik olarak kanıtlanmış optimizasyon yöntemlerini içermektedir.

---

## Elden Ring Performans Sorunlarının Teknik Nedenleri

Elden Ring'de yaşanan performans sorunlarının temelinde yazılımsal ve mimari kararlar yatar. Bu nedenleri anlamak, uygulayacağımız çözümlerin mantığını kavramaya yardımcı olur.

### DirectX 12 ve Shader Derleme Gecikmeleri (Stuttering)
DirectX 12, donanıma daha düşük seviyeli (low-level) erişim sağlar ancak shader derleme yönetimini oyun motoruna bırakır. Elden Ring, yeni bir bölgeye girdiğinizde veya yeni bir efekt tetiklendiğinde shader'ları gerçek zamanlı olarak derler. Bu durum, anlık CPU yükünü %100'e ulaştırarak milisaniyelik takılmalara (micro-stuttering) neden olur.

### CPU Darboğazı ve İş Parçacığı (Thread) Dağılımı
Oyun motoru, fizik hesaplamalarını ve yapay zeka işlemlerini ana iş parçacığı (render thread) üzerinde yoğunlaştırır. Çok çekirdekli modern işlemcilerde bile tek çekirdek performansının yetersiz kalması, GPU'nun tam kapasiteyle çalışmasını engeller ve FPS'i düşürür.

---

## En İyi Elden Ring Grafik Ayarları (FPS ve Görsel Denge)

Oyun içi grafik ayarlarını optimize etmek, görsel kaliteden minimum ödün vererek en yüksek performans kazancını sağlar. Aşağıdaki tablo, her ayarın performans ve görsel kalite üzerindeki etkisini göstermektedir:

| Grafik Ayarı | Önerilen Değer | Performans Etkisi | Teknik Açıklama |
| :--- | :--- | :--- | :--- |
| **Ray Tracing Quality** | Off (Kapalı) | Çok Yüksek (%20-30) | Donanımsal ışın izleme, BVH hesaplamaları nedeniyle GPU'yu aşırı yorar. Kesinlikle kapatılmalıdır. |
| **Texture Quality** | Medium / High | Düşük (VRAM sınırına bağlı) | VRAM kapasiteniz 6 GB ve altındaysa Medium, 8 GB ve üzerindeyse High seçin. |
| **Antialiasing Quality** | High | Orta (%3-5) | Kenar yumuşatma kapatıldığında görsel kırılmalar çok belirginleşir. High idealdir. |
| **SSAO** | Medium | Orta (%5-8) | Ortam kapatma, gölgelerin derinliğini belirler. High yerine Medium performansı dengeler. |
| **Shadow Quality** | Medium | Yüksek (%10-12) | Gölgelerin çözünürlüğünü belirler. Max/High değerleri CPU ve GPU'ya aşırı yük bindirir. |
| **Volumetric Effect Quality** | Medium | Yüksek (%8-10) | Sis ve ışık süzmesi efektleridir. Savaş esnasında FPS düşüşlerini önlemek için Medium yapılmalıdır. |
| **Global Illumination Quality** | Medium | Düşük (%2-3) | Genel aydınlatma kalitesidir. Performansa etkisi düşüktür. |
| **Grass Quality** | Medium | Orta (%5-7) | Açık dünyadaki çim yoğunluğunu belirler. Limgrave bölgesindeki FPS düşüşlerini azaltır. |

---

## İşletim Sistemi ve Sürücü Düzeyinde Optimizasyonlar

Elden Ring'in işletim sistemi kaynaklarını daha verimli kullanmasını sağlamak için Windows ve ekran kartı sürücülerinde yapılması gereken kritik ayarlar şunlardır:

### Windows Grafik Ayarları ve Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS (Hardware-Accelerated GPU Scheduling), bellek yönetimini doğrudan GPU'ya devrederek CPU gecikmesini azaltır.

1. Windows arama çubuğuna **Grafik Ayarları** yazın ve açın.
2. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini aktif hale getirin.
3. "Grafik performansı tercihi" bölümünden **Göz At** butonuna tıklayarak `eldenring.exe` dosyasını seçin (Genellikle `Steam\steamapps\common\ELDEN RING\Game` dizinindedir).
4. Seçilen oyunun üzerine tıklayıp **Seçenekler**'i açın ve **Yüksek Performans** olarak ayarlayın.

### NVIDIA ve AMD Kontrol Paneli İnce Ayarları
Ekran kartı sürücüsü seviyesinde yapılacak optimizasyonlar, shader derleme sorunlarını doğrudan hedefler.

#### NVIDIA Kullanıcıları İçin:
* **NVIDIA Denetim Masası** > **3D Ayarlarının Yönetilmesi** > **Program Ayarları** sekmesine gelin ve Elden Ring'i seçin.
* **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** **Sınırsız (Unlimited)** veya **10 GB** yapın. Bu ayar, shader'ların diske yazılmasını sağlayarak oyun içi takılmaları (stutter) büyük oranda engeller.
* **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et** olarak ayarlayın.
* **Dikey Senkronizasyon (V-Sync):** **Hızlı (Fast)** veya **Açık** yapın (Oyun içi V-Sync'i devre dışı bırakmak için).

#### AMD Kullanıcıları İçin:
* **AMD Software** > **Oyunlar** > **Elden Ring** profilini açın.
* **Radeon Anti-Lag:** **Etkin** (Giriş gecikmesini azaltır).
* **Radeon Image Sharpening:** **Etkin (%50-70)** (Görsel netliği artırır).
* **Shader Cache:** Sıfırlayın ve sürücü seviyesinde açık tutun.

### Microsoft Exploit Protection Ayarı (Önemli Çözüm)
Elden Ring'in DX12 API çağrılarında Windows güvenlik denetimlerinin yarattığı gecikmeyi engellemek için bu yöntemi uygulayın:

1. Windows arama çubuğuna **Exploit Protection** yazın.
2. **Program ayarları** sekmesine geçin ve **Özelleştirmek için program ekle** seçeneğinden `eldenring.exe` dosyasını ekleyin.
3. Listeden oyunu seçip **Düzenle** deyin.
4. **Denetim akışı koruması (CFG)** ayarını bulun, **Sistem ayarlarını geçersiz kıl** kutucuğunu işaretleyin ve ayarı **Kapalı** konuma getirin. Uygula deyip bilgisayarı yeniden başlatın.

---

## İleri Düzey ve Mod Tabanlı FPS Artırma Yöntemleri

*Not: Bu bölümde yer alan üçüncü taraf yazılımlar ve modlar Easy Anti-Cheat (EAC) sistemini tetikleyebilir. Çevrimiçi (Online) modda oynamak istiyorsanız bu adımları uygulamayınız.*

### Elden Ring 60 FPS Kilidini Kaldırma (Flawless Widescreen)
Elden Ring, varsayılan olarak 60 FPS sınırına sahiptir. Güçlü bir donanıma sahipseniz bu sınırı kaldırmak için **Flawless Widescreen** programını kullanabilirsiniz.

1. Flawless Widescreen yazılımını indirin ve kurun.
2. Sol menüden **Elden Ring** eklentisini bulun ve yükleyin.
3. **Framerate Limit** seçeneğini ekran kartınızın yenileme hızına (Hz) göre ayarlayın.
4. Oyunu başlatmadan önce anti-cheat sistemini devre dışı bırakmanız gerekir.

### Easy Anti-Cheat (EAC) Devre Dışı Bırakma
EAC, arka planda sürekli olarak bellek taraması yaptığı için ciddi bir CPU yükü oluşturur. Çevrimdışı (Offline) modda oynamak kaydıyla EAC'yi kapatmak FPS kararlılığını artırır.

1. Steam kütüphanenizde Elden Ring'e sağ tıklayıp **Yerel Dosyalara Göz At** deyin.
2. `Game` klasörünün içindeki `start_protected_game.exe` dosyasının adını `start_protected_game_original.exe` olarak değiştirin.
3. `eldenring.exe` dosyasının bir kopyasını oluşturun ve bu kopyanın adını `start_protected_game.exe` yapın.
4. Oyunu Steam üzerinden başlattığınızda oyun doğrudan çevrimdışı modda ve EAC kapalı olarak açılacaktır.

---

## Donanım Tarafında Yapılması Gerekenler

Yazılımsal çözümlerin yanı sıra, donanım mimarinizin Elden Ring'in veri akış hızına yetişebilmesi gerekir.

### RAM Frekansı ve Dual-Channel Etkisi
Elden Ring, açık dünya verilerini sürekli olarak RAM ve VRAM arasında taşır. 
* **Dual-Channel (Çift Kanal):** Tek modül (Single-Channel) 16 GB RAM yerine, 2x8 GB Dual-Channel RAM kullanımı, bellek bant genişliğini iki katına çıkararak FPS drop sorunlarını %15 ila %20 oranında azaltır.
* **XMP/EXPO:** BIOS üzerinden XMP (Intel) veya EXPO (AMD) profillerinin açık olduğundan ve RAM'lerinizin vaat edilen maksimum frekansta (örn. 3200 MHz veya 6000 MHz) çalıştığından emin olun.

### SSD Kullanımı ve Sayfa Dosyası (Pagefile) Yapılandırması
Elden Ring, mekanik sabit disklerde (HDD) doku yükleme (texture streaming) gecikmeleri nedeniyle anlık donmalara yol açar. Oyunun kesinlikle bir **NVMe SSD** üzerine kurulu olması gerekir.

Ayrıca, Windows Sanal Bellek (Pagefile) ayarının SSD üzerinde ve sistem tarafından yönetilen boyutta olması, RAM yetersizliğinden kaynaklanan çökmeleri (Crash to Desktop) önler.