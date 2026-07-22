# Ekran Kartı Darboğazı Nasıl Anlaşılır? Teknik Tespit Yöntemleri ve Belirtiler

Ekran kartı (GPU) darboğazı, grafik işlemcinizin sistemdeki diğer bileşenlerin (özellikle işlemci/CPU) gönderdiği verileri işleme kapasitesinin sonuna ulaşması ve sistem performansındaki sınırlayıcı faktör haline gelmesi durumudur. Bilgisayar oyunlarında ve grafik odaklı iş yüklerinde GPU darboğazı yaşandığını anlamak, doğru teşhis araçları ve donanım metriklerinin analizi ile mümkündür.

---

## 1. Ekran Kartı Darboğazının Temel Belirtileri

Bir sistemde ekran kartı darboğazı olup olmadığını anlamak için dikkat edilmesi gereken başlıca teknik göstergeler şunlardır:

*   **%99 - %100 GPU Kullanımı:** Oyun esnasında ekran kartı kullanım oranının sürekli olarak %97-%100 bandında seyretmesi, GPU’nun tam kapasitede çalıştığının ve sistemdeki frene basan ana unsur olduğunun en net kanıtıdır.
*   **Düşük CPU Kullanımı:** GPU %100 yük altındayken, işlemci (CPU) kullanımının genel olarak %20 - %60 gibi düşük veya orta seviyelerde kalması.
*   **Çözünürlük ve Grafik Ayarlarına Doğrudan Tepki:** Grafik ayarlarını (örneğin High'dan Low'a) veya çözünürlüğü (örneğin 4K'dan 1080p'ye) düşürdüğünüzde FPS değerinde belirgin bir artış yaşanıyorsa, sistem GPU sınırına takılıyor demektir.
*   **Stabil Fakat Düşük FPS:** Ekran kartı darboğazında, işlemci darboğazının aksine anlık takılmalar (stuttering) ve ani FPS düşüşleri (drop) az görülür. Kare süreleri (frametime) genellikle sabittir, ancak saniye başına düşen toplam kare sayısı (FPS) donanım gücüyle sınırlıdır.

---

## 2. Adım Adım GPU Darboğazı Tespit Testi

Ekran kartı darboğazını kesin olarak doğrulamak için canlı donanım izleme yazılımları kullanılmalıdır.

### Gerekli Yazılımlar
*   **MSI Afterburner** ve **RivaTuner Statistics Server (RTSS)** (Canlı OSD göstergesi için)
*   **CapFrameX** veya **HWiNFO64** (Detaylı veri takibi için)

### Test Prosedürü

1.  **MSI Afterburner Kurulumu ve Ayarı:**
    *   Yazılımı kurun ve `Ayarlar > İzleme` sekmesine gidin.
    *   `GPU Kullanımı`, `GPU Sıcaklığı`, `CPU Kullanımı (Tüm Çekirdekler)`, `FPS` ve `Kare Süresi (Frametime)` metriklerini "Bilgi Ekranında Göster (OSD)" olarak işaretleyin.
2.  **Oyun İçi Test:**
    *   Test etmek istediğiniz, grafik yükü yüksek bir oyunu başlatın.
    *   Dikey Eşitlemeyi (V-Sync) ve FPS kilitlerini kapatın.
3.  **Veri Analizi:**
    *   **Durum A (GPU Darboğazı):** `GPU: %99` | `CPU: %40` | `Frametime: Düz Çizgi` -> Sistem ekran kartı limitindedir.
    *   **Durum B (CPU Darboğazı):** `GPU: %75` | `CPU: %95` (veya tek çekirdek %100) | `Frametime: Dalgalı` -> İşlemci, ekran kartını besleyememektedir.

---

## 3. Ekran Kartı Darboğazı ve İşlemci Darboğazı Karşılaştırması

İki durum arasındaki farkı doğru analiz etmek, yanlış parçayı değiştirmeyi önler:

| Metrik / Durum | Ekran Kartı (GPU) Darboğazı | İşlemci (CPU) Darboğazı |
| :--- | :--- | :--- |
| **GPU Kullanımı** | %98 - %100 | %90'ın altında (Örn: %60-%80) |
| **CPU Kullanımı** | Düşük / Orta (%20 - %60) | Yüksek (%80 - %100 veya tek çekirdek doyumu) |
| **Oyun Deneyimi** | Akıcı ancak düşük FPS | Anlık takılmalar (Stuttering) ve FPS dropları |
| **Çözünürlük Etkisi** | Çözünürlük düştükçe FPS artar | Çözünürlük düşse de FPS değişmez/az artar |
| **Sistem Sağlığı** | **İdeal/Kabul Edilebilir** (İstenen durumdur) | **İstenmeyen Durum** (Oynanabilirliği düşürür) |

> **Teknik Not:** Oyun sistemlerinde ekran kartının %100 kapasitede çalışması (GPU darboğazı), işlemci darboğazına kıyasla **tercih edilen bir durumdur**. Çünkü GPU darboğazında kare üretim süreleri kararlıdır ve girdi gecikmesi (input lag) öngörülebilirdir.

---

## 4. Ekran Kartı Darboğazı Nasıl Giderilir?

Eğer ekran kartınızın sunduğu FPS değeri beklentinizin altındaysa ve GPU darboğazı tespit ettiyseniz aşağıdaki yazılımsal ve donanımsal çözümleri uygulayabilirsiniz:

### Yazılımsal Çözümler (Maliyet Gerektirmeyen)
1.  **Yapay Zeka Ölçekleme Teknolojilerini Kullanın:** Nvidia DLSS, AMD FSR veya Intel XeSS özelliklerini açarak işleme çözünürlüğünü düşürün. Bu işlem GPU üzerindeki yükü doğrudan hafifletir.
2.  **Ağır Grafik Ayarlarını Düşürün:**
    *   Ray Tracing (Işın İzleme) - GPU'ya en çok yük bindiren teknolojidir.
    *   Hacimsel Bulutlar ve Gölgeler (Volumetric Fog/Shadows).
    *   Kenar Yumuşatma (Anti-Aliasing - MSAA/SSAA yerine TAA veya FXAA seçin).
3.  **Çözünürlüğü Düşürün:** Örneğin 4K çözünürlükten 1440p veya 1080p seviyesine inin.

### Donanımsal Çözümler
1.  **GPU Overclock (Hız Aşırtma):** Ekran kartının çekirdek ve bellek frekanslarını artırarak %5-%10 arası performans kazanımı elde edin.
2.  **Ekran Kartı Yükseltmesi:** Yazılımsal çözümler yetersiz kaldığında tek kesin çözüm, daha yüksek işlem gücüne (VRAM, CUDA/Stream Çekirdeği) sahip bir ekran kartına geçmektir.