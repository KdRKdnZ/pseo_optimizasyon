# Windows 11 Oyun Performansı Artırma Rehberi: FPS ve Sistem Optimizasyonu

Windows 11, gelişmiş grafik mimarisi ve DirectStorage gibi yeni nesil teknolojilerle oyun odaklı bir işletim sistemi olarak tasarlanmıştır. Ancak, varsayılan güvenlik ilkeleri, arka plan hizmetleri ve yanlış yapılandırılmış donanım ayarları kare hızlarında (FPS) düşüşe ve sistem gecikmesine (system latency) neden olabilir. 

Bu rehberde, Windows 11 üzerinde maksimum FPS, minimum gecikme ve kararlı bir oyun deneyimi elde etmek için uygulanması gereken teknik optimizasyon adımları yer almaktadır.

---

## 1. Güvenlik Tabanlı Sanallaştırmaları Devre Dışı Bırakma (VBS ve HVCI)

Windows 11 ile varsayılan olarak açık gelen **Sanal Makine Platformu (VBS - Virtualization-based Security)** ve **Çekirdek Yalıtımı (HVCI - Hypervisor-Protected Code Integrity)**, işlemci üzerinde ek bir yük oluşturur. Microsoft'un verilerine göre bu özelliklerin kapatılması, oyunlarda %5 ila %15 arasında performans artışı sağlar.

### Çekirdek Yalıtımı Kapatma Adımları:
1. `Windows + I` tuşlarına basarak **Ayarlar** menüsünü açın.
2. **Gizlilik ve Güvenlik** > **Windows Güvenliği** > **Cihaz Güvenliği** sekmesine gidin.
3. **Çekirdek Yalıtımı Ayrıntıları** seçeneğine tıklayın.
4. **Bellek Bütünlüğü (Memory Integrity)** seçeneğini **Kapalı** konuma getirin.
5. Bilgisayarı yeniden başlatın.

---

## 2. Grafik Ayarları ve Donanım Hızlandırması Yapılandırması

Windows 11, grafik işlemcinin (GPU) bellek yönetimini optimize eden gelişmiş grafik seçeneklerine sahiptir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS (Hardware-Accelerated GPU Scheduling), yüksek bellek yükü altındaki senaryolarda CPU gecikmesini azaltarak ekran kartının VRAM yönetimini doğrudan üstlenmesini sağlar.

1. **Ayarlar** > **Sistem** > **Ekran** > **Grafikler** yolunu izleyin.
2. **Varsayılan Grafik Ayarlarını Değiştir** bağlantısına tıklayın.
3. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** hale getirin.
4. **Pencere Cinsinden Oyunlar İçin İyileştirmeler** seçeneğini aktif edin.

### Özel Grafik Performansı Atama
Oynadığınız spesifik oyunların her zaman harici GPU ile çalışmasını zorunlu kılabilirsiniz:
1. **Grafikler** menüsünden **Göz At** butonuna tıklayarak oyunun `.exe` dosyasını seçin.
2. Eklenen oyunun üzerine tıklayıp **Seçenekler**'e girin.
3. **Yüksek Performans** (Ekran kartınızın modeli) seçeneğini işaretleyip kaydedin.

---

## 3. Windows Oyun Modu (Game Mode) Yapılandırması

Windows 11 Oyun Modu, oyun çalışırken arka plan işlemlerinin CPU ve RAM kullanımını sınırlandırır, Windows Güncellemelerini duraklatır ve sistem kaynaklarını oyuna yönlendirir.

1. **Ayarlar** > **Oyun** > **Oyun Modu** sekmesine gidin.
2. **Oyun Modu** durumunu **Açık** konuma getirin.

> **İpucu:** **Xbox Game Bar** ve **Captures (Yakalamalar)** özelliklerini aktif olarak kullanmıyorsanız, **Ayarlar > Oyun > Yakalamalar** altındaki "Arka planda kaydet" seçeneğini kapatarak disk ve GPU yükünü azaltın.

---

## 4. Nihai Performans Güç Planını Etkinleştirme

Windows 11'in standart "Yüksek Performans" planı, güç tasarrufu durumlarını tamamen ortadan kaldırmaz. İşlemci çekirdeklerinin mikro saniyelik gecikmelerini (Core Parking) engellemek için **Nihai Performans (Ultimate Performance)** modu etkinleştirilmelidir.

