# CS2 FPS Artırma Rehberi: En İyi Grafik, Sistem ve Konsol Ayarları

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte Counter-Strike: Global Offensive'e (CS:GO) kıyasla çok daha yüksek işlemci (CPU) ve ekran kartı (GPU) kaynağı tüketmektedir. Bu teknik rehber, CS2'de maksimum FPS elde etmek, girdi gecikmesini (input lag) en aza indirmek ve kare hızı dalgalanmalarını önlemek için uygulanması gereken en etkili optimizasyon adımlarını içerir.

---

## 1. Oyun İçi Grafik Ayarları (In-Game Settings)

CS2'de grafik ayarlarını tamamen "En Düşük" seviyeye çekmek her zaman en yüksek performansı vermez. Görsel netlik ile FPS arasındaki dengeyi kurmak kritik önem taşır.

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Kontrastı** | Etkin (Enabled) | Düşük FPS etkisi; düşman görünürlüğünü önemli ölçüde artırır. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı (Disabled) | Girdi gecikmesini (input lag) engellemek için kesinlikle kapatılmalıdır. |
| **Gelişmiş Video Ayarları** | Custom | Özelleştirilmiş performans için gereklidir. |
| **Çoklu Örneklemeli Kenar Yumuşatma** | 2x MSAA veya CMAA | 2x MSAA, piksellenmeyi önler ve performansı fazla düşürmez. Çok düşük sistemlerde CMAA seçilebilir. |
| **Gölge Kalitesi (Global Shadow)** | Orta (Medium) | Yüksek gölge kalitesi, rakip gölgelerini uzaktan görmeyi sağlar. Performans kritikse "Düşük" yapılabilir. |
| **Model / Doku Kalitesi** | Düşük (Low) | GPU VRAM kullanımını düşürür, FPS'i doğrudan artırır. |
| **Doku Filtreleme Modu** | İki Çizgili (Bilinear) | GPU üzerindeki yükü en aza indirir. |
| **Parçacık Detayı** | Düşük (Low) | Sis ve molotof efektlerindeki FPS düşüşlerini engeller. |
| **Aydınlatma (Shader) Detayı** | Düşük (Low) | Yansımaları ve karmaşık ışıklandırmaları kapatarak FPS kazandırır. |
| **Ortam Kapatma (Ambient Occlusion)** | Devre Dışı (Disabled) | Derinlik gölgelerini kapatır, işlem yükünü hafifletir. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (Disabled) | Görüntüyü bulanıklaştırır. Sadece çok düşük konfigürasyonlarda "Ultra Quality" kullanılmalıdır. |
| **NVIDIA Reflex Low Latency** | Etkin + Boost | Sistem gecikmesini azaltır ve GPU frekansını maksimumda tutar. |

---

## 2. En Etkili CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** bölümüne aşağıdaki kodları ekleyebilirsiniz.

```text
-novid -nojoy -high +fps_max 0 +cl_updaterate 128 +cl_cmdrate 128
```

*   `-novid`: Açılış introsunu atlar, oyunun daha hızlı açılmasını sağlar.
*   `-nojoy`: Joystik/Gamepad desteğini kapatır, arka planda RAM ve CPU kullanımını azaltır.
*   `-high`: Oyuna CPU önceliği atar (Bazı sistemlerde kararsızlığa yol açarsa kaldırılmalıdır).
*   `+fps_max 0`: FPS kısıtlamasını kaldırır.

---

## 3. NVIDIA Denetim Masası Optimizasyonu

NVIDIA ekran kartı kullanıcıları için sürücü düzeyindeki ayarlar doğrudan kare hızına etki eder.

1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesine gidin ve `cs2.exe`yi seçin.
3.  Aşağıdaki parametreleri uygulayın:
    *   **Güç Yönetimi Modu:** Maksimum performansı tercih et
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık (On) veya Ultra
    *   **Doku Filtreleme - Kalite:** Yüksek Performans
    *   **Threaded Optimization (Masaüstü İş parçacığı Opt.):** Açık (On)
    *   **Gölgelendirici Önbellek Boyutu (Shader Cache Size):** 10 GB veya Sınırsız (Stuttering/anlık takılmaları önler)

