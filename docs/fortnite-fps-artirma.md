---
title: fortnite fps artırma
description: fortnite fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Fortnite FPS Artırma Rehberi: Donanım ve Yazılım Optimizasyonu

Fortnite, Unreal Engine 5 (UE5) mimarisine geçişiyle birlikte modern grafik teknolojilerini (Nanite, Lumen, Virtual Shadow Maps) kullanmaya başlamıştır. Bu durum, oyunun hem CPU hem de GPU üzerindeki yükünü ciddi oranda artırmıştır. Rekabetçi bir avantaj elde etmek ve gecikme süresini (input lag) en aza indirmek için sistem kaynaklarının optimize edilmesi şarttır. 

Bu rehber, donanım ve yazılım mimarisi düzeyinde uygulayabileceğiniz, kanıtlanmış **Fortnite FPS artırma** yöntemlerini içermektedir.

---

## Fortnite ve Unreal Engine 5 Mimarisini Anlamak

Unreal Engine 5, çok iş parçacıklı (multi-threaded) çalışan ve işlemci önbelleği ile ekran kartı VRAM'ini yoğun şekilde kullanan bir motordur. Fortnite'ta yüksek FPS değerlerine ulaşmak için öncelikle oyun motorunun donanımınızla nasıl etkileşime girdiğini optimize etmeniz gerekir.

### Rendering API Seçimi: DirectX 11, DirectX 12 ve Performance Mode

Fortnite üç farklı render motoru seçeneği sunar. Doğru API seçimi, donanım mimarinize doğrudan bağlıdır:

*   **DirectX 11:** Eski nesil GPU'lar için uygundur ancak modern çok çekirdekli işlemcilerin (CPU) avantajlarından yararlanamaz. Draw call (çizim çağrısı) darboğazı yaratır.
*   **DirectX 12:** Modern GPU'larda (NVIDIA RTX ve AMD RX serisi) daha kararlı kare hızları ve daha düşük CPU darboğazı sunar. Shader derleme (shader compilation) işlemlerini arka planda daha iyi yönetir.
*   **Performance (Lower Graphical Fidelity) Mode:** Mobil platformlar için optimize edilmiş render boru hattını (pipeline) PC'ye uyarlar. CPU üzerindeki draw call yükünü %50'ye yakın azaltır, gereksiz görsel efektleri devre dışı bırakır ve bellek (RAM) kullanımını optimize eder.

**Öneri:** Maksimum FPS ve en düşük gecikme süresi için **Performance Mode** seçilmelidir. Eğer yeni nesil bir ekran kartınız varsa ve oyunun görsel kalitesinden ödün vermek istemiyorsanız **DirectX 12** tercih edilmelidir.

### Nanite ve Lumen Teknolojilerinin Etkisi

DirectX 12 modunda aktif olabilen **Nanite (Sanal Geometri)** ve **Lumen (Dinamik Küresel Aydınlatma)**, GPU'nun rasterizasyon ve ışın izleme (ray tracing) birimlerine aşırı yük bindirir. Rekabetçi oyunlarda bu iki ayar kesinlikle **kapatılmalıdır**.

---

## İşletim Sistemi ve Sürücü Düzeyinde Optimizasyonlar

Windows işletim sisteminin arka plan servisleri ve grafik sürücüsü ayarları, oyun içi kare hızınızı doğrudan etkiler.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) Aktivasyonu

HAGS (Hardware-Accelerated GPU Scheduling), Windows'un grafik belleği yönetimini doğrudan GPU'nun kendi özel zamanlayıcısına devretmesini sağlar. Bu, CPU üzerindeki yükü azaltarak gecikmeyi düşürür.

1. Windows Arama çubuğuna **Grafik Ayarları** yazın.
2. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini aktif hale getirin.
3. Bilgisayarınızı yeniden başlatın.

### NVIDIA ve AMD Grafik Sürücü Ayarları

Ekran kartı denetim masası üzerinden yapılan optimizasyonlar, sürücü seviyesindeki gecikmeleri (driver overhead) azaltır.

#### NVIDIA Denetim Masası Ayarları:
*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra (CPU'nun kareleri önceden hazırlamasını engelleyerek doğrudan GPU'ya aktarır).
*   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
*   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık (Oyunun çoklu çekirdek desteğini zorlar).
*   **Doku Süzme - Kalite:** Yüksek Performans.

#### AMD Radeon Software Ayarları:
*   **Radeon Anti-Lag:** Etkin (Giriş gecikmesini azaltır).
*   **Radeon Boost:** Devre Dışı (Çözünürlüğü dinamik olarak düşürür, rekabetçi oyunlarda kararsızlığa yol açabilir).
*   **Doku Filtreleme Kalitesi:** Performans.

