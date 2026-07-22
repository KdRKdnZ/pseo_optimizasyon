---
title: "fortnite performans ayarları"
description: "fortnite performans ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Fortnite Performans Ayarları: En Yüksek FPS ve Düşük Gecikme Rehberi

Fortnite, Unreal Engine 5 altyapısına geçiş yaptıktan sonra sistem kaynaklarını daha yoğun kullanan bir yapıma dönüştü. Oyunda maksimum kare hızı (FPS) elde etmek, kare düşüşlerini (stutter/drop) engellemek ve girdi gecikmesini (input lag) en aza indirmek için doğru grafik, sürücü ve işletim sistemi konfigürasyonlarının yapılması kritik önem taşır.

Bu rehber, Fortnite'ta donanımınızdan maksimum verimi almanız için teknik ve uygulanabilir optimizasyon adımlarını içermektedir.

---

## 1. Oyun İçi Grafik ve Görüntü Ayarları

Oyun içi ayarlar, işlemci (CPU) ve ekran kartı (GPU) üzerindeki yük dağılımını doğrudan etkiler. Rekabetçi avantaj ve yüksek FPS için aşağıdaki konfigürasyon uygulanmalıdır:

### Görüntü (Ekran) Ayarları
* **Ekrana Yerleştirme Modu:** Tam Ekran (Fullscreen)
  * *Teknik Neden:* Pencereli modlar Windows Masaüstü Pencere Yöneticisi'ni (DWM) devreye sokarak ek gecikme (input lag) yaratır. Tam Ekran modu GPU'ya doğrudan erişim sağlar.
* **Çözünürlük:** Monitörünüzün Doğal Çözünürlüğü (Örn: 1920x1080)
* **Kare Hızı Sınırı:** Monitör Yenileme Hızı + 1 veya Sabit
  * *Örnek:* 144 Hz monitör için 160 FPS veya 144 FPS sınırlandırması. Sınırsız (Uncapped) FPS, GPU'nun %100 yükte çalışmasına ve kare zamanlaması (frame pacing) bozulmalarına neden olarak takılma hissi yaratır.

### Grafik Modu ve Kalitesi (En Kritik Ayar)
* **İşleme Modu (Rendering Mode):** Performans - Düşük Grafik Özellikleri (Performance - Lower Graphical Fidelity)
  * *Teknik Neden:* Bu mod, Unreal Engine'in ağır aydınlatma ve gölge hesaplamalarını devre dışı bırakarak yükü GPU'dan CPU'ya dengeli bir şekilde dağıtır ve VRAM kullanımını minimuma indirir.

### Performans Modu Alt Grafik Ayarları
* **3D Çözünürlük:** %100 (Ekran kartınız çok zayıfsa %80-90 seviyesine çekilebilir, ancak görüntü bulanıklaşır).
* **Görüş Mesafesi (View Distance):** Yakın (Near) veya Orta (Medium)
  * *Not:* Bu ayar oyuncu modellerini etkilemez, yalnızca uzak harita nesnelerinin çizim mesafesini belirler.
* **Dokular (Textures):** Düşük (Low)
* **Ağlar (Meshes):** Düşük (Low) veya Yüksek (High)
  * *Düşük:* Yapıları "baloncuk/mobil" görünümüne sokar, CPU yükünü en aza indirir.
  * *Yüksek:* Yapıların normal görünmesini sağlar, görüş açısını artırır ancak az miktarda VRAM ve CPU kaynağı tüketir.

### Gelişmiş Grafik Ayarları
* **V-Sync (Dikey Eşitleme):** Kapalı (Off)
* **Hareket Bulanıklığı (Motion Blur):** Kapalı (Off)
* **NVIDIA Reflex Düşük Gecikme:** Açık + Takviye (On + Boost)
  * *Teknik Neden:* CPU ve GPU arasındaki senkronizasyonu optimize eder, GPU sınırına takılan senaryolarda sistem gecikmesini ciddi oranda düşürür.

---

## 2. İşleme Modları Karşılaştırması: DX11 vs. DX12 vs. Performans Modu

| Özellik | DirectX 11 | DirectX 12 | Performans Modu |
| :--- | :--- | :--- | :--- |
| **Hedef Donanım** | Eski Sistemler | Üst Düzey GPU / Çok Çekirdekli CPU | Rekabetçi / Orta-Düşük Sistemler |
| **FPS Verimliliği** | Orta | Yüksek (İstikrarlı) | En Yüksek |
| **Girdi Gecikmesi** | Yüksek | Orta | En Düşük |
| **VRAM Kullanımı** | Orta | Yüksek | Çok Düşük |

