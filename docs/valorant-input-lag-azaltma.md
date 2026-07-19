---
title: valorant input lag azaltma
description: valorant input lag azaltma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Valorant Input Lag Azaltma: Donanım ve Yazılım Seviyesinde Gecikme Optimizasyonu

Valorant gibi taktiksel nişancı oyunlarında milisaniyeler, galibiyet ile mağlubiyet arasındaki çizgiyi belirler. "Input lag" (girdi gecikmesi), farenize tıkladığınız an ile bu eylemin ekranda piksel değişikliği olarak yansıması arasında geçen süredir. Bu rehberde, Valorant'ta girdi gecikmesini minimuma indirmek için uygulayabileceğiniz donanım, işletim sistemi ve oyun içi optimizasyonlarını teknik detaylarıyla inceleyeceğiz.

---

## Input Lag Nedir ve Valorant'ta Neden Kritik Önem Taşır?

Sistem gecikmesi (system latency), uçtan uca (end-to-end) gecikme olarak tanımlanır ve üç ana bileşenden oluşur: **Girdi Gecikmesi (Input Latency)**, **İşleme Gecikmesi (Processing Latency)** ve **Görüntüleme Gecikmesi (Display Latency)**.

```
[Fare/Klavye] ──(USB Polling)──> [CPU (Oyun Motoru)] ──(Render Sırası)──> [GPU] ──(V-Sync/Tarama)──> [Monitör]
```

Valorant, Riot Games'in 128-tick sunucularında çalışan senkronize bir oyundur. Sunucu her 7.81 milisaniyede bir (ms) oyun durumunu günceller. Eğer sisteminizin uçtan uca gecikmesi bu sürenin üzerindeyse, düşmanı görseniz bile sunucuya gönderdiğiniz ateş etme paketi gecikecek ve "merminin gitmemesi" veya "duvar arkasından ölme" gibi durumlar yaşanacaktır.

### Sistem Gecikmesi (System Latency) Bileşenleri
1. **Periferik Gecikmesi:** Fare/klavye anahtarlarının (switch) debounce süresi ve USB sorgulama hızı (polling rate).
2. **Oyun Gecikmesi (Game Latency):** CPU'nun oyun mekaniklerini, fiziklerini ve kullanıcı girdilerini işleme süresi.
3. **Render Gecikmesi (Render Latency):** Karelerin GPU render kuyruğunda bekletilmesi ve çizilmesi süresi.
4. **Ekran Gecikmesi (Display Latency):** Monitörün piksel yanıt süresi (pixel response time) ve tarama (scan-out) süresi.

---

## Windows ve İşletim Sistemi Seviyesinde Gecikme Optimizasyonu

Windows işletim sistemi, varsayılan ayarlarında arka plan hizmetlerine ve enerji tasarrufuna öncelik verir. Bu durum, gerçek zamanlı (real-time) uygulamalar olan oyunlarda gecikmeye yol açar.

### HPET (High Precision Event Timer) Devre Dışı Bırakma
HPET, donanım tabanlı bir zamanlayıcıdır. Ancak modern işlemcilerde (TSC - Time Stamp Counter) kullanımı daha verimlidir. HPET'in açık olması, CPU'ya ek sorgu yükü bindirerek "micro-stuttering" (mikro takılma) ve girdi gecikmesine neden olur.

**Uygulama:**
1. Komut İstemi'ni (CMD) yönetici olarak çalıştırın.
2. Aşağıdaki komutları sırasıyla girin ve Enter'a basın:
   ```bash
   bcdedit /set useplatformclock no
   bcdedit /set disabledynamictick yes
   ```
3. Bilgisayarınızı yeniden başlatın. Bu işlem, işletim sisteminin doğrudan işlemcinin kendi saat hızını (TSC) kullanmasını sağlayarak sistem çağrısı gecikmesini düşürür.

### FSO (Fullscreen Optimizations) ve Game Mode Ayarları
Windows Fullscreen Optimizations (Tam Ekran İyileştirmeleri), oyunları pencereli tam ekran modunda çalıştırarak masaüstü pencere yöneticisinin (DWM) gecikmesini oyuna dahil eder. Gerçek "Exclusive Fullscreen" (Özel Tam Ekran) modunu zorlamak gecikmeyi azaltır.

