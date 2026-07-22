# CS2 En İyi Ayarlar: Maksimum FPS ve Rekabetçi Grafik Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte görsel kalitesini önemli ölçüde artırırken, sistem kaynaklarına olan ihtiyacı da yükseltti. Rekabetçi bir FPS oyununda yüksek kare hızı (FPS) ve düşük girdi gecikmesi (input lag), görsel kaliteden çok daha kritik bir role sahiptir. 

Bu rehber; oyun içi grafik, ses, fare, sistem ve Nvidia/AMD sürücü ayarlarını teknik detaylarıyla optimize ederek en yüksek FPS ve en düşük gecikmeyi elde etmenizi sağlamak amacıyla hazırlanmıştır.

---

## 1. Gelişmiş Video Ayarları (Maksimum FPS ve Görüş Avantajı)

CS2’de grafik ayarları yapılırken temel hedef; akıcılığı korumak, düşmanların arka plandan ayırt edilmesini kolaylaştırmak ve gölgeler üzerinden bilgi edinmektir.

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama / Sebebi |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | İşletim sisteminin masaüstü pencere yöneticisini (DWM) devre dışı bırakarak girdi gecikmesini minimuma indirir. |
| **Çözünürlük** | 1280x960 veya 1920x1080 | 4:3 (1280x960 Stretched) çözünürlük oyuncu modellerini genisleterek hedef almayı kolaylaştırır ve FPS'i artırır. 16:9 (1080p) ise daha geniş bir bakış açısı (FOV) sunar. |
| **Yenileme Hızı (Hz)** | Maksimum (144Hz / 240Hz+) | Monitörünüzün desteklediği en yüksek değeri seçin. |
| **Gelişmiş Karakter Kaplaması** | Açık (Enabled) | Karakterlerin karanlık alanlarda ve karmaşık kaplamalarda kontrastını artırarak görünürlüğü sağlar. FPS etkisi düşüktür. |
| **Çoklu Sunucu Kenar Yumuşatma (MSAA)** | 2x MSAA veya 4x MSAA | CS2'de MSAA kapatılırsa kenarlar çok fazla pikselleşir (aliasing). 2x veya 4x, performans ile görsel netlik arasındaki en iyi dengedir. |
| **Küresel Gölge Kalitesi** | **Yüksek (High)** | **Kritik Ayar:** Düşük veya Orta seviyede köşe arkasındaki oyuncuların gölgeleri çizilmez. Yüksek ayar, düşmanın yaklaşmakta olduğunu gölgesinden anlamanızı sağlar. |
| **Model / Doku Detayı** | Düşük (Low) | Ekran kartı (VRAM) yükünü azaltır, gereksiz görsel detayları temizler. |
| **Doku Süzme Modu** | Çift Çizgili (Bilinear) veya 4x | Bilinear veya Anisotropic 4x, performans kaybı yaratmadan kaplamaların net görünmesini sağlar. |
| **İnce Detay (Shader) Detayı** | Düşük (Low) | Cam, su ve ışık yansımalarının işlemci/ekran kartı üzerindeki yükünü azaltır. |
| **Parçacık Detayı** | Düşük (Low) | Molotof ve sis bombalarının içindeki efekt yükünü azaltarak patlama anlarındaki FPS düşüşlerini önler. |
| **Ortam Kapatma (Ambient Occlusion)** | Devre Dışı (Disabled) | Temassız gölgeleri hesaplar. Kapalı olması hem FPS kazandırır hem de karanlık bölgeleri daha aydınlık yapar. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (Disabled - En Yüksek Kalite) | FSR, görüntüyü alt çözünürlükte işleyip ölçeklendirir. CS2'de çamurlu/bulanık bir görüntüye ve ciddi görsel bozulmalara yol açtığı için kapatılmalıdır. |
| **NVIDIA Reflex Düşük Gecikme** | **Açık + Takviye (Enabled + Boost)** | GPU saat hızlarını maksimumda tutarak işlemci-ekran kartı arasındaki kuyruk gecikmesini (render queue) minimize eder. |

---

## 2. Ses Ayarları (Adım ve Ses Konumlandırma)

CS2'deki ses motoru, sesin geldiği yönü ve yüksekliği tespit etmek üzerine yeniden tasarlandı.

*   **Ses Profili:** **Crisp (Keskin)** veya **Natural (Doğal)**
    *   *Crisp*, yüksek frekansları (adım ve silah doldurma sesleri) öne çıkarır.
*   **Sol/Sağ İzolasyon (L/R Isolation):** **%50 - %70**
    *   %0 değerinde sesler tamamen birleştirilir, %100 değerinde ise sol kulağa gelen ses sağdan hiç duyulmaz. %50-70 arası ideal mekânsal derinlik sağlar.
