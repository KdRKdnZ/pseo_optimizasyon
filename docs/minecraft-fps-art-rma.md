---
title: "minecraft fps artırma"
description: "minecraft fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Minecraft FPS Artırma Rehberi: Donanım ve Yazılım Odaklı Kesin Çözümler

Minecraft, Java altyapısı ve sonsuz rastgele oluşturulan dünyaları (procedural generation) nedeniyle sistem kaynaklarını, özellikle işlemci (CPU) ve belleği (RAM) yoğun şekilde kullanan bir oyundur. Bu rehber, Minecraft'ta kare hızını (FPS) maksimum seviyeye çıkarmak için kullanabileceğiniz teknik optimizasyon yöntemlerini, mod çözümlerini ve işletim sistemi ayarlarını içermektedir.

---

## 1. Oyun İçi Grafik Ayarlarının Optimize Edilmesi

Oyun içi grafik ayarları, GPU ve CPU üzerindeki yükü doğrudan etkiler. Aşağıdaki konfigürasyon, görsel kaliteden minimum düzeyde ödün vererek maksimum FPS elde etmenizi sağlar:

*   **Görüş Mesafesi (Render Distance):** En çok kaynak tüketen ayardır. Düşük ve orta sistemlerde **8 - 12 Chunk** arasında tutulmalıdır.
*   **Simülasyon Mesafesi (Simulation Distance):** Varlıkların (mob'lar, kızıltaş devreleri) işlendiği mesafedir. **6 - 8 Chunk** seviyesine düşürmek CPU yükünü ciddi oranda azaltır.
*   **Grafikler (Graphics):** "Gerçekçi" (Fancy) yerine **"Hızlı" (Fast)** olarak ayarlanmalıdır. Bu işlem, yaprakların saydamlığını ve gölge hesaplamalarını devre dışı bırakır.
*   **Yumuşak Aydınlatma (Smooth Lighting):** **Kapalı** veya **Minimum** konuma getirilmelidir.
*   **Maksimum Kare Hızı (Max Framerate):** Monitörünüzün yenileme hızına (Hz) sabitleyin veya **Sınırsız (Unlimited)** yapın.
*   **Parçacıklar (Particles):** **En Az (Minimal)** veya **Azaltılmış (Decreased)** yapılmalıdır.
*   **Biyom Karışımı (Biome Blend):** **Kapalı (Off)** konuma getirilmesi, yeni alanlar yüklenirken oluşan anlık takılmaları (stuttering) önler.
*   **V-Sync (Dikey Eşitleme):** Girdi gecikmesine (input lag) neden olduğu ve FPS'i kısıtladığı için **Kapalı** tutulmalıdır. (Görüntü yırtılması yaşanmıyorsa).

---

## 2. Minecraft’a RAM Tahsis Edilmesi (JVM Bellek Ayarı)

Minecraft varsayılan olarak yalnızca 2 GB RAM kullanır. Büyük doku paketleri veya yüksek görüş mesafelerinde bu miktar yetersiz kalır ve oyunun takılmasına neden olur.

### RAM Verme Adımları (Resmi Launcher):
1. Minecraft Launcher'ı açın ve **Yüklemeler (Installations)** sekmesine gidin.
2. Oynadığınız sürümün yanındaki **üç noktaya** tıklayıp **Düzenle (Edit)** seçeneğini seçin.
3. **Daha Fazla Seçenek (More Options)** bölümünü genişletin.
4. **JVM Bağlantı Noktaları (JVM Arguments)** metin kutusundaki en baştan `-Xmx2G` ifadesini bulun.
5. Buradaki `2G` ibaresini sisteminizdeki RAM miktarına göre değiştirin:
   * **8 GB RAM için:** `-Xmx4G`
   * **16 GB RAM için:** `-Xmx6G` veya `-Xmx8G`

> **Not:** Sisteminizde 16 GB RAM olsa bile Minecraft'a 10 GB'tan fazla RAM vermek, Java'nın Çöp Toplayıcı (Garbage Collector) mekanizmasını yavaşlatarak anlık FPS düşüşlerine (stutter) yol açabilir. Optimum değer **4 GB - 8 GB** arasıdır.

---

## 3. Performans Modlarının Kullanımı (Fabric Ekosistemi)

Geleneksel bir optimizasyon modu olan **OptiFine**, Minecraft'ın yeni sürümlerinde (1.16 ve üzeri) yetersiz kalmaktadır. Güncel sürümler için **Fabric Mod Loader** altyapısını kullanan performans modları çok daha yüksek FPS sağlar.

### Tavsiye Edilen Performans Mod Kombinasyonu:

1. **Sodium:** Oyunun işleme (rendering) motorunu baştan yazar. GPU kullanımını optimize ederek FPS'i 2 ila 5 kat artırabilir.
2. **Lithium:** Oyunun fizik, yapay zeka ve chunk yükleme mekanizmalarını optimize eden bir CPU performans modudur.
3. **Phosphor / FerriteCore:** Işıklandırma motorunu optimize eder ve bellek (RAM) kullanımını düşürür.
4. **Indium:** Sodium ile diğer modların (örneğin dekorasyon modları) uyumlu çalışmasını sağlar.
5. **Iris Shaders:** Sodium ile uyumlu çalışan, yüksek performanslı bir shader (gölgelendirici) modudur.

---

## 4. Ekran Kartı Ayarları (NVIDIA / AMD)

Minecraft (Java Edition), dizüstü bilgisayarlarda veya çift ekran kartlı sistemlerde bazen harici ekran kartı yerine işlemcinin dahili grafik birimini (Intel HD Graphics / AMD Radeon Graphics) kullanabilir.

### NVIDIA Denetim Masası Ayarları:
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesine gidin.
3. Ekle butonuna basarak `javaw.exe` dosyasını bulun (Genellikle `C:\Program Files\Java\...` veya launcher'ın kendi çalışma dizinindedir).
4. **Bu program için tercih edilen grafik işlemci:** "Yüksek performanslı NVIDIA işlemcisi" olarak seçin.
5. Aşağıdaki özel ayarları uygulayın:
   * **Güç Yönetimi Modu:** Maksimum performansı tercih et.
   * **Doku Süzme - Kalite:** Yüksek Performans.
   * **Eşyönsüz Süzme (Anisotropic Filtering):** Kapalı.

---

## 5. Windows Grafik Ayarları ve Güç Planı

İşletim sisteminizin performans modunda çalışması, işlemci çekirdek frekanslarının maksimumda kalmasını sağlar.

### Windows Grafik Performansı Tercihi:
1. Windows Arama çubuğuna **Grafik Ayarları** yazın ve açın.
2. **Gözat** butonuna tıklayarak Minecraft'ın kullandığı `javaw.exe` dosyasını seçin.
3. Eklendikten sonra üzerine tıklayıp **Seçenekler**'e basın ve **Yüksek Performans**'ı işaretleyin.

### Güç Planı Ayarı:
* **Denetim Masası > Güç Seçenekleri** yolunu izleyin.
* Güç planını **Yüksek Performans** veya **Nihai Performans (Ultimate Performance)** olarak değiştirin.

---

## 6. Gelişmiş JVM Çöp Toplayıcı (GC) Parametreleri

Java'nın belleği temizleme yöntemi (Garbage Collection), arka planda mikro takılmalara neden olabilir. G1GC (Garbage-First Garbage Collector) parametrelerini optimize ederek daha akıcı bir oyun deneyimi elde edebilirsiniz.

Launcher'daki **JVM Arguments** kısmına aşağıdaki gelişmiş kod satırını yapıştırabilirsiniz (RAM miktarını sisteminize göre `-Xmx4G` kısmından ayarlayın):

```bash
-Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=20 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=15 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
```

---

## Özet Çalma Listesi (Checklist)

* [ ] Grafik ayarlarında **Render Distance** değerini düşürün, **Graphics: Fast** yapın.
* [ ] Modern sürümlerde (1.16+) OptiFine yerine **Fabric + Sodium** kullanın.
* [ ] Launcher üzerinden oyunun **RAM** miktarını en az 4 GB olarak güncelleyin.
* [ ] Oyunun dahili grafik kartı yerine **harici GPU (NVIDIA/AMD)** ile çalıştığından emin olun.
* [ ] Arka planda kaynak tüketen Chrome, Discord (Ekran kaplama) vb. uygulamaları kapatın.
* [ ] İşletim sistemi güç planını **Yüksek Performans** konumuna getirin.