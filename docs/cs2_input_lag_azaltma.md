# CS2 Input Lag (Gecikme) Azaltma Rehberi: Teknik ve Kesin Çözümler

Counter-Strike 2 (CS2), yeni Source 2 motoru ve "sub-tick" sistemi nedeniyle girdi gecikmesine (input lag) karşı CS:GO'ya kıyasla daha hassastır. Farenizi hareket ettirdiğiniz an ile eylemin ekrana yansıması arasındaki süreyi (end-to-end latency) en aza indirmek, sprey kontrolü ve tepki süresi için kritik önem taşır.

Bu rehberde, CS2'de input lag değerini milisaniye (ms) seviyesinde düşürmenizi sağlayacak teknik optimizasyon adımları yer almaktadır.

---

## 1. Oyun İçi Görüntü Ayarları (In-Game Settings)

Grafik kalitesinden çok kare işleme süresini (render latency) düşürmeye odaklanan optimizasyonlar:

*   **Görüntü Modu:** Mutlaka **Tam Ekran (Fullscreen)** olmalıdır. Pencereli veya Çerçevesiz Pencereli modlar, Windows Masaüstü Pencere Yöneticisi'ni (DWM) devreye sokarak ek 1-2 kare gecikme ekler.
*   **NVIDIA Reflex Low Latency:** **Açık + Boost (Enabled + Boost)** yapılmalıdır. GPU kullanımının %99'a ulaştığı durumlarda oluşan işlem kuyruğunu temizler ve sistem gecikmesini doğrudan azaltır. (AMD kullanıcıları için Radeon Anti-Lag).
*   **Dikey Eşitleme (V-Sync):** **Devre Dışı (Off)**. V-Sync, kareleri monitörün tazeleme hızına hizalamak için gecikme kuyruğu oluşturur.
*   **G-Sync / FreeSync:** Rekabetçi düzeyde en düşük gecikme için **Kapatılması** önerilir. Ancak yırtılmasız ve akıcı görünüm isteniyorsa; NVIDIA Denetim Masası'ndan G-Sync Açık + V-Sync Açık + FPS Sabitleme (Monitör Hz değerinin 3-4 eksiği) konfigürasyonu kullanılmalıdır. En düşük gecikme için ise ikisi de **Kapalı** olmalıdır.
*   **Çoklu Örneklemeli Kenar Yumuşatma (MSAA):** **4x MSAA** veya **2x MSAA**. "Yok" yapmak piksel kenarlarını bozarak odaklanmayı zorlaştırır; 8x MSAA ise GPU üzerindeki yükü artırarak render süresini uzatır.
*   **Gelişmiş Gölge Kalitesi:** **Düşük (Low)** veya **Orta (Medium)**. Yüksek gölge ayarları GPU işleme süresini artırır.

---

