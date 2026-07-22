---
title: "windows 11 hags açılmalı mı"
description: "windows 11 hags açılmalı mı hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 HAGS (Donanım Hızlandırmalı GPU Zamanlaması) Açılmalı mı?

Windows 11'deki **HAGS (Hardware-Accelerated GPU Scheduling / Donanım Hızlandırmalı GPU Zamanlaması)**, ekran kartının kendi belleğini (VRAM) ve iş yükü zamanlamasını doğrudan yönetmesine izin veren kritik bir sistem özelliğidir. 

**Kısa Cevap:** Güncel bir ekran kartına (özellikle NVIDIA RTX serisi veya AMD RX 5000/6000/7000 serisi) ve modern bir işlemciye sahipseniz, **Windows 11'de HAGS kesinlikle açılmalıdır.** Özellikle NVIDIA RTX 40 serisi kartlarda **DLSS 3 (Frame Generation)** teknolojisini kullanabilmek için HAGS’ın açık olması zorunludur.

Ancak, sistem bileşenlerinize ve oynadığınız oyunlara bağlı olarak bu durum değişiklik gösterebilir. İşte HAGS'ın teknik detayları, avantajları, dezavantajları ve açıp açmamanız gerektiğine dair kapsamlı analiz.

---

## HAGS (Donanım Hızlandırmalı GPU Zamanlaması) Nedir?

Geleneksel sistem mimarisinde, grafik verilerinin işlenmesi ve VRAM'e aktarılması öncelikli olarak **İşlemci (CPU)** tarafından yönetilir. CPU, GPU'ya ne zaman ve hangi sırayla çalışması gerektiğini söyler (High-Priority Queue).

HAGS etkinleştirildiğinde ise bu zamanlama görevi CPU'dan alınır ve ekran kartının üzerinde bulunan özel **GPU Zamanlama İşlemcisine (Scheduling Processor)** devredilir. 

### Teknik Olarak Ne Değişir?
* **CPU Yükü Azalır:** İşlemci, grafik zamanlama görevleriyle uğraşmaz; bu da işlemci darboğazını (CPU Bottleneck) azaltır.
* **Bellek Yönetimi Hızlanır:** GPU, VRAM üzerindeki verileri doğrudan ve daha düşük gecikmeyle yönetir.
* **Giriş Gecikmesi (Input Lag) Düşer:** Veri komut zinciri kısaldığı için komut gecikmesi azalır.

---

## HAGS Açmanın Avantajları Nelerdir?

### 1. DLSS 3 ve Frame Generation Zorunluluğu
NVIDIA'nın RTX 40 serisi kartlarıyla tanıttığı DLSS 3 (Kare Oluşturma) teknolojisi, yapay zeka ile ara kareler üretir. Bu özelliğin çalışabilmesi için **HAGS'ın açık olması şarttır**. HAGS kapalıysa DLSS 3 aktif edilemez.

### 2. %1 ve %0.1 Low FPS Değerlerinde İyileşme
HAGS, ortalama FPS'yi (Average FPS) her zaman devasa oranda artırmaz. Ancak oyunlardaki ani takılmaları (stuttering) engelleyerek **minimum FPS değerlerini yükseltir**. Bu da daha akıcı bir oyun deneyimi sağlar.

### 3. Sistem Gecikmesinin (System Latency) Düşmesi
CPU aradan çekildiği için karelerin işlenme süresi (frame time) daha kararlı hale gelir. Bu durum, özellikle FPS ve e-Spor oyunlarında (CS2, Valorant, Warzone) milisaniyelik avantajlar sağlar.

### 4. İşlemci Darboğazı Yaşayan Sistemlerde Performans Artışı
Eğer güçlü bir ekran kartınız ama nispeten zayıf bir işlemciniz varsa, HAGS CPU üzerindeki yükü alarak kayda değer bir FPS artışı sağlayabilir.

---

## HAGS Ne Zaman Kapatılmalı? (Olası Dezavantajlar)

HAGS genel olarak faydalı olsa da bazı özel senaryolarda sorunlara yol açabilir:

1. **Eski Donanımlar ve Sürücüler:** NVIDIA GTX 10 serisi (Pascal) veya eski AMD kartlarda HAGS, kararsızlığa ve oyunların aniden kapanmasına (Crash) neden olabilir.
2. **Eski Oyun Motorları:** DirectX 9 ve DirectX 11 tabanlı bazı eski oyunlar, HAGS ile uyumsuz çalışabilir ve mikro takılmalara (micro-stuttering) yol açabilir.
3. **Yayıncılar İçin OBS Sorunları:** Nadir de olsa, tek bilgisayardan yayın yapan kullanıcılar OBS üzerinden ekran yakalama yaparken kare düşmesi (frame drop) yaşayabilir. *(Güncel OBS sürümlerinde bu sorun büyük oranda çözülmüştür).*

---

## Kimler HAGS'ı Açmalı, Kimler Kapatmalı?

| Kullanıcı Profili / Sistem Özellikleri | HAGS Durumu | Neden? |
| :--- | :--- | :--- |
| **NVIDIA RTX 40 Serisi Kullanıcıları** | **AÇIK** | DLSS 3 Frame Generation kullanımı için zorunludur. |
| **NVIDIA RTX 20/30 Serisi Kullanıcıları** | **AÇIK** | Düşük gecikme ve daha kararlı kare süreleri sağlar. |
| **AMD RX 6000 / 7000 Serisi Kullanıcıları** | **AÇIK** | Güncel Adrenalin sürücüleri ile tam uyumlu çalışır. |
| **CPU Darboğazı Yaşayan Sistemler** | **AÇIK** | İşlemci yükünü hafifletir. |
| **Eski Ekran Kartları (GTX 10xx, RX 5xx)** | **KAPALI** | Performans kaybı veya çökme riski bulunmaktadır. |
| **Eski Oyunlarda Takılma Yaşayanlar** | **KAPALI** | Oyun motoru uyumsuzluklarını giderebilir. |

---

## Windows 11'de HAGS Nasıl Açılır veya Kapatılır?

Windows 11'de HAGS özelliğini kontrol etmek son derece basittir:

1. **Başlat** menüsüne tıklayın ve **Ayarlar**'ı açın (veya `Win + I` kısayolunu kullanın).
2. **Sistem** sekmesinden **Ekran** bölümüne girin.
3. En alt kısımda yer alan **Grafikler** seçeneğine tıklayın.
4. Varsayılan ayarlar bölümünde bulunan **Varsayılan grafik ayarlarını değiştir** bağlantısına tıklayın.
5. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** veya **Kapalı** konuma getirin.
6. Değişikliklerin geçerli olması için **bilgisayarınızı yeniden başlatın**.

```text
Sistem > Ekran > Grafikler > Varsayılan grafik ayarlarını değiştir > Donanım Hızlandırmalı GPU Zamanlaması
```

---

## Özet ve Sonuç

Windows 11 güncel bir işletim sistemidir ve HAGS mimarisi artık olgunlaşma aşamasını tamamlamıştır. Modern bir ekran kartına (NVIDIA RTX veya AMD RX 5000 ve üzeri) sahipseniz, **HAGS özelliğini açık tutmak sisteminizden maksimum performans ve en düşük gecikmeyi almanızı sağlar.**

Eski bir donanıma sahipseniz ve oyunlarda açıklanamayan takılmalar veya çökmeler yaşıyorsanız, HAGS'ı kapatıp sistemi test etmek en doğru arıza tespit yöntemidir.