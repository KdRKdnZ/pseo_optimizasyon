---
title: "gta 5 fps artırma"
description: "gta 5 fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# GTA 5 FPS Artırma Rehberi: Donanım, Yazılım ve Oyun İçi Optimizasyonlar

Grand Theft Auto V (GTA 5), iyi optimize edilmiş bir RAGE motoru kullansa da, güncel sistemlerde dahi yanlış konfigürasyonlar veya işlemci/ekran kartı darboğazları nedeniyle performans kayıplarına yol açabilir. Bu rehber; kare hızını (FPS) maksimuma çıkarmak, takılmaları (stuttering/FPS drop) engellemek ve sistem kaynaklarını en verimli şekilde kullanmak için uygulayabileceğiniz teknik yöntemleri içermektedir.

---

## 1. Oyun İçi Grafik Ayarlarının (In-Game Settings) Optimizasyonu

GTA 5'teki her grafik ayarının işlemci (CPU) ve ekran kartı (GPU) üzerindeki yükü farklıdır. FPS'yi doğrudan etkileyen kritik ayarları doğru konfigüre etmek performance/görsellik dengesini sağlar.

### Kritik Grafik Ayarları

*   **DirectX Version:** `DirectX 11` olarak seçilmelidir. Eski ekran kartlarında DirectX 10.1 VRAM kullanımını düşürse de DX11 modern sürücülerde daha kararlı çalışır.
*   **Resolution (Çözünürlük):** Monitörünüzün doğal (native) çözünürlüğünde kalmalıdır. Çözünürlük düşürmek yerine *Frame Scaling* kullanmak daha net görüntü sunar.
*   **FXAA:** `On` (Açık). FPS üzerinde neredeyse hiç olumsuz etkisi yoktur.
*   **MSAA:** `Off` (Kapalı). MSAA (Multi-Sample Anti-Aliasing) ekran kartını en çok yoran teknolojilerden biridir. 2x MSAA bile FPS'yi %15-20 oranında düşürebilir.
*   **TXAA:** `Off` (Kapalı). (MSAA kapalıyken kullanılamaz).
*   **V-Sync:** `Off` (Kapalı). Input lag'i (girdi gecikmesini) önlemek ve FPS limitini kaldırmak için kapatılmalıdır. (Ekran yırtılması yaşarsanız `Adaptive` veya `G-Sync/FreeSync` tercih edilmelidir).
*   **Population Density / Variety / Distance Scaling:** Tüm çubukları `%0 ile %30` arasına çekin. Bu ayarlar doğrudan CPU ve VRAM'e yük bindirir. Şehirdeki yaya/araç sayısını belirler.

### Gelişmiş Grafik Detayları

| Grafik Ayarı | Önerilen Değer | Etkilediği Donanım | FPS Kaybı Riski |
| :--- | :--- | :--- | :--- |
| **Texture Quality** | High / Normal | VRAM | VRAM yeterliyse düşük, yetersizse yüksek |
| **Shader Quality** | High | GPU | Orta |
| **Shadow Quality** | Normal | GPU / CPU | **Yüksek** |
| **Reflection Quality** | High / Normal | GPU | Orta |
| **Grass Quality** | Normal / High | GPU / CPU | **Çok Yüksek** (Özellikle kırsal alanda) |
| **Post FX** | Normal / High | GPU | Yüksek (Motion Blur engellenir) |
| **Anisotropic Filtering** | x16 | GPU | Çok Düşük (Performansı etkilemez, netlik sağlar) |
| **Ambient Occlusion** | Off / Normal | GPU | Orta |
| **Tessellation** | Off / Normal | GPU | Düşük/Orta |

### Advanced Graphics (Gelişmiş Grafik Ayarları)

Bu sekmedeki **tüm ayarlar kapatılmalıdır**:
*   **Long Shadows:** `Off`
*   **High Resolution Shadows:** `Off`
*   **High Detail Streaming While Flying:** `Off`
*   **Extended Distance Scaling:** `%0`
*   **Extended Shadows Distance:** `%0`

---

## 2. NVIDIA ve AMD Sürücü Optimizasyonları

Grafik kartı denetim masası üzerinden yapılacak ince ayarlar, oyun içi ayarlardan bağımsız olarak render süresini kısaltır.

### NVIDIA Denetim Masası Ayarları

1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesinden `gta5.exe` dosyasını seçin.
3.  Aşağıdaki değişiklikleri uygulayın:
    *   **Güç Yönetimi Modu:** *Maksimum performansı tercih et*
    *   **Düşük Gecikme Oranı (Low Latency Mode):** *Açık* veya *Ultra*
    *   **Doku Süzme - Kalite:** *Yüksek Performans*
    *   **Eşyönsüz Süzme Optimizasyonu:** *Açık*
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** *Açık* (Çok çekirdekli CPU kullanımını zorlar)

### AMD Radeon Software Ayarları

