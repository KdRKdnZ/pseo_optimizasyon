---
title: pc darboğaz nasıl anlaşılır
description: pc darboğaz nasıl anlaşılır hakkında detaylı optimizasyon ve donanım rehberi.
---

# PC Darboğaz Nasıl Anlaşılır? Donanım Sınırlarını Tespit Etme Rehberi

Bilgisayar sistemlerinde darboğaz (bottleneck), bir bileşenin maksimum performans sınırına ulaşarak diğer bileşenlerin tam kapasiteyle çalışmasını engellemesi durumudur. Sistem mimarisinde bu durum, veri akış hattındaki (pipeline) en yavaş halkanın toplam sistem performansını belirlemesi kuralına (Amdahl Yasası) dayanır. 

Bir sistemde darboğaz olup olmadığını anlamak, doğru teşhis araçlarını ve donanım metriklerini doğru okumayı gerektirir.

---

## Darboğaz Türleri ve Sistem Mimarisine Etkileri

Sistem performansını optimize etmek için öncelikle darboğazın hangi bileşenler arasında gerçekleştiğini tanımlamak gerekir.

### 1. CPU (İşlemci) Darboğazı
İşlemcinin, ekran kartının (GPU) hazırlayabileceği kareleri (frames) işleme hızına yetişemediği durumdur. Özellikle düşük çözünürlüklerde (1080p ve altı) ve yüksek kare hızlarında (FPS) ortaya çıkar. İşlemci çekirdeklerinden bir veya birkaçının %100 yük altında çalışması, ancak GPU kullanımının %80'in altında kalması ile karakterize edilir.

### 2. GPU (Ekran Kartı) Darboğazı
Grafik işlemcinin %99-%100 yük altında çalışırken, CPU kullanımının çok daha düşük seviyelerde kalması durumudur. Oyun bilgisayarlarında bu durum **istenilen bir darboğaz türüdür**; çünkü ekran kartının tam kapasiteyle kullanıldığını ve yatırılan bütçenin karşılığının alındığını gösterir.

### 3. RAM ve Depolama Darboğazı
Sistem belleğinin (RAM) yetersiz kapasitede olması veya düşük frekansta çalışması, CPU'nun veri beklemesine (CPU wait state) yol açar. Benzer şekilde, yavaş bir sabit diskin (HDD) veya dramless bir SSD'nin veri okuma/yazma hızları, oyun içi kaplamaların (textures) yüklenmesinde anlık takılmalara (stuttering) neden olur.

---

## PC Darboğaz Nasıl Anlaşılır? Adım Adım Tespit Yöntemleri

Sisteminizdeki darboğazı tespit etmek için sentetik testler yerine gerçek zamanlı telemetri verilerini analiz etmeniz gerekir.

### 1. Oyun İçi Telemetri ve İzleme Araçlarını Yapılandırın
Darboğaz tespiti için en güvenilir yöntem **MSI Afterburner** ve beraberinde gelen **RivaTuner Statistics Server (RTSS)** yazılımlarını kullanmaktır.

**İzlenmesi Gereken Kritik Metrikler:**
*   **GPU Usage (GPU Kullanımı):** Grafik çekirdeğinin yük yüzdesi.
*   **CPU Usage (CPU Kullanımı - Genel ve Çekirdek Bazlı):** İşlemcinin toplam ve her bir mantıksal çekirdeğinin yük yüzdesi.
*   **Framerate (FPS):** Saniyedeki kare sayısı.
*   **Frametime (Kare Süresi - ms):** İki kare arasındaki milisaniye cinsinden süre (milisaniye dalgalanmaları takılmaları gösterir).
*   **RAM Usage:** Kullanılan sistem belleği miktarı.

### 2. CPU ve GPU Kullanım Oranlarını Analiz Edin

Yazılımları yapılandırdıktan sonra donanım yüklerini analiz etmek için aşağıdaki senaryoları inceleyin:

