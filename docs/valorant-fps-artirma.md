---
title: valorant fps artırma
description: valorant fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Valorant FPS Artırma Rehberi: Donanım ve Yazılım Optimizasyonu

Valorant, Riot Games tarafından geliştirilen ve Unreal Engine 4 (UE4) motorunu kullanan, rekabetçi bir taktiksel nişancı oyunudur. Espor odaklı yapısı gereği, oyundaki milisaniyelik gecikmeler (input lag) ve anlık kare hızı (FPS) düşüşleri doğrudan performansınızı etkiler. 

Bu rehber, donanım mimarisi ve yazılım optimizasyonu prensiplerine dayanarak, sisteminizden maksimum kararlılıkta ve en yüksek değerde FPS almanızı sağlayacak bilimsel yöntemleri sunmaktadır.

---

## Valorant Oyun Motoru (Unreal Engine 4) ve CPU/GPU İlişkisi

Valorant, grafik işlemciden (GPU) ziyade merkezi işlemciye (CPU) bağımlı (**CPU-bound**) bir oyundur. Oyun motoru mimarisi, oyun içi fizik hesaplamalarını, oyuncu konumlarını, mermi yollarını (hitreg) ve kullanıcı arayüzünü (UI) ana iş parçacığı (**Game Thread**) üzerinde işler. Grafiksel hesaplamalar ise **Render Thread** üzerinden GPU'ya aktarılır.

Sisteminizde RTX 4090 gibi üst düzey bir ekran kartı olsa dahi, işlemcinizin tek çekirdek performansı (Single-Thread Performance) düşükse "darboğaz" (bottleneck) yaşarsınız. Bu nedenle **valorant fps artırma** sürecinde öncelikli hedefimiz CPU üzerindeki yükü hafifletmek ve bellek (RAM) gecikmesini minimuma indirmektir.

---

## Windows ve İşletim Sistemi Seviyesinde Optimizasyonlar

İşletim sisteminin arka plan servisleri, CPU döngülerini tüketerek oyunun ihtiyaç duyduğu kaynakları bloke edebilir. Aşağıdaki adımlar, Windows çekirdeğinin (kernel) önceliği Valorant'a vermesini sağlar.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) ve Oyun Modu

Windows 10 ve 11 ile gelen HAGS (Hardware-Accelerated GPU Scheduling), yüksek öncelikli grafik görevlerini doğrudan GPU'nun kendi özel zamanlama işlemcisine devreder. Bu, CPU üzerindeki yükü azaltır.

1. Windows Arama çubuğuna **Grafik Ayarları** yazın.
2. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini aktif hale getirin.
3. **Oyun Modu** ayarını aratın ve bu özelliği "Açık" konumuna getirin. Oyun Modu, arka plan güncellemelerini ve sürücü bildirimlerini askıya alarak CPU kaynaklarını oyuna tahsis eder.

### Güç Planı ve CPU Çekirdek Park Etme (Core Parking) Ayarları

Windows, enerji tasarrufu sağlamak amacıyla aktif olmayan CPU çekirdeklerini "uyku" (park) moduna alır. Bir çekirdeğin uykudan uyanması milisaniyeler sürer ve bu durum oyunda anlık takılmalara (stuttering) yol açar.

* **Nihai Performans (Ultimate Performance) Modunu Aktif Etme:**
  Komut İstemi'ni (CMD) yönetici olarak çalıştırın ve aşağıdaki kodu yapıştırıp Enter'a basın:
  ```bash
  powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
  ```
  Ardından Denetim Masası > Güç Seçenekleri bölümünden yeni oluşan **Nihai Performans** planını seçin. Bu işlem, CPU'nun sürekli olarak maksimum temel frekansta çalışmasını sağlar.

---

## Ekran Kartı (GPU) Sürücü Optimizasyonları

Ekran kartı sürücülerinin 3D ayarları, kare işleme kuyruğunu doğrudan etkiler. Doğru yapılandırılmamış bir sürücü, gereksiz kenar yumuşatma (Anti-Aliasing) ve doku filtreleme işlemleriyle GPU'yu yorar.

### NVIDIA Denetim Masası Ayarları

NVIDIA GPU kullanıcıları için en düşük gecikme ve en yüksek kararlılık sağlayan profil ayarları şunlardır:

