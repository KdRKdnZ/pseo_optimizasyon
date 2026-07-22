# PC Darboğazı Nasıl Anlaşılır? Belirtileri, Tespiti ve Çözüm Yolları

Bilgisayar performansında **darboğaz (bottleneck)**, sistemdeki bir donanım bileşeninin kapasite sınırına ulaşarak diğer bileşenlerin tam verimle çalışmasını engellemesi durumudur. Genellikle yüksek güçlü bir ekran kartı (GPU) ile zayıf bir işlemcinin (CPU) eşleştirilmesi sonucu ortaya çıkar. Ancak RAM yetersizliği veya yavaş depolama birimleri de darboğaza neden olabilir.

Bu teknik rehberde; darboğazın nasıl tespit edileceğini, belirtilerini, canlı izleme yöntemlerini ve çözüm adımlarını detaylandırıyoruz.

---

## 1. PC Darboğazının Temel Belirtileri Nelerdir?

Sisteminizde darboğaz olup olmadığını oyun oynarken veya ağır iş yükleri altında şu belirtilerden anlayabilirsiniz:

* **Ani FPS Düşüşleri (Micro-Stuttering):** Oyun akıcı bir şekilde çalışırken anlık olarak karesel takılmaların yaşanması ve FPS'in aniden düşmesi.
* **Düşük Ekran Kartı Kullanımı:** Ekran kartının (GPU) %99-%100 yerine %50-%80 bandında çalışması ve bu esnada işlemci (CPU) kullanımının %90-%100 seviyelerinde seyretmesi.
* **Grafik Ayarları Değişse de FPS'in Artmaması:** Grafik kalitesini veya çözünürlüğü düşürmenize rağmen FPS değerinin yükselmemesi (Tipik işlemci darboğazı belirtisi).
* **Giriş Gecikmesi (Input Lag):** İşlemci aşırı yüklendiğinde klavye ve fare komutlarının oyuna geç yansıması.

---

## 2. Donanım Türlerine Göre Darboğaz Çeşitleri

### A. İşlemci (CPU) Darboğazı
En yaygın görülen darboğaz türüdür. İşlemci, ekran kartının ürettiği kareleri işleyip ekrana göndermekte yetersiz kalır.
* **Gösterge:** CPU kullanımı %90-100, GPU kullanımı %80'in altındadır.
* **Çözünürlük İlişkisi:** Düşük çözünürlüklerde (örneğin 1080p) işlemciye düşen yük arttığı için CPU darboğazı daha belirgin hale gelir.

### B. Ekran Kartı (GPU) Darboğazı
Aslında oyun sistemlerinde **istenen durumdur**. Ekran kartının %99-100 oranında kullanılması, sistemin grafik gücünden tam verim aldığınızı gösterir. Ancak ekran kartı hedeflenen FPS'i sağlayamıyorsa teknik bir GPU sınırına takılmış olursunuz.
* **Gösterge:** GPU kullanımı %99-100, CPU kullanımı %20-60 seviyesindedir.

### C. RAM ve Depolama Darboğazı
Yetersiz RAM kapasitesi veya yavaş bir HDD/SSD, sistemin veri akışını kilitler.
* **Gösterge:** RAM kullanımı %95 üzerine çıkar. Oyun içi kaplamalar (texture) geç yüklenir, haritada ilerlerken takılmalar yaşanır.

---

## 3. Adım Adım PC Darboğaz Tespiti (MSI Afterburner Kullanımı)

Darboğazı en doğru şekilde tespit etmek için sentetik testler veya web sitelerindeki "darboğaz hesaplayıcılar" yerine oyun içi canlı veri takibi yapılmalıdır.

### Adım 1: MSI Afterburner ve RTSS Kurulumu
1. **MSI Afterburner** yazılımını ve beraberinde gelen **RivaTuner Statistics Server (RTSS)** programını indirin.
2. Programı açıp **Ayarlar (Dişli simgesi) > İzleme (Monitoring)** sekmesine gidin.