1.  AMD Software panelini açın ve **Oyun > GTA 5** profilini seçin.
2.  Ayarları şu şekilde yapılandırın:
    *   **Radeon Anti-Lag:** *Etkin*
    *   **Radeon Boost:** *Devre Dışı* (GTA 5'te çözünürlük dalgalanmalarına sebep olabilir)
    *   **Görüntü Keskinleştirme (Radeon Image Sharpening):** *%30 - %50*
    *   **Güç Doku Filtreleme Kalitesi:** *Performans*

---

## 3. `commandline.txt` ve `settings.xml` İle Derin Yapılandırma

GTA 5, başlatma komutlarını veya dosya seviyesindeki alt ayarları okuma yeteneğine sahiptir.

### `commandline.txt` Oluşturma

Oyunun kurulu olduğu ana dizine (`GTA5.exe`'nin bulunduğu yer) metin belgesi açıp adını `commandline.txt` yapın ve içine şu kodları ekleyin:

```text
-ignoreDifferentVideoCard
-KB
-DX11
-noBenchmark
-listOfYields
-percentVidMem 100
-numMinerThreads 4
```
*(Not: `-numMinerThreads` değerini işlemcinizin izlek (thread) sayısına göre değiştirebilirsiniz.)*

### `settings.xml` Dosyası Üzerinden Gölgeleri Tamamen Kapatma (Düşük Sistemler İçin)

Eğer VRAM ve GPU kapasiteniz çok düşükse gölgeleri tamamen sıfırlayabilirsiniz:

1.  `Belgelerim\Rockstar Games\GTA V\` konumuna gidin.
2.  `settings.xml` dosyasını Not Defteri ile açın.
3.  `<ShadowQuality value="1" />` satırını bulun ve değeri `0` yapın: `<ShadowQuality value="0" />`
4.  Dosyayı kaydedip kapatın ve sağ tıklayıp **Özellikler > Salt Okunur** olarak işaretleyin.

---

## 4. Windows 10/11 İşletim Sistemi Optimizasyonu

İşletim sisteminin arka plan kaynak yönetimi, GTA 5'teki anlık takılmaların (stuttering) birincil sebebidir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows'un VRAM yönetimini ekran kartına devretmesini sağlar.
*   **Ayarlar > Sistem > Monitör > Grafik Ayarları** bölümüne gidin.
*   **Donanım hızlandırmalı GPU zamanlaması** seçeneğini *Açık* konuma getirin ve bilgisayarı yeniden başlatın.

### Windows Oyun Modu ve Yüksek Performans Güç Planı
*   **Oyun Modu:** **Ayarlar > Oyun > Oyun Modu** adımlarını izleyip *Açık* duruma getirin.
*   **Güç Planı:** **Denetim Masası > Güç Seçenekleri** üzerinden *Yüksek Performans* veya *Nihai Performans* planını seçin.

### Sanal Bellek (Pagefile) Düzenlemesi
8 GB veya daha az RAM'e sahip sistemlerde GTA 5, bellek yetersizliğinde çökebilir veya kilitlenebilir.
1.  `Gelişmiş Sistem Ayarları > Performans > Ayarlar > Gelişmiş > Sanal Bellek` yolunu izleyin.
2.  "Tüm sürücülerde disk bellek dosyası boyutunu otomatik yönet" tikini kaldırın.
3.  GTA 5'in kurulu olduğu diski seçip **Özel Boyut** belirleyin:
    *   *Başlangıç boyutu:* `8192` MB
    *   *En yüksek boyut:* `16384` MB

---

## 5. Başlatıcı (Launcher) ve Arka Plan İşlemleri

GTA 5 çalışırken Rockstar Games Launcher ve Steam arka planda CPU tüketebilir.

1.  **Öncelik Ataması:** Oyun açıldıktan sonra `ALT + Tab` yaparak Görev Yöneticisi'ni açın. `Ayrıntılar` sekmesinden `GTA5.exe` üzerine sağ tıklayıp **Öncelik Ayarla > Yüksek** seçeneğini işaretleyin.
2.  **Arka Plan Uygulamaları:** Discord (Özellikle *Arayüz/Overlay* özelliği kapatılmalıdır), Chrome ve Spotify gibi uygulamaları kapatın.

---

## Özet: Donanım Segmentine Göre FPS Hedefleri

*   **Giriş Seviyesi (Dahili GPU / Eski Kartlar):** 720p/1080p Normal Ayarlar, MSAA Kapalı, Gölgeler Normal/Kapalı -> **45 - 60 FPS**
*   **Orta Seviye (GTX 1650, RX 580 vb.):** 1080p High Ayarlar, FXAA Açık, Grass Quality High -> **75 - 100 FPS**
*   **Üst Seviye (RTX 3060 ve Üzeri):** 1080p/2K Very High/Ultra Ayarlar, Extended Distance Scaling %50 -> **120+ FPS**