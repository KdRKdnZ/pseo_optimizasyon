# Counter-Strike 2 (CS2) FPS Sabitleme Rehberi: Tüm Yöntemler ve En Teknik Ayarlar

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği gelişmiş grafikler ve "sub-tick" sistemi nedeniyle kararlı bir ekran kartı ve işlemci performansına ihtiyaç duyar. FPS dalgalanmaları (FPS drops), milisaniyelik gecikmelere (input lag) ve akıcılığın bozulmasına yol açar. CS2'de FPS sabitlemek (kare hızını sınırlamak); sistem sıcaklığını düşürmek, "frame time" (kare süresi) tutarlılığını sağlamak ve ekran yırtılmalarını (screen tearing) önlemek için kritik bir adımdır.

Bu rehberde, CS2'de FPS sabitleme işlemlerini oyun içi komutlardan sürücü düzeyindeki ayarlara kadar tüm teknik detaylarıyla inceleyebilirsiniz.

---

## CS2'de FPS Neden Sabitlenmelidir?

1. **Kare Süresi (Frame Time) Stabilitesi:** Dalgalanan bir FPS değeri (örneğin 300'den 180'e düşüş), kareler arasındaki sürenin uzamasına ve oyunun anlık olarak takılmasına (micro-stuttering) neden olur.
2. **Giriş Gecikmesi (Input Lag) Kontrolü:** Ekran kartının %99-%100 yükte çalışması sistem seviyesinde gecikmeyi artırır. FPS'i ekran kartı kullanımını %90-95 seviyesinde tutacak bir değere sabitlemek, giriş gecikmesini minimize eder.
3. **Donanım Sıcaklığı ve Güç Tüketimi:** Sınırsız FPS, bileşenlerin sürekli tam yükte çalışmasına, ısınmasına ve bir süre sonra "thermal throttling" (ısıya bağlı performans düşüşü) yaşanmasına sebep olur.
4. **G-Sync / FreeSync Uyumu:** Değişken yenileme hızlı monitörlerde yırtılmayı önlemek için FPS değerinin monitörün yenileme hızının (Hz) 3-4 kare altında sabitlenmesi gerekir.

---

## Yöntem 1: Oyun İçi Konsol Komutları İle FPS Sabitleme (En Önerilen)

Oyun motoru seviyesinde yapılan kısıtlama, fazladan gecikme eklemediği için en sağlıklı yöntemdir.

### Adım 1: Geliştirici Konsolunu Etkinleştirme
1. CS2'yi açın ve **Ayarlar (Dişli Çark)** simgesine tıklayın.
2. **Oyun** sekmesine gelin.
3. **Geliştirici Konsolunu Etkinleştir (~)** seçeneğini **"Evet"** yapın.

### Adım 2: FPS Sabitleme Komutları
Konsolu açmak için klavyenizdeki `~` veya `"` tuşuna basın ve aşağıdaki komutları girin:

* **Oyun İçi FPS Sabitleme:**
  ```text
  fps_max [istenen_fps_değeri]
  ```
  *Örnek:* 144Hz monitör için tavsiye edilen sabit değer: `fps_max 160` veya `fps_max 300` (sistem gücünüze göre).

* **Menü FPS Sabitleme:**
  Arka planda gereksiz kaynak kullanımını önlemek için ana menüdeki FPS'i sınırlayabilirsiniz:
  ```text
  fps_max_ui 60
  ```

