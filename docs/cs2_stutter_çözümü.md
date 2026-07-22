# CS2 Stutter (Takılma) Sorunu Çözümü: Detaylı ve Teknik Rehber

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte yüksek ortalama FPS (FPS AVG) alınsa dahi anlık takılmalar (stuttering) ve kare süresi (frametime) dalgalanmaları ile gündeme gelmektedir. CS2'deki takılma sorunu genellikle ortalama FPS düşüklüğünden değil, **%1 ve %0.1 Low FPS** değerlerinin çökmesinden kaynaklanır. 

Bu rehberde, CS2'deki anlık takılmaları ve kare süresi spikelarını ortadan kaldırmak için uygulamanız gereken teknik ve güncel çözüm adımlarını bulabilirsiniz.

---

## 1. Ekran Kartı Sürücü ve Panel Ayarları

Stuttering sorununun en büyük nedenlerinden biri gölgelendirici (Shader) derleme süreçleri ve yanlış yapılandırılmış sürücü ayarlarıdır.

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve **Program Ayarları** sekmesinden `cs2.exe` dosyasını seçin.
3. Aşağıdaki ayarları uygulayın:
   * **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** **10 GB** veya **Sınırsız (Unlimited)** *(En kritik ayardır. Varsayılan değer yetersiz kalıp takılmaya sebep olur).*
   * **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et**.
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** **Açık (On)** veya **Ultra**.
   * **Doku Süzme - Kalite:** **Yüksek Performans**.
   * **Dikey Eşitleme (V-Sync):** **Kapalı**.

