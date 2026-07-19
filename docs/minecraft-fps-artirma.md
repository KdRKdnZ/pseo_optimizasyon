---
title: minecraft fps artırma
description: minecraft fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Minecraft FPS Artırma: Donanım, JVM ve Mod Seviyesinde Optimizasyon Rehberi

Minecraft, piksel tabanlı grafiklerine rağmen optimizasyon sorunlarıyla bilinen, CPU ve RAM limitlerini zorlayan bir yapıya sahiptir. Java Virtual Machine (JVM) üzerinde çalışması, oyunun bellek yönetimini ve işlemci iş parçacığı (thread) kullanımını doğrudan etkiler. Bu rehberde, Minecraft FPS artırma hedefine ulaşmak için donanım, yazılım mimarisi ve oyun içi motor seviyesinde uygulayabileceğiniz en etkili optimizasyon yöntemlerini teknik detaylarıyla ele alacağız.

---

## Minecraft'ın Çalışma Mantığı ve Performans Darboğazları (Bottlenecks)

Minecraft'ta performans kaybının ana nedeni ekran kartınız (GPU) değil, genellikle işlemciniz (CPU) ve Java'nın bellek yönetim biçimidir.

### CPU (İşlemci) ve Tek Çekirdek Performansı
Minecraft, özellikle Vanilla (modsuz) sürümünde, oyun içi mantık (tick rate), fizik hesaplamaları, yapay zeka ve chunk (bölge) yükleme işlemlerini büyük oranda **tek bir iş parçacığı (single-thread)** üzerinde yürütür. Bu durum, çok çekirdekli modern işlemcilerde bile tek çekirdek saat hızının (IPC) hayati önem taşımasına yol açar. İşlemcinizin tek çekirdek performansı düşükse, GPU'nuz ne kadar güçlü olursa olsun darboğaz (bottleneck) yaşanacaktır.

### Java Sanal Makinesi (JVM) ve Bellek Yönetimi
Minecraft Java Edition, bellek temizliği için **Garbage Collector (Çöp Toplayıcı - GC)** mekanizmasını kullanır. GC aktif olduğunda, JVM anlık olarak oyun döngüsünü durdurabilir. Bu durum, oyuncular tarafından "stuttering" (anlık takılma/mikro kekemelik) olarak hissedilir. Doğru JVM argümanları kullanılmadığında, RAM miktarı ne kadar yüksek olursa olsun bu takılmalar engellenemez.

---

## Java ve Bellek (RAM) Optimizasyonu

Minecraft'a yanlış miktarda RAM atamak veya varsayılan Java parametrelerini kullanmak performans düşüşüne neden olur.

### Doğru RAM Miktarını Atama
Oyuna çok az RAM vermek `OutOfMemory` hatalarına yol açarken, gereğinden fazla RAM vermek (örneğin modsuz oyuna 16 GB RAM ayırmak) Garbage Collector'ın temizlemesi gereken alanı büyüterek daha uzun süreli takılmalara (GC pauses) neden olur.

*   **Vanilla (Modsuz) Minecraft:** 2 GB - 4 GB RAM
*   **Hafif Modlu Minecraft (1-50 Mod):** 4 GB - 6 GB RAM
*   **Ağır Mod Paketleri (100+ Mod):** 6 GB - 8 GB RAM

RAM miktarını ayarlamak için Minecraft Launcher'da **Yüklemeler (Installations) > Tercih Edilen Sürüm > Daha Fazla Seçenek** adımlarını takip edin ve `JVM Arguments` kısmındaki `-Xmx` değerini değiştirin (Örn: 4 GB için `-Xmx4G`).

### Gelişmiş JVM Argümanları (Garbage Collector Ayarları)
Varsayılan çöp toplayıcı yerine modern ve düşük gecikmeli **G1GC (Garbage-First Garbage Collector)** algoritmasını etkinleştirmek, anlık FPS düşüşlerini (frametime spikes) neredeyse tamamen ortadan kaldırır. Aşağıdaki optimize edilmiş JVM argümanlarını başlatma seçeneklerine ekleyin:

```text
-Xms4G -Xmx4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1ReservePercent=15 -XX:G1HeapRegionSize=32m -XX:G1ReservePercent=15 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
```

*Bu kod bloğundaki `-Xms4G` ve `-Xmx4G` değerlerini, bilgisayarınızın RAM kapasitesine göre (örn. 6 GB için `-Xms6G -Xmx6G`) güncelleyin.*

---

## En İyi Minecraft FPS Artırma Modları (Fabric vs Forge)

Geleneksel bir optimizasyon modu olan OptiFine, modern Minecraft sürümlerinde (1.16 ve üzeri) kod tabanının eskimesi nedeniyle yerini daha efektif alternatiflere bırakmıştır. Günümüzde en yüksek FPS artışını **Fabric** kütüphanesi üzerinde çalışan modlar sağlamaktadır.

### Sodium ve Iris Shaders (Grafik Motoru Değişimi)
*   **Sodium:** Minecraft'ın OpenGL işleme (rendering) motorunu tamamen yeniden yazar. Çok çekirdekli işlemcilerden yararlanarak chunk çizimlerini optimize eder, veri transferini GPU belleğine (VRAM) doğrudan aktarır. OptiFine'a kıyasla **%200 ila %400 arasında daha yüksek FPS** artışı sağlar.
*   **Iris Shaders:** Sodium ile tam uyumlu çalışarak, shader (gölgelendirici) paketlerini performans kaybını minimize ederek çalıştırmanızı sağlar.

