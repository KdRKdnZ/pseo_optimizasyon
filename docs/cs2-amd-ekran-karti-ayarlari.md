---
title: cs2 amd ekran kartı ayarları
description: cs2 amd ekran kartı ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 AMD Ekran Kartı Ayarları: Maksimum FPS ve En Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği fiziksel tabanlı ışıklandırma ve gelişmiş gölge sistemleri nedeniyle önceki sürüme kıyasla GPU (Grafik İşlem Birimi) kaynaklarını çok daha yoğun şekilde tüketir. AMD Radeon kullanıcıları için doğru sürücü ve oyun içi konfigürasyon, milisaniyelik gecikmeleri (input lag) önlemek ve stabil bir kare hızı (FPS) elde etmek için kritiktir. 

Bu rehberde, donanım mimarisi seviyesinde optimize edilmiş en güncel **CS2 AMD ekran kartı ayarları** adım adım analiz edilmiştir.

---

## AMD Software: Adrenalin Edition Global Ayarları

Sürücü seviyesinde yapılan optimizasyonlar, oyun içi ayarların temelini oluşturur. AMD Adrenalin yazılımında CS2 için özel bir profil oluşturarak işe başlayın.

### Ekran Kartı Profili ve Gecikme Önleme (Anti-Lag)

*   **Radeon Anti-Lag:** **Etkin**. Anti-Lag, CPU'nun GPU'dan çok fazla öne geçmesini engelleyerek kare kuyruğunu (frame queueing) minimize eder. Bu, özellikle GPU sınırına takıldığınız anlarda giriş gecikmesini (input lag) %30'a varan oranda düşürür. *(Not: Anti-Lag+ özelliğini, Valve'ın VAC sistemiyle uyumluluk sorunları tamamen çözülene kadar kapalı tutun; standart Anti-Lag güvenlidir).*
*   **Radeon Boost:** **Devre Dışı**. Bu özellik dinamik çözünürlük ölçeklemesi yapar. Fareyi hızlı çevirdiğinizde çözünürlüğü düşürerek FPS artırır ancak rekabetçi oyunlarda kas hafızasını ve piksel hassasiyetini olumsuz etkiler.
*   **Radeon Chill:** **Devre Dışı**. FPS'i sınırlayarak güç tasarrufu sağlar ancak kare sürelerinde (frametime) dalgalanmaya yol açar. Rekabetçi oyunlarda kesinlikle kapatılmalıdır.
*   **Gelişmiş Senkronizasyon (Enhanced Sync):** **Devre Dışı**. V-Sync türevi bu teknoloji ek gecikmeye neden olur.

### Görüntü Keskinleştirme ve Ölçeklendirme (RIS & RSR)

*   **Radeon Image Sharpening (Radeon Görüntü Keskinleştirme):** **Etkin (%30 - %50 arası)**. Source 2'nin MSAA ve TAA kenar yumuşatma yöntemleri görüntüyü hafifçe bulandırabilir. RIS, performans kaybı yaşatmadan (0.1 ms'den az etkiyle) pikselleri keskinleştirerek düşmanların uzak mesafeden daha net seçilmesini sağlar.
*   **Radeon Super Resolution (RSR):** **Devre Dışı**. Sürücü tabanlı bu ölçeklendirme yerine, oyun içi yerel çözünürlüğü veya oyun içi FSR ayarını kullanmak çok daha kararlı sonuçlar verir.

### Gelişmiş Grafik ve Doku Filtreleme Ayarları

*   **Örtüşme Önleme (Anti-Aliasing):** **Uygulama ayarlarını geçersiz kıl**.
*   **Örtüşme Önleme Yöntemi:** **Çoklu Örnekleme (Multisampling)**.
*   **Yüzey Biçimi Optimizasyonu:** **Etkin**. Sürücünün doku formatlarını daha hızlı işlemesini sağlar, performansı artırır.
*   **Doku Filtreleme Kalitesi:** **Performans**. Yüksek kaliteli dokular CS2 gibi rekabetçi bir oyunda gereksiz GPU yükü yaratır. "Performans" modu, görsel kaliteden ödün vermeden bant genişliğini optimize eder.
*   **Mozaikleme Modu (Tessellation):** **Uygulama ayarlarını geçersiz kıl** ve **Maksimum Mozaikleme Seviyesi'ni "Kapalı" veya "2x"** yapın. Source 2 haritalarındaki gereksiz geometri yükünü azaltır.

---

## CS2 Oyun İçi Grafik Ayarları ile Senkronizasyon

Sürücü ayarlarının tam performans gösterebilmesi için oyun içi grafik motorunun da bu parametrelerle senkronize çalışması gerekir.

### Performans Odaklı Video Ayarları

