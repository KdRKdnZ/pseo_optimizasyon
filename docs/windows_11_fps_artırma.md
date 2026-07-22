# Windows 11 FPS Artırma Rehberi: Donanım ve Sistem Bazlı Performans Optimizasyonu

Windows 11, gelişmiş grafik arabirimi ve arka plan servisleri nedeniyle doğru konfigüre edilmediğinde oyunlarda FPS düşüşlerine (frame drop) ve girdi gecikmesine (input lag) neden olabilir. Bu rehber, işletim sistemi çekirdek ayarlarından ekran kartı konfigürasyonuna kadar sisteminizi maksimum kare hızına ulaştıracak teknik adımları içermektedir.

---

## 1. Windows 11 Çekirdek ve Grafik Ayarlarının Optimizasyonu

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) Aktivasyonu
HAGS, VRAM yönetimini doğrudan GPU'ya devrederek CPU üzerindeki yükü ve komut gecikmesini azaltır.

1. **Ayarlar > Sistem > Ekran > Grafik** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** (Hardware-Accelerated GPU Scheduling) seçeneğini **Açık** konuma getirin.
4. **Pencereli oyunlar için optimizasyonlar** seçeneğini aktif edin (DirectX 10 ve 11 oyunlarda gecikmeyi düşürür).
5. Sistemi yeniden başlatın.

### Bellek Bütünlüğü (VBS / HVCI) Kapatılması
Windows 11'de varsayılan olarak gelen Çekirdek Yalıtımı (VBS), sanallaştırma tabanlı güvenlik sağlar ancak oyun performansında %5 ila %15 arasında düşüşe yol açabilir.

1. Başlat menüsüne **Çekirdek Yalıtımı** (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** duruma getirin.
3. Sistemi yeniden başlatın. *(Not: Güvenlik seviyesini hafifçe düşürür, sadece saf performans odaklı sistemlerde önerilir.)*

### Oyun Modu (Game Mode) Yapılandırması
Windows 11 Oyun Modu, arka plan güncellemelerini durdurur ve CPU çekirdek önceliğini doğrudan çalışan oyuna (executable) atar.

* **Ayarlar > Oyun > Oyun Modu** adımlarını takip ederek özelliği **Açık** hale getirin.

---

## 2. Güç Yönetimi ve İşlemci Parametreleri

### "Nihai Performans" (Ultimate Performance) Güç Planı
Standart "Yüksek Performans" planına ek olarak, mikro mimari seviyesindeki güç tasarrufu durumlarını (C-States) devre dışı bırakan Nihai Performans modunu aktifleştirin.

1. **Komut İstemi'ni (CMD)** Yönetici olarak çalıştırın.
2. Şu kodu yapıştırın ve Enter'a basın:
   ```bash
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Güç Seçenekleri** bölümüne gidin ve **Nihai Performans** planını seçin.

---

## 3. GPU Sürücü ve Sürücü Denetim Masası Ayarları

Eski sürücü kalıntılarını temizlemek için **DDU (Display Driver Uninstaller)** kullanarak güvenli modda mevcut sürücüyü kaldırın ve en güncel WHQL sürücüsünü yükleyin.

### NVIDIA Denetim Masası Optimizasyonu
* **3D Ayarlarının Yönetilmesi** sekmesine gidin:
  * **Güç Yönetimi Modu:** Maksimum performansı tercih et
  * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra
  * **Doku Süzme - Kalite:** Yüksek Performans
  * **Eşyönsüz Süzme (Anisotropic Filtering):** Uygulama Kontrolünde
  * **Dikey Eşitleme (V-Sync):** Kapalı (Monitörünüz G-Sync/FreeSync destekliyorsa oyun içi V-Sync kapatılıp G-Sync açılmalıdır).

### AMD Radeon Software Optimizasyonu
* **Ekran Kartları (Graphics)** sekmesine gidin:
  * **Radeon Anti-Lag:** Etkin (Girdi gecikmesini azaltır)
  * **Radeon Boost:** Devre Dışı (Çözünürlük dalgalanmalarını önlemek için)
  * **Radeon Image Sharpening:** Etkin (%10 - %20 arası keskinleştirme)
  * **Ekran Kartı Profili:** Performans/Oyun

---

## 4. Sistem Görsel Efektleri ve Arka Plan Servisleri

### Görsel Efektlerin Kısılması
1. `Win + R` tuşlarına basın, `sysdm.cpl` yazıp Enter'a basın.
2. **Gelişmiş** sekmesinden Performans altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini işaretleyin.
4. Okunabilirliği korumak için sadece **"Ekran yazı tipi kenarlarını düzelt"** seçeneğini tekrar işaretleyin ve uygulayın.

### Game Bar ve Arka Plan Kaydını Devre Dışı Bırakma
Arka planda sürekli VRAM ve disk yazımı yapan Xbox Game DVR özelliğini kapatın.

1. **Ayarlar > Oyun > Yakalamalar** bölümüne gidin.
2. **Arka planda kaydet** seçeneğini **Kapalı** konuma getirin.
3. **Ayarlar > Oyun > Xbox Game Bar** anahtarını **Kapalı** yapın.

---

## 5. İleri Düzey Windows Kayıt Defteri (Registry) Tweak'leri

> **Uyarı:** Kayıt defteri değişiklikleri öncesinde sistem geri yükleme noktası oluşturmanız tavsiye edilir.

### GameDVR ve Sistem Tepki Süresi Optimizasyonu
1. `Win + R` tuşlarına basıp `regedit` yazın.
2. Aşağıdaki yola gidin:
   `HKEY_CURRENT_USER\System\GameConfigStore`
   * `GameDVR_Enabled` DWORD değerini **0** yapın.
3. Aşağıdaki yola gidin:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile`
   * `NetworkThrottlingIndex` değerine çift tıklayın ve FFFFFFFF (Onaltılık/Hex) yazın.
   * `SystemResponsiveness` değerini **0** yapın.

---

## 6. Oyun İçi Yapılandırma ve Özet Kontrol Listesi

| Parametre | Önerilen Ayar | Teknik Açıklama |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Exclusive Fullscreen) | DWM (Desktop Window Manager) gecikmesini bypass eder. |
| **Ölçekleme (DLSS / FSR / XeSS)** | Kalite (Quality) veya Dengeli | Render çözünürlüğünü düşürüp yapay zeka ile ölçekler, FPS'i artırır. |
| **Görsel Gölge Kalitesi** | Orta / Düşük | VRAM ve GPU Shader birimlerindeki yükü doğrudan hafifletir. |
| **Reflex / Anti-Lag** | Açık + Boost | CPU-GPU kuyruk gecikmesini minimize eder. |

Bu adımların eksiksiz uygulanması, Windows 11 üzerindeki sistem darboğazlarını (overhead) ortadan kaldırarak maksimum donanım verimliliği ve kararlı bir %1 / %0.1 FPS değeri sağlar.