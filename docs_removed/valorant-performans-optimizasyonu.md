---
title: "valorant performans optimizasyonu"
description: "valorant performans optimizasyonu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Valorant Performans Optimizasyonu Rehberi: Maksimum FPS ve Minimum Input Lag

Valorant, Unreal Engine 4 motoru üzerinde çalışan ve büyük ölçüde işlemci (CPU) performansına dayanan bir rekabetçi FPS oyunudur. Yüksek kare hızları (FPS) elde etmek yalnızca daha akıcı bir görüntü sağlamakla kalmaz, aynı zamanda sistem gecikmesini (input lag) düşürerek tepki sürenizi doğrudan iyileştirir. 

Bu rehber; oyun içi grafik konfigürasyonlarından Windows çekirdek seviyesi ayarlarına, ekran kartı kontrol panellerinden ağ optimizasyonlarına kadar en efektif teknik adımları içermektedir.

---

## 1. Oyun İçi Grafik Ayarları Optimizasyonu

Valorant'ta grafik kalitesini düşürmek, ekran kartı (GPU) üzerindeki yükü azaltır ve işlemcinin kareleri daha hızlı işlemesine olanak tanır.

### Genel Grafik Ayarları
* **Görüntü Modu:** Tam Ekran *(Pencereli veya Çerçevesiz Pencereli modlar DWM (Desktop Window Manager) gecikmesi ekler).*
* **Çözünürlük:** Monitörün yerel (native) çözünürlüğü ve en yüksek yenileme hızı (Hz).
* **Görünüş Oranı Yöntemi:** Doldur (Fill).
* **NVIDIA Reflex Düşük Gecikme:** Açık + Takviye (On + Boost). *(Ekran kartı frekansını maksimumda tutarak işlemci sınırlaması olan durumlarda gecikmeyi minimize eder).*

### Gelişmiş Grafik Ayarları
* **Çoklu İzlek İşleme (Multithreaded Rendering):** Açık *(İşlemcinizde 8'den fazla izlek/thread varsa FPS'i önemli ölçüde artırır).*
* **Materyal Kalitesi:** Düşük
* **Doku Kalitesi:** Düşük
* **Detay Kalitesi:** Düşük
* **Arayüz Kalitesi:** Düşük
* **Netliği Arttır:** Kapalı *(Görsel netliği artırır ancak GPU yükünü artırabilir).*
* **Deneysel Keskinleştirme:** Kapalı
* **Eşyönsüz Filtreleme (Anisotropic Filtering):** 1x
* **Kenar Yumuşatma (Anti-Aliasing):** Hiçbiri veya FXAA *(MSAA 4x gibi seçenekler gecikmeyi artırır).*
* **Bozulma (Distortion):** Kapalı
* **Gölge Oluşturma (Cast Shadows):** Kapalı
* **V-Sync (Dikey Eşitleme):** Kapalı *(Kesinlikle kapatılmalıdır, ciddi girdi gecikmesine yol açar).*

---

## 2. Windows 10/11 İşletim Sistemi Optimizasyonları

Windows'un arka plan süreçlerini ve güç yönetimini oyun odaklı yapılandırmak, "frame drop" (ani FPS düşüşü) sorunlarını engeller.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
1. Valorant'ın ana yürütülebilir dosyasını bulun:  
   `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64\VALORANT-Win64-Shipping.exe`
