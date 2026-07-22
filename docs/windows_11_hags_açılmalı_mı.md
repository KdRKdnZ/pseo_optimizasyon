# Windows 11 HAGS Açılmalı mı? Donanım Hızlandırmalı GPU Zamanlaması Teknik İnceleme

**Donanım Hızlandırmalı GPU Zamanlaması (HAGS - Hardware-Accelerated GPU Scheduling)**, Windows 10 (2004 sürümü) ile hayatımıza giren ve Windows 11 ile daha kararlı hale getirilen bir grafik mimarisi özelliğidir. 

Özetle cevap vermek gerekirse: **Evet, modern bir ekran kartına (NVIDIA GTX 1000 serisi ve üzeri, AMD RX 5000 serisi ve üzeri, Intel Arc) sahipseniz Windows 11'de HAGS açık kalmalıdır.** Ancak sistem bileşenlerinize ve oynadığınız oyun türlerine bağlı olarak bu durum değişiklik gösterebilir.

---

## HAGS (Donanım Hızlandırmalı GPU Zamanlaması) Nedir ve Nasıl Çalışır?

Geleneksel grafik mimarisinde (HAGS Kapalı), VRAM (Video RAM) yönetimi ve grafik önceliklendirme görevleri **Merkezi İşlemci (CPU)** tarafından yürütülür. CPU, ekran kartına hangi verilerin ne zaman işleneceğini söyler. Bu durum, özellikle işlemci limitine takılan (CPU Bottleneck) sistemlerde gecikmeye (latency) ve işlemci üzerinde ek yüke neden olur.

HAGS açıldığında ise Microsoft WDDM (Windows Display Driver Model) 2.7 ve üzeri sürücüler vasıtasıyla bu görev doğrudan **GPU'nun kendi bünyesindeki özel zamanlama işlemcisine (RISC tabanlı çekirdek)** devredilir.

### Teknik Avantajı:
* **Gecikmenin Azaltılması:** CPU ve GPU arasındaki veri trafiği azaltılarak kare oluşturma süresi (frametime) düşürülür.
* **İşlemci Yükünün Hafifletilmesi:** CPU, grafik zamanlamasıyla uğraşmak yerine fizik hesaplamaları ve oyun mantığına odaklanır.
* **Daha İyi VRAM Yönetimi:** VRAM'deki bellek ayırma ve boşaltma işlemleri GPU tarafından daha agresif ve verimli yönetilir.

---

## HAGS Açmanın Avantajları ve Dezavantajları

### Avantajları
1. **DLSS 3 (Frame Generation) Zorunluluğu:** NVIDIA RTX 40 serisi kartlarda bulunan Kare Oluşturma (DLSS 3) teknolojisinin çalışabilmesi için HAGS'ın **açık olması şarttır**.
2. **%1 ve %0.1 Low FPS İyileşmesi:** Ortalama FPS çok değişmese bile, anlık takılmalar (stuttering) azalır ve kare iletimi (frame pacing) daha pürüzsüz hale gelir.
3. **Zayıf İşlemcilerde Performans Artışı:** Giriş ve orta seviye işlemcilerin üzerindeki grafik yükünü aldığı için darboğazı bir miktar hafifletir.
4. **Yayıncılar İçin Avantaj:** OBS gibi yazılımlarla ekran kartı üzerinden yayın yaparken kare düşmelerini engeller.

### Dezavantajları
1. **Eski Oyunlarda Uyumluluk Sorunları:** DirectX 9 ve DirectX 11 kullanan bazı eski oyunlarda nadiren de olsa mikro takılmalara veya ç çökmelere (crash) neden olabilir.
2. **Eski Sürücülerde Kararsızlık:** Güncel olmayan GPU sürücülerinde MPO (Multi-Plane Overlay) çakışmaları nedeniyle siyah ekran sorunları yaşanabilir.
3. **Üst Seviye Sistemlerde Hissedilmeyen Fark:** Ryzen 7 7800X3D veya i9-14900K gibi ultra güçlü işlemcilerde varsayılan performans etkisi yok denecek kadar azdır.

---

## HAGS Performansa Nasıl Etki Eder? (Benchmark ve Test Mantığı)

| Senaryo / Sistem Tipi | HAGS Etkisi | Öneri |
| :--- | :--- | :--- |
| **NVIDIA RTX 40 Serisi (DLSS 3 Kullanımı)** | Kritik Performans Artışı (Zorunlu) | **Kesinlikle Açık** |
| **Giriş / Orta Seviye CPU + Güçlü GPU** | %1 Low FPS değerlerinde %5-%10 artış | **Açık** |
| **Rekabetçi Espor Oyunları (CS2, Valorant vb.)** | Gecikmede 1-2 ms düşüş (Sistem bağımlı) | **Açık (Test Edilmeli)** |
| **Eski Nesil GPU (GTX 900 serisi / RX 400-500)** | Kararsızlık, potansiyel takılma | **Kapalı** |

---

## Windows 11'de HAGS Nasıl Açılır veya Kapatılır?

1. **Başlat** menüsünü açın ve **Ayarlar**'a (Windows + I) gidin.
2. **Sistem** sekmesinden **Ekran** bölümüne tıklayın.
3. En alt kısımda yer alan **Grafikler** seçeneğine girin.
4. İlgili sayfada **"Varsayılan grafik ayarlarını değiştir"** bağlantısına tıklayın.
5. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** (veya Kapalı) konuma getirin.
6. Değişikliklerin geçerli olması için **bilgisayarınızı yeniden başlatın**.

---

## Sıkça Sorulan Sorular (SSS)

### HAGS ekran kartının ısınmasına neden olur mu?
Hayır. HAGS, GPU'ya fazladan bir iş yükü bindirmez; sadece işlerin sırasını yöneten işlemciyi değiştirir. Sıcaklık ve güç tüketimi üzerinde hissedilebilir bir etkisi yoktur.

### HAGS açıkken Valorant veya CS2'de ban sebebi mi?
Hayır. HAGS, Microsoft tarafından işletim sistemi düzeyinde sunulan ve grafik sürücüleri tarafından resmi olarak desteklenen bir özelliktir. Herhangi bir anti-cheat sistemi tarafından engel sebebi sayılmaz.

### AMD ekran kartlarında HAGS açılmalı mı?
RDNA2 (RX 6000) ve RDNA3 (RX 7000) mimarisine sahip güncel AMD kartlarda, güncel Adrenalin sürücüleriyle HAGS performansı oldukça kararlıdır ve açık tutulması tavsiye edilir.

---

## Sonuç ve Karar

Windows 11 kullanıyorsanız, sisteminiz güncel bileşenlerden oluşuyorsa ve özellikle **NVIDIA DLSS 3 veya modern DirectX 12 / Vulkan oyunları** oynuyorsanız **HAGS varsayılan olarak AÇIK tutulmalıdır**.

Yalnızca eski nesil DirectX 9/11 oyunlarında kararsızlık, anlık çökme veya oyun içi takılma yaşarsanız sorun giderme (troubleshooting) adımı olarak HAGS'ı kapatıp test etmeniz teknik olarak önerilir.