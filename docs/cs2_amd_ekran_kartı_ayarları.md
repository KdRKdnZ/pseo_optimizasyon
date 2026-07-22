# CS2 AMD Ekran Kartı Ayarları: En Yüksek FPS ve En Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte ekran kartı (GPU) bağımlılığı yüksek bir oyun haline gelmiştir. AMD Radeon ekran kartlarında maksimum FPS elde etmek, girdi gecikmesini (input lag) en aza indirmek ve görsel netliği korumak için sürücü ve oyun içi ayarların senkronize edilmesi kritik önem taşır.

Bu rehber, AMD Software: Adrenalin Edition ve CS2 oyun içi grafik ayarlarını teknik detaylarıyla optimize etmeniz için hazırlanmıştır.

---

## 1. AMD Software: Adrenalin Edition Ayarları

Sürücü seviyesindeki ayarlar, oyunun işleme hattına (rendering pipeline) doğrudan müdahale eder. Ayarları uygulamak için **AMD Software > Oyun > Counter-Strike 2** profiline gidin.

### Grafik Profili Ayarları

*   **Radeon Anti-Lag:** **Açık**
    *   *Teknik Açıklama:* CPU'nun GPU'dan çok fazla öne geçmesini engelleyerek kare kuyruğunu daraltır. CS2'de girdi gecikmesini ciddi oranda düşürür.
*   **Radeon Chill:** **Kapalı**
    *   *Teknik Açıklama:* Harekete bağlı olarak FPS'i dinamik sınırlar. Rekabetçi oyunlarda kare süresi (frame time) dalgalanmasına neden olduğu için kapatılmalıdır.
*   **Radeon Boost:** **Kapalı**
    *   *Teknik Açıklama:* Fare hareketi sırasında çözünürlüğü dinamik olarak düşürür. CS2 gibi piksel hassasiyeti gerektiren oyunlarda kas hafızasını ve piksel netliğini olumsuz etkiler.
*   **Radeon Image Sharpening (RIS):** **Açık (%30 - %50)**
    *   *Teknik Açıklama:* Düşük çözünürlüklerde (örneğin 1280x960 4:3 esnetilmiş) kenar yumuşatma nedeniyle oluşan bulanıklığı, performans kaybı yaşatmadan kontrast tabanlı netleştirme algoritmasıyla giderir.
*   **Radeon Enhanced Sync:** **Kapalı**
    *   *Teknik Açıklama:* Ekran yırtılmasını önlemeye çalışırken gecikme ekler.
*   **Dikey Yenileme İçin Bekle (V-Sync):** **Her Zaman Kapalı**
    *   *Teknik Açıklama:* Monitörün yenileme hızına kilitler ve yüksek oranda girdi gecikmesi yaratır.

### Gelişmiş Grafik Ayarları (AMD Adrenalin)

*   **Örtüşme Önleme (Anti-Aliasing):** **Uygulama ayarlarını kullan**
*   **Yönlü Süzme (Anisotropic Filtering):** **Kapalı** *(Oyun içinden yönetilecek)*
*   **Doku Süzme Kalitesi:** **Performans**
    *   *Teknik Açıklama:* Doku birimlerinin (TMU) yükünü hafifleterek kararlı FPS sağlar.
*   **Yüzey Biçim Eniyilemesi (Surface Format Optimization):** **Açık**
    *   *Teknik Açıklama:* Sürücünün doku biçimlerini daha hızlı işlemesine izin verir.
*   **Tessellation Modu:** **Uygulama ayarlarını aş**
*   **Maksimum Tessellation Seviyesi:** **Kapalı** veya **2x**
    *   *Teknik Açıklama:* Source 2 motorundaki karmaşık yüzey detaylarının GPU üzerindeki gereksiz geometrik yükünü sınırlar.

---

## 2. CS2 Oyun İçi Video Ayarları

CS2'deki video ayarları doğrudan kare sürelerini ve rakiplerin görünürlüğünü etkiler. **Ayarlar > Görüntü > Gelişmiş Görüntü** sekmesinden aşağıdaki konfigürasyonu uygulayın.