### Yardımcı Optimizasyon Modları
En yüksek performans için Sodium'un yanına şu modları da eklemeniz önerilir:

1.  **Lithium:** Oyunun fizik, yapay zeka ve chunk yükleme mekanizmalarını (sunucu ve tek oyunculu tarafta) optimize eder. CPU yükünü azaltır.
2.  **FerriteCore:** JVM'in bellek kullanımını optimize ederek Minecraft'ın RAM tüketimini yaklaşık %30-50 oranında düşürür.
3.  **Krypton:** Ağ protokollerini optimize ederek çok oyunculu (multiplayer) sunucularda bağlantı kaynaklı gecikmeleri ve FPS düşüşlerini engeller.

---

## Oyun İçi Grafik Ayarlarının Matematiksel Etkisi

Oyun içi ayarları doğru yapılandırmak, donanım üzerindeki yükü doğrudan azaltır.

### Render Mesafesi (Render Distance) ve Chunk Yükleme
Render mesafesi doğrusal değil, karesel olarak artar. 8 chunk render mesafesinde toplam $17 \times 17 = 289$ chunk yüklenirken, bu değer 16 chunk'a çıkarıldığında $33 \times 33 = 1089$ chunk'a yükselir. 
*   **Öneri:** Performans odaklı sistemlerde bu değeri **8 - 12 chunk** arasında tutun.
*   **Simulation Distance (Simülasyon Mesafesi):** Fiziksel olayların ve yaratık hareketlerinin hesaplandığı mesafedir. Bu değeri **5 - 6 chunk** seviyesine çekmek CPU yükünü %40 oranında azaltır.

### Grafik Kalitesi, Yumuşak Aydınlatma ve Parçacıklar
*   **Grafikler (Graphics):** "Hızlı" (Fast) moduna alınmalıdır. Bu ayar, yaprakların şeffaflığını kapatarak GPU üzerindeki çizim çağrılarını (draw calls) azaltır.
*   **Yumuşak Aydınlatma (Smooth Lighting):** Kapatılması veya minimuma getirilmesi, ışık hesaplamalarındaki CPU döngülerini azaltır.
*   **Bulutlar (Clouds):** Kapatılması veya 2D yapılması FPS'e doğrudan olumlu etki eder.

---

## İşletim Sistemi ve Sürücü Optimizasyonları

Donanımınızın tam performansla çalışabilmesi için işletim sistemi düzeyinde yapılması gereken kritik ayarlar mevcuttur.

### GPU Sürücü Güncellemeleri ve Yüksek Performans Modu
Ekran kartı sürücülerinin güncel olmaması, OpenGL API'sinin verimsiz çalışmasına neden olur. NVIDIA veya AMD sürücülerinizi en güncel sürüme yükseltin.

#### NVIDIA Denetim Masası Ayarları:
1.  NVIDIA Denetim Masası'nı açın.
2.  **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3.  *Program Ayarları* kısmından `javaw.exe` (Minecraft'ın kullandığı Java sürümü) dosyasını seçin.
4.  **Güç Yönetimi Modu** ayarını **Maksimum Performansı Tercih Et** olarak değiştirin.
5.  **Bağlantılı Optimizasyon (Threaded Optimization)** ayarını **Açık** konumuna getirin.

### Windows Grafik Zamanlaması (HAGS) ve Oyun Modu
*   **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Windows Ayarları > Grafik Ayarları bölümünden bu özelliği açın. GPU'nun bellek yönetimini doğrudan üstlenmesini sağlayarak gecikmeyi (latency) azaltır.
*   **Windows Oyun Modu:** Arka plandaki Windows güncellemelerini ve gereksiz servisleri askıya alarak işlemci önceliğini Minecraft'a verir. Bu ayarı mutlaka **Açık** konumda tutun.

---

## Performans Karşılaştırma Tablosu

Aşağıdaki tabloda, farklı optimizasyon aşamalarının ortalama FPS ve Frametime (milisaniye cinsinden kare oluşturma süresi - düşük olması akıcılığı gösterir) üzerindeki teorik etkisi gösterilmiştir:

| Optimizasyon Seviyesi | Ortalama FPS Değişimi | Frametime Kararlılığı (1% Low FPS) | CPU Sıcaklığı / Yükü |
| :--- | :--- | :--- | :--- |
| **Vanilla (Varsayılan)** | %100 (Referans) | Kötü (Sık takılmalar) | Yüksek |
| **Sadece RAM ve JVM Ayarı** | %115 - %125 | Orta-İyi (Daha az takılma) | Dengeli |
| **OptiFine Entegreli** | %140 - %160 | Orta | Dengeli |
| **Sodium + Lithium + JVM** | **%250 - %400** | **Mükemmel (Sıfıra yakın takılma)** | **Düşük** |

Bu adımları sırasıyla uyguladığınızda, Minecraft'ın donanım kaynaklarını tüketim biçimi optimize edilecek, darboğazlar engellenecek ve hem yüksek FPS hem de kararlı bir oyun deneyimi elde edilecektir.