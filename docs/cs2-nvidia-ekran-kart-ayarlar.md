---
title: "cs2 nvidia ekran kartı ayarları"
description: "cs2 nvidia ekran kartı ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 NVIDIA Ekran Kartı Ayarları: Maksimum FPS ve En Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte sistem kaynaklarını, özellikle de ekran kartını (GPU) önceki oyuna kıyasla çok daha yoğun kullanmaktadır. CS2'de yüksek kare hızı (FPS) almak kadar, girdi gecikmesini (input lag) minimize etmek ve görsel netliği korumak da kritik önem taşır. 

Bu rehberde, NVIDIA Denetim Masası ve oyun içi grafik ayarlarının CS2 için en optimize teknik yapılandırması adım adım sunulmaktadır.

---

## 1. NVIDIA Denetim Masası CS2 Özel Ayarları

NVIDIA Denetim Masası üzerindeki ayarlar, ekran kartınızın sürücü seviyesinde nasıl davranacağını belirler. Bu ayarları uygulamak için:

1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. Sol menüden **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3. **Program Ayarları** başlığı altında Counter-Strike 2 (`cs2.exe`) profilini seçin (Listede yoksa "Ekle" butonundan oyunun kurulu olduğu dizindeki `cs2.exe` dosyasını gösterin).

Aşağıdaki teknik parametreleri eksiksiz uygulayın:

| Ayar İsmi | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Arka Plan Uygulamaları Maksimum Kare Hızı** | Kapalı | Yan uygulamaların GPU kaynağını kısıtlamasını engeller. |
| **Bağlantılı Optimize Etme (Threaded Optimization)** | Açık | İşlemcinin çoklu çekirdek avantajını CS2'ye aktarır. |
| **Düşük Gecikme Oranı Modu (Low Latency Mode)** | Kapalı / Açık | Oyun içinde *NVIDIA Reflex* aktif edileceği için burada **Kapalı** veya **Açık** bırakılması önerilir. (Ultra modu Reflex ile çakışabilir). |
| **Doku Süzme - Kalite** | Yüksek Performans | GPU üzerindeki yükü azaltır, milisaniyelik FPS kazanımları sağlar. |
| **Doku Süzme - Eşyönsüz Örnek Optimizasyonu** | Açık | Performansı artırmak için doku süzme yükünü hafifletir. |
| **Doku Süzme - Trilineer Optimizasyon** | Açık | Doku geçişlerindeki yükü düşürür. |
| **Eşyönsüz Süzme (Anisotropic Filtering)** | Kapalı / Uygulama Kontrolünde | İşlem yükünü azaltır. Oyun içinden kontrol edilmesi daha sağlıklıdır. |
| **Güç Yönetimi Modu** | Maksimum Performansı Tercih Et | GPU saat hızlarının (clock speeds) oyun esnasında düşmesini engeller, kararlı FPS sağlar. |
| **Gölgelendirici Önbelleği Boyutu (Shader Cache Size)** | 10 GB veya Sınırsız | CS2'deki harita yüklemelerinde ve çatışma anlarındaki anlık takılmaları (stuttering) önler. |
| **Kenar Yumuşatma (Antialiasing) Ayarları** | Uygulama Kontrolünde | Kenar yumuşatma işlemini oyun içi motorun yönetmesine izin verir. |
| **Maksimum Kare Hızı** | Kapalı | Kare hızını sürücü seviyesinde limitlemez. |
| **Dikey Eşitleme (V-Sync)** | Kapalı | Girdi gecikmesini (input lag) doğrudan artırdığı için kesinlikle kapatılmalıdır. |

---

## 2. NVIDIA Masaüstü Boyutunu ve Konumunu Ayarlama (4:3 Stretched)

Profesyonel oyuncuların büyük çoğunluğu genişletilmiş (stretched) çözünürlük tercih etmektedir. Ekran kartı tabanlı ölçeklendirmenin doğru yapılması, görüntünün bulanıklaşmasını ve gecikmeyi önler.

1. NVIDIA Denetim Masası'nda **Masaüstü Boyutunu ve Konumunu Ayarla** sekmesine gelin.
2. Ölçeklendirme modunu **Tam Ekran (Full-screen)** olarak seçin.
3. **Ölçeklendirmeyi Şurada Yap:** seçeneğini **GPU** olarak ayarlayın. (Görüntü işleme yükünü monitör yerine ekran kartına vermek girdi gecikmesini azaltır).
4. **Oyunlar ve Programlar Tarafından Belirlenen Ölçekleme Modunu Geçersiz Kıl** kutucuğunu **işaretleyin**.

