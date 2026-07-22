---
title: "valorant düşük sistem ayarları"
description: "valorant düşük sistem ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Valorant Düşük Sistem Ayarları ve FPS Arttırma Rehberi

Riot Games'in FPS oyunu Valorant, işlemci (CPU) ağırlıklı çalışan ve optimize edilmiş bir oyun motoruna (Unreal Engine 4) sahiptir. Ancak düşük konfigürasyona sahip bilgisayarlarda (düşük RAM, dahili GPU veya eski nesil işlemciler) kararlı 60+ FPS almak ve giriş gecikmesini (input lag) en aza indirmek için doğru grafik ve sistem ayarlarının yapılması kritik önem taşır.

Bu rehber, Valorant'ta maksimum kare hızı (FPS) ve en düşük sistem gecikmesi elde etmek için uygulanması gereken teknik ayarları içermektedir.

---

## 1. Valorant Oyun İçi Grafik Ayarları

Oyun içi grafik ayarları, GPU (Ekran Kartı) ve VRAM üzerindeki yükü doğrudan etkiler. Düşük sistemlerde hedef, işleme yükünü sıfıra yakın bir seviyeye indirmektir.

### Genişletilmiş Görüntü Ayarları (Display)
* **Görüntü Modu:** Tam Ekran (Fullscreen)
  > *Teknik Açıklama:* Pencereli veya Çerçevesiz Pencereli modlar, Windows Masaüstü Pencere Yöneticisi'nin (DWM) araya girmesine neden olarak kare gecikmesine (input lag) yol açar. "Tam Ekran" modu, GPU'nun doğrudan oyuna odaklanmasını sağlar.
* **Çözünürlük:** Monitörün Doğal Çözünürlüğü (Örn: 1920x1080) veya Düşük Sistemler İçin (1280x720 / 1024x768)
  > *Not:* Çözünürlüğü düşürmek GPU yükünü hafifletir ancak işlemci darboğazı olan sistemlerde FPS artışı sınırlı kalabilir.
* **FPS Sınırlama Ayarları:** Tümü **Kapalı** (Oyun içi akıcılığı engellememek için).

### Grafik Kalitesi (Graphics Quality)
| Ayar Kategorisi | Önerilen Değer | Teknik Etkisi |
| :--- | :--- | :--- |
| **Materyal Kalitesi** | Düşük | Yüzey kaplamalarının detayını azaltır, VRAM kullanımını düşürür. |
| **Doku Kalitesi** | Düşük | Doku çözünürlüklerini düşürür, bellek bant genişliğini korur. |
| **Detay Kalitesi** | Düşük | Haritadaki küçük objeleri ve görsel detayları kaldırır. |
| **Arayüz Kalitesi** | Düşük | HUD öğelerinin işlenme kalitesini düşürür, az miktarda CPU yükünü azaltır. |
| **Netliği Arttır** | Kapalı | Ekstra keskinleştirme filtresi uygular; GPU yükünü artırır. |
| **Deneysel Keskinleştirme** | Kapalı | Post-process efekti; düşük GPU'larda mikro takılmalara (stuttering) yol açabilir. |
| **Eşyönsüz Filtreleme (Anisotropic Filtering)** | 1x | Dokuların açısal netliğini ayarlar. 1x, GPU belleğini en az yoran değerdir. |
| **Kenar Yumuşatma (Anti-Aliasing)** | Hiçbiri veya FXAA | MSAA yüksek GPU performansı gerektirir. FXAA ise minimal performans kaybıyla kenarları düzeltir. |
| **V-Sync (Dikey Eşitleme)** | Kapalı | Ekran yırtılmasını önler ancak ciddi düzeyde giriş gecikmesine (input lag) neden olur. |
| **Bozulma (Distortion)** | Kapalı | Patlama ve yetenek efektlerindeki kırılmaları hesaplar; GPU yükünü artırır. |
| **Gelişmiş Gölgeler** | Kapalı | Karakter ve harita gölge detaylarını kapatır. |

