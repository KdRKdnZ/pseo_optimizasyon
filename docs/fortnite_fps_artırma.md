# Fortnite FPS Artırma Rehberi: En Yüksek Performans İçin Detaylı Optimizasyon

Fortnite, Unreal Engine 5 motoruna geçiş yaptıktan sonra sistem kaynaklarını daha yoğun kullanan bir yapıma dönüştü. Rekabetçi bir avantaj elde etmek, girdi gecikmesini (input lag) düşürmek ve kare hızını (FPS) maksimum seviyeye çıkarmak için hem yazılımsal hem de donanımsal optimizasyonlar gereklidir.

Bu rehberde, Fortnite'ta en yüksek FPS değerlerine ulaşmanızı sağlayacak teknik adımları ve SEO uyumlu, güncel optimizasyon yöntemlerini bulabilirsiniz.

---

## 1. Epic Games Başlatıcısı (Launcher) Optimizasyonu

Oyun dosyalarının yönetimi ve başlatıcı ayarları, arka plan kaynak kullanımını doğrudan etkiler.

* **Yüksek Çözünürlüklü Dokuları Silin:**
  1. Epic Games Launcher'ı açın ve **Kütüphane** sekmesine gidin.
  2. Fortnite'ın yanındaki **üç noktaya (...)** tıklayın ve **Seçenekler**'i seçin.
  3. **"Yüksek Çözünürlüklü Dokular" (High-Resolution Textures)** seçeneğindeki işareti kaldırın. Bu işlem yaklaşık 30 GB disk alanı kazandırır ve ekran kartı VRAM yükünü ciddi oranda azaltır.
  4. **"Abonelik Akışı Ön İndirmesi" (DirectX 12 Shaders / Pre-stream Assets)** kutucuğunu işaretleyin. Bu, oyun esnasında yaşanabilecek anlık takılmaları (stuttering) önler.

---

## 2. Oyun İçi Grafik ve Performans Ayarları

Fortnite içerisinde kullanılan işleme modu (Rendering Mode), FPS üzerindeki en belirleyici faktördür.

### En İyi Görüntü Modu: Performans Modu (Performance - Lower Graphical Fidelity)
Zayıf ve orta segment sistemlerin yanı sıra yüksek sistemli espor oyuncuları da **Performans Modu**'nu tercih etmektedir.

* **Görüntü Modu:** Tam Ekran (Pencereli tam ekran gecikmeyi artırır)
* **Çözünürlük:** Monitörün doğal çözünürlüğü (Örn: 1920x1080)
* **Kare Hızı Limiti:** Monitör yenileme hızınızın (Hz) bir tık üzeri (Örn: 144 Hz monitör için 160 FPS veya Sınırsız)
* **İşleme Modu:** Performans (Düşük Grafik Kalitesi)
* **Dikey Eşitleme (V-Sync):** Kapalı
* **Kullanıcı Arayüzü 3D Çözünürlüğü:** %100 (Düşüş yaşanıyorsa %90-%95 seviyesine çekilebilir)
* **Görüş Mesafesi (View Distance):** Yakın veya Orta
* **Dokular (Textures):** Düşük
* **Örgüler (Meshes):** Düşük (Yapıların içi net görünsün isteniyorsa Yüksek yapılabilir, ancak CPU yükünü artırır)

> **Not:** Sisteminizde güçlü bir GPU (RTX 3060 ve üzeri) ve modern bir CPU varsa, **DirectX 12** modu da kararlı FPS sağlayabilir. Ancak en düşük girdi gecikmesi için Performans Modu ilk tercihtir.

---

## 3. Ekran Kartı Denetim Masası Ayarları

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve *Program Ayarları* sekmesinden Fortnite'ı seçin (`FortniteClient-Win64-Shipping.exe`).
3. Aşağıdaki ayarları uygulayın:
   * **Bağlantılı Optimizasyon (Threaded Optimization):** Açık
   * **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra
   * **Doku Süzme - Kalite:** Yüksek Performans
   * **Doku Süzme - Trilineer Optimizasyon:** Açık
   * **G-Sync / FreeSync:** Rekabetçi oyunlar için kapalı tutulması önerilir (veya Reflex ile entegre kullanılmalıdır).