* **Valorant için FSO Kapatma:**
  1. Valorant'ın kurulu olduğu dizine gidin: `Riot Games\VALORANT\live\ShooterGame\Binaries\Win64`
  2. `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayıp **Özellikler**'i seçin.
  3. **Uyumluluk** sekmesine gelin.
  4. **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
  5. **"Yüksek DPI ayarlarını değiştir"** kısmından "Yüksek DPI ölçeklendirme davranışını geçersiz kıl" seçeneğini aktif edin (Uygulama tarafından gerçekleştirilsin).

* **Windows Oyun Modu (Game Mode):**
  Windows Ayarları > Oyun > Oyun Modu seçeneğini **Açık** konuma getirin. Bu ayar, Valorant çalışırken arka plan Windows güncellemelerini ve CPU kaynaklarının diğer uygulamalar tarafından sömürülmesini engeller.

---

## Valorant Oyun İçi Grafik ve Motor Ayarları

Valorant'ın Unreal Engine tabanlı motoru, girdi gecikmesini doğrudan etkileyen bazı API entegrasyonlarına sahiptir.

### NVIDIA Reflex Low Latency Teknolojisi
NVIDIA Reflex, CPU ile GPU arasındaki render kuyruğunu (render queue) dinamik olarak sıfıra indirir. CPU, GPU'nun bir sonraki kareyi çizmeye hazır olduğu tam anda render komutlarını gönderir.

| Ayar Seçeneği | Açıklama | Hangi Durumda Seçilmeli? |
| :--- | :--- | :--- |
| **Kapalı** | Standart render kuyruğu kullanılır. | Önerilmez. |
| **Açık (On)** | Render kuyruğunu temizler, gecikmeyi azaltır. | GPU darboğazı olan sistemlerde. |
| **Açık + Takviye (On + Boost)** | GPU saat hızlarını (core clock) her zaman maksimumda tutar. | CPU darboğazı olan sistemlerde (Valorant genelde CPU bound'dur). |

**Öneri:** Valorant'ta NVIDIA Reflex ayarını **Açık + Takviye (On + Boost)** yapın. Bu, işlemcinizin ekran kartını beslerken GPU'nun düşük güç moduna geçmesini engeller ve kare sürelerini (frame times) stabilize eder.

### Raw Input Buffer (Ham Girdi Tamponu) Aktifleştirme
Valorant, farenizden gelen verileri işlemek için Windows API'lerini (WM_INPUT) kullanır. Raw Input Buffer ayarı aktif edildiğinde, oyun doğrudan farenin donanım sürücüsünden gelen paketleri okur.

* **Ayarlar > Genel > Ham Girdi Tamponu (Raw Input Buffer) -> AÇIK**

Bu ayar, özellikle **8000Hz** gibi yüksek sorgulama hızına (polling rate) sahip modern oyuncu farelerinde işlemci yükünü azaltır ve fare hareketlerinin oyuna milisaniyenin altında bir sürede iletilmesini sağlar.

---

## Donanım ve Sürücü Seviyesinde Optimizasyonlar

Yazılımsal optimizasyonlar, donanımınızın sınırları dahilinde çalışır. Fiziksel gecikmeyi azaltmak için donanım yapılandırması doğru yapılmalıdır.

### Fare Polling Rate ve USB Port Seçimi
* **Polling Rate (Sorgulama Hızı):** Farenizin bilgisayara saniyede kaç kez konum bilgisi gönderdiğini belirler. 125Hz (8ms gecikme), 500Hz (2ms gecikme), 1000Hz (1ms gecikme) ve 4000Hz/8000Hz (0.25ms - 0.125ms gecikme) değerlerini sunar. Farenizi en az **1000Hz** veya destekliyorsa daha yüksek bir değere ayarlayın.
* **USB Portu:** Farenizi doğrudan anakarta bağlı (arka panel) bir **USB 3.0 (Mavi)** veya **USB 3.1 (Kırmızı)** portuna takın. Ön paneldeki USB portları veya harici USB çoklayıcılar (hub), sinyal iletim hattına ek entegre devreler eklediği için gecikmeyi (jitter ve latency) artırır.

### Ekran Kartı Sürücü Ayarları (NVIDIA Control Panel)
NVIDIA Denetim Masası üzerinden yapılacak spesifik 3D ayarları, sürücü seviyesindeki gecikme yönetimini optimize eder.

1. **Düşük Gecikme Modu (Low Latency Mode):** **Ultra** konumuna getirin. (Eğer oyun içinde NVIDIA Reflex aktifse, bu ayar oyun tarafından otomatik olarak yönetilir ancak genel sistem kararlılığı için Ultra'da kalması önerilir).
2. **Güç Yönetimi Modu (Power Management Mode):** **Maksimum Performansı Tercih Et** olarak ayarlayın. GPU'nun voltaj ve frekans dalgalanmalarını engelleyerek kare sürelerini sabitler.
3. **Düşey Senkronizasyon (V-Sync):** Kesinlikle **Kapalı** olmalıdır. V-Sync, ekran yırtılmalarını önlemek için kareleri bir tampon bellekte (frame buffer) bekletir ve bu durum sisteme **30ms ila 80ms** arasında devasa bir girdi gecikmesi ekler.

---

## Sonuç ve Performans Takibi

Valorant input lag azaltma işlemleri tamamlandıktan sonra, yapılan değişikliklerin doğrulanması gerekir. Oyun içindeki gecikme değerlerini izlemek için şu adımları izleyin:

1. Valorant **Ayarlar > Nitelikler > Performans** sekmesine gidin.
2. **"Oyun Gecikmesi (CPU)"** ve **"Oluşturma Gecikmesi (Render)"** grafiklerini "Yalnızca Metin" veya "Her İkisi" olarak aktif edin.

İdeal bir sistemde **Oluşturma Gecikmesi (Render Latency)** değerinin **5ms'nin altında** olması gerekir. Yukarıdaki optimizasyonlar doğru uygulandığında, uçtan uca sistem gecikmeniz minimum seviyeye inecek, mermilerinizin tescili (hit registration) iyileşecek ve oyun içi tepki süreniz gözle görülür şekilde artacaktır.