---

## En İyi Fortnite Oyun İçi Grafik Ayarları (Competitive Config)

En yüksek **Fortnite FPS artırma** verimliliği için oyun içi grafik ayarlarının "Competitive" (Rekabetçi) standartlara getirilmesi gerekir.

| Ayar | Önerilen Değer | Teknik Gerekçesi |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | Windows DWM (Desktop Window Manager) katmanını devre dışı bırakarak en düşük gecikmeyi sağlar. |
| **Çözünürlük** | Monitörün Doğal Çözünürlüğü | Ölçekleme kaynaklı bulanıklığı ve input lag'i önler. |
| **Kare Hızı Sınırı** | Monitör Hz Değeri + 1 (veya Sınırsız) | G-Sync/FreeSync kullanılıyorsa Hz değerinin 3 FPS altına sabitlenmelidir. |
| **3D Çözünürlük** | %100 (veya %90-%95) | GPU darboğazı varsa düşürülmelidir. CPU darboğazı varsa %100 kalmalıdır. |
| **Görüş Mesafesi** | Orta (Medium) veya Destansı (Epic) | Oyuncuların render edilme mesafesini etkilemez, sadece yapıları etkiler. |
| **Gölgeler** | Kapalı | Gölgeler tamamen CPU ve GPU gölgelendirici (shader) birimlerini yorar. |
| **Dokular** | Düşük (Low) | VRAM kullanımını minimumda tutarak stuttering (anlık takılma) sorununu önler. |
| **Efektler ve İşlem Sonrası** | Düşük (Low) | Patlama ve alan efektlerindeki GPU yükünü azaltır. |

---

## Donanım Seviyesinde FPS ve Gecikme (Latency) İyileştirmeleri

Yazılımsal optimizasyonlar bir noktaya kadar etkilidir. Donanım darboğazlarını çözmek, kararlı bir FPS eğrisi (frametime) elde etmenin tek yoludur.

### RAM Frekansı ve Dual-Channel Etkisi

Fortnite, bellek gecikmesine (memory latency) karşı son derece hassastır. Tek kanal (Single-Channel) RAM kullanımı, CPU'nun veriye erişim süresini uzatarak ani FPS düşüşlerine (1% ve 0.1% Low FPS) neden olur.

*   **Dual-Channel:** Belleklerin mutlaka çift kanal (örn: 2x8 GB veya 2x16 GB) olarak takıldığından emin olun. Bu, bellek bant genişliğini iki katına çıkarır.
*   **XMP/EXPO Profilini Etkinleştirin:** BIOS üzerinden XMP (Intel) veya EXPO (AMD) profillerini aktif ederek RAM'lerinizi fabrikasyon olarak belirlenmiş en yüksek frekansta (örn: 3200 MHz veya 6000 MHz) çalıştırın.

### Termal Darboğaz (Thermal Throttling) Kontrolü

İşlemci veya ekran kartı sıcaklığı kritik sınırları (genellikle CPU için 90°C, GPU için 83°C) aştığında, donanım kendini korumak adına saat hızlarını (clock speed) düşürür. Bu durum ani FPS düşüşlerine yol açar.

*   **Çözüm:** Donanım sıcaklıklarını MSI Afterburner ile oyun içinde izleyin. Gerekirse termal macun yenilemesi yapın ve kasa içi hava sirkülasyonunu optimize edin.

---

## Fortnite Config Dosyası (GameUserSettings.ini) Düzenleme

Oyun içi menülerde yer almayan bazı gelişmiş parametreler, yapılandırma dosyası üzerinden optimize edilebilir.

1. `Win + R` tuş kombinasyonu ile Çalıştır penceresini açın.
2. `%localappdata%\FortniteGame\Saved\Config\WindowsClient\` dizinine gidin.
3. `GameUserSettings.ini` dosyasına sağ tıklayıp Not Defteri ile açın.

Aşağıdaki satırları bulun ve değerlerini belirtilen şekilde değiştirin:

```ini
bShowGrass=False
bDisableMouseAcceleration=True
r.MobileHDR=False
r.RayTracing=False
```

*   **bShowGrass:** Haritadaki çimleri devre dışı bırakarak hem görüşü netleştirir hem de GPU yükünü azaltır.
*   **bDisableMouseAcceleration:** Windows fare ivmesini tamamen kapatarak kas hafızanızı ve nişan alma doğruluğunuzu artırır.

Bu değişiklikleri kaydettikten sonra dosyaya sağ tıklayıp **Özellikler** seçeneğinden **Salt Okunur** kutucuğunu işaretleyin. Bu, Fortnite'ın güncellemeler sonrasında bu ayarları sıfırlamasını engeller.