*Gelişmiş bir sisteminiz (RTX 3060 / RX 6600 ve üzeri) olsa dahi, en düşük gecikme süresi için **Performans Modu** tercih edilmelidir.*

---

## 3. NVIDIA / AMD Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1. **Masaüstüne sağ tıklayın** > **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve *Program Ayarları* sekmesinden Fortnite'ı (`FortniteClient-Win64-Shipping.exe`) seçin.
3. Aşağıdaki değerleri uygulayın:
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra
   * **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et
   * **Doku Süzme - Kalite:** Yüksek Performans
   * **Eşyönsüz Süzme (Anisotropic Filtering):** Kapalı
   * **Dikey Eşitleme (V-Sync):** Kapalı
   * **Bağlantılı Optimizasyon (Threaded Optimization):** Açık

### AMD Radeon Software Ayarları
1. **Radeon Software** panelini açın > **Oyunlar** > **Fortnite**.
2. **Radeon Anti-Lag:** Etkin
3. **Radeon Boost:** Devre Dışı (Çözünürlük dalgalanmasını önlemek için)
4. **Ekran Kartı Profili:** Performans
5. **Doku Filtreleme Kalitesi:** Performans

---

## 4. Windows İşletim Sistemi Optimizasyonları

### Windows Oyun Modu ve HAGS
* **Oyun Modu:** `Ayarlar > Oyun > Oyun Modu` yolunu izleyin ve **Açık** konuma getirin. Windows arka plan işlemlerini kısıtlayarak önceliği oyuna verir.
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar > Sistem > Ekran > Grafik Ayarları` altından **Açık** yapın (Sistemi yeniden başlatmanız gerekir).

### Geçici Dosyaları Temizleme ve Güç Planı
1. **Nihai Performans Modu:** Komut İstemini (CMD) yönetici olarak çalıştırın ve şu kodu yapıştırın:
   `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`
   Ardından Güç Seçenekleri'nden **Nihai Performans**'ı seçin.
2. **Önbellek Temizliği:** `Windows + R` tuşlarına basıp `%temp%` yazın ve açılan klasördeki tüm geçici dosyaları silin.

---

## 5. GameUserSettings.ini Dosyası Üzerinden İnce Ayar

Fortnite'ın konfigürasyon dosyasını manuel olarak düzenleyerek gizli performans parametrelerini değiştirebilirsiniz.

1. `Windows + R` tuş kombinasyonu ile Çalıştır penceresini açın.
2. `%LOCALAPPDATA%\FortniteGame\Saved\Config\WindowsClient\` dizinine gidin.
3. `GameUserSettings.ini` dosyasını Not Defteri ile açın.
4. Aşağıdaki satırları bulun ve değerlerini güncelleyin:

```ini
bShowGrass=False
bDisableMouseAcceleration=True
sg.ResolutionQuality=100.000000
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=0
sg.ShadowQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=0
sg.EffectsQuality=0
sg.FoliageQuality=0
sg.ShadingQuality=0
```

*Dosyayı kaydetip kapattıktan sonra, sağ tıklayıp **Özellikler**'e gidin ve **Salt Okunur** seçeneğini işaretleyin (Oyunun ayarları sıfırlamasını engeller).*

---

## 6. Ağ ve Başlatma Seçenekleri (Epic Games Launcher)

### Epic Games Başlatma Komutları
1. **Epic Games Launcher**'ı açın > Sağ üstteki **Profil** ikonuna tıklayın > **Ayarlar**.
2. En alttaki **Fortnite** sekmesini genişletin.
3. **Ek Komut Satırı Argümanları** kutusunu işaretleyin ve şu kodu ekleyin:

```text
-PREFERREDPROCESSOR -USEALLAVAILABLECORES -NOSPLASH -NOTEXTURESTREAMING
```

* **`-USEALLAVAILABLECORES`:** Oyunun işlemcinizdeki tüm izlekleri (thread) kullanmasını sağlar.
* **`-NOTEXTURESTREAMING`:** Dokuların oynanış sırasında yüklenmesini engeller, doğrudan VRAM'e aktarır. (Stutter/takılma sorununu çözer; en az 4GB VRAM önerilir).

### Yüksek Çözünürlüklü Dokuları Silme
Epic Games Kütüphanesi'nde Fortnite'ın yanındaki **üç noktaya** tıklayın > **Seçenekler** bölümüne gidin. **"Yüksek Çözünürlüklü Dokular" (High-Resolution Textures)** seçeneğindeki işareti kaldırın. Bu işlem yaklaşık 20-30 GB disk alanı kazandırır ve yükleme sürelerini kısaltır.