---
title: "fortnite fps artırma"
description: "fortnite fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Fortnite FPS Artırma Rehberi: En İyi Grafik ve Sistem Optimizasyon Ayarları

Fortnite, Unreal Engine 5 motoruna geçiş yaptıktan sonra sistem kaynaklarını daha yoğun kullanan bir oyun haline gelmiştir. Anlık FPS düşüşleri (stuttering/drop) ve düşük kare hızları, rekabetçi oyunda ciddi bir dezavantaj oluşturur. Bu rehberde; oyun içi grafik konfigürasyonlarından Windows optimizasyonlarına, sürücü ayarlarından kayıt defteri düzenlemelerine kadar Fortnite'ta maksimum FPS elde etmenizi sağlayacak teknik adımları bulabilirsiniz.

---

## 1. Fortnite Oyun İçi Grafik ve Performans Ayarları

Oyun içi grafik ayarları, FPS değerinizi doğrudan etkileyen en kritik faktördür. Rekabetçi avantaj ve maksimum kare hızı için aşağıdaki konfigürasyon uygulanmalıdır:

### Ekran (Display) Ayarları
* **Pencere Modu (Window Mode):** Tam Ekran (Fullscreen) *(Giriş gecikmesini en aza indirir ve GPU'nun tüm gücünü oyuna verir).*
* **Çözünürlük (Resolution):** Monitörünüzün doğal çözünürlüğü (Örn: 1920x1080).
* **Kare Hızı Limiti (Frame Rate Limit):** Monitör yenileme hızınızın (Hz) bir tık üstü. (Örn: 144Hz monitör için 160 FPS, 240Hz için 240 FPS veya Uncapped).

### Grafik Hazır Ayarları (Graphics Quality)
* **İşleme Modu (Rendering Mode):** **Performans - Düşük Grafik Sadakati (Performance - Lower Graphical Fidelity)** *(FPS artışındaki en büyük etkendir).*
* **3D Çözünürlük (3D Resolution):** %100 *(Görüntü netliğini korur; sistem çok zayıfsa %80-%90 seviyesine çekilebilir).*
* **Görüş Mesafesi (View Distance):** Yakın (Near) veya Orta (Medium).
* **Dokular (Textures):** Düşük (Low).
* **Ağlar / Karmaşık Yapılar (Meshes):** Düşük (Low) *(İnşa yapılarını basitleştirerek CPU yükünü hafifletir).*
* **Kare Hızını Göster (Show FPS):** Açık (On).
* **V-Sync (Dikey Eşitleme):** Kapalı (Off).

---

## 2. Epic Games Launcher Optimizasyonu

Fortnite çalıştırılmadan önce arka planda çalışan ve performansı etkileyen veri yüklemeleri devre dışı bırakılmalıdır.

1. **Epic Games Launcher** uygulamasını açın ve **Kütüphane**'ye gidin.
2. Fortnite’ın altındaki **üç noktaya (...)** tıklayın ve **Seçenekler (Options)** menüsünü açın.
3. **Yüksek Çözünürlüklü Kaplamalar (High-Resolution Textures):** İptal edin (İşareti kaldırın). *(Yaklaşık 30 GB disk alanı kazandırır ve VRAM kullanımını düşürür).*
4. **Akış Yapan Varlıkları Önceden Yükle (Pre-load Streamed Assets):** **İşaretleyin.** *(Oyun esnasında internet üzerinden anlık doku indirilmesini engelleyerek drop sorununu çözer).*

---

## 3. Windows Sistem Optimizasyonları

Windows işletim sisteminizin oyun performansına odaklanmasını sağlamak için şu teknik adımları uygulayın:

### Oyun Modu ve Donanım Hızlandırma
* **Windows Oyun Modu (Game Mode):** `Başlat > Ayarlar > Oyun > Oyun Modu` yolunu izleyin ve **Açık** konuma getirin.
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar > Sistem > Ekran > Grafik Ayarları` bölümünden **Açık** konuma getirin. (Sistemi yeniden başlatmanız gerekir).

### Güç Planı Ayarları
1. `Windows + R` tuşlarına basıp `powercfg.cpl` yazın ve Enter'a basın.
2. Güç planını **Yüksek Performans (High Performance)** veya varsa **Nihai Performans (Ultimate Performance)** olarak seçin.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. Fortnite'ın kurulu olduğu dizine gidin:  
   `C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64`
2. `FortniteClient-Win64-Shipping.exe` dosyasına sağ tıklayıp **Özellikler**'e girin.
3. **Uyumluluk** sekmesinde **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçeklendirme davranışını geçersiz kıl** kutucuğunu işaretleyip "Uygulama" olarak ayarlayın.

---

## 4. Ekran Kartı Sürücü Ayarları

### NVIDIA Denetim Masası Ayarları
Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın:

* **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesinden Fortnite'ı seçin:
  * **Güç Yönetimi Modu:** Maksimum performansı tercih et.
  * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık (On) veya Ultra.
  * **Doku Süzme - Kalite:** Yüksek Performans.
  * **Eşyönsüz Süzme (Anisotropic Filtering):** Kapalı.
  * **Düşey Senkronizasyon (V-Sync):** Kapalı.
  * **Maksimum Kare Hızı:** Kapalı.

### AMD Radeon Software Ayarları
AMD ekran kartı kullanıcıları için önerilen konfigürasyon:

* **Radeon Anti-Lag:** Etkin.
* **Radeon Boost:** Devre Dışı.
* **Radeon Image Sharpening:** İsteğe bağlı (%10-%20 arası netlik sağlar).
* **Anisotropik Filtreleme:** Devre Dışı.
* **Doku Filtreleme Kalitesi:** Performans.
* **Dikey Yenileme için Bekleyin (V-Sync):** Her zaman kapalı.

---

## 5. Geçici Dosyaları ve Önbelleği Temizleme

Zamanla biriken önbellek dosyaları Fortnite'ta takılmalara (stuttering) neden olur.

1. `Windows + R` tuş kombinasyonu ile Çalıştır penceresini açın.
2. Aşağıdaki komutları sırasıyla çalıştırıp açılan klasörlerdeki tüm dosyaları silin:
   * `%temp%`
   * `temp`
   * `prefetch`
3. **DirectX Önbelleğini Temizleme:** `Başlat > Disk Temizleme` uygulamasını açın, C: sürücüsünü seçin ve **DirectX Şekillendirici Önbelleği (DirectX Shader Cache)** seçeneğini işaretleyip temizleyin.

---

## 6. Fortnite Konfigürasyon Dosyası (GameUserSettings.ini) İnce Ayarı

Gelişmiş kullanıcılar için gizli grafik parametrelerini düşürmek ek FPS sağlar.

1. `Windows + R` açın ve `%localappdata%\FortniteGame\Saved\Config\WindowsClient` yazın.
2. `GameUserSettings.ini` dosyasını Not Defteri ile açın.
3. Aşağıdaki değerleri bulun ve belirtildiği gibi değiştirin:
   * `bShowGrass = False`
   * `bEnableMouseSmoothing = False`
   * `bMotionBlur = False`
4. Dosyayı kaydedip kapatın. Dosyaya sağ tıklayıp **Özellikler** deyin ve **Salt Okunur (Read-Only)** olarak işaretleyin.

---

## 7. Donanım ve Sistem Düzeyinde Kritik İpuçları

* **Çift Kanal (Dual-Channel) RAM:** Fortnite, Unreal Engine 5 mimarisi nedeniyle bellek bant genişliğine aşırı duyarlıdır. Tek kanal (Single-Channel) RAM kullanıyorsanız, çift kanala geçmek FPS drop sorunlarını %80 oranında çözer.
* **SSD Kullanımı:** Oyunu HDD yerine bir NVMe M.2 SSD veya SATA SSD'ye yüklemek, harita yüklenirken oluşan takılmaları tamamen engeller.
* **Arka Plan Uygulamaları:** Discord (Overly kapalı olmalı), Spotify ve Chrome gibi uygulamaları oyun esnasında kapatın. Discord içerisinde **Donanım İvmesi** özelliğini kapatmak CPU yükünü azaltır.