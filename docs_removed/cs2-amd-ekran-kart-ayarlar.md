---
title: "cs2 amd ekran kartı ayarları"
description: "cs2 amd ekran kartı ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 AMD Ekran Kartı Ayarları: En Yüksek FPS ve Düşük Gecikme Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte ekran kartı (GPU) kaynaklarını önceki oyuna (CS:GO) kıyasla çok daha yoğun kullanmaktadır. AMD Radeon ekran kartlarında maksimum FPS, minimum girdi gecikmesi (input lag) ve net görsel görünürlük elde etmek için hem **AMD Software: Adrenalin Edition** paneli hem de oyun içi grafik ayarlarının senkronize optimize edilmesi gerekir.

---

## 1. AMD Software: Adrenalin Edition Ayarları

AMD kontrol panelindeki ayarlar, sürücü seviyesinde gecikmeyi düşürmek ve kare işleme süreçlerini optimize etmek için kritik öneme sahiptir.

Ayarlara erişmek için masaüstüne sağ tıklayıp **AMD Software: Adrenalin Edition** uygulamasını açın. **Oyun (Gaming)** > **Ekran Kartları (Graphics)** sekmesine gidin.

### Grafik Profili Ayarları

*   **Radeon Anti-Lag:** **AÇIK**
    *   *Teknik Neden:* İşlemci (CPU) ile ekran kartı (GPU) arasındaki kare kuyruğunu senkronize ederek sistem gecikmesini (system latency) düşürür. Reaksiyon süresini doğrudan iyileştirir.
*   **Radeon Chill:** **KAPALI**
    *   *Teknik Neden:* Hareket etmediğinizde FPS'i düşürerek güç tasarrufu sağlar ancak CS2 gibi rekabetçi oyunlarda ani FPS dalgalanmalarına ve takılmalara (stuttering) yol açar.
*   **Radeon Boost:** **KAPALI**
    *   *Teknik Neden:* Fare hareket ettikçe çözünürlüğü dinamik olarak düşürür. CS2'de piksel piksel adam tarama gereksinimi nedeniyle görüntüde bulanıklığa yol açar ve hedef almayı zorlaştırır.
*   **Radeon Image Sharpening (RIS):** **AÇIK (%80 - %100)**
    *   *Teknik Neden:* CS2'nin zorunlu kılınan TAA (Temporal Anti-Aliasing) kenar yumuşatma teknolojisinin getirdiği bulanıklığı giderir. Kenar netliğini artırarak düşmanların tespitini kolaylaştırır.
*   **Görüntü Oluşturma Gecikmesini Önleme (Enhanced Sync):** **KAPALI**
    *   *Teknik Neden:* Ekran yırtılmasını engeller ancak girdi gecikmesi ekler. Rekabetçi oyunlarda kesinlikle önerilmez.
*   **Dikey Yenileme İçin Bekleyin (V-Sync):** **Gelen Kutusu Dışındaysa Kapalı (Always Off)**
    *   *Teknik Neden:* Girdi gecikmesini en üst düzeye çıkardığı için V-Sync kapatılmalıdır.

### Gelişmiş Grafik Ayarları (Advanced)

*   **Doku Filtreleme Kalitesi (Texture Filtering Quality):** **Performans**
*   **Yüzey Biçim Entegrasyonu (Surface Format Optimization):** **AÇIK**
*   **Mozaikleme Modu (Tessellation Mode):** **Uygulama Ayarlarını Geçersiz Kıl**
*   **Maksimum Mozaikleme Seviyesi:** **Off (Kapalı) veya 8x** (Haritalardaki gereksiz geometrik detay yükünü GPU üzerinden alır).
*   **OpenGL Üçlü Arabelleğe Alma (OpenGL Triple Buffering):** **KAPALI**

---

## 2. AMD Ekran (Display) ve Ölçekleme Ayarları

Özellikle 4:3 çözünürlük boyutlarında (1280x960, 1024x768 vb.) "Stretched" (genişletilmiş) oynayan kullanıcılar için bu ayarlar zorunludur.

