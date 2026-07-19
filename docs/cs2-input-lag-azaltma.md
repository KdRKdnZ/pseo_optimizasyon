---
title: cs2 input lag azaltma
description: cs2 input lag azaltma hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 Input Lag Azaltma: Donanım ve Yazılım Optimizasyon Rehberi

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği yeni fiziksel hesaplamalar ve **sub-tick** sunucu altyapısı nedeniyle, girdi gecikmesine (input lag) karşı CS:GO'dan çok daha hassastır. Milisaniyelerle ölçülen bu gecikme, mermi tescilini (hit registration) ve sprey kontrolünü doğrudan etkiler. 

Bu rehberde, donanım, işletim sistemi ve oyun motoru seviyesinde **CS2 input lag azaltma** yöntemlerini bilimsel ve teknik detaylarıyla inceleyeceğiz.

---

## 1. Input Lag Nedir ve CS2'de Neden Kritik Önem Taşır?

Giriş gecikmesi (input lag), farenize tıkladığınız an ile bu eylemin ekranda piksellere dönüşmesi arasında geçen süredir. CS2'nin sub-tick mimarisi, hareketlerinizi tick-rate sınırlarına bağlı kalmadan kaydeder; ancak yerel sisteminizdeki yüksek gecikme, sunucuya gönderilen paketlerin gecikmesine ve dolayısıyla "merminin gitmeme" hissiyatına yol açar.

Sistem gecikmesi üç ana bileşenden oluşur:
1. **Giriş Gecikmesi (Peripheral Latency):** Fare/klavyenin sinyali bilgisayara iletme süresi.
2. **Oyun ve İşleme Gecikmesi (Game & Render Latency):** CPU'nun girdiyi işlemesi ve GPU'nun kareyi çizmesi arasında geçen süre.
3. **Görüntü Gecikmesi (Display Latency):** Monitörün çizilen kareyi tarayıp ekrana yansıtma süresi.

---

## 2. Donanım Seviyesinde Input Lag Optimizasyonu

Yazılımsal ayarlar, donanımınızın fiziksel sınırlarını aşamaz. Bu nedenle optimizasyona donanım katmanından başlanmalıdır.

### Monitör ve Görüntü Teknolojileri
*   **Yüksek Yenileme Hızı (Hz):** 60Hz bir monitörün kare yenileme süresi 16.6 ms iken, 360Hz bir monitörde bu süre 2.7 ms'ye düşer. CS2 için minimum 144Hz, rekabetçi seviye için 240Hz veya 360Hz monitörler tercih edilmelidir.
*   **G-Sync / FreeSync ve V-Sync Kombinasyonu:** Geleneksel V-Sync ciddi bir input lag kaynağıdır. Ancak, **NVIDIA Reflex + G-Sync (Açık) + V-Sync (Oyun İçi Kapalı, NVIDIA Denetim Masası Açık)** kombinasyonu, kare hızını monitörün maksimum Hz değerinin 3 FPS altına sabitleyerek yırtılmaları önler ve en kararlı kare geçiş süresini (frame pacing) sunar.

### Çevre Birimleri (Mouse & Keyboard)
*   **Polling Rate (Raporlama Hızı):** Farenizin raporlama hızını 1000Hz (1 ms) veya destekliyorsa 4000Hz/8000Hz (0.25 ms / 0.125 ms) değerine ayarlayın. Yüksek polling rate değerleri CPU yükünü artırır; bu nedenle güçlü bir işlemciniz (Ryzen 7 7800X3D veya Intel i7-13700K ve üzeri) yoksa 1000Hz en stabil seçenektir.
*   **Debounce Delay:** Mekanik klavyelerde tuş basım algılama gecikmesini (debounce delay) klavye yazılımından en düşük değere (mümkünse 1 ms veya Rapid Trigger özellikli optik anahtarlarda 0.1 mm) indirin.

---

## 3. İşletim Sistemi ve Sürücü Ayarları

Windows ve ekran kartı sürücülerinin varsayılan ayarları genellikle enerji tasarrufu odaklıdır. Rekabetçi oyunlar için bu ayarların performans moduna alınması gerekir.

### NVIDIA Denetim Masası Ayarları
NVIDIA ekran kartı kullananlar için en düşük gecikmeyi sağlayan kritik ayarlar şunlardır:

*   **Düşük Gecikme Oranı Modu (Low Latency Mode):** **Ultra** veya **Açık (On)** konumuna getirin. Bu ayar, CPU'nun hazırladığı kare kuyruğunu (render queue) sıfıra indirerek doğrudan GPU'ya aktarır.
*   **Güç Yönetimi Modu:** **Maksimum Performansı Tercih Et** olarak ayarlayın. Ekran kartı çekirdek saat hızlarının (core clocks) oyun esnasında dalgalanmasını önler.
*   **Dikey Senkronizasyon (V-Sync):** G-Sync kullanmıyorsanız kesinlikle **Kapalı** yapın.
*   **Bağlantılı Optimizasyon (Threaded Optimization):** **Açık** konumda olmalıdır. Source 2 motorunun çoklu çekirdek performansını optimize eder.

