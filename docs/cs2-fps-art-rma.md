---
title: "cs2 fps artırma"
description: "cs2 fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 FPS Artırma Rehberi: En İyi Grafik, Başlatma ve Sistem Ayarları

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte CS:GO’ya kıyasla çok daha yüksek sistem kaynakları talep etmektedir. Gelişmiş ışıklandırma, dinamik sis bombaları ve yenilenen fizik motoru, işlemci (CPU) ve ekran kartı (GPU) üzerindeki yükü artırmıştır. 

Bu rehber, CS2'de maksimum FPS elde etmek, gecikmeyi (input lag) en aza indirmek ve kare hızındaki ani düşüşleri (micro-stutter) engellemek için uygulanması gereken teknik adımları içermektedir.

---

## 1. Oyun İçi En İyi Grafik Ayarları (In-Game Settings)

CS2’de grafik ayarlarını tamamen "En Düşük" seviyeye getirmek her zaman en yüksek FPS’i vermez. Görsel netlik ile performans arasındaki en ideal dengeyi sağlayan teknik konfigürasyon şu şekildedir:

### Gelişmiş Video Ayarları

*   **Oyuncu Kontrastını Artır:** *Etkin* (FPS'e etkisi %1-2 civarındadır ancak düşman görünürlüğü için kritik önem taşır.)
*   **Dikey Eşitleme (V-Sync):** *Devre Dışı* (Input lag yaratır.)
*   **Gelişmiş Doku Filtreleme Modu:** *Eşyönsüz (Anisotropic) 4x* (Performans kaybı yaratmadan uzak mesafelerdeki dokuları netleştirir.)
*   **Çoklu Örneklemeli Kenar Yumuşatma Modu (MSAA):** *2x MSAA* veya *4x MSAA*
    *   *Not:* CS2'de MSAA'yı kapatmak (CMAA veya Yok) Kenar yumuşatmada ciddi bozulmalara yol açar. Sisteminiz çok zayıf değilse 2x MSAA önerilir.
*   **Gölge Kalitesi:** *Orta*
    *   *Teknik Neden:* "Düşük" ayarda oyuncu gölgeleri tamamen kaybolabilir. "Orta" ayar, stratejik avantaj sağlayan gölgeleri çizerken FPS'i korur.
*   **Model / Doku Detayı:** *Düşük*
*   **Doku Detayı:** *Düşük*
*   **Parçacık Detayı:** *Düşük*
*   **Ortam Kapatma (Ambient Occlusion):** *Devre Dışı* (Doğrudan FPS artışı sağlar.)
*   **Yüksek Dinamik Aralık (HDR):** *Performans*
*   **FidelityFX Super Resolution (FSR):** *Devre Dışı (En Yüksek Kalite)*
    *   *Teknik Neden:* FSR görüntüyü bulanıklaştırır ve giren gecikmesini artırabilir. Yalnızca ekran kartı çok yetersiz kalan sistemlerde "Kalite" modunda açılmalıdır.
*   **NVIDIA Reflex Düşük Gecikme:** *Etkin + Boost* (Ekran kartı kullanımının yüksek olduğu anlarda sistem gecikmesini düşürür.)

---

## 2. CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kutusuna aşağıdaki kodları ekleyebilirsiniz.

```text
-novid -high -nojoy +engine_low_latency_sleep_after_client_tick true
```

### Kodların Teknik Açıklamaları:
*   `-novid`: Giriş videosunu atlayarak oyunun daha hızlı açılmasını sağlar.
*   `-high`: İşlemciye CS2 önceliğini "Yüksek" olarak atar. (Bazı sistemlerde takılmaya yol açarsa kaldırılmalıdır.)
*   `-nojoy`: Joystick/Gamepad desteğini kapatır, RAM kullanımını ve arka plan yükünü azaltır.
*   `+engine_low_latency_sleep_after_client_tick true`: Kare sürelerini (frame pacing) stabilize ederek daha akıcı bir görüntü sunar.

> **Uyarı:** CS:GO döneminden kalma `-threads`, `-cl_updaterate`, `-tickrate 128` gibi komutlar CS2 motorunda işlevsizdir veya kararsızlığa neden olabilir.

---

## 3. Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları

1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesinden **Counter-Strike 2 (cs2.exe)** yi seçin.
3.  Aşağıdaki değerleri uygulayın:
    *   **Güç Yönetimi Modu:** *Maksimum performansı tercih et*
    *   **Düşük Gecikme Oranı (Low Latency Mode):** *Açık* veya *Ultra*
    *   **Doku Süzme - Kalite:** *Yüksek Performans*
    *   **Eşyönsüz Süzme Optimizasyonu:** *Açık*
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** *Açık*
    *   **Maksimum Kare Hızı:** *Kapalı* (Gecikmeyi düşürmek için FPS sınırlandırılmamalıdır.)

### AMD Radeon Software Ayarları

1.  AMD Software panelini açın ve **Oyun > CS2** profilini seçin.
2.  **Radeon Anti-Lag:** *Etkin*
3.  **Radeon Boost:** *Devre Dışı* (Çözünürlüğü dinamik düşürdüğü için görüntü netliğini bozar.)
4.  **Ekran Kartı Önbelleğini Temizle:** *Shader Cache'i sıfırlayın.* (Güncellemeler sonrası oluşan takılmaları çözer.)

---

## 4. Windows ve Sistem Düzeyi Optimizasyonlar

### Windows Grafik ve Oyun Modu Ayarları
*   **Oyun Modu:** Windows Arama çubuğuna "Oyun Modu Ayarları" yazın ve **Açık** konuma getirin. Windows 10/11'de arka plan süreçlerini başarıyla kısıtlar.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** *Ayarlar > Sistem > Ekran > Grafik Ayarları* bölümünden HAGS'ı **Açık** konuma getirin ve bilgisayarı yeniden başlatın.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1.  Steam kütüphanesinde CS2'ye sağ tıklayın: **Yönet > Yerel Dosyalara Göz At**.
2.  `game/bin/win64/cs2.exe` dosyasını bulun.
3.  Sağ tıklayıp **Özellikler > Uyumluluk** sekmesine gidin.
4.  **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
5.  **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçeklendirme davranışını geçersiz kıl"** kutucuğunu onaylayın.

### Shader Cache (Gölgelendirici Önbelleği) Temizliği
Güncellemeler sonrasında anlık FPS düşüşleri yaşıyorsanız DirectX Önbelleğini temizlemek sorunu çözecektir:
1.  `Windows + R` tuşlarına basıp `cleanmgr` yazın.
2.  C: sürücüsünü seçin.
3.  Yalnızca **DirectX Gölgelendirici Önbelleği** seçeneğini işaretleyip **Tamam**'a basın.

---

## 5. CS2 Konsol Komutları ile Performans İyileştirme

Oyun içindeki geliştirici konsolunu (`~`) açarak aşağıdaki komutları uygulayabilirsiniz:

```text
fps_max 0
```
*(Monitör yenileme hızınızın çok üzerinde FPS alıyorsanız gecikmeyi en aza indirmek için `0` yapın. Ancak FPS dalgalanması çok yüksekse, ortalama FPS değerinize sabitlemek kare sürelerini stabilize eder.)*

```text
cl_showfps 1
```
*(FPS ve gecikme değerlerinizi anlık olarak izlemenizi sağlar.)*

---

## Özet Kontrol Listesi

| İşlem | Önerilen Ayar | Etki Alanı |
| :--- | :--- | :--- |
| **Çözünürlük** | 1280x960 (4:3 Stretched) veya 16:9 Özgün | Yüksek FPS / Geniş Düşman Modelleri |
| **Gölge Kalitesi** | Orta | Stratejik Avantaj + Stabil FPS |
| **NVIDIA Reflex** | Etkin + Boost | Minimum Input Lag |
| **Windows Güç Planı** | Yüksek / Nihai Performans | CPU Frekans Sabitleme |
| **RAM** | XMP / EXPO Profil Açık (Dual Channel) | Minimum Micro-Stutter |

CS2, bellek bant genişliğine duyarlı bir oyundur. Sisteminizde RAM'lerin **Dual-Channel (Çift Kanal)** çalışması ve BIOS üzerinden **XMP/EXPO** profilinin açık olması, CS2'deki %1 ve %0.1 low FPS değerlerini doğrudan artırarak takılmaları engeller.