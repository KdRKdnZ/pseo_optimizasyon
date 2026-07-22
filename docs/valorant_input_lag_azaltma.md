# Valorant Input Lag (Gecikme) Azaltma Rehberi: Donanım ve Yazılım Optimizasyonları

Input lag (girdileri işleme gecikmesi), bir fare tıklamasının veya klavye tuşunun ekrandaki eyleme dönüşmesi arasında geçen süredir. Valorant gibi milisaniyelerin önemli olduğu rekabetçi FPS oyunlarında yüksek input lag, nişan alma hassasiyetini ve tepki süresini doğrudan olumsuz etkiler.

Bu rehber; oyun içi ayarlardan Windows çekirdek optimizasyonlarına, ekran kartı sürücülerinden çevre birimlerine kadar Valorant'ta sistem gecikmesini minimuma indirmek için uygulayabileceğiniz teknik adımları içermektedir.

---

## 1. Valorant Oyun İçi Görüntü ve Sistem Ayarları

Oyun içi grafik ayarlarının düşürülmesi yalnızca FPS'i artırmakla kalmaz, GPU üzerindeki yükü azaltarak "Render Latency" (işleme gecikmesi) değerini düşürür.

### Grafik Kalitesi Ayarları
*   **Çözünürlük:** Monitörün yerel (native) çözünürlüğü ve en yüksek yenileme hızı (Hz) seçilmelidir.
*   **Görüntü Modu:** Mutlaka **Tam Ekran (Fullscreen)** yapılmalıdır. *Pencereli* veya *Sınırsız Pencereli* modlar, Windows Masaüstü Pencere Yöneticisi'ni (DWM) araya sokarak ek gecikme yaratır.
*   **Material, Texture, Detail, UI Quality:** **Düşük (Low)**.
*   **V-Sync (Dikey Eşitleme):** **Kapalı**. (V-Sync, kare yırtılmalarını engeller ancak ciddi oranda input lag ekler).
*   **Anti-Aliasing (Kenar Yumuşatma):** **Kapalı** veya **FXAA**.
*   **Anisotropic Filtering:** **1x**.
*   **Distortion, Vignette, Bloom:** **Kapalı**.

### Sistem Ayarları ve NVIDIA Reflex
*   **NVIDIA Reflex Low Latency:** **Açık + Takviye (On + Boost)**. 
    *   *Açık:* GPU kuyruğunu sıfırlayarak işlemci-grafik kartı senkronizasyonunu optimize eder.
    *   *Takviye:* GPU çekirdek frekanslarının sürekli yüksek kalmasını sağlayarak işlemci kaynaklı gecikmeleri de azaltır.
*   **Raw Input Buffer (Ham Girdi Tamponu):** **Açık**.
    *   Fare girdilerinin Windows API süreçlerini atlayarak doğrudan oyuna iletilmesini sağlar. Özellikle yüksek polling rate (1000Hz ve üzeri) farelerde işlemci yükünü düşürür ve gecikmeyi azaltır.

---

## 2. Ekran Kartı Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi** bölümüne gidin ve şu ayarları uygulayın:
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** **Ultra** (Oyun içinde NVIDIA Reflex açık ise Reflex bu ayarı devralır, ancak genel sistem stabilitesi için Ultra önerilir).
    *   **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et**.
    *   **Max Frame Rate (Maksimum Kare Hızı):** **Kapalı**.
    *   **G-Sync / FreeSync:** Rekabetçi oyunlarda en düşük gecikme için **Kapalı** tutulması tavsiye edilir.
    *   **Doku Süzme - Kalite:** **Yüksek Performans**.
    *   **Eşyönsüz Süzme Optimizasyonu:** **Açık**.

### AMD Radeon Software Ayarları
1.  **Radeon Anti-Lag:** **Etkin**.
2.  **Radeon Chill:** **Devre Dışı**.
3.  **Radeon Boost:** **Devre Dışı** (Dinamik çözünürlük ölçeklemesi tutarsız gecikmeye yol açabilir).
4.  **Ekran Kartı Profili:** **Performans**.

---

