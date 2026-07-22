# Valorant Düşük Sistem Ayarları: Maksimum FPS ve En Düşük Gecikme Rehberi

Valorant, Unreal Engine 4 motoru üzerinde çalışan ve büyük ölçüde İşlemci (CPU) performansına dayalı bir FPS oyunudur. Düşük konfigürasyonlu sistemlerde (düşük RAM, entegre grafik kartı veya eski nesil işlemciler) kararlı bir kare hızı (FPS) elde etmek ve girdi gecikmesini (input lag) en aza indirmek için oyun içi ayarların ve sistem optimizasyonlarının doğru yapılandırılması kritik önem taşır.

Bu rehber, sistem kaynaklarını en az seviyede kullanarak maksimum FPS elde etmenizi sağlayacak teknik ayarları içermektedir.

---

## 1. Valorant Oyun İçi Grafik Ayarları

Oyun içi grafik ayarlarında temel hedef, Ekran Kartı (GPU) üzerindeki yükü sıfırlayarak işlemcinin kare işleme süresini (Frame Time) düşürmektir.

### Genel Ekran Ayarları
*   **Görüntü Modu:** Tam Ekran (Pencereli veya Sınırlandırılmış Tam Ekran modları Windows masaüstü yöneticisini araya sokarak girdi gecikmesini artırır).
*   **Çözünürlük:** Monitörün yerel çözünürlüğü (Örn: 1920x1080). GPU sınırına takılan çok düşük sistemlerde `1280x720` veya `1024x768` seviyesine çekilebilir.
*   **Görüntü Boyutu Yöntemi:** Doldur (Fill).
*   **FPS Sınırlama (Tüm Seçenekler):** Kapalı. (FPS sabitlemek sistem gecikmesini artırabilir, işlemci ısınma sorunu yoksa sınırsız bırakılmalıdır).

### Grafik Kalitesi Ayarları

| Ayar | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Materyal Kalitesi** | Düşük | Yüzey kaplamalarının detayını düşürür, VRAM kullanımını azaltır. |
| **Doku Kalitesi** | Düşük | Doku veri boyutunu düşürerek VRAM bant genişliğini rahatlatır. |
| **Detay Kalitesi** | Düşük | Haritadaki ikincil nesneleri azaltır, CPU işleme yükünü hafifletir. |
| **Arayüz Kalitesi** | Düşük | HUD elemanlarının işlenme kalitesini düşürür. |
| **Vinyet (Vignette)** | Kapalı | Ekran kenarlarındaki gölgelemeyi kapatır, GPU yükünü azaltır. |
| **VSync (Dikey Eşitleme)** | Kapalı | **Kesinlikle Kapalı.** Ekran yırtılmasını önler ancak ciddi girdi gecikmesi yaratır. |
| **Kenar Yumuşatma (Anti-Aliasing)** | Hiçbiri (veya FXAA) | MSAA yerine FXAA kullanılabilir; ancak en yüksek FPS için tamamen kapatılmalıdır. |
| **Eşyönsüz Filtreleme** | 1x | Dokuların uzak mesafedeki netliğini belirler, 1x seviyesi GPU'yu yormaz. |
| **Netliği Arttır** | Kapalı | Piksel kontrastını artırır, ekstra GPU işleme gücü tüketir. |
| **Deneysel Keskinleştirme** | Kapalı | Görüntüye ek keskinleştirme filtresi uygular, kapatılmalıdır. |
| **Işık Patlaması (Bloom)** | Kapalı | Silah efektleri ve parlaklıktaki görsel haleleri kapatır. |
| **Bozulma (Distortion)** | Kapalı | Patlama ve yetenek alanlarındaki kırılma efektlerini kapatır. |
| **Gölgeleri Dök** | Kapalı | Karakter ve nesne gölgelerinin detayını kapatarak FPS'i artırır. |