### AMD Radeon Software Ayarları
1. **AMD Software** uygulamasını açın ve **Oyun > CS2** profilini seçin.
2. **Radeon Anti-Lag:** **Açık**.
3. **Radeon FreeSync:** Monitörünüze bağlı olarak test edin (Genellikle CS2'de kapalı tutulması frametime kararlılığını artırır).
4. **Shader Cache (Gölgelendirici Önbelleği):** Sürücü üzerinden sıfırlayın (Reset Shader Cache).

---

## 2. Oyun İçi Grafik Ayarlarının Optimize Edilmesi

CS2'de bazı grafik ayarları CPU/GPU yük dengesini bozarak mikro takılmalara yol açar.

* **Gelişmiş Video Ayarları:**
  * **Player Contrast (Oyuncu Kontrastını Artır):** **Devre Dışı** *(Sistemde ani FPS düşüşlerine neden olabilir).*
  * **Model / Doku Detayı:** **Orta** veya **Düşük**.
  * **Gölge Kalitesi:** **Orta** *(Çok düşük yapıldığında avantaj kaybı yaşanır, yüksek yapmak CPU'ya yük bindirir).*
  * **Parçacık Detayı:** **Düşük**.
  * **Çevre Gözlemleme (Ambient Occlusion):** **Devre Dışı**.
  * **NVIDIA Reflex Düşük Gecikme:** **Açık + Takviye (Enabled + Boost)**.
  * **FidelityFX Super Resolution (FSR):** **Devre Dışı (En Yüksek Kalite)** *(FSR açmak, ekran kartı limitli olmayan sistemlerde CPU darboğazını tetikleyip stutter yapabilir).*

---

## 3. Windows Sistem ve Kaynak Yönetimi

Windows arka plan süreçleri ve yetersiz bellek yönetimi, Source 2 motorunun gereksinim duyduğu anlık veri akışını kesintiye uğratabilir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 ve 11'de bulunan HAGS özelliği bazı sistemlerde CS2 stutter sorununu çözerken, bazılarında tetikleyebilir.
1. Windows Arama çubuğuna **Grafik Ayarları** yazın.
2. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Kapatın** (veya kapalıysa Açıp bilgisayarı yeniden başlatın ve test edin).

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. CS2'nin kurulu olduğu dizine gidin:  
   `...Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64`
2. `cs2.exe` dosyasına sağ tıklayıp **Özellikler**'e tıklayın.
3. **Uyumluluk** sekmesinde **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna basın ve **Yüksek DPI ölçeklendirme davranışını geçersiz kıl** seçeneğini işaretleyip **Uygulama** olarak ayarlayın.

### Oyun Modu ve Arka Plan Uygulamaları
* **Windows Oyun Modu:** **Açık** konumda olmalıdır.
* **Discord / Spotify Overlay:** Discord ve Spotify'ın "Donanım İvmesi" (Hardware Acceleration) ve "Arayüz" (Overlay) özelliklerini kapatın.

---

## 4. CS2 Başlatma Seçenekleri (Launch Options)

CS:GO döneminden kalan eski kodlar (`-threads`, `-high`, `-nod3d9ex` vb.) CS2'de oyunun motor yapısını bozmakta ve takılmalara yol açmaktadır. Başlatma seçeneklerinizi temizleyin.

**Önerilen Temiz Başlatma Kodu:**
```text
-nojoy
```
*(Not: Sadece `-nojoy` kullanmak, oyunun joystick/gamepad girdilerini taramasını engelleyerek arka plandaki gereksiz CPU çağrılarını keser. Diğer tüm eski komutları silin.)*

---

## 5. Shader Önbelleğini (Shader Cache) Manuel Sıfırlama

Oyun güncellemelerinden sonra eski shader dosyaları yenileriyle çakışabilir ve şiddetli takılmalara (stutter) sebep olur.

1. CS2 ve Steam'i tamamen kapatın.
2. Klavyeden `Win + R` tuşlarına basıp `%localappdata%` yazın ve Enter'a basın.
3. **NVIDIA** kullanıyorsanız: `NVIDIA\DXCache` klasörü içindeki tüm dosyaları silin.
4. **AMD** kullanıyorsanız: `AMD\DxCache` klasörünü temizleyin.
5. Steam'i açın, CS2 kütüphane sayfasına gelin -> **Özellikler > Yerel Dosyalar > Oyun Dosyalarının Bütünlüğünü Doğrula** işlemini yapın.
6. Oyuna girdiğinizde ilk 1-2 haritada shaderlar yeniden yükleneceği için hafif takılmalar olabilir, sonrasında performans stabilize olacaktır.

---

## 6. Ağ Kaynaklı Takılmaların (Network Stutter) Önlenmesi

İnternet bağlantısındaki paket kayıpları (Packet Loss) ve Jitter, donanımsal takılma ile aynı hissi yaratır.

1. CS2 Oyun İçi Ayarlar > **Oyun** sekmesine gidin.
2. **Paket Kaybını Düzeltmek İçin Tamponlama (Buffering to smooth over packet loss):** Bunu **1 Paket** veya **2 Paket** olarak ayarlayın. *(Kötü bağlantılarda anlık takılmaları (teleport/stutter) tamamen engeller).*
3. Wi-Fi yerine mutlaka **Ethernet (Kablolu)** bağlantı kullanın.

---

## Özet Performans Kontrol Listesi

| İşlem | Hedef | Beklenen Sonuç |
| :--- | :--- | :--- |
| **Shader Cache Size -> 10GB** | GPU Sürücüsü | Yükleme esnasındaki drop'ları engeller. |
| **NVIDIA Reflex -> Enabled+Boost** | Oyun İçi | Frametime süresini sabitler, gecikmeyi düşürür. |
| **Tam Ekran İyileştirmelerini Kapatma** | Windows | Giriş gecikmesini ve pencereli mod çakışmalarını önler. |
| **Eski Başlatma Kodlarını Silme** | Steam | CPU çekirdek çakışmalarını çözer. |
| **Paket Tamponlama -> 1/2 Paket** | Ağ | İnternet dalgalanması kaynaklı takılmayı çözer. |

Yukarıdaki adımlar uygulandığında CS2'deki **1% Low FPS** değerleriniz yükselecek ve karesel spikelar (stuttering) minimize edilecektir.