* **Bağlantılı Optimizasyon (Threaded Optimization):** Açık (Unreal Engine'in çoklu çekirdek desteğini optimize eder).
* **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık (Kare kuyruğunu sıfırlayarak girdi gecikmesini minimuma indirir).
* **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
* **Doku Süzme - Kalite:** Yüksek Performans.
* **Dikey Senkronizasyon (V-Sync):** Kapalı (Girdi gecikmesini önlemek için kesinlikle kapatılmalıdır).

### AMD Radeon Software Ayarları

AMD kullanıcıları için performans odaklı sürücü yapılandırması:

* **Radeon Anti-Lag:** Etkin (Girdi gecikmesini azaltır).
* **Radeon Boost:** Devre Dışı (Çözünürlüğü dinamik değiştirdiği için rekabetçi oyunlarda tutarsızlığa yol açar).
* **Doku Filtreleme Kalitesi:** Performans.
* **Mozaikleme Modu (Tessellation):** Uygulama ayarlarını geçersiz kıl / Kapat.

---

## Valorant Oyun İçi Grafik ve Ağ Ayarları

Oyun içi ayarların doğru yapılandırılması, hem görsel netliği korur hem de işlemci üzerindeki çizim çağrısı (draw call) yükünü azaltır.

### FPS Değerini Doğrudan Etkileyen Grafik Ayarları

Valorant'ı başlatın ve Ayarlar > Görüntü > Grafik Kalitesi adımlarını takip edin:

| Ayar | Önerilen Değer | Teknik Gerekçesi |
| :--- | :--- | :--- |
| **Çoklu İzlek Oluşturma (Multithreaded Rendering)** | **AÇIK** | CPU'nun birden fazla çekirdeğini render işlemi için kullanır. FPS'i en çok artıran ayardır (Sadece 4 çekirdek ve üzeri CPU'larda görünür). |
| **Malzeme Kalitesi** | Düşük | GPU üzerindeki shader (gölgelendirici) yükünü azaltır. |
| **Doku Kalitesi** | Düşük / Orta | VRAM (Ekran kartı belleği) kullanımını optimize eder. |
| **Detay Kalitesi** | Düşük | Haritadaki gereksiz çim, taş gibi statik objeleri kaldırarak CPU çizim yükünü düşürür. |
| **Arayüz Kalitesi** | Düşük | UI render süresini kısaltır. |
| **Kenar Yumuşatma (Anti-Aliasing)** | MSAA 2x veya Yok | MSAA, kenarları yumuşatırken GPU'ya ağır yük bindirir. Performans için "Yok" veya "FXAA" seçilmelidir. |
| **Eşyönsüz Filtreleme (Anisotropic Filtering)** | 1x | Dokuların açılı görünüm netliğini ayarlar; performansa etkisi düşüktür ancak kararlılık için 1x önerilir. |
| **NVIDIA Reflex Düşük Gecikme** | **Açık + Takviye (On + Boost)** | GPU'nun saat hızlarını maksimumda tutarak CPU-GPU arasındaki senkronizasyon gecikmesini sıfıra yakınsar. |

### Ağ Arabelleği (Network Buffering) ve Girdi Gecikmesi

Ayarlar > Genel sekmesinde yer alan **Ağ Arabelleği** ayarı, paket kaybı yaşadığınız durumlarda oyunun akıcılığunu etkiler.
* **Önerilen:** **Asgari (Minimum)**. 
* *Gerekçe:* Bu ayar "Orta" veya "Azami" yapıldığında, sunucudan gelen veriler tampon belleğe alınır. Bu durum oyunun takılmasını önleyebilir ancak **girdi gecikmesini (input lag) artırır**. Kararlı bir internet bağlantınız varsa her zaman "Asgari" kullanılmalıdır.

---

## Donanım Seviyesinde İleri Düzey Müdahaleler

Yazılımsal optimizasyonlar bir noktaya kadar etki eder. Gerçek anlamda sürdürülebilir yüksek FPS için donanım bileşenlerinin çalışma frekansları ve sıcaklık değerleri optimize edilmelidir.

### RAM Frekansı (XMP/DOCP) ve Dual-Channel Etkisi

Valorant, bellek gecikmesine (RAM Latency) son derece duyarlıdır. Tek kanal (Single-Channel) RAM kullanımı, CPU'nun veri işleme hızını yarı yarıya düşürerek Valorant'ta ciddi FPS droplarına neden olur.

1. **Dual-Channel Kullanımı:** Sisteminizde mutlaka çift kanal (örneğin 2x8 GB) RAM bulunmalıdır. Bu, bellek bant genişliğini 64-bit'ten 128-bit'e çıkarır.
2. **XMP/DOCP Aktifleştirme:** RAM'leriniz varsayılan olarak 2133 MHz hızında çalışabilir. BIOS ekranına girerek (Açılışta F2 veya DEL tuşu ile) **XMP** (Intel) veya **DOCP** (AMD) profilini aktif hale getirin. Bu işlem, RAM'lerinizin vaat edilen yüksek frekanslara (örn. 3200 MHz, 3600 MHz) çıkmasını sağlayarak minimum FPS (1% ve 0.1% Low FPS) değerlerinizi %20 ila %35 oranında artıracaktır.

### Termal Darboğaz (Thermal Throttling) ve Çözümleri

İşlemci veya ekran kartı belirli bir sıcaklık limitine (genellikle CPU için 90°C, GPU için 83°C) ulaştığında, donanımı korumak adına çalışma frekanslarını (Clock Speed) düşürür. Bu duruma **Thermal Throttling** denir ve oyunda ani FPS düşüşlerinin en yaygın sebebidir.

* **Çözüm Yolları:**
  * İşlemci termal macununu (en azından yılda bir kez) yüksek ısı iletkenliğine sahip (örn. Arctic MX-4 veya Thermal Grizzly Kryonaut) bir macunla yenileyin.
  * Kasa içi hava sirkülasyonunu optimize edin; taze hava giriş (Intake) ve sıcak hava çıkış (Exhaust) fanlarının doğru konumlandırıldığından emin olun.
  * Dizüstü bilgisayar kullanıcıları için, cihazın altını yükseltmek veya kaliteli bir vakumlu soğutucu kullanmak sıcaklıkları 5-10°C düşürerek stabil frekans değerleri sağlayacaktır.