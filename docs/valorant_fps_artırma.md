# Valorant FPS Artırma Rehberi: Donanım ve Yazılım Optimizasyon Teknikleri

Riot Games'in taktiksel yayıncı oyunu Valorant, işlemci (CPU) odaklı bir mimariye sahiptir. Oyunda yüksek ve kararlı bir FPS (Saniye Başına Kare) elde etmek, yalnızca grafik kartını (GPU) zorlamakla değil, sistem gecikmesini (input lag) en aza indirmek ve işlemci darboğazlarını önlemekle mümkündür. 

Bu rehberde, Valorant'ta kare hızınızı maksimuma çıkarmak ve 1% FPS düşüşlerini (takılmaları) engellemek için uygulayabileceğiniz teknik optimizasyon adımları yer almaktadır.

---

## 1. En Optimal Oyun İçi Grafik Ayarları

Valorant'ta grafik ayarlarını düşürmek, yükü GPU'dan alarak CPU'nun kareleri daha hızlı işlemesini sağlar.

* **Görüntü Modu:** Tam Ekran *(Pencereli veya Çerçevesiz Tam Ekran, Windows DWM bileşenini devreye sokarak gecikmeye ve FPS düşüşüne neden olur).*
* **Çözünürlük:** Monitörün yerel (native) çözünürlüğü veya performansı artırmak için $1690 \times 1080$ / $1280 \times 720$.
* **Materyal / Doku / Detay / Arayüz Kalitesi:** Düşük
* **V-Sync (Dikey Eşitleme):** Kapalı *(Girdi gecikmesini ciddi oranda artırır).*
* **NVIDIA Reflex Düşük Gecikme:** Açık + Takviye (On + Boost) *(İşlemci ve ekran kartı arasındaki senkronizasyonu optimize ederek sistem gecikmesini düşürür).*
* **Kenar Yumuşatma (Anti-Aliasing):** Hiçbiri veya MSAA 2x
* **Eşyönsüz Filtreleme (Anisotropic Filtering):** 1x
* **Netliği Artır (Improve Clarity):** Kapalı
* **Deneysel Keskinleştirme (Experimental Sharpening):** Kapalı
* **Bloom / Bozulma / Gölgeler:** Kapalı

---

## 2. Windows İşletim Sistemi Optimizasyonları

Windows'un arka plan süreçleri, Valorant gibi işlemciye yük binen oyunlarda anlık takılmalara (stuttering) yol açar.

### Oyun Modu ve Grafik Ayarları
1. **Windows Oyun Modu:** Arama çubuğuna "Oyun Modu Ayarları" yazın ve **Açık** konuma getirin.
2. **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** *Ayarlar > Grafik Ayarları* yolunu izleyin. HAGS'ı **Açık** hale getirin (Sisteminizde VRAM kısıtlıysa performansı artırır).
3. **Grafik Performansı Tercihi:** Aynı menüden Valorant'ın çalıştırılabilir dosyasını (`VALORANT-Win64-Shipping.exe`) ekleyin ve **Yüksek Performans** olarak ayarlayın.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64` dizinine gidin.
2. `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayıp **Özellikler**'e girin.
3. **Uyumluluk** sekmesinde **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçekleme davranışını geçersiz kıl** seçeneğini aktif edip **Uygulama** olarak ayarlayın.

### Güç Planı Optimizasyonu
1. `Windows + R` tuşlarına basıp `powercfg.cpl` yazın.
2. Güç planını **Yüksek Performans** veya (varsa) **Nihai Performans** olarak seçin.
   *(Nihai Performans modunu açmak için CMD'ye komutunu girin: `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`)*

---

## 3. Ekran Kartı Denetim Masası Ayarları

### NVIDIA Denetim Masası
1. **Masaüstüne sağ tıklayın** ve NVIDIA Denetim Masası'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin:
   * **Bağlantılı Optimizasyon (Threaded Optimization):** Açık *(Çok çekirdekli işlemciler için kritiktir).*
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra.
   * **Güç Yönetimi Modu:** Maksimum performansı tercih et.
   * **Doku Süzme - Kalite:** Yüksek Performans.
   * **Doku Süzme - Trilinear Optimizasyon:** Açık.

### AMD Radeon Software
1. AMD Radeon Software panelini açın ve **Oyunlar > Valorant** sekmesine gidin.
2. **Radeon Anti-Lag:** Etkin.
3. **Radeon Boost:** Devre Dışı *(Dinamik çözünürlük ölçeklemesi Valorant'ta bulanıklığa ve tutarsız FPS'e neden olur).*
4. **Doku Filtreleme Kalitesi:** Performans.

---

## 4. Donanım Seviyesinde Kritik Dokunuşlar: RAM ve CPU

Valorant, RAM frekansına ve gecikme sürelerine (CL değerleri) doğrudan tepki veren bir oyundur.

* **XMP / EXPO Profilini Etkinleştirin:** BIOS menüsüne girerek RAM'lerinizin fabrika çıkışlı yüksek frekans değerlerinde (örneğin 3200MHz, 3600MHz veya DDR5 için 6000MHz+) çalıştığından emin olun.
* **Çift Kanal (Dual-Channel) RAM Kullanımı:** Tek kanal (Single-Channel) RAM kullanımı, Valorant'ta %30 ila %50 arasında FPS kaybına ve sürekli drop yaşanmasına neden olur. Sisteminizde mutlaka çift kanal RAM konfigürasyonu kullanın.
* **Isı Değerleri ve Throttling:** İşlemci sıcaklığı kritik eşiği (genellikle 85°C-90°C) aştığında frekans düşürür (Thermal Throttling). İşlemci fan temizliği ve termal macun yenilemesi, kararlı FPS için şarttır.

---

## 5. Geçici Dosyaları Temizleme ve Sistem Bakımı

Arka planda çalışan gereksiz servisler ve biriken geçici veriler işlemci çekirdeklerini meşgul eder.

1. `Windows + R` kombinasyonu ile Çalıştır penceresini açın.
2. Sırasıyla şu komutları yazarak açılan klasörlerdeki tüm dosyaları silin:
   * `temp`
   * `%temp%`
   * `prefetch`
3. **Discord Overlay ve Overwolf:** Discord veya benzeri üçüncü taraf yazılımların "Oyun İçi Arayüz" (Overlay) özelliklerini kapatın. Bu özellikler direkt olarak kare hızından çalar.

---

## Özet FPS Kontrol Listesi

| Yapılacak İşlem | Beklenen Etki | Öncelik Seviyesi |
| :--- | :--- | :--- |
| **XMP / EXPO Açmak** | %20 - %40 FPS Artışı / Minimum Drop | **Kritik** |
| **Tam Ekran Modu & Grafik Düşürme** | %15 - %25 FPS Artışı | **Yüksek** |
| **NVIDIA / AMD Panel Ayarları** | Kararlı 1% Low FPS | **Yüksek** |
| **NVIDIA Reflex (Açık + Boost)** | Minimum Sistem Gecikmesi | **Orta-Yüksek** |
| **Arka Plan Uygulamaları Temizliği** | Drop (Takılma) Engelleme | **Orta** |