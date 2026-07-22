# CS2 Performans Rehberi: Maksimum FPS ve Düşük Gecikme (Input Lag) İçin Teknik Optimizasyon

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte GPU ve CPU kaynaklarını CS:GO’ya kıyasla çok daha yoğun kullanan bir mimariye sahip olmuştur. Bu rehber; kare hızını (FPS) artırmak, kare zamanlamasını (frame pacing) iyileştirmek ve sistem gecikmesini (input lag) en aza indirmek için uygulanması gereken teknik optimizasyon adımlarını içermektedir.

---

## 1. Oyun İçi Grafik Ayarları (In-Game Settings)

CS2'de grafik ayarları doğrudan işlemci (CPU) ve ekran kartı (GPU) yük dengesini belirler. Rekabetçi avantaj ve maksimum akıcılık için aşağıdaki konfigürasyon önerilir:

### Temel Video Ayarları
*   **Görüntü Modu:** Tam Ekran (Fullscreen) *(Pencereli modlar input lag ekler).*
*   **Çözünürlük ve Boyut Oranı:** Tercihe bağlı (4:3 Esnetilmiş veya 16:9). Düşük çözünürlük (örneğin 1280x960) GPU yükünü hafifletir ve CPU sınırına ulaşmanızı sağlar.
*   **Yenileme Hızı (Refresh Rate):** Monitörünüzün desteklediği en yüksek değer (Örn: 144Hz, 240Hz, 360Hz).

