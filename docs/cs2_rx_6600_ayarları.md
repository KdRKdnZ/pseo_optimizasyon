# CS2 RX 6600 En İyi Grafik ve FPS Ayarları Rehberi

AMD Radeon RX 6600 (8 GB GDDR6, RDNA 2 mimarisi), 1080p çözünürlükte Counter-Strike 2 (CS2) için oldukça güçlü ve fiyat/performans oranı yüksek bir ekran kartıdır. Ancak CS2'nin Source 2 motoruna geçişiyle birlikte artan GPU yükü ve değişen ışıklandırma dinamikleri, doğru optimizasyonu zorunlu kılmaktadır. 

Bu rehber; RX 6600 ekran kartınızdan maksimum FPS, minimum input lag (girdi gecikmesi) ve optimum rakip görünürlüğü elde etmeniz için hazırlanmış teknik optimizasyon rehberidir.

---

## 1. CS2 Oyun İçi Grafik Ayarları

CS2'de grafik ayarları yapılırken temel hedef; akıcılığı (FPS) artırırken taktiksel avantaj sağlayan gölge ve karakter netliği detaylarını korumaktır.

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama / Sebebi |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Kontrastı** | **Etkin** | Rakiplerin karanlık arka planlarda net görünmesini sağlar. FPS etkisi yok denecek kadar azdır. |
| **Dikey Eşitleme (VSync)** | **Devre Dışı** | Input lag oluşturur. Kesinlikle kapatılmalıdır. |
| **Gelişmiş Anti-Aliasing Modu** | **CMAA2** veya **MSAA 2x** | CS2'de TAA yerine CMAA2 veya 2x MSAA tercih edilmelidir. RX 6600, 2x MSAA'yı performans kaybı olmadan rahatça işler. |
| **Evrensel Gölge Kalitesi** | **Yüksek (High)** | **Taktiksel Önemi Var:** Rakiplerin köşelerden yaklaşırken gölgelerini önceden görmenizi sağlar. Düşük yapılması tavsiye edilmez. |
| **Model ve Doku Detayı** | **Düşük (Low)** | GPU bellek veri yolunu rahatlatır, FPS dalgalanmasını (1% Low FPS) azaltır. |
| **Doku Filtreleme Modu** | **Anizotropik 4x** | Doku netliğini artırır. RX 6600 bellek bant genişliği için 4x ideal dengedir. |
| **Shader Detayı** | **Düşük (Low)** | Gereksiz yansımaları ve GPU yükünü azaltır, FPS'i doğrudan yükseltir. |
| **Parçacık Detayı** | **Düşük (Low)** | Molotof ve sis bombalarının içinden/kenarından geçerken yaşanan FPS düşüşlerini önler. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı** | Gölgelendirme derinliği ekler ancak belirgin FPS düşüşü ve girdi gecikmesi yaratır. |
| **Yüksek Dinamik Aralık (HDR)** | **Kalite (Quality)** | "Performans" modu renk paletini bozabilir. Kalite modu RX 6600'de stabil çalışır. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (En Yüksek Kalite)** | FSR 1.0/2.0 görüntüyü bulanıklaştırır ve kenar tespitini zorlaştırır. RX 6600 yerel (Native) çözünürlükte yeterince güçlüdür. |

---

## 2. AMD Software: Adrenalin Edition Ayarları

RX 6600’ün yazılım tarafındaki optimizasyonu, sürücü kaynaklı gecikmeleri sıfıra indirmek için kritik önem taşır. **AMD Software > Oyun > Counter-Strike 2** sekmesinden şu ayarları uygulayın:

* **Radeon Anti-Lag:** **Etkin (Enabled)**
  * *İşlev:* İşlemci ile ekran kartı arasındaki senkronizasyonu düzenleyerek girdi gecikmesini düşürür.
* **Radeon Chill:** **Devre Dışı (Disabled)**
  * *İşlev:* FPS'i kısıtlayarak güç tasarrufu sağlar ancak rekabetçi oyunlarda akıcılığı bozar.
* **Radeon Boost:** **Devre Dışı (Disabled)**
  * *İşlev:* Hareket anında çözünürlüğü düşürür; CS2 gibi piksel hassasiyeti gerektiren oyunlarda pikselleşmeye yol açar.
* **Radeon Image Sharpening (RIS):** **Etkin (%80 - %90)**
  * *İşlev:* CS2'nin kenar yumuşatmasından kaynaklanan hafif bulanıklığı giderir. RX 6600 üzerinde sıfır performans kaybı ile keskin görüntü sunar.
* **Ekran Kartı Uyumluluğu / Görüntü Ölçekleme:** **Kapat**
* **Dikey Yenileme İçin Bekleyin (VSync):** **Her Zaman Devre Dışı**
* **Doku Filtreleme Kalitesi:** **Performans**
* **Yüzey Biçim Optimizasyonu:** **Etkin**

---

## 3. Donanım Seviyesinde Kritik Ayar: Smart Access Memory (SAM) / ReBAR

AMD Radeon RX 6600, PCIe 4.0 x8 hattını kullanır. İşlemcinizin ekran kartı belleğinin (VRAM) tamamına tek seferde erişmesini sağlayan **Smart Access Memory (SAM)** özelliğinin açık olması, CS2'deki anlık takılmaları (stutter) engeller.

1. Bilgisayarınızı yeniden başlatıp BIOS'a girin.
2. **Above 4G Decoding** seçeneğini **Enabled** yapın.
3. **Re-Size BAR Support** seçeneğini **Auto/Enabled** yapın.
4. AMD Adrenalin yazılımından *Performans > Ayarlanıyor* sekmesine giderek **Smart Access Memory**'nin "Etkin" olduğunu doğrulayın.

---

## 4. Steam CS2 Başlatma Seçenekleri (Launch Options)

Source 2 motoru eski komutların birçoğunu desteklememektedir. Sistem kaynaklarını doğru yönlendirmek için sadece çalışan şu komutları ekleyin:

**Kullanılacak Kod dizini:**
```text
-high -threads 17 -novid -nojoy +cl_updaterate 128 +cl_cmdrate 128
```

* **`-high`:** İşlemci önceliğini CS2'ye verir.
* **`-threads [Çekirdek Sayısı + 1]`:** İşlemci izlek (thread) atamasını optimize eder. *(Örn: Ryzen 5 5600 [6C/12T] kullanıyorsanız değeri `-threads 13` veya doğrudan fiziksel çekirdek sayısı için zorlayabilirsiniz).*
* **`-novid`:** Açılış introsunu atlar.
* **`-nojoy`:** Joystick/Gamepad desteğini kapatarak RAM kullanımını azaltır.

---

## 5. Performans Benchmark Beklentileri (RX 6600 + Ryzen 5 5600)

Yukarıdaki ayarlar uygulandığında, RX 6600 ve dengeli bir işlemci konfigürasyonunda elde edilecek ortalama performans değerleri şu şekildedir:

* **1080p Native (1920x1080 - Rekabetçi Ayarlar):**
  * **Ortalama FPS:** 240 - 320 FPS
  * **%1 Low FPS:** 140 - 180 FPS
* **4:3 Stretched (1280x960 / 1440x1080 - Rekabetçi Ayarlar):**
  * **Ortalama FPS:** 310 - 420 FPS
  * **%1 Low FPS:** 190 - 240 FPS

**Sonuç:** RX 6600, CS2'de doğru sürücü ve grafik yapılandırması ile 144 Hz, 180 Hz ve 240 Hz monitörlerin tazeleme hızlarını rahatlıkla besleyebilecek kapasitededir.