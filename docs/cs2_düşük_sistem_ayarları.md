# CS2 Düşük Sistem Ayarları: Maksimum FPS ve En Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte CS:GO’ya kıyasla gelişmiş aydınlatma, fizik ve grafik işlem yükü getirmiştir. Düşük ve orta donanımlı sistemlerde sistem kaynaklarını (CPU/GPU) optimize etmek, kare hızını (FPS) artırmak ve sistem gecikmesini (input lag) en aza indirmek için doğru grafik ve sistem ayarlarının yapılması kritik önem taşır.

Aşağıda, CS2'de maksimum performans ve rekabetçi avantaj elde etmek için uygulanması gereken teknik ayarlar detaylandırılmıştır.

---

## 1. Oyun İçi Gelişmiş Video Ayarları

CS2 grafik menüsündeki her ayarın işlemci (CPU) ve ekran kartı (GPU) üzerindeki yükü farklıdır. Rekabetçi oyunlarda hedef; yüksek FPS, kararlı FPS %1-%0.1 minimum değerleri ve maksimum düşman görünürlüğüdür.

| Grafik Ayarı | Tavsiye Edilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | Pencereli modlar Windows Masaüstü Pencere Yöneticisi (DWM) nedeniyle ek gecikme yaratır. Tam ekran doğrudan GPU erişimi sağlar. |
| **Oyuncu Kontrastını Artır** | **Etkin (Enabled)** | Düşman modellerinin arka plandan ayırt edilmesini sağlar. FPS etkisi ihmal edilebilir düzeydedir (~%1). |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı (Disabled)** | Kare hızını monitör tazeleme hızına kilitler ve çok yüksek giriş gecikmesine (input lag) neden olur. |
| **Çoklu Örneklemeli Kenar Yumuşatma** | **CMAA2** veya **2x MSAA** | CS2'de kenar yumuşatmayı kapatmak tırtıklanmaya ve düşmanların uzaktan tespitinin zorlaşmasına yol açar. En düşük GPU yükü için **CMAA2**, performans yeterliyse **2x MSAA** seçilmelidir. |
| **Evrensel Gölge Kalitesi** | **Düşük (Low)** | Yüksek ayarlar dinamik gölgeleri artırır ve GPU/CPU işlem yükünü yükseltir. Rekabetçi avantajı yitirmeden FPS kazanmak için "Düşük" tutulmalıdır. |
| **Model / Doku Detayı** | **Düşük (Low)** | VRAM kullanımını düşürür ve doku yükleme kaynaklı takılmaları (stuttering) önler. |
| **Doku Filtreleme Modu** | **Çift Hatlı (Bilinear)** | En az GPU kaynaklı bellek bant genişliğini kullanan moddur. |
| **Shader Detayı** | **Düşük (Low)** | Işık kırılmaları ve karmaşık yüzey efektlerini basitleştirir. Özellikle eski nesil GPU'larda ciddi FPS artışı sağlar. |
| **Parçacık Detayı** | **Düşük (Low)** | Molotof, sis ve patlama efektlerinin yarattığı ani FPS düşüşlerini (FPS drop) engeller. |
| **Ortam Kapatma (Ambient Occlusion)**| **Devre Dışı (Disabled)** | Köşe ve temas gölgelerini hesaplayan bu teknoloji GPU üzerine gereksiz yük bindirir. |
| **Yüksek Dinamik Aralık (HDR)** | **Performans (Performance)** | Işık geçişlerindeki işleme yükünü düşürür. Görsel kalite kaybı minimumdur. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (En Yüksek Kalite)**| FSR, görüntüyü düşük çözünürlükte işleyip ölçeklendirir. Görüntüde bulanıklığa ve kenar tespit zorluğuna yol açar. Sistem çok zayıf olmadığı sürece kapatılmalıdır. |
| **NVIDIA Reflex Düşük Gecikme** | **Etkin + Boost** | Sisteminiz CPU darboğazındaysa GPU frekansını maksimumda tutarak render gecikmesini en aza indirir. |

---

## 2. Çözünürlük ve En-Boy Oranı Optimize Edilmesi

Çözünürlük doğrudan GPU'nun işlemesi gereken piksel sayısını belirler. CS2'de performans sınırlıysa piksel sayısını azaltmak en etkili çözüm yoludur.