### Windows Optimizasyonları
*   **HAGS (Donanım Hızlandırmalı GPU Zamanlaması):** *Ayarlar > Sistem > Monitör > Grafik ayarları* altından HAGS'ı **Açık** konuma getirin. Bu, CPU üzerindeki zamanlama yükünü doğrudan GPU'ya devrederek render gecikmesini azaltır.
*   **Oyun Modu (Game Mode):** Windows Oyun Modu'nu **Açık** konuma getirin. Bu mod, arka plan işlemlerinin CPU kaynaklarını tüketmesini engeller ve CS2'ye öncelik tanır.
*   **USB Askıya Alma Ayarı:** *Denetim Masası > Güç Seçenekleri > Plan Ayarlarını Değiştir > Gelişmiş Güç Ayarları* altından "USB seçmeli askıya alma ayarını" **Devre Dışı** yapın. Bu, fare ve klavyenizin güç tasarrufu moduna geçip gecikme yaratmasını önler.

---

## 4. CS2 Oyun İçi ve Başlatma Seçenekleri

CS2'nin oyun içi grafik motoru ayarları, sistem gecikmesini doğrudan manipüle etmenize olanak tanır.

### Grafik Ayarları ve NVIDIA Reflex
Oyun içi grafik ayarlarında performansı ve gecikmeyi etkileyen en önemli parametreler şunlardır:

| Ayar | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **NVIDIA Reflex Low Latency** | **Etkin + Takviye (Enabled + Boost)** | GPU saat hızlarını maksimumda tutar ve CPU render kuyruğunu tamamen ortadan kaldırır. |
| **Dikey Eşitleme (V-Sync)** | **Devre Dışı** | Ekran kartı ve monitör senkronizasyon gecikmesini önler. |
| **Görüntü Modu** | **Tam Ekran (Fullscreen)** | Windows Masaüstü Pencere Yöneticisi'nin (DWM) getirdiği ek 1 karelik gecikmeyi (yaklaşık 4-8 ms) baypas eder. |
| **Çoklu Örnekleme Kenar Yumuşatma** | **CMAA2 veya 2x MSAA** | Yüksek MSAA değerleri GPU darboğazına yol açarak render gecikmesini artırır. |
| **Gölge Kalitesi** | **Orta veya Yüksek** | CS2'de oyuncu gölgeleri taktiksel avantaj sağlar; ancak "Çok Yüksek" ayarı CPU/GPU darboğazı yaratır. |

### Başlatma Seçenekleri (Launch Options)
Steam kütüphanenizde CS2'ye sağ tıklayıp *Özellikler > Başlatma Seçenekleri* kısmına aşağıdaki komutları ekleyin:

```text
-nojoy -high +cl_updaterate 128
```

*   `-nojoy`: Joystick/Gamepad taramasını devre dışı bırakarak CPU üzerindeki gereksiz thread yükünü kaldırır.
*   `-high`: CS2 işlemine Windows üzerinde yüksek öncelik (CPU priority) atar. (Eğer sisteminizde kararsızlığa yol açarsa bu komutu kaldırın).

### Konsol Komutları (CFG)
Oyun içi konsolu (`~`) açarak aşağıdaki komutları uygulayın:

*   `fps_max 0` veya `fps_max [Monitör Hz x 2]`: Sınırsız FPS genellikle en düşük input lag'i sunar. Ancak FPS değeriniz çok dalgalıysa (örneğin 150 ile 400 arası), FPS'i stabil bir değere sabitlemek kare geçiş süresini (frametime) düzelterek daha akıcı bir deneyim sağlar.
*   `engine_low_latency_sleep_after_client_tick true`: NVIDIA Reflex aktifken karelerin daha tutarlı işlenmesini sağlar ve mikro takılmaları azaltır.

---

## 5. Sonuç ve Performans Takibi

CS2'de input lag'i minimize etmek, tek bir ayardan ziyade donanım, işletim sistemi ve oyun içi ayarların bütünsel bir optimizasyonudur. Yaptığınız değişikliklerin etkisini ölçmek için oyun içindeyken konsola `cl_showfps 2` veya `telemetry` komutlarını yazarak **Frame Time (Kare Süresi)** değerini milisaniye cinsinden takip edin. Bu değerin olabildiğince düşük ve sabit (örneğin 3 ms ve altı) olması, başarılı bir optimizasyon gerçekleştirdiğinizi gösterir.