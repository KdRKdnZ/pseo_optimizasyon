# GTA 5 FPS Artırma Rehberi: En Etkili Grafik ve Sistem Optimizasyonları

Grand Theft Auto V (GTA 5), RAGE motorunun gelişmiş fizik ve kaplama mimarisini kullanır. Bu rehber, ekran kartı (GPU), işlemci (CPU) ve bellek (RAM) darboğazlarını en aza indirerek GTA 5'te maksimum FPS elde etmenizi sağlayacak teknik optimizasyonları kapsar.

---

## 1. Oyun İçi Grafik Ayarları Optimizasyonu

GTA 5'in grafik menüsündeki her ayarın donanım üzerinde farklı bir yükü vardır. FPS'i en çok etkileyen ayarları doğru yapılandırmak performance/görsel kalite dengesini sağlar.

### Ana Grafik Ayarları (Graphics)

*   **DirectX Version:** `DirectX 11`. Eski sistemlerde (2 GB VRAM altı) `DirectX 10.1` seçilerek işlemci yükü azaltılabilir.
*   **Screen Type:** `Full Screen` (Tam Ekran). Masaüstü pencereli modlar (Borderless) G-Sync/FreeSync entegrasyonunu bozar ve girdi gecikmesini (input lag) artırır.
*   **FXAA:** `On`. Mimarisi gereği FPS'e neredeyse hiç etki etmez, kenar yumuşatmada temel seviyede başarılıdır.
*   **MSAA:** `Off`. GTA 5'te MSAA (özellikle 4x ve 8x) piksel işleme yükünü katlayarak FPS'i %30 ila %50 arasında düşürür.
*   **NVIDIA TXAA:** `Off` (MSAA kapatıldığında devre dışı kalır).
*   **VSync:** `Off`. Ekran yırtılması çok belirginse ve monitör tazeleme hızınız düşükse (60 Hz) açılabilir; ancak girdi gecikmesi yaratır.
*   **Pause Game On Focus Loss:** Kişisel tercih (FPS'e etkisi yoktur).
*   **Population Density (Nüfus Yoğunluğu):** `%20 - %30`. Doğrudan CPU ve RAM'e yük bindirir.
*   **Population Variety (Nüfus Çeşitliliği):** `%20 - %30`. VRAM kullanımını doğrudan etkiler.
*   **Distance Scaling (Mesafe Ölçekleme):** `%0 - %30`. İşlemcinin çizim mesafesi (Draw Distance) yükünü belirler. Düşük tutulması şehir içi kararsız FPS düşüşlerini (stuttering) engeller.
*   **Texture Quality:** VRAM kapasitenize göre ayarlanmalıdır:
    *   2 GB VRAM: `Normal`
    *   3 GB - 4 GB VRAM: `High`
    *   6 GB+ VRAM: `Very High`
*   **Shader Quality:** `Normal` veya `High`. Işıklandırma karmaşıklığını yönetir.
*   **Shadow Quality:** `Normal`. Gölgeler, GTA 5'te GPU işleme süresini en çok artıran ögelerdendir.
*   **Reflection Quality:** `Normal` veya `High`.
*   **Reflection MSAA:** `Off`.
*   **Water Quality:** `Normal`. Su fiziği ve kırılmaları özellikle kıyı bölgelerinde FPS düşürür.
*   **Particles Quality:** `Normal`. Patlama ve toz efektlerindeki ani FPS düşüşlerini önler.
*   **Grass Quality:** `Normal` veya `High`. **(Kritik Ayar)** "Very High" ve "Ultra" seviyeleri haritanın kuzeyindeki (Blaine County) çim alanlarda FPS'i yarı yarıya düşürür.
*   **Soft Shadows:** `Soft` veya `AMD CHS / NVIDIA PCSS` yerine `Softer`.
*   **Post FX:** `Normal`. "Ultra" seviyesi alan derinliği (Depth of Field) ve hareket bulanıklığı (Motion Blur) ekleyerek ekran kartını yorar.
*   **Anisotropic Filtering:** `x8` veya `x16`. Modern GPU'larda performansa etkisi yok denecek kadar azdır, kaplama keskinliğini artırır.
*   **Ambient Occlusion:** `Off` veya `Normal`.
*   **Tessellation:** `Off` veya `Normal`.

### Gelişmiş Grafik Ayarları (Advanced Graphics)

Bu bölümdeki tüm ayarlar yüksek konfigürasyonlu sistemler içindir. FPS artışı için **tamamını kapatın**:

*   **Long Shadows:** `Off`
*   **High Resolution Shadows:** `Off`
*   **High Detail Streaming While Flying:** `Off`
*   **Extended Distance Scaling:** `%0`
*   **Extended Shadows Distance:** `%0`

---

## 2. Windows ve Sürücü Düzeyinde Optimizasyonlar

### NVIDIA Denetim Masası Ayarları

1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi** > **Program Ayarları** sekmesine gidin ve `gta5.exe` dosyasını seçin.
3.  Aşağıdaki değerleri uygulayın:
    *   **Güç Yönetimi Modu:** *Maksimum performansı tercih et*
    *   **Doku Süzme - Kalite:** *Yüksek Performans*
    *   **Doku Süzme - Trilineer Optimizasyon:** *Açık*
    *   **Eşyönsüz Örnek Optimizasyonu:** *Açık*
    *   **Düşük Gecikme Oranı (Low Latency Mode):** *On* veya *Ultra*
    *   **Güç Bağlantı Özelliği (Threaded Optimization):** *Açık* (Çok çekirdekli CPU kullanımını zorlar).

### AMD Radeon Software Ayarları

1.  **AMD Radeon Software** uygulamasını açın.
2.  **Oyun** > **GTA 5** profilini seçin.
3.  Aşağıdaki özellikleri düzenleyin:
    *   **Radeon Anti-Lag:** *Etkin*
    *   **Radeon Boost:** *Devre Dışı* (Bazı sahnelerde çözünürlük ölçekleme sorununa yol açabilir).
    *   **Anizotropik Süzme:** *Uygulama Ayarlarını Kullan*
    *   **Yüzey Biçim Optimizasyonu:** *Etkin*
    *   **Tessellation Modu:** *Uygulama ayarlarını geçersiz kıl* -> *Maksimum Tessellation Seviyesi: 4x veya 8x*

### Windows 10/11 Ayarları

*   **Oyun Modu (Game Mode):** `Ayarlar` > `Oyun` > `Oyun Modu` yolunu izleyip **Açık** konumuna getirin.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar` > `Sistem` > `Monitör` > `Grafikler` sekmesinden bu özelliği **Açık** yapın (Yeniden başlatma gerektirir).
*   **Yüksek Performans Güç Planı:** `Denetim Masası` > `Güç Seçenekleri` üzerinden **Yüksek Performans** veya **Nihai Performans** modunu seçin.

---

## 3. Komut Satırı (Commandline) ve Config Dosyası Müdahalesi

GTA 5'in ana dizinine eklenecek bir konfigürasyon dosyası ile oyun varsayılan sınırların ötesinde optimize edilebilir.

### `commandline.txt` Oluşturma

GTA 5'in kurulu olduğu ana klasöre (`GTA5.exe` dosyasının bulunduğu yer) gidip **`commandline.txt`** adında yeni bir metin belgesi oluşturun ve içine şu kodları yapıştırın:

```text
-high
-norestr
-nomemrestrict
-ignorepipelinecache
-noDXBuffer
-percentage
```

*   `-high`: Oyuna işlemci önceliğinde yüksek öncelik atar.
*   `-ignorepipelinecache`: Derlenmiş gölgelendirici belleği hatalarından kaynaklanan takılmaları (stutter) önler.

### Shadow Quality'i Tamamen Kapatmak (Aşırı Düşük Sistemler İçin)

Oyundaki gölgeleri tamamen kaldırmak GPU yükünü önemli ölçüde hafifletir.

1.  `C:\Users\KullanıcıAdı\Documents\Rockstar Games\GTA V` klasörüne gidin.
2.  `settings.xml` dosyasını Not Defteri ile açın.
3.  `<ShadowQuality value="..." />` satırını bulun ve değeri **`0`** yapın:
    ```xml
    <ShadowQuality value="0" />
    ```
4.  Dosyayı kaydedip kapatın ve "Salt Okunur" olarak işaretleyin.

---

## 4. Donanım Seviyesinde Darboğaz Engelleme (RAM ve SSD)

*   **Çift Kanal (Dual-Channel) RAM:** GTA 5, bellek bant genişliğine aşırı duyarlı bir oyundur. Tek kanal (1x8GB) RAM yerine çift kanal (2x4GB veya 2x8GB) RAM kullanımı, özellikle şehir içinde araç sürerken yaşanan anlık takılmaları ve FPS düşüşlerini (1% Low FPS) %30'a varan oranda düzeltir.
*   **SSD Kullanımı:** Oyun içi kaplamaların geç yüklenmesi (Texture Streaming sorunu) ve araçla hızlı giderken haritanın kaybolması sorunu doğrudan HDD okuma hızından kaynaklanır. Oyunu bir NVMe veya SATA SSD'ye kurmak akıcılığı doğrudan artırır.

---

## Özet: Sistem Türüne Göre Önerilen Profil Tablosu

| Ayar | Düşük Sistem (GTX 1050 / RX 560) | Orta Sistem (GTX 1660 / RX 6600) |
| :--- | :--- | :--- |
| **Çözünürlük** | 1080p (veya 720p) | 1080p |
| **DirectX** | DX11 | DX11 |
| **MSAA / FXAA** | Off / On | Off / On |
| **Textures** | Normal | High / Very High |
| **Shadows** | Normal (veya kapalı) | Normal / High |
| **Grass Quality** | Normal | High |
| **Post FX** | Normal | Normal |
| **Advanced Graphics** | Tamamen Kapalı | Tamamen Kapalı |