### NVIDIA Reflex Düşük Gecikme
* **Ayar:** Açık + Takviye (On + Boost)
  > *Teknik Açıklama:* CPU ve GPU senkronizasyonunu optimize ederek sistem gecikmesini düşürür. "Boost" seçeneği, GPU saat hızlarının oyun esnasında yüksek kalmasını sağlar. (Yalnızca NVIDIA GPU'larda mevcuttur).

---

## 2. Windows Sistem Optimizasyonları

Valorant, işlemci çekirdek performansı ve bellek erişim hızına duyarlıdır. Windows arka plan süreçlerinin optimize edilmesi kare tutarlılığını artırır.

### Oyun Modu ve Grafik Grafikleri
1. Windows Arama çubuğuna **"Oyun Modu Ayarları"** yazın ve **Açık** konuma getirin.
2. **"Grafikler"** bölümüne gidin.
3. **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** seçeneğini **Açık** yapın (Destekleyen kartlarda GPU belleğini optimize eder).
4. Göz at butonundan `VALORANT-Win64-Shipping.exe` dosyasını seçin ve grafik tercihini **"Yüksek Performans"** olarak ayarlayın.

*(Dosya Yolu Genellikle: `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64`)*

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayın ve **Özellikler**'e girin.
2. **Uyumluluk** sekmesine gelin.
3. **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
4. **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçekleme davranışını geçersiz kıl"** seçeneğini işaretleyip **Uygulama** seçeneğini belirleyin.

---

## 3. Ekran Kartı Denetim Masası Ayarları

### NVIDIA Denetim Masası
* **Bağlantılı Optimizasyon (Threaded Optimization):** Açık *(Valorant'ın çoklu çekirdek kullanımını zorunlu kılar).*
* **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
* **Düşük Gecikme Oranı Modu (Low Latency Mode):** On veya Ultra.
* **Doku Süzme - Kalite:** Yüksek Performans.

### AMD Radeon Software
* **Radeon Anti-Lag:** Etkin *(Giriş gecikmesini azaltır).*
* **Radeon Boost:** Devre Dışı *(Dinamik çözünürlük düşüşleri görüntü çamurlaşmasına yol açabilir).*
* **Ekran Kartı Belleği Ayarlama (Texture Filtering Quality):** Performans.

---

## 4. GameUserSettings.ini ile Özel Çözünürlük Ayarı (En Düşük Sistemler İçin)

Oyun içi arayüzden düşürülemeyen bazı grafik parametreleri konfigürasyon dosyasından sıfırlanabilir.

1. `Windows + R` tuşlarına basarak `Run` (Çalıştır) pencerisini açın.
2. `%LOCALAPPDATA%\VALORANT\Saved\Config` yazın ve Enter'a basın.
3. Rastgele karakterlerden oluşan klasörün içine girin ve `Windows` klasöründeki `GameUserSettings.ini` dosyasını Not Defteri ile açın.
4. Aşağıdaki değerleri bulun ve değiştirin:

```ini
sg.ResolutionQuality=60.000000 (Düşük GPU'larda ölçeklemeyi düşürür, FPS'i ciddi oranda artırır)
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=0
sg.ShadowQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=0
sg.EffectsQuality=0
sg.FoliageQuality=0
```

*Not: `sg.ResolutionQuality` değerini 50.000000 ile 80.000000 arasında sisteminize göre deneyebilirsiniz. Değer düştükçe görüntü kalitesi bulanıklaşacaktır.*

---

## 5. Düşük Sistemler İçin Temel Kontrol Listesi

* **RAM Tarafı:** Valorant çalışırken arka planda Chrome, Discord overlay veya ikincil uygulamaları kapatın. 8 GB RAM ve altı sistemlerde arka plan uygulamaları "Stutter" (anlık takılma) sorununa yol açar.
* **Riot Vanguard:** Vanguard hile koruma yazılımının arka planda tam yetkiyle çalışması nedeniyle, çakışan üçüncü taraf optimizasyon yazılımlarını (Razer Cortex, CCleaner vb.) bilgisayardan kaldırın.
* **Sıcaklık Değerleri:** İşlemci veya GPU ısınmaya başladığında frekans düşürür (Thermal Throttling). Bu durum ani FPS düşüşlerinin (FPS Drop) ana sebebidir.