# İşlemci Darboğazı Nasıl Anlaşılır? Bütüncül ve Teknik Teşhis Rehberi

İşlemci (CPU) darboğazı, işlemcinin grafik kartının (GPU) gönderdiği verileri işleme hızına yetişememesi ve ekran kartının tam kapasiteyle çalışmasını engellemesi durumudur. Bilgisayar sistemlerinde performans kaybının en yaygın nedenlerinden biri olan bu durum, kare hızı (FPS) düşüşlerine, anlık takılmalara (stuttering) ve sistem kararsızlıklarına yol açar. 

Bu rehberde, bir sistemde işlemci darboğazı olup olmadığını kesin teknik yöntemlerle nasıl tespit edebileceğinizi adım adım inceleyeceğiz.

---

## İşlemci Darboğazının Temel Belirtileri Nelerdir?

Teknik ölçüm araçlarına başvurmadan önce, oyun veya ağır iş yükleri sırasında karşılaşılan şu belirtiler işlemci darboğazına işaret eder:

* **Anlık FPS Düşüşleri (Micro-Stuttering):** Oyun oynarken ortalama FPS yüksek görünse dahi, aniden %1 ve %0.1 FPS değerlerinin aşırı düşmesi ve ekranda mikro takılmaların hissedilmesi.
* **Ekran Kartı Kullanımının Düşük Kalması:** Oyun esnasında GPU kullanımının %99-100 seviyelerine ulaşamaması (örneğin %60-%80 bandında kalması).
* **Gözle Görülen Giriş Gecikmesi (Input Lag):** Fare ve klavye girdilerinin ekrana geç yansıması. İşlemci %100 yük altındayken çevre birimlerinden gelen komutları işleme önceliği düşer.
* **Grafik Ayarları Düşürüldüğünde FPS'in Artmaması:** Oyundaki çözünürlük veya detay seviyesi düşürüldüğü halde FPS değerinde anlamlı bir yükseliş yaşanmaması.

---

## İşlemci Darboğazı Nasıl Anlaşılır? (Adım Adım Teşhis Yöntemleri)

Donanımınızdaki limitasyonları belirlemenin en kesin yolu, sistem yük altındayken gerçek zamanlı telemetri verilerini analiz etmektir.

```
[İşlemci (CPU)] ---> Veri Akışı Kısıtlı (Darboğaz) ---> [Ekran Kartı (GPU)] (Bekleme Modunda / %60 Yük)
```

### 1. Yazılımsal İzleme Araçları ile Veri Analizi

En güvenilir teşhis, **MSI Afterburner** ve **RivaTuner Statistics Server (RTSS)** yazılımları kullanılarak oyun içi OSD (On-Screen Display) verilerinin incelenmesidir.

**İzlenmesi Gereken Metrikler:**
* **GPU Usage (Ekran Kartı Kullanımı):** Ideal şartlarda %97 - %100 olmalıdır.
* **CPU Usage (İşlemci Kullanımı):** Toplam CPU kullanımı ve çekirdek bazlı (Core/Thread) kullanım oranları.
* **CPU Temperatures (İşlemci Sıcaklığı):** Termal kısma (thermal throttling) olup olmadığını belirlemek için.

**Teknik Değerlendirme Senaryoları:**

