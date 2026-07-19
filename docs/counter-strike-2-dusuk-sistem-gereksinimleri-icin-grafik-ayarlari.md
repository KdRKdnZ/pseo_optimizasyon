---
title: Counter-Strike 2 düşük sistem gereksinimleri için grafik ayarları
description: Counter-Strike 2 düşük sistem gereksinimleri için grafik ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# Counter-Strike 2 Düşük Sistem Gereksinimleri İçin Grafik Ayarları ve Optimizasyon Rehberi

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte dinamik ışıklandırma, fizik tabanlı renderlama (PBR) ve hacimsel sis gibi modern grafik teknolojilerini beraberinde getirdi. Bu geçiş, oyunun işlemci (CPU) ve ekran kartı (GPU) üzerindeki yükünü ciddi oranda artırdı. Eski nesil veya giriş seviyesi donanımlarda rekabetçi avantajı kaybetmeden akıcı bir oyun deneyimi elde etmek, doğru grafik konfigürasyonunu yapmaktan geçer.

Bu rehberde, donanım darboğazlarını en aza indirmek ve gecikme süresini (input lag) düşürmek için uygulamanız gereken **Counter-Strike 2 düşük sistem gereksinimleri için grafik ayarları** ve teknik optimizasyon yöntemlerini inceleyeceğiz.

---

## Source 2 Motorunun Donanım Üzerindeki Etkisi

CS:GO büyük oranda işlemci bağımlı (CPU-bound) bir oyunken, CS2 ile birlikte yük dengesi ekran kartına (GPU) kaymıştır. Source 2 motoru, modern API'leri (DirectX 11 ve Vulkan) kullanarak çoklu çekirdek optimizasyonunu daha iyi yönetir ancak GPU bellek (VRAM) ve bant genişliği tüketimi oldukça yüksektir.

### CPU ve GPU Dengesi
Düşük sistemlerde en sık karşılaşılan sorun, GPU'nun %100 yük altında çalışırken CPU'nun kare zamanlamalarını (frame times) yetiştirememesidir. Bu durum ani FPS düşüşlerine (stuttering) neden olur. CS2'de stabil bir 1% low FPS değeri elde etmek, yüksek ortalama FPS almaktan daha kritiktir.

### Bellek (RAM) ve VRAM Yönetimi
CS2, minimum 8 GB RAM talep etse de arka plan servisleriyle birlikte bu miktar yetersiz kalmaktadır. Sistem belleğinin yetersiz kalması durumunda işletim sistemi disk üzerindeki sanal belleği (pagefile) kullanır ve bu da mikro takılmalara yol açar. Benzer şekilde, 4 GB altındaki VRAM'e sahip ekran kartlarında doku kalitesini yüksek tutmak, VRAM taşmasına ve FPS'in yarı yarıya düşmesine neden olur.

---

## CS2 Düşük Sistemler İçin En İyi Grafik Ayarları

Aşağıdaki ayarlar, donanım kaynaklarını minimum düzeyde tüketirken düşman görünürlüğünü (visibility) maksimumda tutmak üzere optimize edilmiştir.

### Gelişmiş Görüntü Ayarları Tablosu

| Grafik Ayarı | Önerilen Değer | Performans Etkisi | Teknik Açıklama |
| :--- | :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır** | Etkin | Çok Düşük | Karakterlerin arka plandan ayrışmasını sağlar. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı | Yüksek (Gecikme) | Giriş gecikmesini (input lag) önlemek için kesinlikle kapatılmalıdır. |
| **Çoklu Örnek Kenar Yumuşatma (MSAA)** | 2x MSAA veya CMAA2 | Orta | Kenar kırılmalarını önler. Tamamen kapatmak düşman tespitini zorlaştırır. |
| **Evrensel Gölge Kalitesi** | Düşük / Orta | Yüksek | Gölgeler düşman konumunu ele verir. Orta ayar idealdir, çok düşükse gölgeler kaybolur. |
| **Model / Doku Detayı** | Düşük | Düşük | VRAM kullanımını doğrudan etkiler. 4GB altı kartlar için "Düşük" olmalıdır. |
| **Doku Filtreleme Modu** | Çift Doğrusal (Bilinear) | Çok Düşük | Bant genişliğini optimize eder. |
| **Shader Detayı** | Düşük | Orta | Işık yansımalarını ve efekt kalitesini düşürerek GPU yükünü azaltır. |
| **Parçacık Detayı** | Düşük | Yüksek | El bombası ve molotof patlamalarındaki FPS düşüşlerini engeller. |
| **Ortam Kapatma (Ambient Occlusion)** | Devre Dışı | Orta | Köşelerdeki gerçekçi gölgelendirmeyi kapatarak GPU'yu rahatlatır. |
| **Yüksek Dinamik Aralık (HDR)** | Performans | Orta | Işık patlamalarını optimize eder ve kare hızını artırır. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (veya Kalite) | Çok Yüksek | Görüntüyü çamurlaştırmadan FPS artırmak için sadece "Kalite" modunda açılmalıdır. |
| **NVIDIA Reflex Düşük Gecikme** | Etkin + Boost | Düşük (Pozitif) | CPU-GPU senkronizasyonunu sağlayarak sistem gecikmesini minimize eder. |

