# Windows 11 Input Lag (Girdi Gecikmesi) Azaltma Rehberi: Donanım ve Sistem Düzeyinde Optimizasyon

Windows 11 işletim sisteminde input lag (girdi gecikmesi); farenin, klavyenin veya denetleyicinin (gamepad) fiziksel komutları ile ekrandaki eylemin gerçekleşmesi arasında geçen süredir. Özellikle rekabetçi FPS ve ritim oyunlarında ms (milisaniye) düzeyindeki gecikmeler performans doğrudan etkiler. 

Aşağıdaki adımlar, Windows 11 sürücü katmanından grafik arabirimine (DWM) kadar sistemdeki tüm gecikme kaynaklarını minimize etmek için tasarlanmış teknik çözümlerdir.

---

## 1. Windows 11 Çekirdek ve Grafik Ayarları

### Oyun Modunu (Game Mode) Aktifleştirin
Windows 11'in Oyun Modu, arka plan işlemlerinin işlemci (CPU) önceliğini düşürerek mevcut kaynakları oyuna atar ve kare zamanlamasını (frame timing) kararlı hale getirir.

* **Yol:** `Ayarlar > Oyun > Oyun Modu` -> **Açık**

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS (Hardware-Accelerated GPU Scheduling), VRAM yönetimini CPU'dan alarak doğrudan GPU'ya devreder. Bu işlem, arabellek gecikmesini (buffer latency) azaltır.

* **Yol:** `Ayarlar > Sistem > Ekran > Grafik Ayarları` -> **Donanım Hızlandırmalı GPU Zamanlaması** -> **Açık**
* *(Not: Değişikliğin uygulanması için bilgisayarı yeniden başlatın.)*

### Pencere Modundaki Oyunlar İçin İyileştirmeler (Optimizations for Windowed Games)
Windows 11 ile gelen bu özellik, pencereli veya kenarlıksız (borderless) çalışan oyunların geleneksel DWM (Desktop Window Manager) gecikmesini bypass ederek "Legacy Flip Model" yerine "DirectX 12 Flip Model" kullanmasını sağlar.

* **Yol:** `Ayarlar > Sistem > Ekran > Grafik Ayarları` -> **Pencere Modunda Oyunlar İçin İyileştirmeler** -> **Açık**

---

## 2. Grafik Sürücüsü Optimizasyonları

### NVIDIA Denetim Masası Ayarları
NVIDIA ekran kartı kullanıyorsanız, grafik sürücüsünün komut kuyruğunu (render queue) kısaltmak gecikmeyi doğrudan düşürür.

1. Masaüstüne sağ tıklayın ve **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3. Aşağıdaki değerleri değiştirin:
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** `Üstün (Ultra)` *(Kare hızınızı CPU sınırlandırıyorsa gecikmeyi sıfıra yakın tutar).*
   * **Güç Yönetim Modu:** `Maksimum Performansı Tercih Et`.
   * **Dikey Eşitleme (V-Sync):** `Kapalı` *(Oyun içi V-Sync gecikmeyi ciddi oranda artırır).*
   * **Maksimum Kare Hızı:** Monitörün yenileme hızının (Hz) 3-4 FPS altına sabitleyin (Örn: 144Hz için 141 FPS).

### AMD Radeon Software Ayarları
AMD ekran kartlarında sürücü tabanlı gecikme engelleyicileri aktif edin:

1. **Radeon Software** uygulamasını açın.
2. `Ayarlar > Ekran Kartları` sekmesine gidin.
3. **Radeon Anti-Lag:** **Etkin** konumuna getirin.
4. **Radeon Chill:** **Devre Dışı** yapın (Değişken FPS gecikme dalgalanmalarına yol açabilir).

---

## 3. Fare ve Çevre Birimleri Optimizasyonu

### İşaretçi Hassasiyetini Artır (Mouse Acceleration) Kapatma
Windows'un varsayılan fare ivmelendirme özelliği, farenin hızına göre imleç mesafesini değiştirir. Bu durum kas hafızasını olumsuz etkiler ve sisteme ek işleme yükü getirir.

