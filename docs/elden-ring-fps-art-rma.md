---
title: "elden ring fps artırma"
description: "elden ring fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Elden Ring FPS Artırma ve Optimizasyon Rehberi: Teknik Çözümler

Elden Ring, DirectX 12 mimarisi ve FromSoftware'in oyun motoru yapısı nedeniyle özellikle işlemci (CPU) ve ekran kartı (GPU) kaynaklarını yoğun kullanan, zaman zaman "shader compilation stutter" (gölgelendirici derleme takılması) sorunlarıyla karşılaşılabilen bir yapımdır. 

Aşağıdaki adımlar, Elden Ring'de minimum görsel kayıpla maksimum FPS elde etmenizi sağlayacak teknik optimizasyonları içermektedir.

---

## 1. En Yüksek FPS İçin Oyun İçi Grafik Ayarları

Oyun içi grafik ayarlarının performansa etkisi eşit değildir. Bazı ayarlar görsel kaliteyi az etkilerken ekran kartını aşırı derecede yükler.

Aşağıdaki yapılandırma, **Kalite/Performans dengesi** için optimize edilmiştir:

| Grafik Ayarı | Önerilen Değer | Performans Etkisi |
| :--- | :--- | :--- |
| **Ray Tracing Quality** | **Off (Kapalı)** | %30 - %50 Düşüş (Kesinlikle Kapatın) |
| **Screen Mode** | **Borderless Windowed** | Takılmaları (Stuttering) Azaltır |
| **Resolution** | Monitör Özgün Çözünürlüğü | Yüksek |
| **Texture Quality** | **High** (6GB+ VRAM) / **Medium** (4GB VRAM) | Düşük (VRAM Yeterliyse) |
| **Antialiasing Quality** | **High** | Düşük |
| **SSAO** | **Medium** | Orta |
| **Depth of Field** | **Off** veya **Low** | Düşük (Kişisel Tercih) |
| **Motion Blur** | **Off** | Düşük |
| **Shadow Quality** | **Medium** | **Yüksek** |
| **Lighting Quality** | **Medium** | Orta |
| **Effects Quality** | **Medium** | **Yüksek** (Büyü ve Patlamalarda FPS Düşüşünü Önler) |
| **Volumetric Quality** | **Low** veya **Medium** | **Çok Yüksek** |
| **Reflection Quality** | **Low** | Orta |
| **Global Illumination Quality**| **Medium** | Orta |
| **Grass Quality** | **Medium** | **Yüksek** (Açık Dünyada FPS'i Doğrudan Etkiler) |

---

## 2. NVIDIA ve AMD Sürücü Optimizasyonları

Elden Ring’deki anlık FPS düşüşlerinin (Micro-stuttering) ana sebebi Shader önbelleğinin yetersizliğidir. Sürücü seviyesinde yapılacak ayarlamalar bu sorunu büyük oranda çözer.

### NVIDIA Denetim Masası Ayarları:
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** > **Program Ayarları** sekmesine gidin.
3. Ekle butonundan `eldenring.exe` dosyasını seçin.
4. Aşağıdaki ayarları uygulayın:
   * **Shader Cache Size (Gölgelendirici Önbellek Boyutu):** `10 GB` veya `Unlimited` (Sınırsız). *(Takılmaları çözen en kritik ayardır).*
   * **Power Management Mode (Güç Yönetimi Modu):** `Prefer Maximum Performance` (Maksimum Performansı Tercih Et).
   * **Low Latency Mode (Düşük Gecikme Oranı Modu):** `On` veya `Ultra`.
   * **Threaded Optimization (Oyun İzleği Optimizasyonu):** `On`.
   * **Max Frame Rate:** `60` (Oyun zaten 60 FPS kilitli olduğu için GPU dalgalanmasını önler).

### AMD Radeon Software Ayarları:
1. **AMD Radeon Software** uygulamasını açın.
2. **Oyun** sekmesinden Elden Ring’i seçin.
3. **Radeon Anti-Lag:** `Etkin`.
4. **Radeon Boost:** `Devre Dışı`.
5. **Radeon Enhanced Sync:** `Devre Dışı`.
6. **Reset Shader Cache (Gölgelendirici Önbelleğini Sıfırla):** Bu butona basarak eski önbelleği temizleyin.

---

## 3. Windows Sistem ve Güç Ayarları

Windows'un varsayılan kaynak yönetimi, DirectX 12 oyunlarında darboğaza sebep olabilir.

### Windows Grafik Ayarları (HAGS)
1. Windows Arama çubuğuna **Grafik Ayarları** yazın ve açın.
2. **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)** seçeneğini `Açık` konuma getirin.
3. Aşağıdaki "Gözat" butonuna tıklayarak `eldenring.exe` yolunu bulun:
   *(Varsayılan: `C:\Program Files (x86)\Steam\steamapps\common\ELDEN RING\Game\eldenring.exe`)*