1. **AMD Software** > **Ekran (Display)** sekmesine gidin.
2. **GPU Ölçekleme (GPU Scaling):** **AÇIK** (Ölçekleme yükünü monitörden alıp GPU'ya verir, gecikmeyi azaltır).
3. **Ölçekleme Modu (Scaling Mode):**
   *   Siyah barlar olmadan oynamak için: **Tam Panel (Full Panel)**
   *   Siyah barlarla (Black Bars) oynamak için: **En Boy Oranını Korula (Preserve Aspect Ratio)**
4. **AMD FreeSync:** **KAPALI** (Yüksek FPS değerlerinde FreeSync kullanmak milisaniyelik gecikmelere sebep olabilir. Yalnızca ekran yırtılması çok rahatsız ediyorsa açılmalıdır).

---

## 3. CS2 Oyun İçi Grafik Ayarları (AMD Uyumlu)

Oyun içi grafikler, hem AMD sürücüsüyle çakışmayacak hem de maksimum FPS/görüş avantajı sağlayacak şekilde yapılandırılmalıdır.

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Kontrastı** | **Etkin (Enabled)** | Düşmanların karanlık alanlarda göze çarpmasını sağlar. Çok az performans etkisi vardır. |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı (Disabled)** | Ekran gecikmesini önler. |
| **NVIDIA Reflex / AMD Anti-Lag** | **Devre Dışı (Disabled)** | *Note:* CS2 menüsündeki bu ayar Nvidia odaklıdır. AMD Anti-Lag sürücüden yönetilmelidir. |
| **Çoklu Örneklemeli Kenar Yumuşatma Modu** | **CMAA2** veya **MSAA 2x** | CMAA2, AMD sistemlerde minimum FPS kaybı ile en net görüntüyü verir. Performans sorunu yoksa MSAA 4x yapılabilir. |
| **Evrensel Gölge Kalitesi** | **Orta (Medium) / Yüksek (High)** | Düşman gölgelerinin açılarını görmek için kritik. Düşük ayarda gölge detayları kaybolur. |
| **Model / Doku Detayı** | **Düşük (Low) / Orta (Medium)** | VRAM kullanımını düşürür, FPS istikrarı sağlar. |
| **Doku Filtreleme Modu** | **İki Çizgili (Bilinear)** veya **Anizotropik 4x** | Performans odaklı en optimize seçenektir. |
| **Parçacık Detayı** | **Düşük (Low)** | Sis ve molotof bombalarının yarattığı FPS düşüşlerini engeller. |
| **Aydınlatma (Shader) Detayı** | **Düşük (Low)** | GPU yükünü azaltır. |
| **Yüksek Dinamik Aralık (HDR)** | **Performans (Performance)** | Işık patlamalarındaki FPS düşüşünü engeller. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Kapalı - En Yüksek Kalite)** | FSR açmak görüntüyü çamurlaştırır. CS2'de rekabetçi avantaj için kapatılmalıdır (Native Çözünürlük). |

---

## 4. Windows ve AMD Sürücü Optimizasyonu

*   **Gelişmiş Arayüz (Overlay) Kapatma:** AMD Software içerisindeki `Ayarlar > Tercihler` sekmesinden **Oyun İçi Arayüz (In-Game Overlay)** seçeneğini **KAPALI** konuma getirin. Bu işlem ani FPS drop (takılma) sorunlarını büyük oranda çözer.
*   **Sürücü Durumu:** CS2, güncel sürücülere doğrudan tepki verir. Adrenalin Edition üzerinden her zaman en güncel **WHQL** onaylı AMD sürücüsünü kullanın.
*   **D3D9EX / Başlatma Seçenekleri:** CS2 Native 64-bit DirectX 11 motoru kullandığı için CS:GO'dan kalma `-high`, `-threads`, `+mat_queue_mode` gibi başlatma kodlarını kullanmayın. Bu kodlar CS2'de unstable (kararsız) FPS'e sebep olur.

### Örnek CS2 Başlatma Seçeneği:
```text
-novid -nojoy
```
*(Sadece açılış videosunu atlar ve joystick girdilerini kapatarak önbellek yükünü hafifletir.)*

---

## Özet Performans Yapılandırması

AMD sistemlerde CS2 için kilit formül: **Radeon Anti-Lag (Açık) + Radeon Image Sharpening (%80-100) + Game FSR (Kapalı)** konfigürasyonudur. Bu kombinasyon, GPU kullanımını optimize ederken Source 2 motorunun getirdiği bulanıklığı giderir ve en düşük girdi gecikmesini sağlar.