1. `Calıştır` penceresini açın (`Win + R`), `main.cpl` yazıp Enter'a basın.
2. **İşaretçi Seçenekleri** sekmesine gelin.
3. **İşaretçi hassasiyetini artır** seçeneğindeki **işareti kaldırın**.
4. İşaretçi hızını varsayılan değer olan **6/11** konumunda tutun.

### Polling Rate (Bildirim Hızı) Ayarı
Mouse yazılımınız üzerinden (Logitech G Hub, Razer Synapse vb.) farenin tarama frekansını ayarlayın:
* Standart değer: **1000 Hz** (1 ms gecikme).
* Donanımınız destekliyorsa **2000 Hz - 8000 Hz** aralığına çekebilirsiniz (Yüksek CPU kullanımı oluşturabileceğini unutmayın).

### USB Port Seçimi
* Girdi cihazlarınızı arka panelde bulunan (Doğrudan Anakarta Bağlı) **USB 3.0/3.1 (Mavi/Kırmızı)** portlarına takın. 
* Çoğaltıcı (Hub) veya ön panel konnektörlerini kullanmayın.

---

## 4. Gelişmiş Sistem ve Register (Kayıt Defteri) İnce Ayarları

### HPET (High Precision Event Timer) Devre Dışı Bırakma
HPET, donanım zamanlayıcısıdır. Modern işlemcilerde (TSC/LAPIC) HPET'in açık kalması mikrokekelemeye (micro-stuttering) ve girdi gecikmesine neden olabilir.

1. **Komut İstemi**'ni (CMD) Yönetici olarak çalıştırın.
2. Aşağıdaki komutları sırasıyla girin ve Enter'a basın:
   ```cmd
   bcdedit /set useplatformclock false
   bcdedit /deletevalue useplatformclock
   bcdedit /set disabledynamictick yes
   ```
3. Bilgisayarı重新 başlatın.

### USB Güç Tasarrufunu Kapatma
Windows'un USB denetleyicilerini güç tasarrufu için uyku moduna almasını engelleyin.

1. Başlat menüsüne sağ tıklayıp **Aygıt Yöneticisi**'ni açın.
2. **Evrensel Seri Veri Yolu Denetleyicileri** kategorisini genişletin.
3. Tüm **USB Kök Hücre (USB Root Hub)** ögelerine sağ tıklayıp `Özellikler > Güç Yönetimi` sekmesine gidin.
4. **"Güç tasarrufu yapmak için bilgisayar bu aygıtı kapatsın"** seçeneğindeki işareti kaldırın.

---

## 5. Güç Yönetimi ve İşlemci Zamanlaması

### Nihai Performans Güç Planını Aktifleştirme
Windows 11'in gizli yüksek performans modunu aktif ederek CPU çekirdeklerinin düşük güç durumlarına (C-states) geçip gecikme yaratmasını önleyin.

1. **CMD**'yi Yönetici olarak açın ve şu komutu çalıştırın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
2. `Ayarlar > Sistem > Güç ve Pil > Güç Modu` adımlarından **En Yüksek Performans** veya Denetim Masası Güç Seçenekleri'nden **Nihai Performans**'ı seçin.

---

## Özet Kontrol Listesi (Quick Checklist)

| Ayar | İdeal Durum | Etkilediği Bileşen |
| :--- | :--- | :--- |
| **Monitör Yenileme Hızı** | Mümkün Olan En Yüksek Hz | Ekran / DWM |
| **G-Sync / FreeSync** | Açık + V-Sync Açık (NVIDIA Panel) + FPS Limit | Ekran Gecikmesi |
| **NVIDIA Low Latency** | Ultra | GPU Render Queue |
| **Fare Hassasiyet İvmesi** | Kapalı | Fare Sensörü |
| **Windows Oyun Modu** | Açık | CPU Önceliği |
| **HPET** | Devre Dışı | Sistem Zamanlayıcısı |

Bu konfigürasyonlar uygulandığında, Windows 11 üzerindeki donanım-yazılım arası işleme adımları minimuma inecek, tıklama-tepki süresi (click-to-photon latency) en alt seviyeye çekilecektir.