1. **Komut İstemi'ni (CMD)** Yönetici olarak çalıştırın.
2. Aşağıdaki kodu yapıştırıp `Enter` tuşuna basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Windows + R` basıp `powercfg.cpl` yazarak **Güç Seçenekleri**'ni açın.
4. Listeden **Nihai Performans** seçeneğini işaretleyin.

---

## 5. Ekran Kartı Sürücü ve Denetim Masası Optimizasyonu

Güncel sürücüler oyun optimizasyonu için kritik öneme sahiptir. Ekran kartı sürücünüzü (NVIDIA / AMD) güncellemeden önce **DDU (Display Driver Uninstaller)** ile güvenli modda temiz bir kurulum yapılması tavsiye edilir.

### NVIDIA Denetim Masası Ayarları:
* **Görüntü Ayarlarını Önayarla Yap:** "Benim tercihlerimi kullan ve şuna önem ver: Performans"
* **Maksimum Kare Hızı (Max Frame Rate):** Monitör yenileme hızına veya sabitlemek istediğiniz değere ayarlayın.
* **Güç Yönetimi Modu:** "Maksimum performansı tercih et"
* **Düşük Gecikme Oranı Modu (Low Latency Mode):** "Açık" veya "Ultra"
* **Doku Süzme - Kalite:** "Yüksek Performans"

### AMD Software: Adrenalin Edition Ayarları:
* **Graphics Profile:** "E-Sports" veya "Custom"
* **Radeon Anti-Lag:** **Açık** (Giriş gecikmesini düşürür)
* **Radeon Boost:** İhtiyaca göre Açık (Hareket anında çözünürlüğü dinamik düşürerek FPS artırır)
* **Radeon Image Sharpening:** %80 (Keskinleştirme netliği artırır)

---

## 6. Gelişmiş Kayıt Defteri (Registry) ve Ağ Optimizasyonları

### GameDVR'ı Kayıt Defterinden Kapatma
Xbox GameDVR hizmeti arka planda kare işleme yükü bindirebilir.

1. `Windows + R` basıp `regedit` yazın.
2. `HKEY_CURRENT_USER\System\GameConfigStore` yoluna gidin.
3. `GameDVR_Enabled` DWORD değerini çift tıklayıp `0` yapın.
4. `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\` altına gidin.
5. Eğer yoksa `GameDVR` adında yeni bir Anahtar (Key) oluşturun ve içine `AllowGameDVR` adında bir DWORD (32-bit) oluşturup değerini `0` yapın.

### Ağ Gecikmesini (Ping) Düşürme (Nagle's Algorithm)
Çevrimiçi oyunlarda veri paketlerinin biriktirilmeden anında gönderilmesi için Nagle algoritması devre dışı bırakılabilir.

1. `regedit` üzerinden aşağıdaki yola gidin:
   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile`
2. `NetworkThrottlingIndex` değerini bulun ve Hexadecimal olarak `ffffffff` yapın.
3. `SystemResponsiveness` değerini `0` yapın.

---

## 7. Gereksiz Arka Plan Hizmetleri ve Bloatware Temizliği

Windows 11, arka planda çalışan birçok telemetri ve varsayılan uygulama ile gelir. Bunlar işlemci döngülerini ve RAM kapasitesini tüketir.

* **Başlangıç Uygulamaları:** `Ctrl + Shift + Esc` ile Görev Yöneticisi'ni açın, **Başlangıç Uygulamaları** sekmesinden Discord, Spotify, Steam gibi sistem açılışında yüklenen gereksiz yazılımları **Devre Dışı Bırakın**.
* **Görsel Efektleri Sıfırlama:** 
  1. `Windows + R` > `sysdm.cpl` yazın.
  2. **Gelişmiş** > Performans altındaki **Ayarlar** butonuna tıklayın.
  3. **En iyi performans için ayarla** seçeneğini seçin (İsteğe bağlı olarak yalnızca ekran yazı tipi kenarlarını düzeltme seçeneğini açık bırakabilirsiniz).

---

## Optimizasyon Özet Kontrol Listesi

| Yapılacak İşlem | Hedef Bileşen | Beklenen Etki |
| :--- | :--- | :--- |
| **VBS / Bellek Bütünlüğü Kapatma** | CPU / Sanallaştırma | %5 - %15 FPS Artışı |
| **HAGS Etkinleştirme** | GPU / VRAM | Düşük CPU Yükü, Kararlı FPS |
| **Nihai Performans Güç Planı** | CPU | Sıfır Core Parking, Minimum Latency |
| **NVIDIA/AMD Sürücü Tweak** | GPU | Yüksek FPS, Düşük Input Lag |
| **Registry Network Tweaks** | Ağ (NIC) | Düşük Ping, Minimum Packet Loss |

Bu teknik adımların uygulanması, Windows 11 işletim sisteminin oyun oynama esnasında yaratabileceği darboğazları (bottleneck) ortadan kaldırarak mevcut donanımınızdan maksimum verimi almanızı sağlar. Her ana güncelleme sonrasında bu ayarların (özellikle VBS ve Grafik Ayarları) denetlenmesi tavsiye edilir.