---

### Kritik Ayarların Teknik Analizi

#### 1. Çoklu Örnek Kenar Yumuşatma Modu (MSAA)
CS2'de kenar yumuşatmayı tamamen kapatmak, piksellenmeye ve dolayısıyla uzak mesafedeki rakipleri seçememeye yol açar. Düşük sistemlerde **CMAA2** (Subpixel Morphological Anti-Aliasing) veya **2x MSAA** tercih edilmelidir. CMAA2, geçici bant genişliği tüketimini azaltarak GPU üzerindeki yükü hafifletir.

#### 2. FidelityFX Super Resolution (FSR 1.0)
FSR, oyunu daha düşük bir çözünürlükte renderlayıp yapay zeka ve filtreleme ile monitör çözünürlüğünüze ölçekler. Düşük sistemlerde FPS'i doğrudan %20 ila %40 arasında artırabilir. Ancak FSR'ı "Performans" moduna almak görüntüyü aşırı derecede flulaştırır ve rekabetçi avantajı yok eder. Bu nedenle yalnızca **"Kalite" (Quality)** veya **"Ultra Kalite"** modları kullanılmalıdır. Eğer ekran kartınız yeterliyse, FSR'ı **"Devre Dışı (En Yüksek Kalite)"** konumunda tutmak en net görüntüyü verecektir.

#### 3. Evrensel Gölge Kalitesi (Global Shadow Quality)
Source 2 motorunda gölgeler dinamiktir ve duvarların arkasından gelen rakiplerin konumunu önceden görmenizi sağlar. Gölgeleri tamamen kapatmak (veya "Çok Düşük" yapmak) taktiksel bir dezavantaj yaratır. Bu sebeple, sisteminiz ne kadar düşük olursa olsun bu ayarı **"Orta" (Medium)** seviyede tutmaya çalışın. Orta seviye, dinamik gölgeleri aktif tutarken performans kaybını minimize eder.

---

## Windows ve Başlatma Seçenekleri (Launch Options) Optimizasyonu

Donanım seviyesindeki darboğazları yazılımsal optimizasyonlarla aşmak mümkündür. Steam üzerinden uygulayacağınız başlatma seçenekleri, oyun motorunun çekirdek dağılımını ve bellek yönetimini optimize eder.

### En Etkili CS2 Başlatma Kodları
Steam kütüphanenizden CS2'ye sağ tıklayıp *Özellikler > Genel > Başlatma Seçenekleri* kısmına aşağıdaki kodları ekleyin:

```text
-high -nojoy -vulkan -threads [Çekirdek_Sayısı+1] +cl_forcepreload 1
```

*   **`-high`**: Windows CPU zamanlamasında CS2 işlemine yüksek öncelik atar.
*   **`-nojoy`**: Joystick/Gamepad sürücülerini devre dışı bırakarak RAM kullanımını azaltır.
*   **`-vulkan`**: Özellikle AMD ekran kartlarında ve eski nesil Intel işlemcilerde DirectX 11'e kıyasla daha stabil kare zamanlamaları (frametimes) sunabilir. (NVIDIA kullanıcıları bu kodu yazmadan DX11 ile test etmelidir).
*   **`-threads`**: İşlemcinizin fiziksel çekirdek sayısına 1 ekleyerek yazın (Örn: 6 çekirdekli işlemci için `-threads 7`).

### Windows Grafik Ayarları (HAGS)
Windows 10 ve 11'de yer alan **Donanım Hızlandırmalı GPU Zamanlaması (HAGS)**, GPU belleğini doğrudan yöneterek gecikmeyi azaltır.

1. Windows arama çubuğuna "Grafik Ayarları" yazın.
2. "Donanım hızlandırmalı GPU zamanlaması" seçeneğini **Açık** konuma getirin.
3. Grafik performansı tercihi altından CS2.exe'yi seçip **"Yüksek Performans"** olarak ayarlayın.

---

## Sonuç ve Performans Analizi

Counter-Strike 2, gelişmiş fizik motoru nedeniyle CS:GO kadar yüksek FPS değerlerine ulaşmanızı zorlaştırabilir. Ancak yukarıda belirtilen **Counter-Strike 2 düşük sistem gereksinimleri için grafik ayarları** uygulandığında, donanım üzerindeki gereksiz yükler (gölge hesaplamaları, yüksek çözünürlüklü dokular, ortam kapatma) devre dışı bırakılır. 

Bu optimizasyonlar sonucunda elde edeceğiniz kazanımlar:
*   **%30'a varan FPS artışı:** Özellikle shader ve parçacık detaylarının düşürülmesiyle patlama anlarındaki ani FPS düşüşleri engellenir.
*   **Düşük Giriş Gecikmesi:** NVIDIA Reflex ve V-Sync optimizasyonları ile fare hareketleriniz ekrana milisaniyeler bazında daha hızlı yansır.
*   **Stabil Frame Time:** İşlemci ve ekran kartı arasındaki veri akışı dengelenerek mikro takılmaların (stuttering) önüne geçilir.