## 3. Windows İşletim Sistemi Optimizasyonları

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1.  Valorant’ın ana çalıştırılabilir dosyasına gidin: 
    `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64\VALORANT-Win64-Shipping.exe`
2.  Dosyaya sağ tıklayıp **Özellikler** > **Uyumluluk** sekmesine gelin.
3.  **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4.  **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçekleme davranışını geçersiz kıl** seçeneğini işaretleyip **Sistem (Gelişmiş)** yapın.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 (2004+) ve Windows 11'de bulunan bu özellik, VRAM yönetimini GPU'ya devreder.
*   **Aarlar** > **Sistem** > **Monitör** > **Grafikler** bölümüne gidin.
*   **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
*   **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** konuma getirin ve bilgisayarı yeniden başlatın.

### Windows Oyun Modu ve Güç Planı
*   **Oyun Modu:** **Açık**. (Windows'un arka plan işlemlerini kısıtlayarak önceliği oyuna vermesini sağlar).
*   **Güç Planı:** **Denetim Masası** > **Güç Seçenekleri** üzerinden **Yüksek Performans** veya **Nihai Performans (Ultimate Performance)** seçilmelidir.

---

## 4. Fare (Mouse) ve Çevre Birimi Ayarları

### Fare Polling Rate (Bildirim Hızı) ve DPI
*   **Polling Rate:** Fare raporlama hızını **1000 Hz** olarak ayarlayın. 2000 Hz, 4000 Hz veya 8000 Hz destekleyen farelerde, işlemciniz yeterince güçlü değilse mikro takılmalar (stuttering) yaşanabilir. Yüksek Hz kullanıyorsanız Valorant'ta *Raw Input Buffer* seçeneğinin açık olduğundan emin olun.
*   **Windows Fare İbre Hassasiyeti:** Windows arama çubuğuna "Fare Ayarları" yazın, **İbre Seçenekleri** sekmesinde hızı **6/11** (tam ortada) tutun ve **İşaretçi hassasiyetini artır (Enhance pointer precision)** seçeneğindeki işareti **kaldırın** (Donanımsal ivmeyi kapatır).

### Monitör Ayarları
*   **Overdrive / Response Time:** Monitörünüzün OSD menüsünden yanıt süresini **Hızlı (Fast)** veya **En Hızlı (Fastest/Extreme)** moduna getirin. *Note: Aşırı yüksek ayarlarda "Inverse Ghosting" (Ters Gölgelenme) oluşuyorsa bir alt seviyeye çekin.*
*   **Bağlantı Türü:** Monitörünüzü ekran kartına mutlaka **DisplayPort (DP)** kablosu ile bağlayın.

---

## 5. Donanım ve Ağ Tarafında Kritik Adımlar

*   **Çift Kanal (Dual-Channel) RAM:** Tek kanal (Single-Channel) RAM kullanımı, işlemci verimini düşürerek %1 Low FPS değerlerini baltalar ve gecikmeyi artırır. Belleklerin çift kanal çalıştığından emin olun.
*   **Ethernet Bağlantısı:** Wi-Fi kullanımı paket kaybına (Packet Loss) ve dalgalı ping değerlerine yol açar. Bu durum sunucu tarafında "Desync" ve girdi algılama gecikmesi yaratır. Kablolu bağlantı tercih edilmelidir.
*   **USB Port Seçimi:** Fare ve klavyeyi anakartın arka panelindeki doğrudan işlemciye bağlı olan **USB 3.0/3.1** portlarına takın. USB çoğaltıcı (Hub) kullanmayın.

---

## Özet Kontrol Listesi (Checklist)

| Ayar | Önerilen Değer | Etki Alanı |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran | İşletim Sistemi Gecikmesi |
| **NVIDIA Reflex** | Açık + Takviye | GPU/Sistem Gecikmesi |
| **Raw Input Buffer** | Açık | Fare Girdisi Gecikmesi |
| **V-Sync** | Kapalı | Ekran Gecikmesi |
| **Windows Oyun Modu**| Açık | İşlemci Önceliği |
| **Fare Polling Rate** | 1000 Hz (veya kararlı en yüksek) | Girdi Hassasiyeti |
| **Güç Planı** | Yüksek / Nihai Performans | Donanım Frekansı |