4. Seçtiğiniz `eldenring.exe` üzerine tıklayıp **Seçenekler**'e basın ve **Yüksek Performans**'ı seçin.

### Güç Planı Optimizasyonu
1. Windows Arama çubuğuna `powercfg.cpl` yazın.
2. Güç planını **Yüksek Performans** veya **Nihai Performans (Ultimate Performance)** olarak ayarlayın.

---

## 4. Easy Anti-Cheat (EAC) ve İşlemci Önceliği

Elden Ring’in kullandığı **Easy Anti-Cheat (EAC)** yazılımı, arka planda yüksek CPU kullanımına neden olarak arka arkaya kare düşüşlerine (stutter) yol açabilir.

> **Uyarı:** EAC'yi devre dışı bırakmak oyunu yalnızca **Çevrimdışı (Offline)** modda oynamanıza izin verir. Ban riski yoktur ancak online özellikler kapanır.

### EAC Devre Dışı Bırakma (Çevrimdışı Yüksek Performans):
1. Steam kütüphanenizden Elden Ring'e sağ tıklayıp **Yönet > Yerel Dosyalara Göz At** deyin.
2. `eldenring.exe` dosyasının adını `start_protected_game.exe` olarak değiştirin (Orijinal `start_protected_game.exe` dosyasının adını yedek olarak değiştirin, örneğin `start_protected_game_backup.exe`).
3. Oyunu Steam üzerinden başlattığınızda EAC olmadan doğrudan başlatılacak ve CPU üzerindeki yük azalacaktır.

---

## 5. 60 FPS Kilidini Kaldırma (İsteğe Bağlı)

Elden Ring, motor seviyesinde 60 FPS ile sınırlandırılmıştır. 144Hz veya üzeri monitöre sahip kullanıcılar bu kilidi kaldırmak için 3. parti araçlar kullanabilir.

* **Flawless Widescreen Kullanımı:**
  1. *Flawless Widescreen* uygulamasını indirin.
  2. Uygulama içinden **Elden Ring** eklentisini (Plugin) yükleyin.
  3. "Framerate Cap Adjustment" seçeneğini aktif ederek FPS kilidini kaldırın.
  4. *Not:* Bu işlem EAC kapalıyken (Çevrimdışı Mod) yapılmalıdır.

---

## 6. Özet Öneriler Check-List

- [ ] Ekran kartı sürücülerini DDU (Display Driver Uninstaller) ile temizleyip en güncel sürüme yükseltin.
- [ ] Oyun içindeki **Ray Tracing** seçeneğinin kapalı olduğundan emin olun.
- [ ] NVIDIA Shader Cache boyutunu **10GB** yapın.
- [ ] Windows Oyun Modunu (Game Mode) aktif hale getirin.
- [ ] Arka planda çalışan Chrome, Discord Overlays ve Spotify gibi GPU/RAM tüketen uygulamaları kapatın.