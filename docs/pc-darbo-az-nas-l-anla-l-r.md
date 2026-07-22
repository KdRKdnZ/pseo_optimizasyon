---
title: "pc darboğaz nasıl anlaşılır"
description: "pc darboğaz nasıl anlaşılır hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# PC Darboğazı (Bottleneck) Nasıl Anlaşılır? Teknik Teşhis ve Çözüm Rehberi

PC darboğazı (bottleneck), bilgisayar sistemindeki bir bileşenin işleme kapasitesinin, diğer bileşenlerin potansiyel performansını sınırlaması durumudur. Veri akış zincirindeki en zayıf halka, tüm sistemin maksimum performans tavanını belirler.

Sisteminizde darboğaz olup olmadığını anlamak, doğru teşhis yöntemleri ve donanım izleme yazılımları ile mümkündür.

---

## 1. Yazılımsal İzleme ile PC Darboğazı Teşhisi

Darboğaz tespiti yapmanın en kesin yolu, sistem yük altındayken (özellikle oyunlarda veya sentetik testlerde) donanım kullanım oranlarını anlık olarak izlemektir.

### Gerekli Araçlar
*   **MSI Afterburner & RivaTuner Statistics Server (RTSS):** Oyun içi OSD (On-Screen Display) ile anlık veri takibi için endüstri standardıdır.
*   **HWInfo64:** Detaylı çekirdek yükleri ve voltaj/sıcaklık değerleri için.
*   **CapFrameX:** Kare süresi (Frametime) ve %1 / %0.1 Low FPS analizi için.

### İzlenmesi Gereken Kritik Parametreler
1.  **GPU Kullanımı (GPU Usage %):** Ekran kartının işleme kapasitesinin ne kadarını kullandığını gösterir.
2.  **CPU Kullanımı (CPU Usage % - Toplam ve Çekirdek Başına):** İşlemcinin genel ve tekil çekirdek yükünü gösterir.
3.  **RAM / VRAM Kullanımı:** Bellek sınırlarına ulaşıp ulaşılmadığını belirtir.
4.  **Kare Süresi Grafiği (Frametime Graph):** Milisaniye (ms) cinsinden kare üretim kararlılığını gösterir.

---

## 2. Darboğaz Türleri ve Teşhis Senaryoları

### A. İşlemci (CPU) Darboğazı Nasıl Anlaşılır?
İşlemci darboğazı, GPU'nun render etmeye hazır olduğu kareleri CPU'nun zamanında hazırlayamaması durumudur.

*   **Belirtiler:**
    *   **GPU Kullanımı %90'ın altındadır** (Örn: %50 - %75 arası dalgalanır).
    *   **CPU Kullanımı (Genel veya tek bir çekirdek) %90 - %100 civarındadır.**
    *   Grafik ayarları veya çözünürlük düşürüldüğünde FPS artmaz.
    *   Oyunlarda ani ve takılma şeklinde kare düşüşleri (**Micro-stuttering**) yaşanır.
    *   *Örnek:* 1080p çözünürlükte RTX 4080 ile Ryzen 5 3600 kullanımı.

> **Teknik Detay:** Toplam CPU kullanımı %40 görünse bile, oyun yalnızca 2 çekirdeği yoğun kullanıyorsa ve bu çekirdekler %100 yüktesse, sistemde **Tek Çekirdek CPU Darboğazı** vardır.

### B. Ekran Kartı (GPU) Darboğazı Nasıl Anlaşılır?
GPU darboğazı, oyun sistemlerinde aslında istenen ve doğal karşılanan durumdur. Sistem, ekran kartının tüm gücünü kullanıyor demektir.

*   **Belirtiler:**
    *   **GPU Kullanımı kararlı bir şekilde %97 - %99 arasındadır.**
    *   CPU kullanımı %20 - %70 arasında, rahat bir seviyededir.
    *   Çözünürlük veya grafik kalitesi düşürüldüğünde FPS belirgin şekilde artar.
    *   Kare süreleri (Frametime) genellikle sabittir, ani takılmalar azdır.

