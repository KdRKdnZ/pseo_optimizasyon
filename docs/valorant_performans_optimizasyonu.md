# Valorant Performans Optimizasyonu Rehberi: FPS Artırma ve Düşük Gecikme Ayarları

Valorant, Unreal Engine 4 motoru üzerinde çalışan ve büyük oranda CPU (İşlemci) tek çekirdek performansına dayalı bir taktiksel FPS oyunudur. Yüksek kare hızları (FPS) elde etmek yalnızca akıcılık sağlamakla kalmaz, aynı zamanda girdi gecikmesini (input lag) ve kare süresini (frame time) düşürerek rekabetçi avantaj sunar. 

Bu rehber, Valorant'ta maksimum FPS, minimum gecikme ve kararlı bir kare hızı grafiği elde etmek için uygulanması gereken teknik optimizasyon adımlarını içermektedir.

---

## 1. Oyun İçi Video ve Grafik Ayarları

Oyun içi grafik ayarlarında temel hedef, GPU yükünü sıfırlayarak işlemcinin kare üretme hızını maksimuma çıkarmaktır.

### Genel Grafik Ayarları
*   **Görüntü Modu:** Tam Ekran (Fullscreen)
    *   *Teknik Neden:* "Pencereli Tam Ekran" modu, Windows DWM (Desktop Window Manager) katmanını devreye sokarak 10-15 ms ek girdi gecikmesine yol açar. "Tam Ekran" modu, oyuna doğrudan donanım erişimi verir.
*   **Çözünürlük:** Monitörün Doğal (Native) Çözünürlüğü ve Yenileme Hızı (Örn: 1920x1080 144Hz / 240Hz).
*   **NVIDIA Reflex Düşük Gecikme:** Açık + Takviye (On + Boost)
    *   *Teknik Neden:* CPU ve GPU arasındaki işleme kuyruğunu dinamik olarak optimize eder. "Boost" seçeneği, GPU saat hızlarının oyun esnasında alt seviyelere düşmesini engeller.

### Gelişmiş Grafik Ayarları
*   **Çoklu İzlek Okuma (Multithreaded Rendering):** **AÇIK** *(En kritik ayar)*
    *   *Teknik Neden:* İşlemcinin birden fazla çekirdeğini aynı anda kullanmasını sağlar. 8 çekirdekli modern işlemcilerde %40'a varan FPS artışı sağlar. İşlemciniz 8 çekirdek/izlek altındaysa bu seçenek görünmeyebilir.
*   **Materyal / Dokudaki Kalite:** Düşük
*   **Ayrıntı / Arayüz Kalitesi:** Düşük
*   **V-Sync (Dikey Eşitleme):** Kapalı *(Girdi gecikmesini devasa oranda artırır).*
*   **Nitelik Kaybını Önleme (Anti-Aliasing):** Hiçbiri veya MSAA 2x
*   **Eşyönsüz Filtreleme (Anisotropic Filtering):** 1x
*   **Netliği Artır:** Kapalı
*   **Deneysel Keskinleştirme:** Kapalı
*   **Bozulma (Distortion) ve Gölgeler:** Kapalı

---

## 2. Windows İşletim Sistemi Optimizasyonları

Windows 10 ve Windows 11 üzerinde yapılacak çekirdek seviyesindeki düzenlemeler, sistem kaynaklarının Riot Vanguard ve Valorant'a öncelikli aktarılmasını sağlar.

### Windows Oyun Modu ve HAGS
1.  **Oyun Modu:** `Ayarlar > Oyun > Oyun Modu` yolunu izleyin ve **Açık** konuma getirin. Windows, arka plan işlemlerini kısıtlayarak CPU önceliğini oyuna verir.
2.  **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar > Sistem > Ekran > Grafik Ayarları` altından **Açık** konuma getirin. VRAM yönetimini CPU'dan alıp doğrudan GPU'ya devrederek gecikmeyi düşürür.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
Valorant'ın çalıştırılabilir dosyası (executable) üzerindeki Windows katmanlarını kaldırmak kare kararlılığı sağlar:

1.  Dosya Gezgini'ni açın ve şu konuma gidin: 
    `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64`
2.  `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayıp **Özellikler**'e girin.
3.  **Uyumluluk** sekmesine gelin.
4.  **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
5.  **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçeklendirme davranışını geçersiz kıl"** kutucuğunu işaretleyip *Uygulama* olarak ayarlayın.

### Güç Planı Optimizasyonu
İşlemci çekirdeklerinin düşük güç durumlarına (C-states) geçerek frekans düşürmesini engellemek gerekir.