### Gelişmiş Video Ayarları
*   **Oyuncu Kontrastını Artır:** **Açık** *(Karakterlerin arka plandan ayrışmasını sağlar, performansa etkisi ihmal edilebilir düzeydedir).*
*   **Dikey Eşitleme (V-Sync):** **Devre Dışı** *(Girdi gecikmesini ciddi oranda artırır).*
*   **Çoklu Örneklemeli Kenar Yumuşatma Modu (MSAA):** **4x MSAA** veya **2x MSAA** *(Devre dışı bırakılması piksel kenarlarında titremeye yol açarak odaklanmayı zorlaştırır. 4x MSAA performans/görsellik dengesi için idealdir).*
*   **Gölge Kalitesi:** **Düşük** veya **Orta** *(Yüksek ayar, oyuncu gölgelerini daha uzak mesafeden çizer. Rekabetçi avantaj için "Orta" önerilir).*
*   **Model / Doku Detayı:** **Düşük** *(VRAM kullanımını ve GPU yükünü azaltır).*
*   **Doku Filtreleme Modu:** **Çift Çizgili (Bilinear)** veya **Eşyönsüz 4x** *(Performans etkisi çok düşüktür).*
*   **Bağlantılı Gölge Detayı (Shader Detail):** **Düşük** *(Işık yansımalarını azaltır, FPS dalgalanmalarını önler).*
*   **Parçacık Detayı (Particle Detail):** **Düşük** *(Molly ve sis bombalarının içindeki FPS düşüşlerini engeller).*
*   **Ortam Kapatma (Ambient Occlusion):** **Devre Dışı** *(Gereksiz gölgelendirme yükü oluşturur, input lag artırır).*
*   **Yüksek Dinamik Aralık (HDR):** **Performans** *(Kalite modu GPU'ya ek yük bindirir).*
*   **FidelityFX Super Resolution (FSR):** **Devre Dışı (En Yüksek Kalite)** *(FSR açmak görüntüyü bulanıklaştırır. Yalnızca çok düşük donanımlarda "Ultra Kalite" modunda kullanılmalıdır).*
*   **NVIDIA Reflex Low Latency:** **Açık + Boost** *(Ekran kartı frekansını üst seviyede tutarak sistem gecikmesini en aza indirir).*

---

## 2. CS2 Başlatma Seçenekleri (Launch Options)

CS2, Source 2 motoru kullandığı için CS:GO'dan kalma `-threads`, `-high`, `-nod3d9ex` gibi komutların çoğu işlevsizdir veya çökmelere neden olabilir. En kararlı başlatma seçenekleri şunlardır:

```text
-novid -nojoy +cl_forcepreload 1
```

*   **`-novid`:** Giriş videosunu atlayarak oyunun daha hızlı açılmasını sağlar.
*   **`-nojoy`:** Oyun kolu (joystick) desteğini kapatır, RAM kullanımını ve arka plan işlemlerini azaltır.
*   **`+cl_forcepreload 1`:** Harita yüklenirken tüm kaplamaların önceden belleğe alınmasını sağlar, oyun içi takılmaları (stutter) önler.

---

## 3. Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1.  **3D Ayarlarının Yönetilmesi** sekmesine gidin ve **Program Ayarları** altından `cs2.exe`yi seçin.
2.  Aşağıdaki değişiklikleri uygulayın:
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra
    *   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et
    *   **Maksimum Kare Hızı:** Kapalı *(FPS sınırlaması oyun içinden yapılmalıdır).*
    *   **Doku Süzme - Kalite:** Yüksek Performans

### AMD Software: Adrenalin Edition Ayarları
1.  **Oyun** > **CS2** profilini seçin.
2.  Aşağıdaki ayarları yapılandırın:
    *   **Radeon Anti-Lag:** Etkin
    *   **Radeon Boost:** Devre Dışı
    *   **Radeon Image Sharpening:** Devre Dışı (veya isteğe bağlı %10-%20)
    *   **Ekran Kartı Belleği Optimizasyonu:** Performans

---

## 4. Windows ve Sistem Optimizasyonları

### Oyun Modu ve HAGS
*   **Windows Oyun Modu:** **Açık** *(Windows 10/11 üzerinde arka plan kaynaklarını oyuna önceliklendirmede oldukça başarılıdır).*
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** **Açık** *(Ayarlar > Sistem > Monitör > Grafik Ayarları bölümünden aktifleştirin. CPU yükünü azaltır).*

### Güç Seçenekleri
*   Windows arama çubuğuna `powercfg.cpl` yazın.
*   Güç planını **Yüksek Performans** veya **Nihai Performans (Ultimate Performance)** olarak ayarlayın.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1.  `cs2.exe` dosyasının bulunduğu dizine gidin (Genellikle: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64`).
2.  `cs2.exe` dosyasına sağ tıklayıp **Özellikler** > **Uyumluluk** sekmesine geçin.
3.  **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4.  **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçeklendirme davranışını geçersiz kıl** seçeneğini aktif edip **Uygulama** olarak ayarlayın.

---

## 5. Konsol Kodları ve Autoexec Optimizasyonu

Aşağıdaki komutları oyun içi konsola yazabilir veya `autoexec.cfg` dosyanıza ekleyebilirsiniz:

```text
// FPS ve Performans
fps_max 0 // Sisteminizde dalgalanma çoksa monitör Hz değerinin 2 katına sabitleyin (Örn: 144Hz için fps_max 300)

// Ağ ve Sub-Tick İyileştirmeleri
rate 786432 // En yüksek bant genişliği ayarı (İnternet hızınız iyi ise)
cl_updaterate 128
cl_cmdrate 128

// Ses Performansı (Ses kaynaklı takılmaları önler)
snd_mixahead 0.025 // Ses gecikmesini düşürür
```

---

## 6. Performans Testi ve Takip

Yapılan optimizasyonların kararlılığını test etmek için:

1.  Konsola `cq_netgraph 1` yazarak CS2’nin yeni ağ ve kare zamanlaması grafiğini açın.
2.  Grafikteki **kırmızı ve sarı çizgiler** kare düşüşlerini (frame drop) ve paket kayıplarını gösterir. Çizgilerin sürekli **yeşil/düzgün** olması, sistemin kararlı çalıştığı anlamına gelir.
3.  Maksimum FPS'ten ziyade **%1 Low FPS** değerine odaklanın. MSI Afterburner veya CapFrameX kullanarak %1 Low değerlerinizi izleyin; bu değerlerin yüksek olması oyunun takılmadan akmasını sağlar.