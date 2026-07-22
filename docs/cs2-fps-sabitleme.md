---
title: "cs2 fps sabitleme"
description: "cs2 fps sabitleme hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 FPS Sabitleme Rehberi: Konsol Komutları, GPU Ayarları ve En İyi Performans

Counter-Strike 2 (CS2) oyununda kare hızını (FPS) sabitlemek, sistem bileşenlerinin aşırı ısınmasını önlemek, ekran yırtılmalarını (screen tearing) engellemek ve işlemci/ekran kartı yükünü dengeleyerek daha kararlı bir kare süresi (frame time) elde etmek için kritik bir teknik düzenlemedir. CS2, Source 2 motoruna geçiş yaptığı için eski CS:GO komutlarının bir kısmı değişmiş veya çalışma mantığı farklılaşmıştır.

Bu rehberde, CS2'de FPS sabitleme işlemlerini konsol komutları, başlatma seçenekleri, ekran kartı yazılımları ve konfigürasyon dosyaları üzerinden teknik detaylarıyla inceliyoruz.

---

## CS2'de FPS Neden Sabitlenmelidir?

Uncapped (sınırsız) FPS kullanımı teorik olarak sistemin üretebildiği en düşük girdi gecikmesini (input lag) sunar. Ancak pratik kullanımda sınırsız FPS şu sorunlara yol açar:

1. **Gereksiz Yük ve Isınma:** GPU ve CPU sürekli %100 kapasitede çalışarak daha fazla güç tüketir ve ısınır. Bu durum zamanla "Thermal Throttling" (sıcaklığa bağlı frekans düşürme) kaynaklı ani FPS düşüşlerine (FPS drop) neden olur.
2. **Düzensiz Kare Süresi (Frame Time Spikes):** Dalgalanan FPS değerleri, milisaniye cinsinden karelerin ekrana gelme süresini belirsizleştirir. Sabit 200 FPS, 150 ile 300 arası sürekli dalgalanan bir FPS'ten daha akıcı bir hissiyat sağlar.
3. **VRR (G-Sync / FreeSync) Çakışması:** Değişken yenileme hızına sahip monitörlerde, FPS monitörün Hz değerini aştığında VRR devre dışı kalır ve ekran yırtılmaları başlar.

---

## 1. Konsol Komutları ile CS2 FPS Sabitleme

Oyun içi konsol, FPS değerini anlık ve en düşük sistemsel yük ile sınırlamanın en etkili yoludur.

### Adım 1: Geliştirici Konsolunu Etkinleştirme
1. CS2'yi açın ve **Ayarlar (Dişli Çark)** simgesine tıklayın.
2. **Oyun (Game)** sekmesine gelin.
3. **Geliştirici Konsolunu Etkinleştir (Enable Developer Console)** seçeneğini **"Evet"** yapın.
4. `~` veya `"` (é) tuşuna basarak konsolu açın.

### Adım 2: FPS Sabitleme Komutları
Konsola aşağıdaki komutları ihtiyacınıza göre girin:

* **Oyun İçi FPS Sabitleme:**
  ```text
  fps_max [değer]
  ```
  *Örnek:* 144 Hz monitör için FPS'i 240'a sabitlemek istiyorsanız: `fps_max 240`

* **Ana Menü FPS Sabitleme:**
  Ana menüde ekran kartının tam yükte çalışmasını engellemek için menü FPS'ini ayrı sınırlayabilirsiniz:
  ```text
  fps_max_ui [değer]
  ```
  *Örnek:* `fps_max_ui 60`

* **FPS Sınırını Kaldırma:**
  ```text
  fps_max 0
  ```
  *(Not: `fps_max 0` kullanımı bazı sistemlerde yükleme ekranı sürelerini uzatabilir; bunun yerine `fps_max 999` kullanımı önerilir.)*

---

## 2. Steam Başlatma Seçenekleri (Launch Options) ile FPS Sabitleme

Konsol komutunun her oyuna girişte sıfırlanmasını önlemek için Steam başlatma seçeneklerini kullanabilirsiniz.

1. **Steam** kütüphanenizde **Counter-Strike 2**'ye sağ tıklayın ve **Özellikler**'i seçin.
2. **Genel** sekmesi altındaki **Başlatma Seçenekleri** metin kutusuna gidin.
3. Komutu aşağıdaki formatta ekleyin:
   ```text
   +fps_max 240 +fps_max_ui 60
   ```