1.  Komut İstemi'ni (CMD) Yargıç/Yönetici olarak çalıştırın.
2.  Nihai Performans modunu aktif etmek için şu kodu yapıştırın ve Enter'a basın:
    ```bash
    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
    ```
3.  `Denetim Masası > Güç Seçenekleri` yolundan **Nihai Performans (Ultimate Performance)** planını seçin.

---

## 3. Ekran Kartı Sürücü Ayarları

### NVIDIA Denetim Masası Ayarları
1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi** bölümüne gidin ve **Program Ayarları** sekmesinden Valorant'ı (`VALORANT-Win64-Shipping.exe`) seçin.
3.  Aşağıdaki parametreleri uygulayın:
    *   **Güç Yönetim Modu:** Maksimum performansı tercih et
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık
    *   **Doku Süzme - Kalite:** Yüksek Performans
    *   **Eşyönsüz Süzme Optimizasyonu:** Açık
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık
    *   **Dikey Eşitleme:** Kapalı

### AMD Radeon Software Ayarları
1.  AMD Software uygulamasını açın ve **Oyunlar > Valorant** sekmesine gidin.
2.  **Radeon Anti-Lag:** Etkin *(Input lag'i düşürür).*
3.  **Radeon Chill:** Devre Dışı.
4.  **Radeon Boost:** Devre Dışı *(Dinamik çözünürlük düşüşü pikselleşmeye yol açar).*
5.  **Dikey Yenileme İçin Bekle:** Her zaman kapalı.

---

## 4. Kayıt Defteri (Registry) ve Sistem İnce Ayarları

### HPET (High Precision Event Timer) Devre Dışı Bırakma
HPET, eski bir sistem zamanlayıcısıdır ve modern oyunlarda mikro takılmalara (stuttering) yol açabilir.

1.  CMD'yi Yönetici olarak açın.
2.  Aşağıdaki komutu girin ve Enter'a basın:
    ```cmd
    bcdedit /deletevalue useplatformclock
    ```
3.  İşlemci zamanlayıcı dinamiklerini devre dışı bırakmak için şu komutu ekleyin:
    ```cmd
    bcdedit /set disabledynamictick yes
    ```
4.  Bilgisayarı yeniden başlatın.

### Arka Plan İşlemleri ve Vanguard Temizliği
Riot Vanguard (VGK), çekirdek (kernel) seviyesinde çalışan bir anti-cheat yazılımıdır. Arka planda çalışan üçüncü taraf yazılımlarla (Discord Overlay, MSI Afterburner, Razer Synapse vb.) çakışabilir.

*   Oyun esnasında **Discord Görüntü Ara Yüzü (Overlay)** özelliğini kapatın.
*   Arka planda çalışan ikincil tarayıcı sekmelerini kapatın; Chrome/Edge gibi tarayıcılar RAM ve CPU izleklerini işgal eder.

---

## 5. Donanım ve Ağ Optimizasyonu (Network Latency)

FPS yüksek olsa dahi yüksek ping veya paket kaybı (packet loss) gecikme hissi yaratır.

*   **Ethernet Bağlantısı:** Kesinlikle Wi-Fi yerine kablolu RJ45 Ethernet bağlantısı kullanın. Wi-Fi, sinyal dalgalanmaları nedeniyle paket kaybına neden olur.
*   **Fare Polling Rate (Raporlama Hızı):** Farenizin raporlama hızını **1000 Hz** seviyesinde tutun. 4000 Hz veya 8000 Hz gibi değerler, yüksek CPU kullanımına neden olarak Valorant'ta ani FPS düşüşlerine (FPS drops) yol açabilir. Oyun içi "Ham Girdi Süresi" (Raw Input Buffer) ayarını **AÇIK** konuma getirin.
*   **DNS ve Ağ Temizliği:** CMD ekranına sırasıyla şu komutları yazarak ağ önbelleğini temizleyin:
    ```cmd
    netsh winsock reset
    ipconfig /flushdns
    ```

---

## Özet Performans Kontrol Listesi

| Parametre | İdeal Ayar | Etkisi |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran | DWM gecikmesini sıfırlar |
| **Multithreaded Rendering** | Açık | CPU çekirdek kullanımını artırır |
| **NVIDIA Reflex** | On + Boost | Girdi gecikmesini minimuma indirir |
| **Windows Güç Planı** | Nihai Performans | CPU frekans düşüşlerini engeller |
| **Raw Input Buffer** | Açık | Fare girdilerini doğrudan oyuna iletir |