| Görüntü Ayarı | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran | İşletim sisteminin pencereli mod masaüstü bileşimini (DWM) baypas ederek minimum gecikme sağlar. |
| **Gelişmiş 3D Nesne Ayrıntısı** | Düşük | İşlemci ve ekran kartı arasındaki çizim çağrılarını (draw calls) azaltır. |
| **Gölge Kalitesi** | Orta | **Kritik:** "Düşük" ayarda oyuncu gölgeleri görünmez. "Orta" ayar, köşe arkasından gelen rakip gölgelerini görmenizi sağlar. |
| **Model / Doku Detayı** | Düşük | VRAM kullanımını düşürür, kare süresi kararlılığını artırır. |
| **Doku Filtreleme Modu** | Üç Doğrusal (Trilinear) | GPU bellek bant genişliği kullanımını minimize eder. |
| **Efekt Detayı** | Düşük | Molotof ve sis bombaları içindeki parçacık efektlerinin FPS düşürmesini engeller. |
| **Kaplama Detayı** | Düşük | Mermi izleri ve kan efektlerinin işleme yükünü azaltır. |
| **Çoklu Örneklemeli Örtüşme Önleme (MSAA)** | 2x MSAA veya 4x MSAA | CS2'de Anti-Aliasing tamamen kapatılırsa "sawtooth" (testere diş) etkisi oluşur ve rakipleri seçmek zorlaşır. AMD kartlarda 2x MSAA ideal performans/netlik dengesidir. |
| **FidelityFX Super Resolution (FSR)** | Kapalı (Devre Dışı) | FSR, görüntüyü alt çözünürlükten oluşturup yukarı ölçekler. Kenarlarda bozulmaya ve girdi gecikmesine yol açar. Doğal çözünürlük kullanılmalıdır. |
| **NVIDIA Reflex / AMD Anti-Lag 2** | Açık | Eğer oyun içinde AMD Anti-Lag 2 seçeneği aktifse (sürücü güncelse), doğrudan oyun içinden "Açık" konuma getirilmelidir. |

---

## 3. Ekran Ölçekleme ve 4:3 Esnetilmiş (Stretched) Ayarı

4:3 çözünürlükte esnetilmiş ekran oynamak isteyen AMD kullanıcıları için panel ölçekleme konfigürasyonu:

1. **AMD Software > Ekran** sekmesine gidin.
2. **GPU Ölçekleme (GPU Scaling):** **Açık**
3. **Ölçekleme Modu (Scaling Mode):** **Tam Panel (Full Panel)**

> **Not:** Eğer görüntüde titreme veya gecikme hissediyorsanız, ölçekleme yükünü monitöre devretmek için *GPU Ölçekleme* seçeneğini kapatıp monitör OSD menüsünden "Wide/Full" modunu seçebilirsiniz.

---

## 4. AMD Gölgelendirici Önbelleği (Shader Cache) Temizliği

CS2 güncellemelerinden sonra yaşanan anlık takılmaları (stuttering) önlemek için AMD Shader Cache belleklerinin düzenli sıfırlanması önerilir:

1. **AMD Software > Ayarlar (Dişli simgesi) > Grafik** sekmesine gidin.
2. En alt kısımda bulunan **Gelişmiş** seçeneğini genişletin.
3. **Reset Shader Cache (Gölgelendirici Önbelleğini Sıfırla)** butonuna tıklayın ve işlemi onaylayın.
4. Oyuna ilk girdiğinizde haritaların yüklenmesi birkaç saniye uzun sürebilir; bu durum gölgelendiricilerin yeniden derlenmesinden kaynaklanır ve takılmaları kalıcı olarak çözer.

---

## 5. Özet Performance Check-List

*   [x] AMD Adrenalin üzerinden **Radeon Anti-Lag** aktif edildi.
*   [x] **Radeon Boost** ve **Chill** kapatıldı.
*   [x] CS2 içi **Gölge Kalitesi "Orta"** yapıldı (Stratejik avantaj için).
*   [x] **FSR kapalı** ve **MSAA 2x** olarak ayarlandı.
*   [x] Tam ekran modunda çalıştırılıyor.