---
title: "cs2 performans rehberi"
description: "cs2 performans rehberi hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# CS2 Performans Rehberi: Maksimum FPS ve Minimum Input Lag Ayarları

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte işlemci (CPU) yükünün yanı sıra ekran kartı (GPU) kullanımını da önemli ölçüde artıran bir mimariye sahip oldu. Bu rehber, sistem kaynaklarınızı en verimli şekilde kullanarak maksimum kare hızı (FPS), en düşük gecikme süresi (input lag) ve kararlı bir kare zamanlaması (frame pacing) elde etmeniz için hazırlanmış teknik optimizasyon adımlarını içerir.

---

## 1. Oyun İçi Gelişmiş Video Ayarları

CS2'deki grafik ayarları, sadece görsel kaliteyi değil, render zincirindeki gecikmeyi doğrudan etkiler. Rekabetçi avantaj ve yüksek FPS için önerilen konfigürasyon:

| Grafik Ayarı | Önerilen Değer | Teknik Gerekçe |
| :--- | :--- | :--- |
| **Gelişmiş Karakter Görünürlüğü** | **Etkin** | Düşman modellerinin arka planla kontrastını artırır. Çok küçük bir FPS maliyeti vardır ancak kritik öneme sahiptir. |
| **Çoklu Örneklemeli Kenar Yumuşatma (MSAA)** | **2x MSAA** veya **4x MSAA** | CS2'de MSAA kapatıldığında (None) kenarlar aşırı pikselleşir ve Source 2 ışıklandırması yüzünden görsel gürültü oluşur. FXAA ise görüntüyü bulanıklaştırır. 2x MSAA optimum performans/netlik dengesidir. |
| **Gölge Kalitesi (Global Shadow Quality)** | **Orta (Medium)** | Düşük ayarda oyuncu gölgeleri işlenmez. Orta ayar, düşmanların köşelerden yaklaşırken gölgelerini görmenizi sağlar; stratejik olarak zorunludur. |
| **Model / Doku Detayı** | **Düşük (Low)** | GPU VRAM kullanımını ve doku yükleme bant genişliğini düşürür. |
| **Doku Filtreleme Modu** | **Anizotropik 4x / Bilinear** | Performansa etkisi ihmal edilebilir düzeydedir. Dokuların açılı bakışlarda net kalmasını sağlar. |
| **Efekt Detayı** | **Düşük (Low)** | Molotof, sis ve patlama efektlerindeki parçacık yükünü azaltarak yoğun çatışma anlarında FPS düşüşlerini (frame drop) engeller. |
| **Kaplama Detayı (Shader Detail)** | **Düşük (Low)** | Yüzey yansımalarını ve ışık hesaplamalarını minimize ederek GPU yükünü hafifletir. |
| **Parçacık Detayı** | **Düşük (Low)** | Sis ve patlama simülasyonlarının CPU/GPU üzerindeki yükünü azaltır. |
| **Ortam Kapatma (Ambient Occlusion)** | **Devre Dışı (Disabled)** | Köşe birleşimlerindeki gölgelendirmeleri kapatır, hem input lag'ı düşürür hem de düşman tespitini kolaylaştırır. |
| **FidelityFX Super Resolution (FSR)** | **Devre Dışı (Disabled - Highest Quality)** | FSR, görüntüyü alt çözünürlükten upscale ettiği için belirgin bir bulanıklık ve kenar bozulması yaratır. Yerel çözünürlük (Native) her zaman daha nettir. |
| **NVIDIA Reflex Low Latency** | **Etkin + Boost** | GPU'nun CPU tarafından aşırı beslenip kuyruk oluşturmasını engeller. Render gecikmesini doğrudan düşürür. |

---

## 2. CS2 Başlatma Seçenekleri (Launch Options)

Source 2 motorunda eski CS:GO komutlarının birçoğu (`-threads`, `-high`, `-nod3d9ex` vb.) işlevsiz kalmıştır veya sisteme kararsızlık getirmektedir. Güncel ve optimize edilmiş başlatma dizisi şu şekildedir:

```text
-novid -nojoy -high -fullscreen +fps_max 0
```

* **`-novid`**: Açılış introsunu atlayarak oyunun daha hızlı başlamasını sağlar.
* **`-nojoy`**: Joystiği/Gamepad desteğini devre dışı bırakarak RAM ve CPU izlemesini kaldırır.
* **`-high`**: Oyun işlemine Windows üzerinde yüksek işlemci önceliği atar (Zayıf sistemlerde takılmaya yol açarsa kaldırılmalıdır).
* **`-fullscreen`**: Oyunun özel tam ekran modunda çalışmasını zorunlu kılar; masaüstü pencereli modunun getirdiği gecikmeyi önler.
* **`+fps_max 0`**: Kare hızı limitini kaldırır (Monitör tazeleme hızına ve sistem ısınma durumuna göre sabit bir değere de ayarlanabilir).

---

## 3. Sürücü Seviyesi Optimizasyonlar

