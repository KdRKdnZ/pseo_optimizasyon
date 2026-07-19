---
title: cs2 fps artırma
description: cs2 fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 FPS Artırma Rehberi: Source 2 İçin Donanım ve Yazılım Optimizasyonu

Counter-Strike 2 (CS2), emektar Source motorundan modern **Source 2** motoruna geçiş yaparak oyunun grafiksel ve fiziksel yapısını tamamen değiştirdi. CS:GO'nun aksine CS2, artık sadece işlemci (CPU) odaklı bir oyun değil; ekran kartını (GPU) ve modern çoklu çekirdek mimarilerini de agresif bir şekilde kullanıyor. 

Bu rehberde, bir yazılım mimarı ve donanım uzmanı gözüyle, CS2'deki gecikmeyi (input lag) en aza indirip FPS değerlerinizi (özellikle %1 ve %0.1 Low değerlerini) nasıl maksimize edeceğinizi teknik detaylarıyla inceleyeceğiz.

---

## 1. Source 2 Motorunun Mimarisi ve FPS İlişkisi

CS:GO, DirectX 9 tabanlı ve tek çekirdek performansına aşırı bağımlı bir yapıya sahipti. CS2 ise **DirectX 11** (ve bazı sistemlerde Vulkan) API'sini kullanır. Bu değişim, optimizasyon yaklaşımımızı kökten değiştirmemizi gerektirir.

*   **Gelişmiş İş Parçacığı (Multi-threading):** Source 2, modern işlemcilerin çoklu çekirdek yapısını optimize şekilde kullanır. Bu nedenle işlemci çekirdeklerini yapay olarak sınırlamak performansı düşürür.
*   **Sub-Tick Sistemi:** Sunucu ile istemci arasındaki iletişimi milisaniyelere bölen bu sistem, kararlı bir kare hızına (Frame Pacing) ihtiyaç duyar. Dalgalanan FPS, sub-tick kayıplarına ve mermilerin gitmemesi hissiyatına yol açar. Hedefimiz sadece "en yüksek FPS" değil, "en stabil FPS" olmalıdır.

---

## 2. En İyi CS2 Grafik Ayarları (Performans ve Görüş Odaklı)

Oyun içi grafik ayarlarını optimize ederken, rekabetçi avantajı kaybetmeden GPU üzerindeki gereksiz yükü kaldırmayı hedefliyoruz.

| Grafik Ayarı | Önerilen Değer | Teknik Gerekçesi |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır** | Etkin | CPU'ya hafif yük bindirir ancak düşman görünürlüğü için kritiktir. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı | Ciddi oranda giriş gecikmesine (input lag) neden olur. |
| **Çoklu Örnekleme Kenar Yumuşatma** | 2x MSAA veya CMAA2 | MSAA, GPU'yu en çok yoran ayarlardan biridir. Düşük sistemlerde CMAA2 tercih edilmelidir. |
| **Evrensel Gölge Kalitesi** | Orta (Medium) | "Düşük" ayar, rakiplerin gölgelerini görmenizi engeller. Rekabetçi avantaj için en az "Orta" olmalıdır. |
| **Model / Doku Detayı** | Düşük (Low) | VRAM kullanımını azaltır ve bellek bant genişliğini rahatlatır. |
| **Gölgelendirici Detayı** | Düşük (Low) | Işık yansımalarını ve GPU üzerindeki shader yükünü azaltır. |
| **Parçacık Detayı** | Düşük (Low) | Molotof ve el bombaları patladığında oluşan FPS düşüşlerini (drop) engeller. |
| **Ortam Kapatma (Ambient Occlusion)** | Devre Dışı | Gölgelerin birleşim yerlerindeki derinlik efektidir, rekabetçi oyunda gereksiz GPU yüküdür. |
| **Yüksek Dinamik Aralık (HDR)** | Performans | Görsel kaliteyi optimize ederken kare işleme süresini (frametime) düşürür. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (Hızlı) | Görüntüyü çamurlaştırır. Sadece GPU'nuz çok eskiyse "Ultra Kalite" modunda açılmalıdır. |
| **NVIDIA Reflex Düşük Gecikme** | Etkin + Takviye (Enabled + Boost) | GPU darboğazını engeller ve işlemci-ekran kartı arasındaki kuyruğu (render queue) sıfırlar. |

---

## 3. Windows ve Ekran Kartı Sürücü Optimizasyonları