*   **Görüntü Modu:** **Tam Ekran (Fullscreen)**. Pencereli modlar Windows Masaüstü Pencere Yöneticisi'ni (DWM) araya sokarak gecikmeyi artırır.
*   **Yenileme Hızı:** Monitörünüzün desteklediği en yüksek değer (Örn: 144Hz, 240Hz, 360Hz).

### Gelişmiş Görüntü Ayarları

*   **Oyuncu Kontrastını Artır:** **Etkin**. Gölgelik alanlardaki düşman modellerinin arkasındaki kontrastı artırarak reaksiyon sürenizi kısaltır. Performans etkisi ihmal edilebilir düzeydedir.
*   **Dikey Eşitleme (V-Sync):** **Devre Dışı**. Ciddi oranda giriş gecikmesi yaratır.
*   **Çoklu Örnekleme Kenar Yumuşatma Modu (MSAA):** **2x MSAA** veya **4x MSAA**. Source 2'de MSAA'yı tamamen kapatmak piksellerde aşırı titremeye (shimmering) neden olur ve dikkatinizi dağıtır. 2x MSAA, performans ve netlik arasındaki en iyi dengedir.
*   **Global Gölge Kalitesi:** **Yüksek (High)** veya **Orta (Medium)**. Gölgeler, düşmanların konumunu önceden görmenizi sağlayan kritik taktiksel verilerdir. "Düşük" ayar dinamik gölgeleri devre dışı bırakabileceği için en az "Orta" veya "Yüksek" seçilmelidir.
*   **Model / Doku Detayı:** **Düşük (Low)**.
*   **Shader Detayı:** **Düşük (Low)**. Işık yansımalarını azaltarak dikkatinizin dağılmasını önler ve FPS'i artırır.
*   **Parçacık Detayı:** **Düşük (Low)**. El bombası ve molotof patlamalarındaki FPS düşüşlerini engeller.
*   **Ortam Kapatma (Ambient Occlusion):** **Devre Dışı (Disabled)**. Derinlik gölgelendirmesidir, rekabetçi avantaj sağlamaz ve GPU'ya yük bindirir.
*   **Yüksek Dinamik Aralık (HDR):** **Performans (Performance)**.
*   **FidelityFX Super Resolution (FSR):** **Devre Dışı (En Yüksek Kalite)**. FSR, görüntüyü upscale ederken rekabetçi oyunlarda kabul edilemeyecek bir bulanıklık ve pikselleşme yaratır. Yalnızca çok düşük donanımlarda FPS kurtarmak için "Kalite" modunda kullanılabilir.

---

## Donanım ve Yazılım Seviyesinde Optimizasyon Sırları

Bir yazılım mimarı ve donanım uzmanı gözüyle, CS2'deki AMD performansını donanımsal darboğazları çözerek optimize etmenin yolları şunlardır:

### Resizable BAR (SmartAccess Memory) Aktivasyonu

AMD işlemci (Ryzen) ve AMD ekran kartı (Radeon) kombinasyonuna sahipseniz, BIOS üzerinden **SmartAccess Memory (SAM)** özelliğini mutlaka aktif edin. 

SAM, CPU'nun GPU belleğinin (VRAM) tamamına tek seferde erişmesini sağlar. CS2 gibi CPU-GPU veri alışverişinin yoğun olduğu Source 2 oyunlarında, SAM aktivasyonu minimum FPS değerlerini (1% ve 0.1% Low FPS) %5 ila %12 oranında artırarak oyun içi anlık takılmaları (stuttering) tamamen engeller.

### Shader Cache (Gölgelendirici Önbelleği) Temizliği

CS2 güncellemelerinden sonra veya sürücü değiştirdiğinizde anlık takılmalar yaşıyorsanız, bunun nedeni bozulmuş gölgelendirici önbelleğidir.

1.  **AMD Software** uygulamasını açın.
2.  **Ayarlar (Dişli Çark) > Ekran Kartları > Gelişmiş** sekmesine gidin.
3.  En altta yer alan **"Gölgelendirici Önbelleğini Sıfırla"** seçeneğine tıklayın.
4.  Bilgisayarı yeniden başlatın. İlk oyuna girdiğinizde haritalar yüklenirken hafif takılmalar olabilir, ancak shader'lar yeniden derlendikten sonra oyun pürüzsüz hale gelecektir.

### AMD Fluid Motion Frames (AFMF) Uyarısı

AMD'nin sürücü seviyesindeki kare oluşturma (Frame Generation) teknolojisi olan AFMF, CS2 için **kesinlikle kapatılmalıdır**. Kare oluşturma teknolojileri, yapay kareler ekleyerek FPS sayacını yüksek gösterse de, sisteme ek işlem yükü bindirerek giriş gecikmesini (input lag) iki katına çıkarır. Rekabetçi arenalarda bu durum dezavantaj yaratır.