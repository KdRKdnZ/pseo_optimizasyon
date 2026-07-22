# Valorant En İyi Ayarlar: Maksimum FPS, Minimum Gecikme ve Profesyonel Konfigürasyon

Valorant gibi mikrosaniye düzeyinde tepki sürelerinin önemli olduğu taktiksel FPS oyunlarında, sistem konfigürasyonu doğrudan performansınızı etkiler. Bu rehber; maksimum FPS elde etmek, girdi gecikmesini (input lag) en aza indirmek ve görsel netliği artırmak için optimize edilmiş teknik ayarları içermektedir.

---

## 1. En İyi Grafik Ayarları (Görsel Netlik ve Yüksek FPS)

Riot Games'in Unreal Engine 4 motoru üzerinde geliştirdiği Valorant'ta grafik ayarlarını "Düşük" seviyede tutmak, ekran kartı (GPU) üzerindeki yükü azaltarak işlemcinin (CPU) daha fazla kare (FPS) üretmesini sağlar.

### Genel Görüntü Ayarları (General)

| Ayar | Önerilen Değer | Teknik Açıklama |
| :--- | :--- | :--- |
| **Görüntü Modu (Display Mode)** | Tam Ekran (Fullscreen) | Pencereli modlar Windows DWM (Desktop Window Manager) gecikmesi ekler. Tam Ekran, doğrudan GPU erişimi sağlar. |
| **Çözünürlük (Resolution)** | Monitörün Doğal Çözünürlüğü (Örn: 1920x1080 144Hz/240Hz) | Piksel bazlı netlik için doğal çözünürlük şarttır. Hz değerinin en yüksekte olduğundan emin olun. |
| **Görüntü Boyut Sınırı (Aspect Ratio Method)** | Doldur (Fill) / Letterbox | Kişisel tercih. Ancak "Letterbox" piksel bozulmasını önler. |
| **NVIDIA Reflex Düşük Gecikme** | Açık + Takviye (On + Boost) | İşlemci ve GPU arasındaki kuyruğu optimize eder. CPU frekansını yüksek tutarak sistem gecikmesini (render latency) düşürür. |

### Grafik Kalitesi (Graphics Quality)

| Ayar | Önerilen Değer | Nedeni |
| :--- | :--- | :--- |
| **Materyal Kalitesi** | Düşük | Gereksiz doku detaylarını ve GPU yükünü kaldırır. |
| **Doku (Texture) Kalitesi** | Düşük | VRAM kullanımını düşürür, arka plandaki işlemleri rahatlatır. |
| **Ayrıntı Kalitesi** | Düşük | Haritadaki gereksiz nesneleri (çöp, yaprak vb.) gizleyerek düşman görünürlüğünü artırır. |
| **Arayüz (UI) Kalitesi** | Düşük | HUD elemanlarının render yükünü azaltır. |
| **Netliği Artır (Improve Clarity)** | Açık (On) | Orta mesafedeki piksel kontrastını artırarak düşman silüetlerini belirginleştirir. |
| **Deneysel Keskinleştirme** | Kapalı (Off) | Görüntüde yapay kenarlar oluşturur, göz yorgunluğuna yol açabilir. |
| **Eşyönsüz Filtreleme (Anisotropic Filtering)** | 1x veya 4x | FPS'e etkisi yok denecek kadar azdır. 4x, uzak zemin dokularını netleştirir. |
| **Kenar Yumuşatma (Anti-Aliasing)** | MSAA 2x veya Kapalı | FXAA görüntüyü bulanıklaştırır. MSAA 2x, FPS kaybettirmeden kırılmaları önler. |
| **Bozulma (Distortion)** | Kapalı | Yetenek efektlerindeki (Örn: Phoenix duvarı) kırılmaları kaldırır, FPS düşüşünü engeller. |
| **Eşleme Gölgeleri (Cast Shadows)** | Kapalı | Sadece kendi karakterinizin gölgesini etkiler, düşman gölgelerini kapatmaz. Kapatılmalıdır. |

---

## 2. En İyi Kontrol ve Fare Ayarları (eDPI ve Raw Input)

Valorant'ta tutarlı bir nişan alma (aim) performansı için düşük hassasiyet (sensitivity) ve kas hafızası esastır.