İşletim sistemi ve sürücü seviyesindeki gecikmeleri azaltmak, CS2 FPS artırma sürecinin en kritik adımıdır.

### NVIDIA Denetim Masası Ayarları
NVIDIA ekran kartı kullanıyorsanız, masaüstüne sağ tıklayıp NVIDIA Denetim Masası'na girin ve "3D Ayarlarının Yönetilmesi" altından şu değişiklikleri yapın:

*   **Bağlantılı Optimizasyon (Threaded Optimization):** Açık (Source 2'nin çoklu çekirdek desteği için zorunludur).
*   **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
*   **Düşük Gecikme Kolaylığı Modu (Low Latency Mode):** Açık veya Ultra (NVIDIA Reflex oyun içinde aktifse bu ayar oyun tarafından yönetilir, ancak genel kararlılık için "Açık" konumda kalması güvenlidir).
*   **Doku Süzme - Kalite:** Yüksek Performans.

### Windows Grafik Ayarları ve Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows arama çubuğuna "Grafik Ayarları" yazın:
1.  **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Bu ayarı **Açık** konuma getirin. (Özellikle RTX serisi kartlarda frametime kararlılığını artırır).
2.  **Grafik Performansı Tercihi:** Listeden `cs2.exe` dosyasını bulun (genellikle `Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64` dizinindedir), "Seçenekler"e tıklayın ve **Yüksek Performans** olarak ayarlayın.

---

## 4. CS2 Başlatma Seçenekleri (Launch Options)

CS:GO döneminden kalan birçok başlatma seçeneği CS2'de çalışmamakta, hatta bazıları oyunun kararsız çalışmasına neden olmaktadır. `-threads` gibi işlemci çekirdeklerini sınırlayan eski komutları kesinlikle kullanmayın.

Steam kütüphanenizde CS2'ye sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kısmına sadece aşağıdaki güncel komutları ekleyin:

```text
-novid -nojoy -high
```

*   `-novid`: Giriş videosunu atlayarak oyunun daha hızlı açılmasını sağlar ve RAM yükünü azaltır.
*   `-nojoy`: Denetleyici (gamepad) desteğini kapatır, arka planda çalışan gereksiz bir iş parçacığını (thread) sonlandırır.
*   `-high`: İşlemcinin CS2 işlemine yüksek öncelik (CPU priority) atamasını sağlar.

---

## 5. Donanım Seviyesinde Darboğaz (Bottleneck) ve Gecikme Analizi

Yazılımsal optimizasyonlar bir noktaya kadar yardımcı olur. CS2'de 300+ FPS ve akıcı bir deneyim için donanım mimarinizin doğru yapılandırılması gerekir.

### RAM Frekansı ve Gecikme Süresi (XMP / EXPO)
Source 2 motoru, RAM hızına ve gecikme sürelerine (CL değerleri) aşırı duyarlıdır. 
*   BIOS ekranına girerek **XMP** (Intel) veya **EXPO/DOCP** (AMD) profilinin aktif olduğundan emin olun. 2133 MHz hızında çalışan bir DDR4 bellek ile 3600 MHz hızında çalışan bellek arasında CS2'de %20'ye varan FPS farkı oluşmaktadır.
*   Belleklerinizin **Dual-Channel (Çift Kanal)** modunda çalıştığından emin olun (Anakart üzerinde 2. ve 4. slotlar).

### CPU L3 Önbellek (Cache) Etkisi
CS2, işlemcinin L3 önbellek boyutuna doğrudan tepki verir. AMD'nin **3D V-Cache** teknolojisine sahip işlemcileri (örneğin Ryzen 7 7800X3D), CS2'de Intel muadillerine göre çok daha yüksek %1 Low FPS değerleri sunar. Eğer sistem toplama veya yükseltme aşamasındaysanız, L3 önbelleği yüksek işlemcilere yönelmeniz CS2 performansınızı doğrudan katlayacaktır.

### Termal Kısıtlama (Thermal Throttling)
İşlemci veya ekran kartınız belirli bir sıcaklık limitine ulaştığında (genellikle CPU için 90°C, GPU için 83°C), donanım kendini korumak için saat hızlarını (clock speed) düşürür. Bu durum ani FPS düşüşlerine (stuttering) yol açar. MSI Afterburner gibi yazılımlarla oyun içi sıcaklık değerlerinizi kontrol edin; gerekirse termal macun yenilemesi yapın ve fan eğrilerini optimize edin.