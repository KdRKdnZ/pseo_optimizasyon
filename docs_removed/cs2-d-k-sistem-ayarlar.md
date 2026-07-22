---
title: "cs2 düşük sistem ayarları"
description: "cs2 düşük sistem ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 Düşük Sistem Ayarları: Maksimum FPS ve Minimum Gecikme Rehberi

Source 2 motoru ile geliştirilen Counter-Strike 2 (CS2), CS:GO'ya kıyasla işlemci (CPU) yükünün yanı sıra ekran kartına (GPU) da ciddi oranda yük bindirmektedir. Giriş ve orta seviye donanımlarda akıcı bir oyun deneyimi elde etmek, gecikmeyi (input lag) düşürmek ve kare hızını (FPS) artırmak için doğru grafik yapılandırması kritik önem taşır.

Bu rehber; CS2 oyun içi grafik seçeneklerini, ekran kartı sürücü ayarlarını ve sistem seviyesindeki optimizasyonları teknik detaylarıyla ele almaktadır.

---

## 1. CS2 Oyun İçi Grafik Ayarları (En İyi FPS Performansı)

Oyun içi grafik ayarlarını "Gelişmiş Video" sekmesinden değiştirebilirsiniz. Aşağıdaki yapılandırma, görsel netlikten minimum düzeyde feragat ederek maksimum FPS almanızı sağlar:

| Grafik Ayarı | Önerilen Değer | Teknik Açıklama / Performans Etkisi |
| :--- | :--- | :--- |
| **Oyuncu Kontrastını Artır** | Etkin | Karakterlerin arka plandan ayrışmasını sağlar. FPS etkisi yok denecek kadar azdır (1-2 FPS). |
| **Dikey Eşitleme (V-Sync)** | Devre Dışı | Ekran yırtılmasını engeller ancak **ciddi girdi gecikmesine (input lag)** neden olur. Kesinlikle kapatılmalıdır. |
| **Gelişmiş Video Ayarları** | | |
| **Gölge Kalitesi (Global Shadow)** | Düşük | Düşük sistemlerde en çok FPS düşüren ayardır. Rakiplerin gölgesini görmek için "Orta" yapılabilir ancak düşük sistemde **Düşük** tutulmalıdır. |
| **Model / Doku Detayı** | Düşük | VRAM kullanımını ve işlemci üzerindeki geometrik işleme yükünü azaltır. |
| **Doku Filtreleme Modu** | Çift Hatlı (Bilinear) | Doku kaplamalarını basitleştirir. Ekran kartı üzerindeki bellek bant genişliği yükünü hafifletir. |
| **Çözünürlük Detayı (Shader)** | Düşük | Işık kırılmaları ve cam/su yansımalarını optimize eder. FPS stabilizasyonu için **Düşük** olmalıdır. |
| **Parçacık Detayı (Particle)** | Düşük | Sis, bomba patlamaları ve molotof efektlerinin FPS düşürmesini engeller. |
| **Maksimum Akış Doku Kalitesi** | Devre Dışı | Arka planda doku yüklemesini engeller. Sadece çok düşük VRAM'e sahip kartlarda "Etkin" yapılabilir. |
| **Çevre Gizleme (Ambient Occlusion)**| Devre Dışı | Nesnelerin birleştiği yerlerdeki gerçekçi gölgeleri kapatır. GPU yükünü önemli ölçüde azaltır. |
| **HDR (High Dynamic Range)** | Performans | Işık geçişlerini daha az kaynak kullanarak işler. Kalite moduna göre daha yüksek FPS sağlar. |
| **FidelityFX Super Resolution (FSR)**| Devre Dışı (ya da Kalite) | Çözünürlüğü ölçeklendirir. Görüntüyü bulanıklaştırabilir. Sadece FPS 60'ın altındaysa **Kalite** moduna alınmalıdır. |
| **NVIDIA Reflex Low Latency** | Etkin + Boost | GPU kullanımının %99'a ulaştığı anlarda sistem gecikmesini (system latency) minimuma indirir. |

---

## 2. İdeal Çözünürlük ve Ekran Oranı

CS2'de çözünürlüğü düşürmek, ekran kartına binen piksel işleme yükünü doğrudan azaltır.

