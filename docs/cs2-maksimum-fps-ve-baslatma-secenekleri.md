---
title: CS2 maksimum FPS ve başlatma seçenekleri
description: CS2 maksimum FPS ve başlatma seçenekleri hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 Maksimum FPS ve Başlatma Seçenekleri: Detaylı Optimizasyon Rehberi

Counter-Strike 2 (CS2), emektar Source motorundan modern Source 2 motoruna geçişle birlikte donanım kaynaklarını tüketme biçimini kökten değiştirdi. CS:GO'nun aksine, CS2 yalnızca CPU (İşlemci) odaklı bir oyun olmaktan çıkıp, GPU (Ekran Kartı) mimarisini, modern API'leri ve bellek bant genişliğini agresif şekilde kullanan bir yapıya büründü. 

Bu rehberde, bir yazılım mimarı ve donanım uzmanı gözüyle, **CS2 maksimum FPS ve başlatma seçenekleri** yapılandırmasını bilimsel ve kanıta dayalı yöntemlerle optimize edeceğiz.

---

## Source 2 Motorunun Mimarisi ve FPS İlişkisi

Source 2, modern çoklu çekirdek (multi-threading) optimizasyonuna ve gelişmiş fizik motoruna sahip bir API katmanı kullanır. CS:GO'da kullanılan DirectX 9'un yerini alan DirectX 11 (ve Vulkan), donanım seviyesinde daha düşük sürücü yükü (driver overhead) anlamına gelir.

### CPU vs. GPU Dengesi
CS2'de darboğaz (bottleneck) analizi yapıldığında, oyun içi kare oluşturma süresinin (frame time) hem CPU render kuyruğuna hem de GPU'nun piksel doldurma oranına (fill rate) doğrudan bağlı olduğu görülür. 
* **CPU:** Fizik hesaplamaları, oyuncu konumları (sub-tick verileri) ve ağ paketlerinin işlenmesinden sorumludur. Tek çekirdek performansı (Single-Core IPC) hala en kritik faktördür.
* **GPU:** Dinamik ışıklandırma, hacimsel sis (volumetric smoke) ve gölge hesaplamalarını üstlenir. CS2'de ekran kartı kullanımı %95 ve üzeri seviyelere rahatlıkla ulaşabilir.

### DirectX 11 ve Vulkan API Farkları
Windows işletim sistemlerinde CS2 varsayılan olarak DirectX 11 kullanır. Vulkan API seçeneği de mevcut olsa da, Windows üzerinde Vulkan derleme gölgelendiricileri (shader compilation) nedeniyle mikro takılmalara (stuttering) yol açabilir. Bu nedenle, Windows kullanıcıları için **DirectX 11** her zaman daha kararlı bir kare hızı (frame pacing) sunar.

---

## En İyi CS2 Başlatma Seçenekleri (Launch Options)

Steam başlatma seçenekleri, oyun motoru çekirdeği yüklenmeden önce alt seviye parametreleri belirlemenizi sağlar. CS:GO döneminden kalan birçok kod CS2'de tamamen işlevsizdir veya motor mimarisine zarar vererek performansı düşürür.

Aşağıda, Source 2 motoruyla uyumlu, kararlılığı test edilmiş en optimize **CS2 başlatma seçenekleri** yer almaktadır:

```text
-novid -high -nojoy +cl_updaterate 128 +fps_max 0
```

### Önerilen Başlatma Kodlarının Teknik Açıklamaları

* **`-novid`**: Girişteki Valve animasyonunu yüklemeden doğrudan ana menüye geçiş sağlar. Bellek sızıntılarını ve açılış süresini azaltır.
* **`-high`**: Windows işletim sisteminin CPU zamanlayıcısında (scheduler) CS2 işlemine (cs2.exe) yüksek öncelik vermesini sağlar. Arka plan işlemlerinin kare hızını düşürmesini engeller.
* **`-nojoy`**: Joystick/Gamepad sürücüsü taramasını devre dışı bırakır. Bu tarama, arka planda milisaniyelik CPU döngüsü kayıplarına (polling rate gecikmesi) yol açabilir.
* **`+cl_updaterate 128`**: Sunucu ile istemci arasındaki veri alışveriş sıklığını optimize eder.
* **`+fps_max 0`**: FPS sınırını kaldırır. Ancak, sisteminizde aşırı ısınma veya dalgalı FPS (örneğin 400'den 150'ye ani düşüşler) varsa, bu değeri monitör yenileme hızınızın (Hz) 2 katına sabitlemek (örn: `+fps_max 400`) daha stabil bir kare süresi (frame time) sağlar.

### Artık Kullanılmaması Gereken Geçersiz Kodlar
Aşağıdaki kodlar Source 2 motorunda ya tamamen geçersizdir ya da kararsızlığa neden olur:
* **`-threads`**: Source 2, iş parçacığı (thread) yönetimini işletim sisteminin çekirdek zamanlayıcısına bırakır. Bu kodu manuel zorlamak işlemci önbellek (L3 Cache) kaçırmalarına (cache miss) neden olur.
* **`-nod3d9ex`**: DirectX 9 optimizasyon kodudur, DX11 kullanan CS2'de hiçbir işlevi yoktur.
* **`-tickrate 128`**: CS2 tamamen Valve'ın yeni "Sub-tick" sistemini kullanır. Yerel sunucular dışında bu kodun resmi sunucularda bir etkisi yoktur.

