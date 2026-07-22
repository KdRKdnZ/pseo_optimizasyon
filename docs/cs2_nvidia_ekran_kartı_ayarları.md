# CS2 NVIDIA Ekran Kartı Ayarları: Maksimum FPS ve Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte ekran kartı (GPU) bağımlılığı artan bir oyundur. Yüksek kare hızları (FPS) elde etmek ve sistem gecikmesini (input lag) en aza indirmek için NVIDIA Denetim Masası ve oyun içi ayarların senkronize bir şekilde yapılandırılması gerekir. 

Aşağıda, CS2'de maksimum performans ve rekabetçi avantaj sağlamak için teknik olarak optimize edilmiş NVIDIA ekran kartı ayarları yer almaktadır.

---

## 1. NVIDIA Denetim Masası 3D Yönetim Ayarları

Masaüstüne sağ tıklayarak **NVIDIA Denetim Masası**'nı açın. Sol menüden **3D Ayarlarının Yönetilmesi** sekmesine gidin ve **Program Ayarları** başlığı altından `cs2.exe` dosyasını seçin (Listede yoksa "Ekle" butonundan oyunun kurulu olduğu dizindeki `cs2.exe`yi manuel ekleyin).

Aşağıdaki parametreleri birebir uygulayın:

*   **Arka Plan Uygulamaları Maksimum Kare Hızı:** Kapalı
*   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık *(Source 2 motorunun çoklu çekirdek kullanımını optimize eder).*
*   **Dikey Eşitleme (V-Sync):** Kapalı *(Girdilerde gecikmeye yol açar).*
*   **Doku Süzme - Anizotropik Örnek Optimizasyonu:** Açık
*   **Doku Süzme - Kalite:** Yüksek Performans
*   **Doku Süzme - Negatif LOD Tercihi:** İzin Ver
*   **Doku Süzme - Trilinear Optimizasyon:** Açık
*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra *(Oyun içindeki NVIDIA Reflex ayarıyla çakışmaması için "Açık" konumunda tutulması önerilir).*
*   **Eşyönsüz Süzme (Anisotropic Filtering):** Kapalı veya Uygulama Kontrolünde
*   **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** Sürücü Varsayılanı veya 10 GB *(Takılmaları (stuttering) önlemek için yüksek bellek ayarlanması faydalıdır).*
*   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et *(GPU'nun frekans düşürmesini engeller).*
*   **Kenar Yumuşatma - FXAA:** Kapalı
*   **Kenar Yumuşatma - Mod:** Kapalı / Uygulama Kontrolünde
*   **Maksimum Kare Hızı (Max Frame Rate):** Kapalı *(FPS sınırlaması oyun içinden yapılmalıdır).*
*   **Masaüstü Derinlik Optimizasyonu (OpenGL):** Otomatik
*   **Tercih Edilen Yenileme Hızı:** En Yüksek Kullanılabilir

---

## 2. Masaüstü Renk Ayarları (Dijital Doygunluk - Digital Vibrance)

CS2'de düşman modellerinin haritada daha net seçilebilmesi için renk doygunluğunun artırılması kritik önem taşır.

1.  NVIDIA Denetim Masası sol menüsünden **Masaüstü Renk Ayarlarını Ayarla** sekmesine girin.
2.  **Digital Vibrance (Dijital Doygunluk)** değerini varsayılan %50 seviyesinden **%70 - %80** aralığına getirin.
3.  Bu ayar, oyundaki karanlık alanların ve renk paletlerinin belirginliğini artırarak reaksiyon sürenizi iyileştirir.

---

## 3. NVIDIA Reflex ve Sistem Gecikmesi (Input Lag) Optimizasyonu

CS2, NVIDIA Reflex teknolojisini yerleşik olarak destekler. NVIDIA Denetim Masası'ndaki gecikme modları yerine oyun içi Reflex mimarisini kullanmak daha kararlı sonuçlar verir.

*   **NVIDIA Reflex Low Latency (Oyun İçi):** **Açık (Enabled)** veya **Açık + Takviye (Enabled + Boost)**
    *   **Açık:** Sistem gecikmesini minimuma indirir.
    *   **Açık + Takviye:** İşlemci (CPU) darboğazı yaşanan senaryolarda ekran kartı saat hızlarını en üst seviyede tutarak gecikmeyi daha da düşürür. Ekran kartı sıcaklığınızı göz önünde bulundurarak "Açık + Takviye" modunu tercih edebilirsiniz.

---

## 4. CS2 Oyun İçi Grafik Ayarları ile NVIDIA Senkronizasyonu

NVIDIA Denetim Masası'nda yapılan ayarların tam performans vermesi için oyun içi grafik konfigürasyonunun aşağıdaki gibi ayarlanması gerekir:

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır** | Etkin | Düşman siluetlerini belirginleştirir. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı | Input lag oluşumunu engeller. |
| **Çoklu Örneklemeli Kenar Yumuşatma Modu** | 2X MSAA veya 4X MSAA | Pikselleşmeyi önler, GPU yükünü dengeler. |
| **Gölge Kalitesi** | Orta (Medium) | Düşman gölgelerini görmeyi sağlar, FPS'i düşürmez. |
| **Model / Doku Detayı** | Düşük (Low) | Gereksiz VRAM kullanımını önler. |
| **Çevre Aydınlatma (Ambient Occlusion)** | Devre Dışı | Görsel derinliği azaltır, görüşü netleştirir. |
| **Yansıma Detayı** | Düşük (Low) | Yansıma hesaplamalarını kaldırarak FPS kazandırır. |
| **Parçacık Detayı** | Düşük (Low) | Sis ve patlamalardaki FPS düşüşlerini engeller. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (En Yüksek Kalite) | Görüntüde bulanıklığa yol açar. Doğal çözünürlük kullanılmalıdır. |

---

## 5. NVIDIA GeForce Experience ve Sürücü Optimizasyonu

1.  **Sürücü Güncelliği:** CS2 için yayınlanmış en güncel **Game Ready** sürücüsünü kullanın. Güncel olmayan sürücüler Source 2 motorunda bellek sızıntılarına (memory leak) yol açabilir.
2.  **GeForce Experience İçi Yer Paylaşımı (Overlay):** Oyun içi yer paylaşımı (ShadowPlay/Alt+Z menüsü) anlık FPS düşüşlerine (stutter) sebep olabilir. Performans odaklı sistemlerde **Ayarlar > Genel > Oyun İçi Yer Paylaşımı** seçeneğini **Kapalı** konuma getirin.
3.  **Otomatik Oyun Optimizasyonu:** GeForce Experience'ın oyun ayarlarını otomatik optimize etmesine izin vermeyin. Bu özellik genellikle grafik kalitesini önceler ve FPS kaybına neden olur.

---

## 6. CS2 Başlatma Seçenekleri (Launch Options)

NVIDIA ayarlarını desteklemek amacıyla Steam üzerinden CS2 başlatma seçeneklerine aşağıdaki parametreleri ekleyin:

```text
-high -threads [Çekirdek_Sayısı+1] -novid -nojoy +fps_max 0
```

*   `-high`: İşlemci önceliğini oyuna verir.
*   `-novid`: Başlangıç videosunu atlar.
*   `-nojoy`: Joypad/Joystick desteğini kapatarak RAM kullanımını azaltır.
*   `+fps_max 0`: Oyun içi FPS limitini kaldırır (Monitör yenileme hızınızın çok üzerinde FPS alıyorsanız, yırtılmaları önlemek ve tutarlı gecikme sağlamak için monitör HZ değerinizin 2 katına sabitleyebilirsiniz, örn: `+fps_max 400`).