### Gelişmiş Grafik Ayarları
*   **NVIDIA Reflex Düşük Gecikme:** Açık + Takviye (On + Boost). İşlemcinin ekran kartını bekleme süresini azaltır ve CPU darboğazını minimize eder.
*   **İzlekli İşleme (Multithreaded Rendering):** **Açık.** (İşlemciniz 8 mantıksal çekirdek veya üzerindeyse bu ayar FPS'i doğrudan artırır).

---

## 2. Windows ve Donanım Optimizasyonları

Oyun dışı sistem ayarlarının yapılandırılması, Valorant'ın sistem kaynaklarına doğrudan ve öncelikli erişim sağlamasına yardımcı olur.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `VALORANT-Win64-Shipping.exe` dosyasını bulun (Varsayılan: `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64`).
2. Dosyaya sağ tıklayıp **Özellikler** > **Uyumluluk** sekmesine gidin.
3. **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
4. **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçekleme davranışını geçersiz kıl"** kutucuğunu işaretleyip "Uygulama" olarak ayarlayın.

### Windows Oyun Modu ve Grafik Ayarları
*   **Windows Oyun Modu:** `Ayarlar > Oyun > Oyun Modu` yolunu izleyerek **Açık** konuma getirin. Bu, arka plan işlemlerinin kaynak kullanımını kısıtlar.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar > Sistem > Monitör > Grafik Ayarları` altından **Açık** duruma getirin (Yeniden başlatma gerektirir).

### Güç Planı Ayarı
*   `Denetim Masası > Güç Seçenekleri` yolunu izleyin.
*   Planı **Yüksek Performans** veya (varsa) **Nihai Performans** olarak seçin. Bu işlem işlemci frekansının dinamik olarak düşmesini engeller.

---

## 3. Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve Program Ayarlarından Valorant'ı seçin.
3. Aşağıdaki değerleri uygulayın:
    *   **Güç Yönetim Modu:** Maksimum performansı tercih et.
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık.
    *   **Doku Süzme - Kalite:** Yüksek Performans.
    *   **Eşyönsüz Süzme İyileştirmesi:** Açık.
    *   **Önceden Oluşturulan Maksimum Kare Sayısı:** 1.
    *   **Dikey Senkronizasyon:** Kapalı.

### AMD Radeon Software Ayarları
1. **AMD Radeon Software** uygulamasını açın.
2. **Ekran Kartları (Graphics)** sekmesine gelin.
3. **Radeon Anti-Lag:** Etkin.
4. **Radeon Boost:** Devre Dışı (Çözünürlüğü dinamik değiştirdiği için gecikme yapabilir).
5. **Ekran Kartı Profili:** Performans.
6. **Doku Filtreleme Kalitesi:** Performans.

---

## 4. Valorant Config Dosyası (Çözünürlük Ölçeği Düşürme)

Çok düşük seviye entegre grafik kartlarında (Intel HD Graphics vb.) oyun içi menüden düşürülemeyen render çözünürlüğü config dosyası üzerinden manuel olarak düşürülebilir.

1. `Windows + R` tuşlarına basarak **Çalıştır** penceresini açın.
2. `%LOCALAPPDATA%\VALORANT\Saved\Config` yazın ve Enter'a basın.
3. Rastgele rakamlardan oluşan klasöre girin ve `Windows` klasörü altındaki `GameUserSettings.ini` dosyasını Not Defteri ile açın.
4. `[ScalabilityGroups]` başlığı altındaki şu değerleri değiştirin:
   ```ini
   sg.ResolutionQuality=80.000000
   sg.ViewDistanceQuality=0
   sg.AntiAliasingQuality=0
   sg.ShadowQuality=0
   sg.PostProcessQuality=0
   sg.TextureQuality=0
   sg.EffectsQuality=0
   sg.FoliageQuality=0
   ```
*(Not: `sg.ResolutionQuality` değerini 100'den 80 veya 70 seviyesine çekmek, oyunun işleme çözünürlüğünü düşürerek GPU yükünü ciddi oranda azaltır ancak pikselleşmeye neden olur.)*

---

## 5. Sistem Belleği (RAM) ve Arka Plan Temizliği

Valorant, Riot Vanguard hile koruma sistemiyle birlikte çalıştığı için arka plandaki diğer uygulamalara karşı hassastır.
*   **RAM Kullanımı:** 8 GB RAM'e sahip sistemlerde Discord (Donanım İvmesi kapalı olmalı), Chrome ve Spotify gibi uygulamalar oyun esnasında kapatılmalıdır.
*   **Vanguard Etkileşimi:** Arka planda çalışan üçüncü taraf overlay (Arayüz gösterimi) yazılımları (Overwolf, RivaTuner, Discord Overlay vb.) kapatılmalıdır. Bu yazılımlar işlemciye ek yük bindirir ve gecikmeyi artırır.