*   **En-Boy Oranı:** 4:3
*   **Çözünürlük:** 1280x960 (Genişletilmiş / Stretched) veya 1024x768

**Teknik Avantajı:** 4:3 esnetilmiş çözünürlük, yatay eksendeki pikselleri genişleterek düşman modellerinin ekranda daha büyük görünmesini sağlar. Ayrıca 1080p (1920x1080) çözünürlüğe kıyasla işlenen piksel sayısı %40'a yakın azaldığı için FPS artar ve işlemciye binen render yükü hafifler.

---

## 3. CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizde CS2'ye sağ tıklayıp *Özellikler > Genel > Başlatma Seçenekleri* kısmına eklemeniz gereken güncel ve performansa dayalı komutlar şunlardır:

```text
-novid -nojoy +cl_showfps 1 +engine_low_latency_sleep_after_client_tick true
```

*   `-novid`: Giriş videosunu atlayarak oyunun açılışını hızlandırır.
*   `-nojoy`: Joystick/Gamepad girdilerini devre dışı bırakarak RAM ve CPU izleme iş parçacığını serbest bırakır.
*   `+engine_low_latency_sleep_after_client_tick true`: Source 2 motorunun kare sürelerini (frame pacing) daha stabil hale getirerek sistem gecikmesini düşürür.

*(Not: CS:GO döneminden kalma `-high`, `-threads`, `-nod3d9ex` gibi komutlar Source 2 motorunda işlevsizdir veya çökme sorunlarına yol açabilir.)*

---

## 4. Ekran Kartı Sürücü Ayarları

### NVIDIA Denetim Masası
1.  **3D Ayarlarının Yönetilmesi > Program Ayarları > CS2** seçin.
2.  **Güç Yönetimi Modu:** *Maksimum Performansı Tercih Et*
3.  **Düşük Gecikme Oranı Modu (Low Latency Mode):** *Açık (On)* veya *Ultra*
4.  **Doku Süzme - Kalite:** *Yüksek Performans*
5.  **Eşyönsüz Süzme Optimizasyonu:** *Açık*

### AMD Software: Adrenalin Edition
1.  **Oyun > CS2** profilini açın.
2.  **Radeon Anti-Lag:** *Etkin* (Giriş gecikmesini azaltır)
3.  **Radeon Boost:** *Devre Dışı* (Dinamik çözünürlük ölçekleme yapacağı için görüntü çamurlaşabilir)
4.  **Ekran Kartı Dokusu Kalitesi:** *Performans*

---

## 5. Windows İşletim Sistemi Optimizasyonu

*   **Oyun Modu (Game Mode):** Windows Ayarları > Oyun > Oyun Modu alanından **Açık** konuma getirin. Bu ayar, CS2 çalışırken arka plan işlemlerinin CPU önceliğini düşürür.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Grafik Ayarları bölümünden **Açık** getirin. GPU belleğinin yönetimini işletim sisteminden alıp GPU'ya devreder, kare süresi tutarlılığını artırır.
*   **Nihai Performans Güç Planı:** Komut İstemi'ni (CMD) yönetici olarak çalıştırın ve şu kodu girin:
    ```cmd
    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
    ```
    Ardından *Güç Seçenekleri* menüsünden **Nihai Performans** modunu seçin.

---

## 6. Konsol İçi Performans Komutları

Oyun esnasında geliştirici konsolunu (`~`) açarak aşağıdaki komutları uygulayabilirsiniz:

*   `fps_max 0`: FPS kısıtlamasını kaldırır. Ancak sisteminizde ısınma veya aşırı FPS dalgalanması oluyorsa monitör tazeleme hızınızın 2 katına sabitlemeniz (Örn: 144Hz için `fps_max 300`) daha stabil kare süreleri verecektir.
*   `cl_ragdoll_workperiod 0`: Ölen oyuncu fiziklerinin (ragdoll) CPU üzerındaki hesaplama yükünü azaltır.

Bu teknik ayarlar, CS2’nin Source 2 mimarisine uygun olarak gereksiz görsel efektleri devre dışı bırakır ve sistem kaynaklarının tamamını kare üretimine ve en düşük tepki süresine yönlendirir.