*   **Ekran Oranı:** 4:3 (Genişletilmiş / Stretched)
*   **Çözünürlük:** 1280x960 veya 1024x768
    *   *Teknik Avantaj:* 4:3 çözünürlük piksel sayısını azaltarak GPU yükünü %30-40 oranında hafifletir. Ayrıca oyuncu modelleri ekranda yatay olarak genişlediği için nişan almayı kolaylaştırır.

---

## 3. CS2 En İyi Başlatma Seçenekleri (Launch Options)

Steam kütüphanenizden **CS2 > Sağ Tık > Özellikler > Genel > Başlatma Seçenekleri** kısmına aşağıdaki kodları ekleyebilirsiniz:

```text
-nojoy -high -threads X +fps_max 0 +cl_forcepreload 1 -fullscreen
```

*   **`-nojoy`**: Joystik/Gamepad desteğini devre dışı bırakarak RAM kullanımını ve arka plan işlemlerini azaltır.
*   **`-high`**: İşlemcinin CS2 işlemine yüksek öncelik atamasını sağlar.
*   **`-threads X`**: İşlemcinizin **fiziksel çekirdek sayısını** girin (Örn: 6 çekirdekli işlemci için `-threads 6`).
*   **`+fps_max 0`**: FPS kısıtlamasını kaldırır. (Eski sistemlerde ısınma sorunu varsa monitör tazeleme hızının 2 katına sabitlenebilir, örn: `+fps_max 300`).
*   **`-fullscreen`**: Oyunun tam ekran modunda çalışmasını zorlayarak Windows masaüstü yöneticisinin (DWM) gecikme oluşturmasını engeller.

---

## 4. Ekran Kartı Denetim Masası Ayarları

### NVIDIA Denetim Masası
1.  **Masaüstü > Sağ Tık > NVIDIA Denetim Masası > Üç Boyutlu Ayarların Yönetilmesi** yolunu izleyin.
2.  **Bağlantılı Optimizasyon (Threaded Optimization):** Açık *(Çok çekirdekli işlemciler için kritiktir).*
3.  **Güç Yönetimi Modu:** Maksimum Performansı Tercih Et.
4.  **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık.
5.  **Doku Süzme - Kalite:** Yüksek Performans.
6.  **Doku Süzme - Trilinear Optimizasyon:** Açık.

### AMD Radeon Software
1.  **Radeon Anti-Lag:** Etkin *(Girdi gecikmesini düşürür).*
2.  **Radeon Boost:** Devre Dışı *(Ani fare hareketlerinde çözünürlüğü düşürerek bulanıklık yaratır).*
3.  **Radeon Image Sharpening:** Devre Dışı veya %20-30 (Netlik kazandırır, FPS etkisi düşüktür).
4.  **Ekran Kartı Uyumluluğu / Doku Filtreleme Kalitesi:** Performans.

---

## 5. Windows ve Sistem Düzeyinde Optimizasyonlar

Oyun performansını etkileyen işletim sistemi ayarlarının yapılandırılması:

*   **Oyun Modu (Game Mode):** `Windows Ayarları > Oyun > Oyun Modu` sekmesini **Açık** konuma getirin. Windows arka plan kaynaklarını oyuna yönlendirir.
*   **Donanım İvmeli GPU Zamanlaması (HAGS):** `Ayarlar > Grafik Ayarları` bölümünden **Açık** hale getirin ve bilgisayarı yeniden başlatın (Düşük VRAM'li sistemlerde VRAM yönetimini iyileştirir).
*   **Güç Planı:** `Denetim Masası > Donanım ve Ses > Güç Seçenekleri` yolundan **Yüksek Performans** veya **Nihai Performans** modunu seçin.

---

## 6. Özet: Akıcılık İçin En Kritik 3 Kural

1.  **Dikey Eşitleme (V-Sync) ve Hareket Bulanıklığı (Motion Blur)** modlarını daima kapalı tutun.
2.  İşlemci ısınmasını kontrol edin; CS2, Source 2 yapısı gereği işlemci sıcaklığı arttığında ani FPS düşüşlerine (thermal throttling) sebep olur.
3.  Oyun içi **MSAA (Çoklu Örnekleme Kenar Yumuşatma)** ayarını sisteminiz çok zayıfsa **Devre Dışı** veya en fazla **CMAA2 / 2x MSAA** seviyesinde tutun. MSAA, CS2'de GPU'yu en çok zorlayan bileşenlerden biridir.