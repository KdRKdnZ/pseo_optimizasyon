---
title: valorant performans optimizasyonu
description: valorant performans optimizasyonu hakkında detaylı optimizasyon ve donanım rehberi.
---

# Valorant Performans Optimizasyonu: Donanım, Yazılım ve Ağ Seviyesinde Kapsamlı Rehber

Valorant, Riot Games tarafından Unreal Engine 4 (UE4) motoru kullanılarak geliştirilmiş, taktiksel bir FPS oyunudur. Rekabetçi düzeyde avantaj elde etmek, yalnızca yüksek kare hızlarına (FPS) değil, aynı zamanda minimum kare süresine (frame time) ve en düşük giriş gecikmesine (input lag) sahip olmaya bağlıdır. Bu rehber, donanım mimarisi, işletim sistemi çekirdeği, sürücü seviyesi ve ağ protokolleri üzerinden **Valorant performans optimizasyonu** süreçlerini bilimsel ve kanıta dayalı yöntemlerle ele almaktadır.

---

## Valorant'ın Oyun Motoru Mimarisi ve CPU Bağımlılığı

Valorant, grafik kartından (GPU) ziyade işlemci (CPU) performansına duyarlı bir mimariye sahiptir. Oyunun render döngüsü (render loop), ana iş parçacığı (Main Thread) ve çizim iş parçacığı (Render Thread) olmak üzere iki temel yapı üzerinde yükselir.

### Unreal Engine 4 ve Tek Çekirdek Performansı
Valorant, çok çekirdekli işlemcileri desteklemekle birlikte (Multithreaded Rendering), oyun içi fizik hesaplamaları, oyuncu konumları (hitbox) ve sunucu senkronizasyonu gibi kritik görevleri tek bir ana iş parçacığı (Main Thread) üzerinde yürütür. Bu durum, işlemcinizin **IPC (Döngü Başına Komut)** değerini ve tek çekirdek saat hızını (Single-Core Boost Clock) en önemli performans kriteri haline getirir. CPU darboğazını (bottleneck) önlemek için işlemci önbelleği (özellikle AMD'nin 3D V-Cache teknolojisi veya Intel'in geniş L3 önbelleği) Valorant'ta FPS kararlılığını doğrudan artırır.

### Frame Time (Kare Süresi) ve Input Lag İlişkisi
Yüksek FPS değerleri (örneğin 300 FPS), oyunun akıcı olduğu illüzyonunu yaratabilir; ancak asıl önemli olan **kare süresi tutarlılığıdır (Frame Time Consistency)**. 
* 300 FPS'te ortalama kare süresi **3.33 milisaniyedir (ms)**.
* Eğer 1% ve %0.1 minimum FPS değerleriniz (1% low FPS) 100'e düşüyorsa, kare süreniz anlık olarak **10 ms**'ye fırlar. Bu durum "micro-stuttering" (mikro takılma) olarak adlandırılır ve nişan alma hassasiyetini (muscle memory) doğrudan baltalar.

---

## İşletim Sistemi ve Windows Seviyesinde Optimizasyon

Windows'un arka plan servisleri ve kaynak yönetimi, oyunun işlemciye doğrudan erişimini engelleyebilir. Aşağıdaki adımlar, işletim sistemi düzeyinde gecikmeyi en aza indirmek için tasarlanmıştır.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 (2004 ve üzeri) ve Windows 11 ile gelen **Hardware-Accelerated GPU Scheduling (HAGS)**, bellek yönetimini CPU'dan alarak doğrudan GPU'nun kendi zamanlama işlemcisine devreder.
* **Nasıl Yapılır?** `Ayarlar > Sistem > Monitör > Grafik ayarları` yolunu izleyin ve "Donanım hızlandırmalı GPU zamanlaması" seçeneğini aktif hale getirin.
* **Etkisi:** CPU üzerindeki yükü azaltarak özellikle orta segment işlemcilerde input lag değerini düşürür.

### Nihai Performans Güç Planı ve CPU Park Etme (Core Parking)
Windows'un standart güç planları, enerji tasarrufu amacıyla CPU çekirdeklerini uyku moduna (C-states) alabilir. Bu durum, ani işlemci yüklerinde gecikmeye yol açar.
1. Komut İstemi'ni (CMD) yönetici olarak açın.
2. Şu kodu yapıştırın ve Enter'a basın: 
   `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`