2. Dosyaya sağ tıklayın ve **Özellikler** > **Uyumluluk** sekmesine gidin.
3. **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna tıklayın ve **Yüksek DPI ölçeklendirme davranışını geçersiz kıl** seçeneğini aktif edip **Uygulama** olarak ayarlayın.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 (2004+) ve Windows 11 ile gelen bu özellik, belleği yönetme görevini CPU'dan alıp GPU'ya devreder.
* **Ayarlar > Sistem > Monitör > Grafik Ayarları** yolunu izleyin.
* **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** konuma getirin ve sistemi yeniden başlatın. *(Giriş seviyesi GPU'larda performans artışı sağlar).*

### Güç Planını "Nihai Performans" Yapma
İşlemcinin çekirdek frekanslarını sürekli en yüksek seviyede tutmak için:
1. Komut İstemi'ni (CMD) Yönetici olarak çalıştırın.
2. Şu komutu girin:  
   `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`
3. **Denetim Masası > Güç Seçenekleri** bölümünden **Nihai Performans** (Ultimate Performance) planını seçin.

---

## 3. Ekran Kartı Sürücü Ayarları

### NVIDIA Denetim Masası Ayarları
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi > Program Ayarları** sekmesinden Valorant'ı (`VALORANT-Win64-Shipping.exe`) seçin.
3. Aşağıdaki değişiklikleri uygulayın:
   * **Güç Yönetimi Modu:** Maksimum performansı tercih et.
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra veya Açık.
   * **Maksimum Kare Hızı:** Kapalı.
   * **Süreç Algılamalı Optimizasyon (Threaded Optimization):** Açık.
   * **Doku Süzme - Kalite:** Yüksek Performans.
   * **Doku Süzme - Trilinear Optimizasyon:** Açık.
   * **Doku Süzme - Eşyönsüz Örnek Optimizasyonu:** Açık.
   * **Dikey Senkronizasyon:** Kapalı.

### AMD Software: Adrenalin Edition Ayarları
1. AMD Software panelini açın ve **Oyunlar > Valorant** profilini seçin.
2. **Radeon Anti-Lag:** Etkin *(Input lag değerini düşürür).*
3. **Radeon Chill:** Devre Dışı.
4. **Radeon Boost:** Devre Dışı *(Dinamik çözünürlük ölçekleme pikselleşmeye neden olur).*
5. **Dikey Yenileme için Bekleyin:** Her zaman kapalı.
6. **Doku Filtreleme Kalitesi:** Performans.

---

## 4. Donanım ve Sistem Seviyesinde Gecikme (Input Lag) Optimizasyonu

### HPET (High Precision Event Timer) Devre Dışı Bırakma
HPET, sistem zamanlamalarını senkronize eder ancak bazı sistemlerde CPU üzerine mikro takılmalar (stuttering) yaratabilir.

1. CMD'yi Yönetici olarak açın.
2. HPET'i kapatmak için şu komutu çalıştırın:  
   `bcdedit /set useplatformclock false`
3. Dinamik kenetlemeyi kapatmak için:  
   `bcdedit /set disabledynamictick yes`
4. Bilgisayarı yeniden başlatın.

### Ağ Önbellekleme (Network Buffering) Ayarı
Oyundaki bağlantı kalitenize göre paket işleme gecikmesini optimize edin:
* **Oyun İçi Ayarlar > Genel > Ağ Önbellekleme:** **Asgari (Minimum)** olarak ayarlayın.
* *Note:* Eğer internet bağlantınızda yüksek paket kaybı (packet loss) veya dalgalanma (jitter) varsa bu ayarı **Orta** seviyeye çekmek ışınlanma (teleport) efektlerini engeller.

---

## 5. Valorant Yapılandırma (Config) Dosyası İnce Ayarları

Çok düşük sistemlerde grafik kalitesini oyun arayüzünün izin verdiğinden daha aşağı çekmek mümkündür:

1. `Win + R` tuşlarına basın ve `%LOCALAPPDATA%\VALORANT\Saved\Config` yazıp Enter'a basın.
2. Rastgele harf ve rakamlardan oluşan klasörün içine girin ve `Windows` klasörünü açın.
3. `GameUserSettings.ini` dosyasını Not Defteri ile açın.
4. `[ScalabilityGroups]` başlığı altındaki değerleri düzenleyin:
   ```ini
   sg.ResolutionQuality=100.000000 (Görüntü çamurlaşırsa düşürmeyin, sabit tutun)
   sg.ViewDistanceQuality=0
   sg.AntiAliasingQuality=0
   sg.ShadowQuality=0
   sg.PostProcessQuality=0
   sg.TextureQuality=0
   sg.EffectsQuality=0
   sg.FoliageQuality=0
   sg.ShadingQuality=0
   ```
5. Dosyayı kaydedin ve sağ tıklayıp **Özellikler** sekmesinden **Salt Okunur** işaretleyin.

---

## Özet Performans Kontrol Listesi

| İşlem | Hedef | Beklenen Etki |
| :--- | :--- | :--- |
| **Tam Ekran Modu** | DWM İptali | -10ms ile -15ms Input Lag |
| **NVIDIA Reflex (Boost)** | GPU/CPU Senkronizasyonu | Stabil Kare Zamanı (Frame Time) |
| **Nihai Güç Planı** | CPU Throttling Önleme | Minimum FPS Değerinde Artış |
| **Gelişmiş Grafik ayarları (Low)** | GPU Yükünü Azaltma | Maksimum FPS Artışı |
| **HAGS ve Anti-Lag** | Donanım Gecikmesi | Düşük Tepki Süresi |

*En kararlı sonuçlar için her büyük Valorant güncellemesinden sonra ekran kartı sürücülerinizi **DDU (Display Driver Uninstaller)** ile temiz bir şekilde kaldırıp yeniden kurmanız tavsiye edilir.*