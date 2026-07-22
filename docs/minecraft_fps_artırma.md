# Minecraft FPS Artırma Rehberi: Donanım, Yazılım ve Oyun İçi Optimize Teknikleri

Minecraft, Java tabanlı mimarisi ve zayıf kod optimizasyonu nedeniyle yüksek donanımlı sistemlerde bile performans sorunlarına (FPS düşüşleri, takılmalar) yol açabilen bir oyundur. Bu rehber; oyun içi grafik konfigürasyonlarından JVM (Java Virtual Machine) parametrelerine, ekran kartı sürücü ayarlarından üçüncü taraf performans modlarına kadar en etkili teknik optimizasyon adımlarını içermektedir.

---

## 1. Oyun İçi Grafik Ayarlarının Konfigürasyonu

Oyun içindeki işleme yükünü azaltmak, işlemci (CPU) ve ekran kartı (GPU) üzerindeki darboğazı doğrudan engeller. Ayarlar menüsünü aşağıdaki teknik değerlere göre yapılandırın:

*   **Görüş Mesafesi (Render Distance):** Oyun performansını en çok etkileyen parametredir. İşlemcinin yükünü hafifletmek için **8 - 12 Chunk** aralığına çekilmelidir.
*   **Grafikler (Graphics):** `Gerçekçi (Fancy)` seçeneğinden `Hızlı (Fast)` moduna getirilmelidir. Bu işlem, yaprak saydamlığı ve gölge detaylarını basitleştirir.
*   **Pürüzsüz Aydınlatma (Smooth Lighting):** `Kapalı` veya `Minimum` seviyesine getirilmelidir.
*   **Maksimum Kare Hızı (Max Framerate):** `Sınırsız (Unlimited)` yapılmalıdır. Monitörünüz G-Sync/FreeSync destekliyorsa V-Sync kapatılmalıdır.
*   **Parçacıklar (Particles):** `En Az (Minimal)` olarak ayarlanmalıdır. Piston, lav, su ve iksir efektlerinin yükünü düşürür.
*   **Varlık Gölgeleri (Entity Shadows):** `Kapalı` konuma getirilmelidir.
*   **Biyom Karışımı (Biome Blend):** `Kapalı (Off)` olarak ayarlanmalıdır. Renk geçişi hesaplamalarını kaldırarak CPU yükünü azaltır.
*   **Simülasyon Mesafesi (Simulation Distance):** `4 - 6 Chunk` olarak ayarlanmalıdır. Görüş mesafesinin ötesindeki mob hareketleri ve kural güncellemelerini sınırlar.

---

## 2. Java Virtual Machine (JVM) ve RAM Tahsisi

Minecraft'ın varsayılan RAM tahsisi genellikle 2 GB'tır. Bu miktar, yüksek çözünürlüklü doku paketleri veya modlar kullanıldığında yetersiz kalır ve **Garbage Collector (Çöp Toplayıcı)** takılmalarına (stuttering) sebep olur.

### RAM Tahsisi Adımları (Minecraft Launcher)
1. Minecraft Launcher'ı açın ve **Yüklemeler (Installations)** sekmesine gidin.
2. Oynadığınız profili seçip **Düzenle (Edit)** butonuna basın.
3. **Daha Fazla Seçenek (More Options)** kısmını genişletin.
4. **JVM Bağlantı Noktaları (JVM Arguments)** alanındaki metnin başlangıcını düzenleyin:

```bash
# 4 GB RAM vermek için:
-Xmx4G -Xms4G

# 8 GB RAM vermek için:
-Xmx8G -Xms8G
```

> **Önemli Not:** Sisteminizde 8 GB RAM varsa oyuna maksimum 4 GB, 16 GB RAM varsa 6 GB ila 8 GB arası veriniz. Sistemin kendisine ve arka plan işlemlerine yeterli RAM bırakmamak tüm bilgisayarın kilitlenmesine yol açar.

### OptiFlow ve G1GC Çöp Toplayıcı Parametreleri
RAM takılmalarını engellemek için aşağıdaki gelişmiş JVM argümanlarını kullanabilirsiniz:

