# Elden Ring FPS Artırma ve Performans Optimizasyon Rehberi

Elden Ring, FromSoftware’in DirectX 12 altyapısıyla geliştirdiği geniş açık dünya mimarisi nedeniyle özellikle işlemci (CPU) ve ekran kartı (GPU) üzerinde yüksek yük oluşturan bir yapımdır. Oyundaki ani FPS düşüşlerini (stuttering) engellemek, takılmaları minimize etmek ve maksimum kare hızına ulaşmak için aşağıdaki teknik adımları sırasıyla uygulayabilirsiniz.

---

## 1. Oyun İçi Grafik Ayarlarının Optimizasyonu

Oyun içi grafik ayarlarında görsel kaliteden minimum ödün vererek en yüksek FPS kazancını sağlayan "Tatlı Nokta" (Sweet Spot) konfigürasyonu şu şekildedir:

*   **Ray Tracing Quality:** Off *(Performansı en çok düşüren ayardır, kesinlikle kapatılmalıdır.)*
*   **Texture Quality:** Medium veya High *(Ekran kartı VRAM’iniz 6 GB ve üzeriyse High, 4 GB ise Medium seçin.)*
*   **AA Quality:** Low veya Medium
*   **SSAO (Screen Space Ambient Occlusion):** Medium *(Off yapmak ciddi FPS kazandırır ancak derinlik algısını azaltır.)*
*   **Depth of Field:** Off *(Görüş netliğini artırır ve hafif FPS kazancı sağlar.)*
*   **Motion Blur:** Off
*   **Shadow Quality:** Medium *(High/Maximum seviyeleri gölge işleme yükünü ikiye katlar.)*
*   **Lighting Quality:** Medium
*   **Effects Quality:** Medium *(Büyü ve efekt yoğun anlardaki FPS droplarını engeller.)*
*   **Volumetric Quality:** Medium veya Low *(Açık dünyadaki sis ve bulut kalitesini yönetir, FPS'e etkisi yüksektir.)*
*   **Reflection Quality:** Low
*   **Water Surface Quality:** Low
*   **Global Illumination Quality:** Medium
*   **Grass Quality:** Medium *(Açık dünyadaki çim yoğunluğunu belirler; işlemci ve GPU yükünü doğrudan etkiler.)*

---

## 2. NVIDIA ve AMD Sürücü Ayarları

Ekran kartı kontrol paneli üzerinden yapılacak özelleştirmeler, oyunun DirectX 12 gölgelendirici (Shader) derleme süreçlerini iyileştirir.

### NVIDIA Denetim Masası Ayarları:
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**’nı açın.
2. **3D Ayarlarının Yönetilmesi** > **Program Ayarları** sekmesine gidin ve `eldenring.exe` dosyasını seçin.
3. Aşağıdaki ayarları uygulayın:
   *   **Güç Yönetimi Modu:** Maksimum performansı tercih et.
   *   **Gölgelendirici Önbelleği Boyutu (Shader Cache Size):** **Unlimited** veya **10 GB** *(Elden Ring'deki anlık takılmaları/stuttering çözmedeki en kritik ayardır).*
   *   **Doku Süzme - Kalite:** Yüksek Performans.
   *   **Eşyönsüz Süzme (Anisotropic Filtering):** 4x veya 8x.
   *   **Dikey Eşitleme (V-Sync):** Hızlı (Fast) veya Açık *(Oyun içi V-Sync kilitliyse buradan yönetilmesi önerilir).*

### AMD Radeon Software Ayarları:
1. **Radeon Software** uygulamasını açın ve **Oyunlar** sekmesinden Elden Ring’i seçin.
2. **Radeon Anti-Lag:** Açık.
3. **Radeon Boost:** Kapalı.
4. **Tessellation Mode:** "Uygulama ayarlarını geçersiz kıl" seçilip **Maximum Tessellation** değeri **8x** veya **16x** olarak sınırlandırılmalıdır.

---

## 3. Windows ve Sistem Seviyesinde Yapılacak Düzenlemeler

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 ve 11'de bulunan bu özellik, GPU belleğinin yönetimini işlemciden alarak ekran kartına devreder.
1. Windows Arama çubuğuna **Grafik Ayarları** yazın.
2. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin.
3. Aynı sayfada "Gözat" butonuna tıklayarak `eldenring.exe` dosyasını bulun (Genellikle `C:\Program Files (x86)\Steam\steamapps\common\ELDEN RING\Game\eldenring.exe`).
4. Seçenekler butonuna tıklayıp **Yüksek Performans** modunu işaretleyin.

### Windows Oyun Modu ve Güç Planı
*   **Oyun Modu:** `Ayarlar > Oyun > Oyun Modu` yolunu izleyin ve **Açık** yapın.
*   **Güç Planı:** `Denetim Masası > Güç Seçenekleri` menüsünden **Yüksek Performans** veya **Nihai Performans** modunu aktif edin.

---

## 4. DirectX 12 Shader Cache (Gölgelendirici) Temizliği

Oyun güncellemelerinden sonra bozulan cache dosyaları ciddi performans kayıplarına yol açabilir. Cache dosyasını sıfırlamak için:

1. `Windows + R` tuşlarına basarak **Çalıştır** penceresini açın.
2. `%localappdata%` yazıp Enter'a basın.
3. **NVIDIA** kullanıyorsanız `NVIDIA\DXCache`, **AMD** kullanıyorsanız `AMD\DxCache` klasörünün içindeki dosyaları silin. (Sistem tarafından kullanılan dosyalar atlanabilir.)
4. Bilgisayarı yeniden başlatın.

---

## 5. Elden Ring 60 FPS Kilidini Kaldırma ve Anti-Cheat (İleri Düzey)

Elden Ring, motor seviyesinde **60 FPS sınırına** sahiptir ve **Easy Anti-Cheat (EAC)** yazılımı ile korunur. Eğer 144Hz/240Hz bir monitöre sahipseniz ve 60 FPS sınırını kaldırmak istiyorsanız, oyunu **Çevrimdışı (Offline)** modda çalıştırmanız gerekir (Aksi takdirde ban riski oluşur).

1. Github üzerinden **Flawless Widescreen** veya **Elden Ring Unlocked FPS** modunu indirin.
2. Oyun dizinindeki `start_protected_game.exe` dosyasının adını `start_protected_game_original.exe` olarak değiştirin.
3. `eldenring.exe` dosyasının bir kopyasını oluşturup adını `start_protected_game.exe` yapın.
4. İndirdiğiniz mod yazılımı üzerinden **FPS Limit** seçeneğini monitör yenileme hızınıza (örn. 144) ayarlayın.

*Note: Bu işlem Steam başarımlarını veya çevrimiçi PvP/Co-op modlarını devre dışı bırakır.*

---

## Özet Performans Kontrol Listesi

| İşlem | Beklenen FPS / Performans Etkisi |
| :--- | :--- |
| **Ray Tracing Kapatmak** | %30 - %50 FPS Artışı |
| **Shader Cache Boyutunu Artırmak** | Anlık Dropların (Stuttering) %80 Engellenmesi |
| **Grass / Shadow / Volumetric Ayarlarını Medium Yapmak** | %15 - %25 FPS Artışı |
| **HAGS ve Yüksek Performans Modu** | %5 - %10 İşlemci Yükü Azalması |