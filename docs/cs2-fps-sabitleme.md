---
title: cs2 fps sabitleme
description: cs2 fps sabitleme hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 FPS Sabitleme Rehberi: En Düşük Gecikme ve Maksimum Akıcılık

Counter-Strike 2 (CS2), Source 2 motorunun getirdiği yeni fiziksel tabanlı renderlama ve "sub-tick" sunucu altyapısı nedeniyle donanım kaynaklarını CS:GO’ya kıyasla çok daha yoğun kullanır. CS2'de sınırsız FPS (kare hızı) almak her zaman en akıcı oyun deneyimi anlamına gelmez. Doğru yapılandırılmış bir **CS2 FPS sabitleme** işlemi; kare zamanlamasını (frame pacing) iyileştirir, giriş gecikmesini (input lag) azaltır ve sistem bileşenlerinin gereksiz ısınmasını önler.

---

## CS2'de FPS Sabitlemek Neden Önemlidir?

Birçok oyuncu yüksek FPS değerlerinin her zaman daha iyi olduğunu düşünür. Ancak donanım mimarisi ve oyun motoru optimizasyonu açısından durum daha karmaşıktır.

### Frame Pacing (Kare Zamanlaması) ve Akıcılık
Ekranda saniyede 300 kare görmek, bu karelerin eşit zaman aralıklarıyla çizildiği anlamına gelmez. Örneğin; bir saniye içindeki ilk 100 kare 200ms'de, geri kalan 200 kare ise 800ms'de çizilirse, yüksek FPS almanıza rağmen oyunda anlık takılmalar (micro-stuttering) hissedersiniz. FPS'i donanımınızın stabil olarak verebildiği bir değere sabitlemek, kare zamanlamasını eşitler ve akıcılığı maksimuma çıkarır.

### Gecikme (Input Lag) ve Isı Yönetimi
Ekran kartınız (GPU) %99 yük altında çalıştığında, render kuyruğu (render queue) şişer ve bu durum giriş gecikmesini (input lag) ciddi oranda artırır. FPS'i GPU kullanımını %90-95 civarında tutacak bir değere sabitlemek, gecikmeyi minimize eder. Ayrıca işlemci (CPU) ve GPU üzerindeki termal yükü azaltarak ani frekans düşüşlerinin (thermal throttling) önüne geçer.

---

## CS2 FPS Sabitleme Yöntemleri

CS2'de kare hızını sabitlemek için kullanabileceğiniz, teknik olarak en kararlı dört farklı yöntem bulunmaktadır.

### 1. Oyun İçi Konsol Komutu (`fps_max`)
Source 2 motorunun kendi iç mekanizmasını kullanmak, ek bir yazılım katmanı gerektirmediği için en kararlı yöntemdir.

1. CS2'yi başlatın ve **Ayarlar > Oyun > Geliştirici Konsolunu Etkinleştir** seçeneğini **Evet** yapın.
2. `"` veya `~` tuşuna basarak konsolu açın.
3. Konsola aşağıdaki komutu yazın ve Enter tuşuna basın:
   ```text
   fps_max 240
   ```
   *(Not: "240" yerine monitörünüzün yenileme hızına (Hz) ve sistem performansınıza uygun bir değer yazmalısınız.)*
4. Eğer ana menüdeki FPS'i de sınırlamak istiyorsanız şu komutu kullanabilirsiniz:
   ```text
   fps_max_ui 120
   ```

### 2. Başlatma Seçenekleri (Launch Options)
Konsol komutunun her oyuna girişte sıfırlanmasını önlemek için bu değeri Steam başlatma seçeneklerine kalıcı olarak ekleyebilirsiniz.

1. Steam kütüphanenizde **CS2**'ye sağ tıklayın ve **Özellikler**'i seçin.
2. **Genel** sekmesinde bulunan **Başlatma Seçenekleri** kutusuna gelin.
3. Buraya aşağıdaki kodu ekleyin:
   ```text
   +fps_max 240
   ```

### 3. NVIDIA Kontrol Paneli ile FPS Sınırlama
NVIDIA sürücü seviyesinde yapılan sınırlama, oyun motorunun sınırlayıcısına göre bazen daha kararlı kare zamanlaması sunabilir.