* **FPS Kilidini Kaldırma:**
  ```text
  fps_max 0
  ```
  *(Not: CS2'de `fps_max 0` kullanımı bazı sistemlerde harita yükleme sürelerini uzatabilir. Bu durumda yüksek bir değer yazmak `fps_max 500` daha stabil sonuç verir).*

---

## Yöntem 2: Başlatma Seçenekleri (Launch Options) İle FPS Sabitleme

Oyunu her açtığınızda komutun otomatik olarak uygulanmasını istiyorsanız Steam başlatma seçeneklerini kullanabilirsiniz.

1. **Steam** kütüphanenizde **Counter-Strike 2**'ye sağ tıklayın ve **Özellikler**'i seçin.
2. **Genel** sekmesi altındaki **Başlatma Seçenekleri** metin kutusunu bulun.
3. Kod satırına şu ifadeyi ekleyin:
   ```text
   +fps_max 240
   ```
   *(Buradaki "240" değerini sisteminize uygun sayı ile değiştirin).*

---

## Yöntem 3: NVIDIA Denetim Masası İle FPS Sabitleme

Ekran kartı sürücüsü üzerinden yapılan kısıtlama, oyun içi komuta alternatif bir çözümdür.

1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. Sol menüden **3D Ayarlarının Yönetilmesi** sekmesine girin.
3. **Program Ayarları** sekmesinden **Counter-Strike 2 (cs2.exe)** öğesini seçin (Listede yoksa "Ekle" butonundan seçin).
4. **Maksimum Kare Hızı (Max Frame Rate)** ayarını bulun, **Açık** konuma getirin ve istediğiniz FPS değerini girin.
5. **NVIDIA Reflex Low Latency** modunu oyun ayarlarından **"On + Boost"** yapmak, bu yöntemle oluşabilecek gecikmeleri engeller.

---

## Yöntem 4: AMD Radeon Software İle FPS Sabitleme

AMD ekran kartı kullanıcıları Radeon Chill veya Frame Rate Target Control (FRTC) teknolojisini kullanabilir.

1. Masaüstüne sağ tıklayıp **AMD Software: Adrenalin Edition** uygulamasını açın.
2. **Oyunlar** sekmesinden **Counter-Strike 2**'yi seçin.
3. **Radeon Chill** özelliğini aktif hale getirin.
4. **Min FPS** ve **Max FPS** değerlerini aynı sayıya ayarlayın (Örn: 200 - 200).
5. Alternatif olarak **Gelişmiş** sekmesi altından **Frame Rate Target Control (FRTC)** ayarını açıp hedef FPS'i belirleyebilirsiniz.

---

## Monitör Yenileme Hızına (Hz) Göre Ideal FPS Limiti Nasıl Seçilir?

Sabitlenecek FPS değeri belirlenirken monitör hızı ve sistemin üretebildiği ortalama FPS dikkate alınmalıdır:

| Monitör Hz | Tavsiye Edilen FPS Limiti | Açıklama |
| :--- | :--- | :--- |
| **60 Hz** | `fps_max 120` veya `144` | Giriş gecikmesini düşürmek için Hz değerinin 2 katı önerilir. |
| **144 Hz** | `fps_max 180` veya `240` | Kare süresi dalgalanmasını önler, akıcı hissettirir. |
| **240 Hz** | `fps_max 300` | CS2'nin ideal e-spor performans eşiğidir. |
| **G-Sync / FreeSync Açık** | `fps_max [Monitör Hz - 3]` | Örn: 144Hz için `fps_max 141`. Yırtılmayı ve V-Sync gecikmesini tamamen engeller. |

---

## Sıkça Sorulan Sorular (SSS)

### CS2'de FPS sabitlemek input lag (giriş gecikmesi) yapar mı?
Oyun içi `fps_max` komutu ile yapılan sabitleme kayda değer bir input lag oluşturmaz. Aksine, GPU kullanımının %100'e ulaşıp "GPU Bottleneck" yarattığı durumlarda FPS'i kısıtlamak input lag değerini **düşürür**.

### Dikey Eşitleme (V-Sync) ile FPS sabitlemek mantıklı mı?
**Hayır.** V-Sync, CS2 gibi rekabetçi FPS oyunlarında ciddi miktarda gecikmeye (input lag) neden olur. Kare hızını sınırlamak için V-Sync yerine her zaman `fps_max` veya NVIDIA/AMD sürücü kısıtlamaları kullanılmalıdır.

### FPS değerim belirlediğim limite ulaşmıyor, nedeni nedir?
FPS kısıtlaması bir üst sınırdır. Eğer sisteminiz (CPU/GPU) belirlediğiniz değere ulaşacak güçte değilse, FPS daha düşük seviyelerde kalacaktır. Bu durumda grafik ayarlarını düşürmek veya işlemci yükünü azaltmak gerekir.