---

## 3. CS2 Oyun İçi Gelişmiş Video Ayarları

NVIDIA kartlarının Source 2 motoru ile tam entegrasyonu için oyun içi ayarların doğru yapılandırılması gerekir.

### Gelişmiş Görüntü Ayarları:

* **NVIDIA Reflex Low Latency:** **Açık + Takviye (Enabled + Boost)**
  * *Teknik Detay:* Ekran kartının frekans değerlerini maksimumda tutar ve CPU kuyruğunu optimize ederek sistem gecikmesini en alt seviyeye çeker.
* **Gelişmiş Oyuncu Görünürlüğü:** **Açık**
  * *Teknik Detay:* Düşman modellerinin arka planla olan kontrastını artırır. Çok düşük FPS alınan sistemlerde Kapalı yapılabilir ancak rekabetçi avantaj için Açık kalmalıdır.
* **Çoklu Örneklemeli Kenar Yumuşatma Modu (MSAA):** **4x MSAA** veya **CMAA2**
  * *Teknik Detay:* CS2'de MSAA Kapalı olduğunda piksellenme ve titreme çok belirginleşir. 2x veya 4x MSAA, piksel netliği ve performans arasındaki en optimum noktadır.
* **Evrensel Gölge Kalitesi:** **Yüksek (High)** veya **Orta (Medium)**
  * *Teknik Detay:* CS2'de rakiplerin gölgelerini köşelerden çıkmadan önce görmek büyük avantaj sağlar. "Düşük" ayarda bu gölgeler oluşmaz. En az **Orta** veya **Yüksek** seçilmelidir.
* **Model / Doku Detayı:** **Düşük (Low)**
* **Parçacık Detayı:** **Düşük (Low)**
* **Doku Filtreleme Modu:** **Üç Çizgili (Trilinear)** veya **Eşyönsüz 4x**
* **Ayrıntılı Gölge Kalitesi:** **Düşük (Low)**
* **Oyun İçi Aydınlatma (Mesafe/Ortam Kapatma):** **Kapalı (Disabled)**
* **Yüksek Dinamik Aralık (HDR):** **Performans**
* **FidelityFX Super Resolution (FSR):** **Kapalı (Devre Dışı - En Yüksek Kalite)**
  * *Teknik Detay:* FSR, görüntüyü alt çözünürlükte işleyip ölçeklendirir. Kenar netliğini bozar ve girdi gecikmesine sebep olabilir. Doğal çözünürlük (Disabled) kullanılmalıdır.

---

## 4. NVIDIA Sürücü ve Sistem Optimizasyonu

* **Sürücü Güncelliği:** CS2, güncel grafik sürücülerine doğrudan bağımlıdır. GeForce Experience veya NVIDIA web sitesi üzerinden **Game Ready** sürücülerinin en son sürümünü kullanın.
* **GeForce Experience Overlay:** Oyun içi yer paylaşımı (Overlay), video kaydı ve Anında Yeniden Oynatma özellikleri FPS düşüşlerine ve anlık takılmalara yol açabilir. Rekabetçi performans için **GeForce Experience -> Ayarlar -> Genel -> Oyun İçi Yer Paylaşımı** seçeneğini kapatın.
* **NVIDIA Digital Vibrance (Dijital Renk Doğoygunluğu):** Düşmanların haritada daha kolay ayırt edilebilmesi için NVIDIA Denetim Masası > **Masaüstü Renk Ayarlarını Ayarla** sekmesinden *Digital Vibrance* değerini **%60 - %75** aralığına getirebilirsiniz.

---

## Özet

Yapılan bu yapılandırmalar sonucunda CS2 üzerinde:
1. **NVIDIA Reflex** entegrasyonu ile sistem gecikmesi (System Latency) minimuma iner.
2. GPU üzerindeki gereksiz işleme yükleri (FSR, ortam kapatma, yüksek doku detayları) kaldırılarak maksimum FPS elde edilir.
3. Gölge ve MSAA ayarları ile rekabetçi avantaj sağlayan görsel netlik korunmuş olur.