1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3. **Program Ayarları** kısmından *Counter-Strike 2 (cs2.exe)* uygulamasını seçin (Listede yoksa "Ekle" diyerek oyunun kurulu olduğu dizinden seçin).
4. **Maksimum Kare Hızı (Max Frame Rate)** ayarını bulun, **Açık** konuma getirin ve hedef FPS değerinizi girip uygulayın.

### 4. AMD Radeon Software ile FPS Sınırlama
AMD ekran kartı kullanıcıları, sürücü düzeyinde gecikmeyi artıran geleneksel sınırlayıcılar yerine **Radeon Chill** teknolojisini kullanmalıdır.

1. **AMD Software: Adrenalin Edition** uygulamasını açın.
2. **Oyun** sekmesinden **CS2**'yi seçin.
3. **Radeon Chill** özelliğini aktif hale getirin.
4. **Min FPS** ve **Max FPS** değerlerini aynı sayıya (örneğin 240) ayarlayarak FPS'i sabitleyin.

---

## G-Sync ve FreeSync Kullanıcıları İçin İdeal FPS Sabitleme Değerleri

Değişken Yenileme Hızı (VRR) teknolojilerini (G-Sync veya FreeSync) kullanan oyuncuların, ekran yırtılmasını önlemek ve en düşük gecikmeyi elde etmek için özel bir sabitleme formülü uygulaması gerekir.

VRR teknolojisinin aktif kalabilmesi için FPS değerinin, monitörün maksimum Hz değerinin altında kalması şarttır. FPS, Hz değerini aştığı anda G-Sync/FreeSync devre dışı kalır ve sistem geleneksel V-Sync gecikmesine maruz kalır veya ekran yırtılmaları başlar.

**Altın Kural Formülü:** `Monitör Hz Değeri - 3 FPS`

| Monitör Yenileme Hızı (Hz) | Önerilen CS2 FPS Sabitleme Değeri |
| :--- | :--- |
| **144 Hz** | `fps_max 141` |
| **240 Hz** | `fps_max 237` |
| **360 Hz** | `fps_max 357` |

*Ekstra İpucu:* VRR kullanıyorsanız, oyun içi ayarlardan **NVIDIA Reflex Low Latency** ayarını **On + Boost** konumuna getirin. Bu ayar, FPS'i otomatik olarak monitör sınırınızın hemen altında tutarak gecikmeyi optimize eder.

---

## CS2 FPS Sabitleme Hakkında Sıkça Sorulan Sorular

### `fps_max 0` yapmak performansı artırır mı?
Hayır. `fps_max 0` komutu FPS sınırını tamamen kaldırır. Bu durum anlık olarak çok yüksek FPS değerleri görmenizi sağlasa da, GPU kullanımını sürekli %100'de tutarak termal darboğaza (thermal throttling) ve yüksek giriş gecikmesine neden olur. CS2 için önerilen, sisteminizin stabil olarak verebildiği en yüksek ortalama FPS değerine sabitleme yapmaktır.

### FPS sabitlemek input lag (gecikme) yaratır mı?
Doğru yöntemle yapıldığında hayır, aksine azaltır. Oyun içi `fps_max` komutu veya NVIDIA Reflex kullanımı, GPU'nun aşırı yüklenmesini önleyerek donanım tabanlı giriş gecikmesini düşürür. Ancak üçüncü parti yazılımlarla (RTSS vb.) yapılan sabitlemeler mikro düzeyde gecikme ekleyebilir. Bu nedenle CS2 içinde öncelikli olarak oyun içi konsol veya sürücü ayarları tercih edilmelidir.

### CS2'de FPS'i kaç Hz'e sabitlemeliyim?
Eğer VRR (G-Sync/FreeSync) kullanmıyorsanız, FPS değerinizi monitörünüzün Hz değerinin **2 katı + 1** olacak şekilde sabitlemek (Örn: 144Hz için 289 FPS) kare geçişlerindeki akıcılığı artırır. Eğer sisteminiz bu değerleri stabil veremiyorsa, doğrudan monitör Hz değerinizin sabit bir katına (Örn: 240Hz için 240 FPS) sabitlemelisiniz.