| GPU Kullanımı | CPU Kullanımı (Tek veya Genel Çekirdek) | Teşhis |
| :--- | :--- | :--- |
| **%60 - %85** | **%90 - %100** | **Net İşlemci Darboğazı** (CPU, GPU'yu besleyemiyor). |
| **%98 - %100** | **%30 - %70** | **İdeal Durum** (Darboğaz yok, GPU tam verimle çalışıyor). |
| **%50 - %70** | **%30 - %50** | **Yazılımsal/RAM Kısıtlaması** (Oyun optimizasyonsuz veya RAM tek kanal/düşük frekanslı). |

> **Önemli Not:** İşlemcinin *toplam* kullanımının %100 olmaması darboğaz olmadığı anlamına gelmez. Oyunlar genellikle tüm çekirdekleri eşit kullanamaz. Eğer işlemcinizin **1. veya 2. çekirdeği %100** yük altındaysa ve GPU kullanımı düşükse, bu durum **tek çekirdek performansına bağlı bir CPU darboğazıdır.**

---

### 2. Çözünürlük ve Grafik Yükü Testi (Çapraz Doğrulama)

İşlemci darboğazını doğrulamak için oyun içi grafik yükünü değiştirerek test yapabilirsiniz:

1. Oyunu **1080p (Full HD)** çözünürlükte ve "Düşük (Low)" grafik ayarlarında çalıştırın. FPS değerini ve GPU kullanımını kaydetin.
2. Çözünürlüğü **1440p (2K)** veya **4K** seviyesine çıkarın veya "Çok Yüksek (Ultra)" grafik ayarlarını açın.
3. **Analiz:**
   * Çözünürlük ve grafikler arttığında **FPS düşmüyor veya çok az değişiyorsa**, sisteminizde **işlemci darboğazı vardır**. Çünkü grafik yükü GPU'ya aktarılmasına rağmen CPU saniyede üretebileceği maksimum kare limitine (frame-bound) takılmıştır.
   * Çözünürlük arttıkça **FPS belirgin şekilde düşüyor ve GPU kullanımı %99'a çıkıyorsa**, sistem dengelidir veya yük GPU tarafındadır.

---

### 3. Sentetik Benchmark ve Stres Testleri

Donanımınızın teorik sınırlarını ölçmek için sentetik test yazılımlarından faydalanabilirsiniz.

* **Cinebench (R23 / 2024):** İşlemcinizin tek çekirdek (Single Core) ve çoklu çekirdek (Multi Core) puanını ölçer. Tek çekirdek puanı düşük olan işlemciler, özellikle e-spor oyunlarında (CS2, Valorant vb.) ekran kartlarına darboğaz yapar.
* **3DMark (Time Spy / Fire Strike):** Test sonucunda verilen "CPU Score" ve "GPU Score" değerlerini karşılaştırır. Grafik testleri sırasında GPU kullanımı düşüyorsa, yazılım bunu raporlayacaktır.

---

## İşlemci Darboğazına Neden Olabilen Yan Faktörler

Bazen sorun doğrudan işlemci modelinin yetersizliği değil, işlemci performansını kısıtlayan alt bileşenlerdir:

1. **RAM (Bellek) Konfigürasyonu:** Tek kanal (Single-Channel) RAM kullanımı, bellek bant genişliğini yarı yarıya düşürür. Bu durum işlemcinin veri beklemesine yol açarak yapay bir CPU darboğazı yaratır.
2. **Aşırı Isınma (Thermal Throttling):** İşlemci yüksek sıcaklıklara (genellikle 90°C ve üzeri) ulaştığında frekansını düşürür (Underclock). Frekans düşüren işlemci, ekran kartını besleyemez hale gelir.
3. **Arka Plan Uygulamaları:** Discord, Chrome, antivirüs yazılımları veya Windows güncellemelerinin arka planda CPU çekirdeklerini tüketmesi.

---

## İşlemci Darboğazı Nasıl Giderilir?

Eğer yapılan testlerde işlemci darboğazı tespit edildiyse, aşağıdaki adımlarla etki azaltılabilir veya tamamen ortadan kaldırılabilir:

* **Çözünürlük ve Grafik Yükünü Artırın:** Çözünürlüğü (DSR/VSR teknolojileri ile) veya grafik kalitesini artırarak yükü CPU'dan alıp GPU'ya yükleyin.
* **Kare Hızını Sınırlayın (FPS Limit / G-Sync / FreeSync):** FPS'i monitörünüzün yenileme hızına (örneğin 144 Hz) sabitlemek, işlemcinin gereksiz yere fazladan kare üretmeye çalışarak %100 yüke girmesini engeller.
* **RAM'leri Çift Kanal (Dual-Channel) Yapın ve XMP/EXPO Açın:** Bellek frekanslarını yükseltmek, işlemcinin veri işleme gecikmesini (latency) düşürür ve darboğazı hafifletir.
* **İşlemciye Overclock (Hız Aşırtma) Yapın:** Soğutma kapasiteniz yeterliyse, işlemci frekansını artırmak tek çekirdek performansını doğrudan yükseltir.
* **Donanım Yükseltmesi (Upgrade):** Yukarıdaki yazılımsal ve konfigüratif çözümler yetersiz kalıyorsa, mevcut ekran kartınızın mimarisine uygun, daha yüksek tek çekirdek ve önbellek (Cache) performansına sahip bir işlemciye geçiş yapılması gerekir.