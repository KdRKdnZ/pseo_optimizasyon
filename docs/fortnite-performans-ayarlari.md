---
title: fortnite performans ayarları
description: fortnite performans ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# Fortnite Performans Ayarları: Donanım ve Yazılım Optimizasyon Rehberi

Fortnite, Unreal Engine 5 (UE5) motoruna geçişiyle birlikte görsel kalitesini artırırken, donanım üzerindeki yükünü de önemli ölçüde artırmıştır. Rekabetçi bir avantaj elde etmek ve milisaniyelerle ölçülen giriş gecikmesini (input lag) en aza indirmek için oyun içi grafik ayarlarının, işletim sisteminin ve sürücülerin optimize edilmesi şarttır. 

Bu rehber, donanım kaynaklarınızı en verimli şekilde kullanarak FPS'inizi (Saniyedeki Kare Sayısı) maksimuma çıkaracak ve kare süresi (frame time) dalgalanmalarını engelleyecek teknik optimizasyon adımlarını içermektedir.

---

## Rendering API Seçimi: DirectX 11, DirectX 12 ve Performance Mode

Fortnite, üç farklı işleme API'si (Application Programming Interface) sunar. Doğru API seçimi, sistem darboğazınızı (bottleneck) doğrudan etkiler.

### Performance Mode (Performans Modu - Alfa)
İşlemci (CPU) darboğazı yaşayan ve düşük-orta segment ekran kartına (GPU) sahip sistemler için en ideal moddur. 
*   **Teknik Altyapı:** Bu mod, UE5'in ağır görsel özelliklerini (Lumen, Nanite, Virtual Shadow Maps) devre dışı bırakır. Bellek (VRAM ve RAM) kullanımını minimize etmek için mobil platformlardaki düşük poligonlu modelleri ve basitleştirilmiş gölgelendiricileri (shaders) kullanır.
*   **Avantajı:** CPU üzerindeki çizim çağrısı (draw call) yükünü azaltarak kararlı bir kare hızı ve en düşük giriş gecikmesini sağlar.

### DirectX 12
Üst segment GPU ve çok çekirdekli modern CPU'lara sahip sistemler için önerilir.
*   **Teknik Altyapı:** CPU iş parçacıklarını (multithreading) daha verimli yönetir ve asenkron hesaplama (asynchronous compute) desteği sunar. 
*   **Avantajı:** Shader derleme (shader compilation) kekemeliklerini (stuttering) azaltır. Ancak rekabetçi oyun için Performance Mode kadar yüksek FPS üretmez.

### DirectX 11
Eski nesil donanımlar için bir alternatif olsa da modern sistemlerde kararsız kare sürelerine yol açtığı için **tercih edilmemelidir**.

---

## Oyun İçi Grafik Ayarları ve Donanım Etkileri

En yüksek performans için oyun içi ayarların donanım mimarisine göre yapılandırılması gerekir. Aşağıdaki tablo ve açıklamalar, rekabetçi düzeyde en optimize ayarları sunmaktadır.

| Ayar Grubu | Önerilen Değer | Donanım Üzerindeki Etkisi |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | Windows DWM (Desktop Window Manager) gecikmesini baypas eder. |
| **Çözünürlük** | Monitörün Doğal Çözünürlüğü | Piksel doldurma oranını (fill rate) optimize eder. |
| **Kare Hızı Sınırı** | Monitör Hz Değeri + 1 veya Sınırsız | GPU kullanımını %99'un altında tutarak gecikmeyi önler. |
| **3D Çözünürlük** | %100 (Gerekirse %85-%90) | Doğrudan GPU render yükünü belirler. |
| **Görüş Uzaklığı** | Orta (Medium) veya Uzak (Far) | CPU çizim mesafesini ve RAM kullanımını etkiler. |
| **Gölgeler** | Kapalı (Off) | GPU gölgelendirici birimlerindeki yükü sıfırlar. |
| **Dokular (Textures)** | Düşük (Low) veya Orta (Medium) | Ekran kartı bellek (VRAM) sınırını aşmamak için kritiktir. |
| **Efektler** | Düşük (Low) | Patlama ve build animasyonlarında FPS düşüşünü engeller. |
| **Post Processing** | Düşük (Low) | Ekran kartı üzerindeki ardıl işlem yükünü kaldırır. |

### Görüş Uzaklığı (View Distance) Neden "Destansı" (Epic) Yapılmamalı?
Görüş uzaklığı ayarı, haritadaki oyuncuların görünme mesafesini etkilemez; oyuncular her ayarda aynı mesafeden görünür. Bu ayar yalnızca binaların, ağaçların ve nesnelerin detay düzeyini (LOD - Level of Detail) belirler. "Destansı" ayarı, CPU'ya binen çizim çağrısı yükünü geometrik olarak artırarak FPS droplarına neden olur. Rekabetçi oyun için **Orta** veya **Uzak** ayarı optimum dengedir.