### NVIDIA Denetim Masası Ayarları
1. **3D Ayarlarının Yönetilmesi > Program Ayarları > CS2 (cs2.exe)** seçin.
2. Aşağıdaki parametreleri uygulayın:
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık (On) veya Ultra. *(Oyun içinde NVIDIA Reflex açık ise bu ayar oyun tarafından otomatik yönetilir).*
   * **Güç Yönetimi Modu:** Maksimum performansı tercih et (Prefer maximum performance).
   * **Dokunun Süzülmesi - Kalite:** Yüksek Performans.
   * **Eşyönsüz Süzme İyileştirmesi:** Açık.
   * **Dikey Senkronizasyon (V-Sync):** Kapalı.
   * **Threaded Optimization (MThread Optimizasyonu):** Açık.

### AMD Radeon Software Ayarları
1. **Ekran Kartları (Graphics) > Oyun (Gaming) > CS2** sekmesine gidin.
2. **Radeon Anti-Lag:** Etkin (Input lag'ı azaltır).
3. **Radeon Boost:** Devre Dışı (Dinamik çözünürlük ölçekleme görüntü netliğini bozar).
4. **Radeon Image Sharpening (RIS):** %70-%80 seviyesinde Etkin (İsteğe bağlı keskinlik artışı).
5. **Dikey Yenileme İçin Bekle (V-Sync):** Her zaman kapalı.

---

## 4. Windows ve Sistem Seviyesi Ayarları

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10/11 ile gelen HAGS özelliği, VRAM yönetimini CPU'dan GPU'ya devreder.
* **Yol:** `Ayarlar > Sistem > Ekran > Grafik Ayarları`
* **İşlem:** *Donanım Hızlandırmalı GPU Zamanlaması* ayarını **Açık** konuma getirin ve bilgisayarı yeniden başlatın. High-end sistemlerde mikrosaniyeler düzeyinde gecikme düşüşü sağlar.

### Windows Oyun Modu (Game Mode)
* **Yol:** `Ayarlar > Oyun > Oyun Modu`
* **İşlem:** **Açık**. Windows'un arka plan işlemlerini kısıtlayarak tüm CPU çekirdeklerini CS2'ye önceliklendirmesini sağlar.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. `cs2.exe` dosyasını bulun (Varsayılan: `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\bin\win64\cs2.exe`).
2. Sağ tıklayıp **Özellikler > Uyumluluk** sekmesine gidin.
3. **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçekleme davranışını geçersiz kıl** seçeneğini aktif edip "Uygulama" olarak ayarlayın.

### Güç Planı Optimizasyonu
* Komut İstemi'ni (CMD) yönetici olarak çalıştırın ve Nihai Performans modunu aktif edin:
  ```cmd
  powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
  ```
* `Denetim Masası > Güç Seçenekleri` yolunu izleyerek **Nihai Performans (Ultimate Performance)** planını seçin.

---

## 5. Kritik Konsol Komutları (Autoexec)

Aşağıdaki komutları `autoexec.cfg` dosyanıza ekleyerek veya oyun içi konsola girerek ağ ve render kararlılığını artırabilirsiniz:

```text
// Performans ve Kare Kararlılığı
fps_max "0"                   // Maksimum FPS limiti (Sabit değer vermek 1% Low FPS'i düzeltebilir)
cl_showfps "0"                // Ekran içi FPS göstergesini kapatır (Çok az da olsa yük bindirir)
r_show_build_info "false"     // Sol alt köşedeki CS2 sürüm bilgisini gizler

// Ağ ve Sub-Tick İyileştirmeleri
rate "1000000"                // Maksimum bant genişliği kullanımı (Yüksek hızlı internetler için)
cl_net_buffer_ticks "0"       // Paket kaybı (Loss) yoksa 0 yapılmalıdır, en düşük ağ gecikmesini sağlar
```

---

## 6. Donanım ve Bellek (RAM) Optimizasyonları

Source 2 motoru, belleğin bant genişliğine ve gecikme süresine (Latency) aşırı duyarlıdır:

1. **Dual-Channel RAM:** Sisteminizde tek kanal (Single-Channel) RAM bulunuyorsa, CS2'de ani FPS düşüşleri (stuttering) yaşamanız kaçınılmazdır. Belleklerin mutlaka Çift Kanal (Dual-Channel) mimarisinde çalışması gerekir.
2. **XMP / EXPO Aktivasyonu:** BIOS üzerinden XMP (Intel) veya EXPO/DOCP (AMD) profilinin açık olduğundan ve RAM'lerin vaat edilen en yüksek frekansta (MHz) çalıştığından emin olun.
3. **Resizable BAR / Smart Access Memory (SAM):** BIOS üzerinden **ReBAR** özelliğinin açılması, CPU'nun GPU VRAM'inin tamamına doğrudan erişmesini sağlayarak CS2'deki yüzde 1'lik (1% Low) minimum FPS değerlerini belirgin şekilde yükseltir.