```text
-XX:+UseG1GC -Dsun.rmi.dgc.client.gcInterval=3600000 -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=50 -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90
```

---

## 3. Performans Modları (Sodium vs OptiFine)

Eski mimariye sahip OptiFine yerine, modern Minecraft sürümlerinde (1.16+) **Fabric API** altyapısını kullanan modern render motorları tercih edilmelidir.

### Önerilen Performans Mod Kombinasyonu (Fabric)

1.  **Sodium (Sodyum):** Minecraft'ın OpenGL render motorunu tamamen yeniden yazar. Chunk işleme hızını %200 ila %400 oranında artırır.
2.  **Lithium (Lityum):** Fizik hesaplamalarını, mob yapay zekalarını ve yükleme mekaniklerini optimize eden bir sunucu/tek oyunculu modudur.
3.  **Phosphor / Starlight:** Işık hesaplama motorunu (Lighting Engine) baştan yazarak chunk yüklenirken oluşan takılmaları engeller.
4.  **FerriteCore:** Minecraft'ın bellek (RAM) kullanımını optimize eder.

*Eğer Forge mimarisi kullanıyorsanız, Sodium karşılığı olan **Rubidium** veya **Embeddium** modlarını yükleyebilirsiniz.*

---

## 4. İşletim Sistemi ve GPU (Ekran Kartı) Ayarları

Minecraft varsayılan olarak işlemcinin dahili grafik kartını (Intel HD Graphics / AMD Radeon Graphics) kullanmaya meyillidir. Oyunu harici ekran kartı (NVIDIA / AMD) üzerinde çalıştırmak şarttır.

### Windows Grafik Ayarları
1. `Windows + I` tuşları ile Ayarlar'ı açın.
2. **Sistem > Monitör > Grafik Ayarları** yolunu izleyin.
3. **Gözat** butonuna tıklayarak Minecraft'ın kullandığı `javaw.exe` dosyasını seçin. *(Genellikle `C:\Program Files\Java\jdk-x.x.x\bin\javaw.exe` veya `.minecraft\runtime` klasöründedir).*
4. Seçilen `javaw.exe` için **Yüksek Performans** profilini atayın.

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesine gelin.
3. Minecraft (`javaw.exe`) profilini ekleyin ve şu ayarları uygulayın:
    *   **Güç Yönetimi Modu:** Maksimum performansı tercih et.
    *   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık.
    *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra.
    *   **Doku Süzme - Kalite:** Yüksek Performans.

---

## 5. Arka Plan Hizmetleri ve Donanım Sürücüleri

*   **GPU Sürücü Güncelliği:** NVIDIA (Game Ready Driver) veya AMD (Adrenalin Software) sürücülerinin güncel olduğundan emin olun.
*   **Java Sürümü Güncellemesi:** Minecraft 1.17 ve üzeri sürümler **Java 17**, 1.20.5 ve üzeri sürümler **Java 21** mimarisi gerektirir. Manuel olarak en güncel 64-bit JDK (Java Development Kit) sürümünü (Adoptium / Temurin önerilir) yüklemek işlemci verimliliğini artırır.
*   **Oyun Modu:** Windows "Oyun Modu" özelliğini aktif hale getirerek arka plan işlemlerinin CPU önceliğini düşürün.

---

## Özet Performans Kontrol Listesi

| İşlem | Beklenen FPS Artışı | Zorluk Seviyesi |
| :--- | :--- | :--- |
| **Sodium Modu Yüklemek** | %100 - %300 | Kolay |
| **Görüş Mesafesini Düşürmek** | %40 - %80 | Çok Kolay |
| **Harici GPU'ya Atama Yapmak** | %200+ (Dahili GPU kullanıcıları için) | Orta |
| **JVM Parametrelerini Düzenlemek** | %15 - %30 (Takılmaları önler) | İleri Seviye |
| **Grafikleri 'Hızlı' Yapmak** | %20 - %35 | Çok Kolay |