### Adım 2: Gerekli Metrikleri Aktif Etme
Aşağıdaki değerleri bulun ve alt kısımdaki **"Bilgi Ekranında Göster (OSD)"** seçeneğini işaretleyin:
* **GPU Kullanımı (GPU Usage)**
* **CPU Kullanımı (CPU Usage - Tüm Çekirdekler)**
* **RAM Kullanımı (RAM Usage)**
* **Kare Hızı (FPS)**
* **Kare Zamanı (Frametime)**

### Adım 3: Oyun İçi Analiz
Sistemi zorlayan bir oyuna girin ve verileri inceleyin:

```text
[Senaryo 1: CPU Darboğazı]
GPU Kullanımı: %65
CPU Kullanımı: %98
Sonuç: İşlemci, ekran kartını besleyemiyor.

[Senaryo 2: İdeal Performans / GPU Sınırı]
GPU Kullanımı: %99
CPU Kullanımı: %45
Sonuç: Sistem dengeli çalışıyor, ekran kartı tam verimde.

[Senaryo 3: RAM Darboğazı]
RAM Kullanımı: 15.8 GB / 16 GB
Frametime Grafiği: Düzensiz dikey sıçramalar
Sonuç: Bellek kapasitesi yetersiz, sistem diskteki sanal belleği kullanıyor.
```

---

## 4. Online Darboğaz Hesaplama Siteleri Güvenilir mi?

İnternette yer alan "Bottleneck Calculator" tarzı siteler **%100 doğru sonuç vermez**. Bu siteler algoritma tabanlı tahminler sunar; ancak:
* Oyunların mimari optimizasyonlarını,
* Çözünürlük ve grafik ayarlarının etkisini,
* Arka planda çalışan yazılımları,
* Çift kanal (Dual-Channel) RAM konfigürasyonunun etkisini hesaba katamazlar.

Bu nedenle en doğru teşhis, **gerçek zamanlı testler (MSI Afterburner)** ile konulan teşhistir.

---

## 5. Darboğaz Nasıl Önlenir ve Çözülür?

Darboğaz tespit edildiğinde sistem değiştirmeden önce uygulanabilecek yazılımsal ve donanımsal çözümler şunlardır:

### İşlemci Darboğazı İçin Çözümler:
* **Çözünürlüğü Yükseltin:** 1080p'den 1440p (2K) veya 4K çözünürlüğe geçmek, yükü işlemciden alıp ekran kartına bindirir.
* **Grafik Ayarlarını Artırın:** Gölge, doku, ışıklandırma ve Ray Tracing gibi yükü GPU'ya bindiren ayarları en yükseğe getirin.
* **Arka Plan İşlemlerini Kapatın:** Discord, Chrome veya antivirüs gibi CPU tüketen uygulamaları sonlandırın.
* **FPS Sınırlayıcı Kullanın:** Monitörün yenileme hızına (örneğin 144 Hz) FPS'i sabitlemek işlemci üzerindeki anlık yükü hafifletir.
* **Donanım Yükseltmesi:** İşlemciyi yükseltmek veya RAM'leri çift kanal (Dual Channel) moduna geçirmek.

### Ekran Kartı Darboğazı İçin Çözümler:
* **Çözünürlüğü ve Grafikleri Düşürün:** Render ölçeğini veya grafik detaylarını düşürün.
* **DLSS / FSR / XeSS Kullanın:** Yapay zeka destekli ölçeklendirme teknolojilerini aktif edin.

### RAM Darboğazı İçin Çözümler:
* **Kapasite Artırımı:** 8 GB RAM kullanıyorsanız 16 GB veya 32 GB'a yükseltin.
* **XMP / EXPO Profilini Açın:** BIOS üzerinden RAM frekanslarını maksimum değere getirin.