### AMD Radeon Software Ayarları
1. **Radeon Software** uygulamasını açın ve **Ekran Kartları (Graphics)** sekmesine gelin.
2. **Radeon Anti-Lag:** Etkin
3. **Radeon Boost:** Devre Dışı (Çözünürlük dalgalanmasını önlemek için)
4. **Ekran Kartı Profili:** Performans
5. **Doku Filtreleme Kalitesi:** Performans

---

## 4. Windows 10 ve Windows 11 Optimizasyonları

İşletim sisteminin arka plan hizmetleri, CPU işlem sürelerini tüketebilir.

### Oyun Modu ve HAGS
* **Oyun Modu'nu Açın:** Windows Ayarları > Oyun > Oyun Modu > **Açık**. Windows'un sistem kaynaklarını oyuna önceliklendirmesini sağlar.
* **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Grafik Ayarları bölümünden bu özelliği açın ve bilgisayarı yeniden başlatın. (Giriş seviyesi CPU'larda akıcılığı artırır).

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64` dizinine gidin.
2. `FortniteClient-Win64-Shipping.exe` dosyasına sağ tıklayıp **Özellikler**'e girin.
3. **Uyumluluk** sekmesinde **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
4. **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçeklendirme davranışını geçersiz kıl"** kutusunu işaretleyip *Uygulama* olarak ayarlayın.

### Geçici Dosyaları (Cache) Temizleme
Anlık takılmaları gidermek için shader ve geçici bellek önbelleğini temizleyin:
* `Win + R` tuşlarına basın, `%temp%` yazın ve Enter'a basın. Açılan klasördeki tüm dosyaları silin.
* `Win + R` tuşlarına basın, `prefetch` yazın ve klasör içeriğini silin.

---

## 5. Donanım Seviyesinde İpuçları ve Sıcaklık Yönetimi

Yazılımsal ayarlar kadar donanım konfigürasyonu da kritiktir:

* **Çift Kanal (Dual-Channel) RAM Kullanımı:** Fortnite, bellek bant genişliğine aşırı duyarlı bir oyundur. Tek kanal (1x16GB) yerine çift kanal (2x8GB) RAM kullanımı FPS'i %20 ila %40 arasında artırabilir ve anlık FPS düşüşlerini (drop) engeller.
* **XMP / DOCP Profili:** BİOS üzerinden RAM'lerinizin fabrika çıkışı yüksek hız değerlerine (Örn: 3200MHz/3600MHz) ulaştığından emin olun.
* **İşlemci ve GPU Sıcaklıkları:** Aşırı ısınan donanımlar frekans düşürür (Thermal Throttling). HWMonitor veya MSI Afterburner ile sıcaklıkları kontrol edin; CPU ve GPU sıcaklıklarının 80°C altında kalmasını sağlayın.

---

## Sıkça Sorulan Sorular (SSS)

**Fortnite'ta DirectX 11 mi, DirectX 12 mi, yoksa Performans Modu mu daha iyi?**  
Düşük ve orta segment sistemler ile maksimum FPS/en düşük girdi gecikmesi hedefleyenler için **Performans Modu** en iyi seçenektir. Yüksek segment ekran kartına (NVIDIA RTX serisi veya AMD RX 6000/7000 serisi) sahip sistemlerde ise **DirectX 12** daha kararlı kare süreleri (frametime) verebilir.

**NVIDIA Reflex Ayarı Nasıl Olmalı?**  
Oyun içi ayarlarda NVIDIA Reflex seçeneğini **"Açık + Takviye" (On + Boost)** yapmak, CPU ve GPU arasındaki iş yükünü dengeleyerek sistem gecikmesini en alt seviyeye indirir.

**3D Çözünürlüğü Düşürmek FPS'i Etkiler mi?**  
Evet, 3D çözünürlüğü düşürmek ekran kartının işlemesi gereken piksel sayısını azalttığı için FPS'i doğrudan artırır. Ancak görsel netlik bozulacağı için %85'in altına inilmesi tavsiye edilmez.