### Ham Girdi Arabelleği (Raw Input Buffer)
*   **Ayar:** Açık (On)
*   **Teknik Nedeni:** Fare girdilerini Windows API'sini atlayarak doğrudan oyuna iletir. Özellikle 1000 Hz ve üzeri tarama hızına (Polling Rate) sahip farelerde girdi gecikmesini ciddi oranda azaltır.

### İdeal eDPI Hesaplaması
eDPI (Effective Dots Per Inch), gerçek fare hassasiyetinizi belirler.
> **Formül:** `Fare DPI` x `Oyun İçi Sens` = **eDPI**

*   **Profesyonel Standart:** Profesyonel Valorant oyuncularının %80'i **200 ile 400 eDPI** aralığını kullanır.
*   **Örnek Konfigürasyon:** 800 DPI fare için `0.315` oyun içi sens = **252 eDPI** (Optimum hassasiyet).
*   **Fare Polling Rate:** 1000 Hz (Mümkünse 2000Hz/4000Hz, ancak Raw Input Buffer açık olmalıdır).

---

## 3. En İyi Ses Ayarları (Uzamsal İşitme ve HRTF)

Düşmanların adım seslerini, şarjör değiştirme ve yetenek seslerini doğru konumlandırmak için ses motoru doğru yapılandırılmalıdır.

*   **Hoparlör Yapılandırması:** Stereo
*   **HRTF (Head-Related Transfer Function):** **Açık (On)**
    *   *Teknik Açıklama:* Kulaklıklar için 3 boyutlu uzamsal ses simülasyonu sağlar. Düşmanın önünüzde mi, arkanızda mı yoksa üst katta mı olduğunu 360 derecelik açıyla tespit etmenizi sağlar.
*   **Windows Sonic / Dolby Atmos:** Kapalı (Oyun içi HRTF ile çakışır ve ses evrenini bozar).
*   **Ses İçi Ses Ses Seviyesi (Voice Chat):** Takım içi iletişimi aksatmayacak şekilde %70-80 seviyesine çekilmelidir.

---

## 4. Rekabetçi Nişangah (Crosshair) Kodları

Görsel olarak ekranın ortasını kapatmayan, yüksek kontrastlı nişangahlar odaklanmayı artırır.

### Profesyonel Oyuncu Crosshair Kodları

*   **Nokta (Dot) Crosshair (Niko/M3C Style):**
    `0;P;c;7;h;0;d;1;z;3;F;0;0l;0;0o;0;0a;0;0f;0;1b;0`
*   **Kompakt Küçük Artı (TenZ Style):**
    `0;s;1;P;c;5;h;0;m;1;0l;4;0o;2;0a;1;0f;0;1b;0;S;c;4;s;0.8;o;1`
*   **Standart Yeşil Pro Artı (Boaster Style):**
    `0;P;c;1;o;1;0l;4;0o;2;0a;1;0f;0;1b;0`

> **Renk Önerisi:** Camgöbeği (Cyan), Yeşil veya Sarı. Bu renkler Valorant haritalarındaki kaplamalarla en az çakışan yüksek kontrastlı renklerdir.

---

## 5. Windows ve Sistem Düzeyinde Optimizasyonlar

Oyun içi ayarların yanı sıra işletim sistemi optimize edilmelidir:

1.  **Oyun Modu (Game Mode):** Windows Ayarları > Oyun > Oyun Modu > **Açık**. Windows'un arka plan kaynaklarını oyuna önceliklendirmesini sağlar.
2.  **Donanım Hızlandırmalı GPU Zamanlaması (HAGS):** Windows Grafik Ayarları > **Açık**. VRAM yönetimini optimize ederek kare süresi (frame time) sapmalarını azaltır.
3.  **Tam Ekran İyileştirmelerini Devre Dışı Bırakma:** 
    *   `VALORANT-Win64-Shipping.exe` dosyasına sağ tıklayın > Özellikler > Uyumluluk > **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.

---

## Özet Hızlı Kontrol Listesi

* [x] Tam Ekran modu aktif.
* [x] Tüm grafik kalitesi ayarları "Düşük" seviyede.
* [x] NVIDIA Reflex "Açık + Takviye" konumunda.
* [x] HRTF ses ayarı açık.
* [x] Raw Input Buffer açık.
* [x] eDPI değeri 200-400 aralığına çekildi.