---

## Oyun İçi Grafik Ayarları ve Donanım Optimizasyonu

Maksimum FPS ve en düşük gecikme (system latency) için oyun içi grafik ayarlarının doğru yapılandırılması hayati önem taşır. CS2'de bazı ayarlar doğrudan rekabetçi avantaj sağlarken, bazıları GPU'yu gereksiz yere yorar.

| Grafik Ayarı | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Gelişmiş Oyuncu Kontrastı** | Etkin | Oyuncuların karanlık bölgelerde seçilmesini kolaylaştırır, CPU yükü düşüktür. |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı | Ciddi oranda giriş gecikmesine (input lag) yol açar. |
| **Çoklu Örnekleme Kenar Yumuşatma** | 4x MSAA | Piksel tırtıklanmasını önler. Devre dışı bırakılması (No AA) rekabetçi oyunda uzak mesafeleri görmeyi zorlaştırır. |
| **Gölge Kalitesi** | Yüksek (High) | **Kritik Ayar:** Düşük gölge kalitesi, rakiplerin gölgelerini görmenizi engeller. Rekabetçi avantaj için High olmalıdır. |
| **Model / Dokulu Detayı** | Düşük (Low) | VRAM kullanımını azaltır ve bellek bant genişliğini rahatlatır. |
| **Gölgelendirici Detayı** | Düşük (Low) | Işık yansımalarını azaltarak GPU üzerindeki matematiksel hesaplama yükünü hafifletir. |
| **Parçacık Detayı** | Düşük (Low) | Molotof ve el bombaları patladığında oluşan FPS düşüşlerini (drop) engeller. |
| **Ortam Kapatma (Ambient Occlusion)**| Devre Dışı | Statik gölgelendirmedir, rekabetçi oyunda gereksiz GPU yükü yaratır. |
| **Yüksek Dinamik Aralık (HDR)** | Performans | Renk doğruluğundan ödün vererek parlak alanlardaki kare hızını korur. |
| **FidelityFX Super Resolution (FSR)** | Devre Dışı (Ultra Kalite) | Görüntüyü çamurlaştırır. Sadece çok eski GPU'larda FPS artırmak için "Ultra Quality" modunda açılabilir. |

---

## NVIDIA Reflex ve G-Sync Yapılandırması

Gecikme süresini (latency) minimize etmek, yüksek FPS almak kadar önemlidir. CS2, NVIDIA Reflex teknolojisini doğrudan destekler.

* **NVIDIA Reflex Düşük Gecikme:** **Etkin + Takviye (Enabled + Boost)** konumuna getirilmelidir. Bu ayar, CPU'nun GPU'yu bekleme süresini sıfıra indirir ve GPU çekirdek frekansını (clock speed) her zaman maksimumda tutar.
* **G-Sync ve FreeSync:** Rekabetçi arenalarda bu teknolojilerin kapatılması önerilir. Ancak yırtılmaları önlemek istiyorsanız, G-Sync Açık + V-Sync (NVIDIA Denetim Masasından Açık) + Oyun içi FPS limitini Hz değerinin 3 FPS altına sabitleme kombinasyonunu kullanmalısınız.

---

## Windows ve Sürücü Düzeyinde İnce Ayarlar

İşletim sistemi düzeyinde yapılacak birkaç kritik dokunuş, CS2'nin donanımınıza doğrudan erişmesini sağlar.

### 1. Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 ve 11'de bulunan bu özellik, ekran kartı belleğini (VRAM) doğrudan yöneterek CPU üzerindeki yükü azaltır.
* **Yol:** Ayarlar > Sistem > Monitör > Grafik ayarları.
* **İşlem:** "Donanım hızlandırmalı GPU zamanlaması" seçeneğini **Açık** konuma getirin ve bilgisayarı yeniden başlatın.

### 2. Shader Cache (Gölgelendirici Önbelleği) Boyutu
NVIDIA Denetim Masası üzerinden Shader Cache boyutunu sınırsız veya en az 10 GB yapmak, CS2'nin harita yüklenirken veya ani bomba patlamalarında gölgelendiricileri yeniden derlemesini önler. Bu, ani FPS düşüşlerini (stutter) tamamen ortadan kaldırır.
* **NVIDIA Denetim Masası** > 3D Ayarlarının Yönetilmesi > **Gölgelendirici Önbelleği Boyutu** > **10 GB** veya **Sınırsız**.

Bu optimizasyon adımları ve güncel **CS2 başlatma seçenekleri** ile sisteminizin darboğaz limitlerini yukarı taşıyabilir, milisaniyelik gecikmeleri önleyerek akıcı bir oyun deneyimi elde edebilirsiniz.