### C. RAM (Bellek) Darboğazı Nasıl Anlaşılır?
Yetersiz RAM kapasitesi veya düşük bellek bant genişliği veri akışında tıkanmaya yol açar.

*   **Belirtiler:**
    *   RAM kullanımı toplam kapasitenin %90-95'ine ulaşır.
    *   Sistem, diski sanal bellek (Pagefile) olarak kullanmaya başlar ve **stutter (anlık donma)** oluşur.
    *   **Tek Kanal (Single Channel) RAM kullanımı:** Çift kanal (Dual Channel) belleğe kıyasla GPU kullanımında dalgalanmalara ve düşük %1 FPS değerlerine neden olur.

### D. Depolama (SSD/HDD) Darboğazı Nasıl Anlaşılır?
Yavaş depolama birimleri, özellikle açık dünya oyunlarında kaplama (texture) ve obje yüklenirken takılmalara sebep olur.

*   **Belirtiler:**
    *   Oyun esnasında diskin **%100 Kullanım** oranına ulaşması.
    *   Yeni bir bölgeye girerken veya hızlı hareket ederken kaplamaların geç yüklenmesi ve FPS'in anlık olarak 0'a düşmesi.

---

## 3. Adım Adım Darboğaz Test Prosedürü

1.  **MSI Afterburner Kurulumu:** Programı kurun ve OSD menüsünden `GPU Usage`, `CPU Usage`, `CPU Clock`, `RAM Usage`, `FPS` ve `Frametime` seçeneklerini aktif edin.
2.  **Test Ortamı:** Test edeceğiniz oyunu başlatın. Açık dünya (GTA V, Cyberpunk 2077) veya kalabalık çok oyunculu (BF2042, Warzone) oyunlar CPU darboğazını daha net gösterir.
3.  **Çözünürlük Testi (Çapraz Kontrol):**
    *   Çözünürlüğü **1920x1080**'den **1280x720**'ye düşürün.
    *   **Sonuç A:** FPS yükseliyorsa -> Sistem **GPU limitlidir** (Darboğaz yok/normal).
    *   **Sonuç B:** FPS aynı kalıyor veya çok az değişiyorsa, GPU kullanımı daha da düşüyorsa -> Sistemde net bir **CPU darboğazı** vardır.

---

## 4. PC Darboğazı Nasıl Çözülür?

| Darboğaz Türü | Anlık / Yazılımsal Çözüm | Kalıcı / Donanımsal Çözüm |
| :--- | :--- | :--- |
| **CPU Darboğazı** | Çözünürlüğü yükseltin (1080p -> 2K). Grafik ayarlarını (Nokta ışıklar, nüfus yoğunluğu, fizik) artırın. DSR/VSR kullanın. | Daha yüksek tek çekirdek performansına (IPC) sahip bir CPU'ya geçin. |
| **GPU Darboğazı** | DLSS / FSR / XeSS açın. Gölge, Kenar Yumuşatma (AA) ve Ray Tracing ayarlarını kısın. | Ekran kartını yükseltin. |
| **RAM Darboğazı** | Arka plandaki RAM tüketen uygulamaları (Chrome vb.) kapatın. | Aynı değerlerde bir RAM ekleyerek Dual Channel mimarisine geçin. |
| **Depolama Darboğazı** | Arka plan indirmelerini durdurun, disk birleştirme yapın (HDD ise). | Oyunu NVMe M.2 SSD'ye taşıyın. |

---

## Özet
PC darboğazını anlamanın temel parametresi **GPU kullanım oranıdır**. Yük altındaki bir oyunda ekran kartı kullanımı sürekli olarak %90'ın altında kalıyorsa ve işlemci yükü yüksekse, sisteminizde işlemci kaynaklı bir darboğaz mevcuttur. Online darboğaz hesaplama siteleri (Bottleneck Calculators) sentetik algoritmalar kullandığı için güvenilir değildir; en doğru sonuç yukarıda belirtilen canlı izleme yöntemleriyle elde edilir.