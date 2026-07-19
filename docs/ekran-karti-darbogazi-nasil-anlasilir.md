---
title: ekran kartı darboğazı nasıl anlaşılır
description: ekran kartı darboğazı nasıl anlaşılır hakkında detaylı optimizasyon ve donanım rehberi.
---

# Ekran Kartı Darboğazı Nasıl Anlaşılır? Teknik Tespit ve Çözüm Rehberi

Bilgisayar donanım mimarisinde "darboğaz" (bottleneck), bir sistemdeki bileşenlerin maksimum performans potansiyelinin, sistemdeki en yavaş bileşen tarafından sınırlandırılması durumudur. Oyunlarda ve yoğun grafik gücü gerektiren iş istasyonu uygulamalarında en sık karşılaşılan senaryo, işlemci (CPU) ve ekran kartı (GPU) arasındaki veri akışı uyuşmazlığıdır. 

Bir sistem mimarı gözüyle bakıldığında, GPU'nun tam kapasiteyle çalışamaması, donanım yatırımınızın amortisman değerini düşürür. Peki, **ekran kartı darboğazı nasıl anlaşılır?** Bu rehberde, donanım telemetri verilerini analiz ederek darboğazı kesin olarak nasıl tespit edeceğinizi ve bu sorunu nasıl optimize edeceğinizi teknik detaylarıyla ele alacağız.

---

## Ekran Kartı Darboğazı (Bottleneck) Nedir?

Donanım boru hattında (pipeline) işlemci ve ekran kartı senkronize çalışır. İşlemci; oyun içi fizik hesaplamalarını, yapay zekayı, ağ paketlerini ve en önemlisi ekran kartına neyi çizmesi gerektiğini söyleyen **"Draw Calls" (Çizim Çağrıları)** verilerini hazırlar. Ekran kartı ise bu verileri alarak ekrana yansıtılacak pikselleri işler (rendering).

Eğer işlemci, ekran kartının render etme hızından daha yavaş veri üretiyorsa, ekran kartı boşta bekler. Bu duruma **CPU Darboğazı (İşlemci Darboğazı)** denir. Tam tersi durumda, işlemci verileri çok hızlı gönderiyor ancak ekran kartı bunları işleyemiyorsa, buna da **GPU Darboğazı** denir. Oyun performansında hedefimiz, ekran kartının %95-100 yük altında çalışması, yani sistem limitinin GPU olmasıdır.

---

## Ekran Kartı Darboğazı Nasıl Anlaşılır? (Adım Adım Teşhis)

Sisteminizde darboğaz olup olmadığını tahminlerle değil, gerçek zamanlı donanım telemetrisi (OSD) verileriyle analiz etmeniz gerekir.

### 1. Telemetri ve İzleme Araçlarının Kurulumu
Darboğaz tespiti için en güvenilir yöntem, oyun esnasında donanım bileşenlerinin anlık yüklerini izlemektir. Bu işlem için **MSI Afterburner** ve onunla birlikte gelen **RivaTuner Statistics Server (RTSS)** yazılımlarını kullanacağız.

*   MSI Afterburner'ı indirin ve kurun.
*   Ayarlar > İzleme (Monitoring) sekmesine gidin.
*   Aşağıdaki metrikleri aktif hale getirin ve "OSD'de Göster" (Show in On-Screen Display) seçeneğini işaretleyin:
    *   **GPU Sıcaklığı ve GPU Kullanımı (GPU Usage)**
    *   **Bellek Kullanımı (VRAM Usage)**
    *   **CPU Sıcaklığı ve CPU Kullanımı (CPU Usage - Tüm çekirdekler ayrı ayrı seçilmelidir)**
    *   **RAM Kullanımı (RAM Usage)**
    *   **Kare Hızı (FPS) ve Kare Süresi (Frametime)**
    *   **%1 Low ve %0.1 Low FPS Değerleri**

### 2. CPU ve GPU Kullanım Oranlarının Analizi
Oyunu başlatın ve sistemin kararlı hale gelmesi için 5-10 dakika oynayın. Ardından ekranın köşesindeki OSD değerlerini inceleyin:

*   **Senaryo A (Sağlıklı Durum - GPU Sınırı):** GPU kullanımı %95 - %100 arasında, CPU kullanımı ise %20 - %70 arasındadır. Bu, ekran kartınızın tam performansla çalıştığını gösterir. İdeal oyun deneyimi budur.
*   **Senaryo B (CPU Darboğazı):** GPU kullanımı %60 - %85 gibi düşük seviyelerde kalırken, CPU kullanımı (özellikle 1 veya 2 çekirdekte) %90 - %100 seviyelerine ulaşıyorsa **kesinlikle işlemci darboğazı vardır.** İşlemci, ekran kartını besleyememektedir.

> **Önemli Donanım Notu:** Toplam CPU kullanımının %50 olması sizi yanıltmasın. Modern oyunlar genellikle tüm CPU çekirdeklerini eşit kullanmaz. Eğer oyun 4 çekirdek optimize edilmişse ve sizin 8 çekirdekli bir işlemciniz varsa, toplam CPU kullanımı %50 görünür ancak ilgili 4 çekirdek %100 yük altındadır. Bu yüzden çekirdeklerin tek tek izlenmesi kritiktir.