*   **Perspektif Düzeltme (Perspective Correction):** **Hayır (No)**
    *   Kameranın açısına göre sesi bükmez, ses kaynağının gerçek konumunu daha doğru iletir.

---

## 3. Fare ve Hassasiyet (Sensitivity) Ayarları

CS2, "Sub-tick" mimarisiyle çalıştığı için fare girdileri milisaniyelik hassasiyetle işlenir.

*   **DPI:** 400 veya 800 DPI (Sensörün en kararlı çalıştığı aralık).
*   **Oyun İçi Hassasiyet:** 800 DPI için 1.0 - 1.5 arası (eDPI: 800 - 1200 ideal rekabetçi aralıktır).
    *   *Formül:* $eDPI = DPI \times Oyun\ İçi\ Sens$
*   **Windows İşaretçi Hassasiyeti:** 6/11
*   **İşaretçi Hassasiyetini Artır (Acceleration):** **Kapalı** (Kas hafızasının gelişimi için ivme kesinlikle kapalı olmalıdır).

---

## 4. Ekran Kartı Denetim Masası Ayarları

### NVIDIA Denetim Masası
1. **Masaüstüne sağ tıklayın** ve *NVIDIA Denetim Masası*nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve *Program Ayarları*ndan CS2'yi (`cs2.exe`) seçin.
3. Aşağıdaki ayarları uygulayın:
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık (Ultra, bazı sistemlerde mikro takılmalara neden olabilir, "Açık" en stabil seçenektir).
   * **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
   * **Dokusal Süzme - Kalite:** Yüksek Performans.
   * **Dikey Eşitleme (V-Sync):** Kapalı.
   * **Threaded Optimization (Eşzamanlı İş Parçacığı Optimizasyonu):** Açık.

### AMD Software: Adrenalin Edition
1. **Ekran Kartları (Graphics)** sekmesine gidin.
2. **Radeon Anti-Lag:** Açık (Girdi gecikmesini düşürür).
3. **Radeon Boost:** Kapalı.
4. **Radeon Image Sharpening:** Açık (%10 - %20 arası, bulanıklığı gidermek için).
5. **Dikey Yenileme İçin Bekle (V-Sync):** Her zaman kapalı.

---

## 5. CS2 Başlatma Seçenekleri (Launch Options)

CS:GO'daki birçok komut CS2 (Source 2) motorunda artık geçersizdir. Sistemi yormayan ve stabilite sağlayan güncel başlatma kodları şunlardır:

```text
-novid -high -threads [Çekirdek Sayısı+1] +cl_interp_ratio 1
```

* **`-novid`:** Açılış logosunu atlar, oyunun daha hızlı açılmasını sağlar.
* **`-high`:** İşlemci önceliğini CS2'ye verir (Sistemde arkada çalışan uygulamalar varsa stabilite sağlar).
* **`-threads X`:** İşlemcinizin fiziksel çekirdek sayısına 1 ekleyerek yazın (Örn: 6 çekirdekli işlemci için `-threads 7`). Source 2 motorunun izlek yönetimini optimize eder.

---

## 6. Oyun İçi Arayüz ve Telemetri (HUD)

Rekabetçi avantaj sağlamak için ağ durumunu ve sistem performansını anlık takip etmek kritik önem taşır.

* **FPS ve Ağ Durumunu Göster (Telemetri):** *Ayarlar > Oyun > Telemetri* yolunu izleyin.
  * **FPS Göstergesi:** Daima Açık.
  * **Ping / Paket Kaybı (Loss):** Yalnızca Kötü Bağlantıda veya Daima Açık.
* **Radar Yakınlaştırması (Radar Hud Scale):** **0.35 - 0.45**
  * Radarın tüm haritayı kapsamasını sağlar. Böylece haritanın diğer ucunda beliren bir düşmanı veya düşen bombayı anında görebilirsiniz.
* **Döndürülebilir Radar:** **Açık**

---

## Özet Performans Kontrol Listesi

1. Windows **Oyun Modu (Game Mode)** özelliğini **Açık** konuma getirin.
2. Arka planda çalışan Discord, Chrome gibi uygulamaların **Donanım İvmesi (Hardware Acceleration)** özelliklerini kapatın.
3. CS2'yi kurduğunuz diskin **NVMe SSD** olduğundan emin olun; Source 2 motoru kaplama yüklemelerini anlık olarak diskten çeker, HDD kullanımı takılmalara (stuttering) yol açar.
4. Oyun içindeki **Gelişmiş Karakter Kaplaması** ve **Küresel Gölge Kalitesi (Yüksek)** dışındaki tüm detayları Düşük/Kapat konumuna getirerek maksimum FPS ve en net görüşü elde edin.