4. Pencereyi kapatıp oyunu başlatın.

---

## 3. Ekran Kartı Sürücüleri Üzerinden FPS Sabitleme

Sürücü seviyesinde yapılan limitleme, Source 2 motorunun kare işleme kuyruğuna doğrudan müdahale ettiği için son derece kararlı kare süreleri sunar.

### Nvidia Kullanıcıları İçin (Nvidia Control Panel)
1. Masaüstüne sağ tıklayıp **Nvidia Denetim Masası**'nı açın.
2. Sol menüden **3D Ayarlarının Yönetilmesi** sekmesine girin.
3. **Program Ayarları** başlığı altında `cs2.exe` dosyasını seçin (Listede yoksa "Ekle" butonundan oyunun dizinini bulun).
4. **Maksimum Kare Hızı (Max Frame Rate)** ayarını **Açık** konuma getirin ve istediğiniz FPS değerini (örn: 240) girin.
5. **Uygula** butonuna tıklayın.

### AMD Kullanıcıları İçin (AMD Software: Adrenalin Edition)
1. **AMD Software** uygulamasını açın.
2. **Oyun** sekmesinden **Counter-Strike 2**'yi seçin.
3. **Radeon Chill** özelliğini aktif edin.
4. **Min FPS** ve **Max FPS** değerlerini aynı sayıya ayarlayın (örn: Min: 200 / Max: 200).
5. Alternatif olarak **Frame Rate Target Control (FRTC)** özelliğini kullanarak küresel bir limit belirleyebilirsiniz.

---

## 4. Kalıcı Yapılandırma: Autoexec.cfg Kullanımı

Konsol komutlarının kalıcı olmasını sağlayan en profesyonel yöntem bir `autoexec.cfg` dosyası oluşturmaktır.

1. `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg` dizinine gidin.
2. Metin belgesi oluşturun ve adını `autoexec.cfg` yapın (Uzantısının `.txt` değil `.cfg` olduğundan emin olun).
3. Dosyayı Notepad++ veya varsayılan Not Defteri ile açıp içine şu satırları ekleyin:
   ```cfg
   fps_max "240"
   fps_max_ui "60"
   host_writeconfig
   ```
4. Kaydedip kapatın.

---

## İdeal FPS Değeri Nasıl Hesaplanmalıdır?

FPS sabitleme değerini seçerken monitörünüzün yenileme hızı (Hz) ve sisteminizin sunduğu ortalama performans belirleyicidir.

| Monitör Hızı (Hz) | VRR (G-Sync/FreeSync) Açık | VRR Kapalı / Rekabetçi Mod |
| :--- | :--- | :--- |
| **60 Hz** | 57 FPS | 120 FPS / 180 FPS |
| **144 Hz** | 138 FPS | 288 FPS veya `fps_max 0` |
| **240 Hz** | 225 FPS | 300 FPS / 400 FPS |
| **360 Hz** | 340 FPS | Sistem Gücüne Göre Sınırsız / 400+ |

* **VRR (G-Sync/FreeSync) Kullanıyorsanız:** Input lag'i en aza indirmek ve G-Sync modunun dışına çıkmamak için FPS değerini monitör Hz değerinin **3-4 FPS altına** sabitleyin (Örn: 144Hz için 140 FPS).
* **Nvidia Reflex Kullanıyorsanız:** CS2 grafik ayarlarındaki **Nvidia Reflex Low Latency** seçeneğini "On + Boost" konumuna getirdiğinizde, sistem GPU sınırına ulaştığında FPS'i otomatik olarak ideal noktada sınırlar. Bu durumda manuel `fps_max` sınırı koymak yerine Reflex'in yönetimine izin vermek gecikme süresini minimumda tutar.

---

## Özet ve Teknik Tavsiyeler

* **Minimum Input Lag İçin:** Eğer sisteminiz sürekli olarak yüksek FPS üretebiliyorsa (örn: 300-400 FPS) ve sıcaklık değerleriniz normalse, `fps_max` değerini sisteminizin en düşük gördüğü düşüş (drop) noktasının biraz üzerine sabitlemek en istikrarlı gecikme süresini sunar.
* **Sıcaklık ve Akıcılık Dengesi İçin:** Monitör yenileme hızınızın 2 katı kadar bir değere sabitlemek (144Hz için ~300 FPS) hem akıcılığı korur hem de GPU'nun gereksiz yere ısınmasını engeller.