3. Denetim Masası > Güç Seçenekleri menüsünden **Nihai Performans (Ultimate Performance)** planını seçin.
4. Bu işlem, CPU çekirdeklerinin park edilmesini (Core Parking) engeller ve işlemcinin sürekli olarak maksimum frekansta çalışmasını sağlar.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
Windows Desktop Window Manager (DWM), pencereli modda çalışan uygulamalara dikey senkronizasyon (V-Sync) zorlar. Valorant'ı "Tam Ekran" modunda çalıştırsanız bile Windows arka planda optimizasyon uygulamaya çalışabilir.
* `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayın (Genellikle `Riot Games\VALORANT\live\ShooterGame\Binaries\Win64` dizinindedir).
* `Özellikler > Uyumluluk` sekmesine gidin.
* **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.

---

## Grafik Kartı (GPU) Sürücü ve Denetim Masası Ayarları

Ekran kartı sürücülerinin doğru yapılandırılması, render kuyruğunun (render queue) optimize edilmesini sağlar.

### NVIDIA Denetim Masası İnce Ayarları
NVIDIA GPU kullanıcıları için 3D ayarlarının global veya Valorant özelinde şu şekilde ayarlanması önerilir:

| Ayar | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Düşük Gecikme Oranı Modu** | Ultra / Açık | Kare kuyruğunu sıfırlayarak giriş gecikmesini minimize eder. |
| **Güç Yönetimi Modu** | Maksimum Performansı Tercih Et | GPU çekirdek saat hızlarının düşmesini engeller. |
| **Doku Süzme - Kalite** | Yüksek Performans | Anizotropik süzme yükünü azaltarak FPS kararlılığı sağlar. |
| **Dikey Senkronizasyon (V-Sync)** | Kapalı | Ekran kartı ile monitör senkronizasyon gecikmesini (input lag) önler. |
| **Bağlantılı Optimizasyon** | Açık | Oyunun çoklu CPU çekirdeği avantajından yararlanmasını sağlar. |

### AMD Radeon Software Yapılandırması
AMD kullanıcıları için performans odaklı sürücü ayarları:
* **Radeon Anti-Lag:** Açık (Giriş gecikmesini azaltmak için CPU çerçeve hizalamasını dinamik olarak kontrol eder).
* **Radeon Boost:** Kapalı (Çözünürlüğü dinamik olarak düşürür, rekabetçi oyunlarda görüntü netliğini bozduğu için önerilmez).
* **Doku Filtreleme Kalitesi:** Performans.

---

## Oyun İçi Grafik ve Video Ayarları

Valorant'ın oyun içi grafik motoru ayarları, CPU ve GPU arasındaki iş yükü dengesini optimize edecek şekilde yapılandırılmalıdır.

### CPU ve GPU Yükünü Dengeleyen Grafik Ayarları
* **Çok İzlekli Görselleştirme (Multithreaded Rendering):** **AÇIK**. Bu ayar, render iş parçacıklarını CPU çekirdeklerine dağıtır. Kapatılması durumunda ciddi FPS kayıpları yaşanır.
* **Malzeme, Doku, Detay ve Arayüz Kalitesi:** **DüşÜK**. Bu ayarlar GPU VRAM band genişliğini ve gölgelendirici (shader) hesaplama yükünü azaltır.
* **Kenar Yumuşatma (Anti-Aliasing):** **MSAA 2x** veya **Hiçbiri**. MSAA, kenarlardaki pikselleşmeyi önler ancak GPU yükünü artırır. Performans odaklı sistemler için FXAA veya tamamen kapatılması önerilir.
* **Eşyönsüz Filtreleme (Anisotropic Filtering):** **1x** veya **2x**.
* **Netliği Artır (Beta), Deneysel Keskinleştirme:** **KAPALI**. Bu filtreler post-processing (sonradan işleme) aşamasında CPU/GPU döngüsü harcar.

### NVIDIA Reflex Düşük Gecikme Teknolojisi
NVIDIA Reflex, CPU ve GPU arasındaki senkronizasyonu optimize ederek render kuyruğunu dinamik olarak yönetir.
* **Açık (On):** Giriş gecikmesini azaltır.
* **Açık + Takviye (On + Boost):** GPU saat hızlarını (GPU Clock) işlemci darboğazı yaşandığı anlarda bile maksimumda tutar. CPU sınırına takılan sistemlerde **"Açık + Takviye"** modu tercih edilmelidir.

---

## Ağ (Network) Optimizasyonu ve Tick Rate Kararlılığı

Valorant, **128-Tick** sunucular üzerinde çalışır. Bu, sunucunun ve istemcinizin (bilgisayarınızın) saniyede 128 kez veri alışverişi yaptığı anlamına gelir. Ağ kararsızlığı, mermilerin gitmemesi (hit registration sorunları) ve "desync" (senkronizasyon kaybı) durumlarına yol açar.

### 128-Tick Sunucular İçin Paket Kaybı (Packet Loss) ve Ping Çözümleri
1. **Kablolu Bağlantı (Ethernet):** Wi-Fi bağlantılarında havada oluşan paket çakışmaları (packet collision) anlık ping dalgalanmalarına (jitter) neden olur. 128-Tick veri akışı için Cat6 veya Cat7 ethernet kablosu kullanımı zorunludur.
2. **Nagle Algoritmasını Devre Dışı Bırakma (TCP No Delay):** Valorant UDP protokolünü kullansa da, Windows'un genel ağ paket kuyruğunu optimize etmek ağ kartı üzerindeki yükü hafifletir.
   * `Regedit` üzerinden `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\` dizinine gidin.
   * Aktif internet bağlantınızın olduğu alt anahtarda `TcpAckFrequency` ve `TCPNoDelay` adında iki adet DWORD (32 bit) değeri oluşturup değerlerini `1` yapın.
3. **DNS ve IP Yapılandırması:** ISS (İnternet Servis Sağlayıcı) DNS sunucuları yerine Cloudflare (`1.1.1.1` / `1.0.0.1`) gibi düşük ping süreli global DNS adreslerini tercih edin.

Bu optimizasyon protokolleri eksiksiz uygulandığında, Valorant üzerinde hem donanımsal gecikmeler (hardware latency) hem de yazılımsal darboğazlar minimuma indirilerek maksimum kararlılıkta bir oyun deneyimi elde edilir.