### Dokular (Textures) ve VRAM Yönetimi
Dokuları "Düşük" yerine "Orta" yapmak, eğer ekran kartınızda yeterli VRAM (en az 4 GB) varsa FPS kaybına yol açmaz. VRAM kapasiteniz yeterliyse, dokuları Orta ayarda tutmak, oyun içi nesnelerin aniden yüklenmesi (texture popping) esnasında oluşan anlık takılmaları engeller.

---

## Giriş Gecikmesini (Input Lag) En Aza İndirme

Rekabetçi oyunlarda düşük gecikme süresi, yüksek FPS kadar önemlidir. Giriş gecikmesini minimize etmek için aşağıdaki donanım tabanlı teknolojileri aktif edin.

### NVIDIA Reflex Low Latency
NVIDIA ekran kartı kullanıcıları için bu ayar **Açık + Takviye (On + Boost)** konumuna getirilmelidir.
*   **Çalışma Prensibi:** CPU'nun render kuyruğunu GPU ile senkronize eder. "Takviye" seçeneği, GPU'nun güç tasarruf modlarına girmesini engelleyerek çekirdek saat hızlarını (core clocks) her zaman maksimumda tutar ve işlemci darboğazı anlarında bile gecikmeyi en düşük seviyede tutar.

### Dikey Senkronizasyon (V-Sync)
*   **Öneri:** Kesinlikle **Kapalı (Off)** olmalıdır.
*   **Teknik Gerekçe:** V-Sync, ekran yırtılmalarını önlemek için kareleri kuyruğa alır ve bu durum 30-50 ms arasında ek sistem gecikmesine (system latency) yol açar. Eğer yırtılmaları önlemek istiyorsanız, monitörünüzün G-Sync/FreeSync teknolojisini sürücü üzerinden aktif edip, oyun içi FPS limitini monitör yenileme hızının (Hz) 3 FPS altına sabitleyin.

---

## İşletim Sistemi ve Sürücü Düzeyinde Optimizasyon

Windows ve GPU sürücülerinin doğru yapılandırılmaması, en güçlü donanımlarda bile performans kaybına yol açar.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 ve 11 ile gelen bu özellik, yüksek öncelikli grafik görevlerini doğrudan GPU'nun kendi özel zamanlama işlemcisine devreder.
*   **Nasıl Açılır:** Windows Ayarları > Sistem > Monitör > Grafik Ayarları yolunu izleyin ve "Donanım hızlandırmalı GPU zamanlaması" seçeneğini aktif edin.
*   **Etkisi:** CPU üzerindeki bağlam geçişi (context switching) yükünü azaltarak minimum FPS değerlerini (1% low FPS) yükseltir.

### NVIDIA Denetim Masası Ayarları
NVIDIA ekran kartı sürücüsünde şu üç ayarın değiştirilmesi kararlılık için kritiktir:
1.  **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra (DirectX 11/12 modlarında etkilidir).
2.  **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
3.  **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** 10 GB veya Sınırsız (Oyun esnasında shader derleme takılmalarını tamamen önlemek için disk üzerinde geniş bir alan ayırır).

---

## Fortnite Config (GameUserSettings.ini) İnce Ayarları

Fortnite'ın yapılandırma dosyasında oyun içinden erişilemeyen bazı kritik performans parametreleri bulunur.

Dosyaya erişmek için: `Win + R` tuşlarına basın, `%localappdata%\FortniteGame\Saved\Config\WindowsClient` yazın ve `GameUserSettings.ini` dosyasını Not Defteri ile açın.

Aşağıdaki satırları bulun ve değerlerini değiştirin:

*   `bShowGrass=False` (Çimleri devre dışı bırakarak GPU yükünü azaltır ve rakiplerin görünürlüğünü artırır.)
*   `bDisableMouseAcceleration=True` (Windows fare ivmesini devre dışı bırakarak kas hafızası tutarlılığını sağlar.)
*   `bRayTracing=False` (Tüm ışın izleme fonksiyonlarının tamamen kapalı olduğundan emin olur.)

*Not: Değişiklikleri kaydettikten sonra dosyaya sağ tıklayıp "Özellikler" seçeneğinden "Salt Okunur" (Read-Only) kutucuğunu işaretleyin. Aksi takdirde oyun, güncellemelerle bu ayarları sıfırlayabilir.*