| Senaryo | GPU Kullanımı | CPU Kullanımı (En az bir çekirdek) | Teşhis |
| :--- | :--- | :--- | :--- |
| **Senaryo A** | %95 - %100 | %20 - %60 | **Sağlıklı Durum (GPU Sınırında)** |
| **Senaryo B** | %40 - %80 | %90 - %100 | **CPU Darboğazı** |
| **Senaryo C** | %50 - %70 | %30 - %50 | **RAM/Yazılım veya Motor Sınırı** |

> **Önemli Donanım Notu:** Toplam CPU kullanımının %50 olması sizi yanıltmasın. Eğer oyun sadece 4 çekirdek kullanıyorsa ve sizin 8 çekirdekli işlemcinizin 4 çekirdeği %100 yük altındaysa, bu bir **CPU darboğazıdır**. Bu yüzden çekirdeklerin tek tek izlenmesi hayati önem taşır.

### 3. Frametime (Kare Süresi) Grafiğini İnceleyin
FPS değeri yüksek görünse bile, frametime grafiğinde ani dikey sıçramalar (spikes) varsa, bu durum işlemcinin veya depolama biriminin ekran kartına veri yetiştiremediğini gösterir. Stabil bir çizgi pürüzsüz bir oyun deneyimini, dalgalı bir grafik ise darboğazı işaret eder.

---

## Darboğaz Testi İçin Sentetik Benchmark Yazılımları

Gerçek zamanlı oyun testlerinin yanı sıra, donanımları izole ederek test eden sentetik yazılımlarla da darboğaz tespiti yapılabilir.

*   **3DMark (Time Spy / Port Royal):** Bu test hem CPU hem de GPU skorlarını ayrı ayrı verir. Eğer GPU skorunuz dünya genelindeki benzer sistemlerin çok altındaysa, CPU veya RAM darboğazı yaşıyor olabilirsiniz.
*   **Cinebench R23 (CPU Testi) & Superposition (GPU Testi):** Bu iki testi ardışık olarak çalıştırın. Eğer Cinebench skorunuz normalken, Superposition testinde GPU kullanımı %99'a ulaşmıyorsa, PCIe veri yolu sınırlandırmaları veya güç kaynağı (PSU) yetersizliği gibi donanımsal darboğazlar mevcut olabilir.

---

## Darboğaz Nasıl Çözülür? Donanım ve Yazılım Çözümleri

Darboğaz tespiti yapıldıktan sonra, darboğazın türüne göre uygulanabilecek optimizasyon yöntemleri şunlardır:

### CPU Darboğazını Gidermek İçin:
1.  **Çözünürlüğü Artırın:** Çözünürlüğü 1080p'den 1440p (2K) veya 2160p (4K) seviyesine çekmek, yükü işlemciden alıp ekran kartına aktarır.
2.  **Grafik Detaylarını Yükseltin:** Gölgeler, yansımalar ve doku kalitesi gibi doğrudan GPU'ya yük bindiren ayarları en üst seviyeye getirin.
3.  **Arka Plan İşlemlerini Kapatın:** Tarayıcılar, Discord donanım ivmesi ve antivirüs taramaları gibi CPU tüketen arka plan servislerini devre dışı bırakın.

### GPU Darboğazını Gidermek İçin:
1.  **Çözünürlüğü Düşürün veya Upscaling Kullanın:** DLSS, FSR veya XeSS gibi yapay zeka destekli yeniden ölçeklendirme teknolojilerini aktif edin.
2.  **Grafik Ayarlarını Optimize Edin:** Volumetrik sis, gölge kalitesi ve kenar yumuşatma (Anti-Aliasing) gibi GPU'yu en çok yoran ayarları kısın.

### RAM ve Depolama Darboğazını Gidermek İçin:
1.  **XMP/EXPO Profilini Aktif Edin:** BIOS üzerinden RAM frekanslarını üreticinin belirlediği maksimum hıza (MHz) sabitleyin.
2.  **Çift Kanal (Dual-Channel) Bellek Kullanın:** Tek modül (Single-Channel) RAM kullanımı, işlemcinin veri bant genişliğini yarı yarıya düşürerek ciddi CPU darboğazına yol açar. Sisteme aynı değerde ikinci bir RAM ekleyin.