---

## 4. AMD Radeon Software Optimizasyonu

AMD ekran kartına sahip kullanıcılar için önerilen ayarlar:

1.  AMD Software'i açın ve **Oyun > CS2** profilini seçin.
2.  **Radeon Anti-Lag:** Etkin (Sistem gecikmesini düşürür).
3.  **Radeon Boost:** Devre Dışı (Çözünürlüğü anlık değiştirerek görüntü netliğini bozabilir).
4.  **Radeon Image Sharpening:** Etkin (%10 - %20 arası netlik ayarı yapabilirsiniz).
5.  **Doku Filtreleme Kalitesi:** Performans.

---

## 5. Windows Sistem Optimizasyonları

### Oyun Modunu ve HAGS'i Etkinleştirme
Windows 10 ve 11'de yerleşik bulunan oyun özellikleri CS2 kaynak tahsisini iyileştirir.

1.  Windows Arama çubuğuna **Oyun Modu Ayarları** yazın ve **Açık** konuma getirin.
2.  Grafik Ayarları menüsüne gidin.
3.  **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** özelliğini **Açık** konuma getirin.
4.  Aynı menüde "Gözat" butonuna basarak `cs2.exe` dosyasını bulun (`.../Counter-Strike Global Offensive/game/bin/win64/cs2.exe`) ve Grafik Tercihini **Yüksek Performans** olarak ayarlayın.

### Tam Ekran Optimizasyonlarını Devre Dışı Bırakma
1.  `cs2.exe` dosyasına sağ tıklayın ve **Özellikler**'e gidin.
2.  **Uyumluluk** sekmesine tıklayın.
3.  **Tam ekran optimizasyonlarını devre dışı bırak** seçeneğini işaretleyin.
4.  **Yüksek DPI ayarlarını değiştir** butonuna tıklayıp **Yüksek DPI ölçekleme davranışını geçersiz kıl** kutucuğunu işaretleyin (Ölçekleme: Uygulama).

---

## 6. DirectX Shader Önbelleğini Temizleme

CS2 güncellemeleri sonrası oluşan anlık FPS düşüşlerini (stuttering) çözmek için gölgelendirici önbelleğini temizlemek etkilidir.

1.  Windows Arama çubuğuna **Disk Temizleme** yazın.
2.  Windows'un kurulu olduğu sürücüyü (Genellikle C:) seçin.
3.  Listeden yalnızca **DirectX Gölgelendirici Önbelleği** seçeneğini işaretleyin ve **Tamam**'a tıklayın.
4.  Bilgisayarı yeniden başlatın.

---

## 7. Konsol Komutları (Autoexec)

Oyun içi konsolu (`~` tuşu) açarak veya bir `autoexec.cfg` dosyası oluşturarak aşağıdaki kodları uygulayabilirsiniz:

```text
fps_max 0
cl_showfps 1
r_drawtracers_firstperson 0
```

*   `r_drawtracers_firstperson 0`: Kendi ateş ettiğiniz mermilerin izlerini (tracer) kapatır. Hem görsel odaklanmayı artırır hem de az miktarda FPS kazanımı sağlar.

---

## Özet ve Tavsiyeler

*   CS2, **CPU çekirdek hızı ve önbelleğine (Örn: AMD Ryzen X3D serisi)** son derece duyarlıdır. Sistem terfi düşünülüyorsa işlemci odaklı yükseltmeler CS2'de daha fazla FPS sağlar.
*   Arka planda çalışan Discord, Chrome, Spotify gibi uygulamaların **Donanım İvmesi (Hardware Acceleration)** ayarlarını kapatmak CPU üzerindeki yükü azaltır.
*   Ekran kartı sürücülerinizi DDU (Display Driver Uninstaller) ile temiz kurulum yaparak güncel tutun.