### 3. Frametime (Kare Süresi) ve %1 / %0.1 Low Değerleri
Sadece ortalama FPS değerine bakmak darboğazı anlamak için yeterli değildir. 

*   **Frametime (Kare Süresi):** Milisaniye (ms) cinsinden her bir karenin ekrana çizilme süresidir. Grafiksel olarak dalgalı, ani dikey çizgilerin (spike) olduğu bir frametime grafiği, işlemcinin çizim çağrılarını yetiştiremediğini ve mikro takılmalar (stuttering) yaşandığını gösterir.
*   **%1 ve %0.1 Low FPS:** Bu değerler, oyun süresince alınan en düşük FPS dilimlerini gösterir. Ortalama FPS değeriniz 100 iken, %1 Low değeriniz 20 FPS ise, sistemde ciddi bir veri akışı tıkanıklığı (darboğaz) mevcuttur.

### 4. Çözünürlük Ölçekleme Testi
Darboğazın kaynağını doğrulamak için oyun içi çözünürlüğü değiştirin:

*   Çözünürlüğü **1080p'den 2K (1440p) veya 4K'ya** yükseltin. 
*   Eğer FPS değeriniz neredeyse hiç düşmüyorsa veya çok az düşüyorsa, sisteminizde net bir **CPU darboğazı** vardır. Çünkü çözünürlük artışı GPU yükünü artırır, CPU yükünü değiştirmez. FPS'in düşmemesi, işlemcinin zaten maksimum verebileceği kare sınırında olduğunu kanıtlar.

---

## İşlemci (CPU) ve Ekran Kartı (GPU) Darboğazı Arasındaki Farklar

| Belirti / Durum | CPU Darboğazı | GPU Darboğazı |
| :--- | :--- | :--- |
| **GPU Kullanım Oranı** | Düşük (%50 - %85) | Yüksek (%95 - %100) |
| **CPU Kullanım Oranı** | Yüksek (%90 - %100, belirli çekirdeklerde) | Değişken (Genellikle düşük-orta) |
| **Oyun İçi Deneyim** | Ani FPS düşüşleri, anlık takılmalar (Stutter) | Akıcı ancak donanım limitine bağlı sabit FPS |
| **Çözünürlük Etkisi** | Çözünürlük düşse de FPS artmaz | Çözünürlük düştükçe FPS doğrusal artar |
| **Grafik Ayarları Etkisi** | Ayarları düşürmek FPS'i artırmaz | Ayarları düşürmek GPU yükünü azaltır, FPS artar |

---

## Ekran Kartı Darboğazı Nasıl Giderilir?

Eğer yaptığınız analizler sonucunda sisteminizde darboğaz tespit ettiyseniz, donanım değiştirmeden veya donanım yükselterek uygulayabileceğiniz çözüm yolları şunlardır:

### Donanımsal Çözümler (Yazılım Dışı)
1.  **İşlemciyi Yükseltmek:** CPU darboğazının kesin çözümü, ekran kartınızın çizim çağrısı (draw call) kapasitesine yanıt verebilecek daha yüksek tekli çekirdek performansına sahip bir işlemciye geçmektir.
2.  **RAM Frekansını ve Gecikme Sürelerini Optimize Etmek:** CPU darboğazlarında RAM hızı kritik rol oynar. BIOS üzerinden **XMP / AMP (EXPO)** profilini aktif edin. Çift kanal (Dual-Channel) RAM kullanımı, CPU'nun veri işleme bant genişliğini ikiye katlayarak darboğazı azaltır.
3.  **Overclock (Hız Aşırtma):** İşlemcinizin saat hızını (GHz) güvenli sınırlar dahilinde artırmak, darboğazı doğrudan azaltacaktır.

### Yazılımsal ve Yapılandırma Çözümleri
1.  **Çözünürlüğü Artırın:** Oyunu daha yüksek bir çözünürlükte (örneğin 1080p yerine DSR/VSR teknolojisi ile sanal olarak 1440p'de) çalıştırın. Bu, yükü CPU'dan alıp GPU'ya aktaracaktır.
2.  **Grafik Detaylarını Yükseltin:** Gölgeler, yansımalar, hacimsel ışıklandırma ve doku kalitesi gibi doğrudan GPU'ya yük bindiren ayarları en üst seviyeye getirin.
3.  **FPS Sınırlandırıcı Kullanın:** FPS'i monitörünüzün tazeleme hızına (Hz) veya kararlı bir değere (örneğin 60 veya 144 FPS) sabitleyin. Bu, işlemcinin sürekli %100 kapasitede yeni kare hazırlamaya çalışmasını engelleyerek frametime dalgalanmalarının önüne geçer.
4.  **Arka Plan İşlemlerini Kapatın:** Discord, tarayıcı sekmeleri, antivirüs taramaları gibi CPU tüketen arka plan uygulamalarını oyun esnasında kapatın.