## 2. NVIDIA ve AMD Sürücü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
1.  Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2.  **3D Ayarlarının Yönetilmesi** bölümüne gidin ve **Program Ayarları** sekmesinden `cs2.exe` dosyasını seçin.
3.  Aşağıdaki parametreleri uygulayın:
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** **Ultra** veya **Açık (On)** (Oyun içi Reflex zaten aktifse bu ayarı otomatik yönetir, ancak Ultra'da kalması önerilir).
    *   **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et**.
    *   **Eşyönsüz Süzme (Anisotropic Filtering):** **Kapalı** veya **Uygulama Kontrolünde**.
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** **Açık**.

### AMD Radeon Software Ayarları
1.  AMD Software panelini açın ve **Oyunlar > Counter-Strike 2** profiline girin.
2.  **Radeon Anti-Lag:** **Etkin**.
3.  **Radeon Boost:** **Devre Dışı** (Dinamik çözünürlük değişimi aim hassasiyetini bozar).
4.  **Dikey Yenileme İçin Bekleyin (V-Sync):** **Her Zaman Kapalı**.

---

## 3. CS2 Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kutusuna aşağıdaki kodları ekleyin:

```text
-nojoy -high -vulkan (Sadece AMD/Intel ekran kartlarında denenmelidir, varsayılan DirectX 11 genelde daha az gecikmelidir)
```

*   `-nojoy`: Oyun kolu (joystick) sistem izleyicisini kapatır, arka planda ekstra thread çalışmasını engeller.
*   `-high`: İşlemcinin CS2 işlemine yüksek öncelik vermesini sağlar. *(Not: Bazı yeni nesil Intel Alder/Raptor Lake işlemcilerde performans çekirdekleri yerine verimlilik çekirdeklerini atayabileceğinden, kasma yaşarsanız bu komutu silin).*

---

## 4. Windows ve Sistem Düzeyinde Optimizasyonlar

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1.  `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64` dizinine gidin.
2.  `cs2.exe` dosyasına sağ tıklayıp **Özellikler** deyin.
3.  **Uyumluluk** sekmesine geçin.
4.  **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
5.  **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçekleme davranışını geçersiz kıl** seçeneğini aktif edip "Uygulama"yı seçin.

### Oyun Modu ve HAGS Ayarları
*   **Windows Oyun Modu:** Windows 10 (21H2 ve üzeri) ile Windows 11'de Oyun Modunu **Açık** konuma getirin. Arka plan işlemlerini kısıtlayarak CPU gecikmesini düşürür.
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** `Ayarlar > Sistem > Monitör > Grafik Ayarları` yolunu izleyin. HAGS özelliğini **Açık** hale getirin. (NVIDIA GTX 1000 serisi ve üzeri / AMD RX 5000 serisi ve üzeri kartlarda gecikmeyi azaltır).

### Fare (Mouse) Ayarları
*   **Polling Rate (Raporlama Hızı):** Farenizin yazılımı üzerinden polling rate değerini **1000 Hz** yapın. 2000 Hz / 4000 Hz / 8000 Hz gibi yüksek değerler güçlü CPU gerektirir; aksi takdirde mikro takılmalara (stuttering) ve tutarsız input lag değerlerine yol açar.
*   **İşaretçi Hassasiyetini Artır (Windows):** `Denetim Masası > Fare > İşaretçi Seçenekleri` sekmesinden bu seçeneğin **işaretini kaldırın** (Raw Input varsayılan olarak CS2'de açıktır ancak Windows ivmesini kapatmak önerilir).

---

## 5. Konsol Kodları ve Autoexec Ayarları

Oyun içi konsola veya `autoexec.cfg` dosyanıza eklemeniz gereken performans ve gecikme odaklı komutlar:

```text
fps_max 0
```
*   FPS sabitlemeyi kapatmak (veya monitör Hz değerinin çok üzerinde sabit bir değere almak), ekran kartının en güncel kareyi oluşturmasını sağlar. Bu durum kare süresini (frame time) düşürerek farenin daha tepkisel hissettirmesini sağlar.

```text
engine_low_latency_sleep_after_client_tick true
```
*   Frame jank (kare sıçramaları) durumunu engelleyerek sub-tick komutlarının daha istikrarlı işlenmesine yardımcı olur.

---

## Özet Gecikme Kontrol Listesi

| Ayar Kategorisi | Önerilen Yapılandırma | Beklenen Etki |
| :--- | :--- | :--- |
| **Görüntü Modu** | Tam Ekran (Fullscreen) | DWM gecikmesini ortadan kaldırır (-5ms ila -15ms) |
| **NVIDIA Reflex** | Açık + Boost | GPU darboğazında sistem gecikmesini sıfırlar |
| **Monitör Hz** | En Yüksek Değer (144Hz / 240Hz / 360Hz) | Piksel yenileme süresini doğrudan düşürür |
| **Mouse Polling Rate**| 1000 Hz | Girdi okuma süresini 1ms'ye sabitler |
| **V-Sync / G-Sync** | Kapalı | Tamponlama (buffering) gecikmesini engeller |