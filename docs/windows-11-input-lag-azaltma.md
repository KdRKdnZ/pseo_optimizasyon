---
title: "windows 11 input lag azaltma"
description: "windows 11 input lag azaltma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Input Lag (Girdi Gecikmesi) Azaltma Rehberi: Donanım ve Sistem Optimize Yöntemleri

Windows 11, gelişmiş görsel efektleri ve arka plan süreçleri nedeniyle varsayılan ayarlarında yüksek **input lag (girdi gecikmesi)** değerlerine neden olabilir. Fare tıklaması, klavye girdisi veya denetleyici komutlarının ekrana yansıma süresini kapsayan bu gecikme, özellikle rekabetçi oyunlarda ve hassas iş istasyonlarında performansı doğrudan etkiler.

Bu rehberde, Windows 11 işletim sisteminde sistem mimarisi, grafik sürücüleri ve çevre birimleri düzeyinde gecikmeyi minimuma indirmek için uygulanması gereken teknik adımlar yer almaktadır.

---

## 1. Sistem ve İşletim Sistemi Düzeyinde Optimizasyonlar

### Oyun Modu (Game Mode) Aktifleştirme
Windows 11 Oyun Modu, arka plan işlemlerinin CPU/GPU üzerindeki yükünü sınırlandırarak çalışan oyuna öncelik atar.

1. `Windows + I` tuşları ile **Ayarlar**'ı açın.
2. **Oyun** > **Oyun Modu** sekmesine gidin.
3. Konumu **Açık** olarak ayarlayın.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS (Hardware-Accelerated GPU Scheduling), bellek yönetimini işletim sisteminden alıp doğrudan GPU'ya devrederek kare oluşturma gecikmesini (render latency) düşürür.

1. **Ayarlar** > **Sistem** > **Ekran** > **Grafikler** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım Hızlandırmalı GPU Zamanlaması** özelliğini **Açık** konuma getirin.
4. Değişikliğin uygulanması için bilgisayarı yeniden başlatın.

### Çekirdek Yalıtımı (Core Isolation / VBS) Kapatma
Sanal Alan Tabanlı Güvenlik (VBS) ve Bellek Bütünlüğü, Windows 11'de varsayılan olarak açıktır. Güvenliği artırsa da, DPC (Deferred Procedure Call) gecikmesine ve doğrudan sistem yanıt süresinin düşmesine neden olur.

1. Başlat menüsüne **Cihaz Güvenliği** yazın ve açın.
2. **Çekirdek Yalıtımı Ayrıntıları** linkine tıklayın.
3. **Bellek Bütünlüğü (Memory Integrity)** seçeneğini **Kapalı** duruma getirin.
4. Sisteminizi yeniden başlatın.

---

## 2. Grafik Sürücüsü ve Ekran Ayarları

### Ekran Yenileme Hızı ve VRR Konfigürasyonu
Yüksek yenileme hızı (Hz), taranan kareler arasındaki süreyi kısaltarak doğrudan girdi gecikmesini azaltır.

* **Yenileme Hızı:** **Ayarlar** > **Sistem** > **Ekran** > **Gelişmiş Ekran** bölümünden monitörünüzün desteklediği en yüksek yenileme hızını (144Hz, 240Hz vb.) seçin.
* **Pencere Oyunları İçin İyileştirmeler:** Grafik ayarları menüsünde bulunan *"Pencere oyunları için iyileştirmeler"* seçeneğini aktif edin. Bu ayar, pencereli modda çalışan oyunların DWM (Desktop Window Manager) gecikmesini bypass etmesini sağlar.

### NVIDIA Denetim Masası Ayarları
NVIDIA ekran kartı kullanıcıları için gecikmeyi en aza indiren kritik ayarlar:

* **Düşük Gecikme Oranı Modu (Low Latency Mode):** `Ultra` konumuna getirin. Bu ayar, karelerin render kuyruğuna girmeden doğrudan işlenmesini sağlar.
* **Güç Yönetimi Modu:** `Maksimum performansı tercih et` olarak değiştirin. GPU'nun düşük güç durumlarına geçerek gecikme yaratmasını engeller.
* **Dikey Senkronizasyon (V-Sync):** Sürücü seviyesinde **Kapalı** olmalıdır. V-Sync, kareleri monitörün tazeleme hızıyla eşlemek için ara bellek (buffering) kullanır ve belirgin bir lag oluşturur.

### AMD Software: Adrenalin Edition Ayarları
* **Radeon Anti-Lag:** Aktif duruma getirin. CPU kare hazırlama hızı ile GPU render hızını senkronize ederek gecikmeyi düşürür.
* **Radeon Boost:** Hareket anında çözünürlüğü dinamik olarak düşürerek tepki süresini artırır (opsiyonel).

---

## 3. Çevre Birimleri (Mouse & Klavye) İyileştirmeleri

### Fare Hassasiyetini Artır (Mouse Acceleration) Kapatma
Windows'un varsayılan fare ivmelenmesi, el hareketinizin hızına göre imleç mesafesini değiştirir ve kas hafızasını bozarak girdi tutarsızlığı yaratır.

1. `Windows + R` basın, `main.cpl` yazıp Enter'a basın.
2. **İşaretçi Seçenekleri** sekmesine gelin.
3. **"İşaretçi hassasiyetini artır" (Enhance pointer precision)** kutusundaki işareti kaldırın.
4. Uygula ve Tamam'a tıklayın.

```
İpucu: Oyun içi hassasiyet için Windows imleç hızını varsayılan değer olan 6/11 seviyesinde tutun.
```

### Polling Rate (Raporlama Hızı) ve USB Port Yapılandırması
* **1000 Hz ve Üzeri Polling Rate:** Farenizin yazılımından raporlama hızını en az 1000 Hz (1ms) olarak ayarlayın.
* **USB Portu Seçimi:** Çevre birimlerinizi doğrudan anakartın arka paneline (I/O) bağlayın. USB hub veya kasa ön paneli adaptörleri ek gecikmeye (latency) neden olabilir.
* **USB Seçmeli Askıya Alma:** Güç Seçenekleri > Ek Plan Ayarları > USB Ayarları altındaki **USB Seçmeli Askıya Alma Özelliği**'ni **Devre Dışı** yapın.

---

## 4. Gelişmiş Teknik Düzenlemeler ve Güç Yönetimi

### Nihai Performans Güç Planını Etkinleştirme
Yüksek performans güç planları, CPU çekirdeklerinin düşük frekanslara düşmesini (CPU Throttling) engeller ve sürekli olarak maksimum tepkiselliği korur.

1. Komut İstemcisi'ni (CMD) Yönetici olarak çalıştırın.
2. Şu komutu yapıştırın ve Enter'a basın:
   `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`
3. **Denetim Masası** > **Güç Seçenekleri** bölümüne gidin ve **Nihai Performans (Ultimate Performance)** planını seçin.

### High Precision Event Timer (HPET) Devre Dışı Bırakma
HPET, bazı donanım konfigürasyonlarında mikro takılmalara ve girdi gecikmesine yol açabilir. Sadece komut satırı üzerinden devre dışı bırakılabilir.

1. Yönetici olarak CMD'yi açın.
2. HPET'i kapatmak için şu komutları sırasıyla çalıştırın:
   ```cmd
   bcdedit /set useplatformclock false
   bcdedit /disabledynamictick yes
   ```
3. Bilgisayarınızı yeniden başlatın.

---

## 5. DPC Latency Analizi ve Teşhis

Yapılan optimizasyonların başarısını ölçmek ve sistemdeki hatalı bir sürücünün gecikmeye sebep olup olmadığını anlamak için **LatencyMon** yazılımı kullanılmalıdır.

1. LatencyMon programını indirin ve çalıştırın.
2. **Start Monitoring** butonuna basın ve arka planda bir oyun veya ağır işlem çalıştırın.
3. *Main* ve *Drivers* sekmelerinde yüksek gecikmeye (ISR/DPC count) neden olan sürücüleri (`nvlddmkm.sys`, `ndis.sys` vb.) tespit edip ilgili donanım sürücülerini güncelleyin veya yeniden yükleyin.

## Özet Kontrol Listesi (Checklist)

| Ayar | İdeal Durum | Etki Alanı |
| :--- | :--- | :--- |
| **Oyun Modu** | Açık | İşlemci / Önceliklendirme |
| **HAGS** | Açık | GPU Zamanlaması |
| **Bellek Bütünlüğü (VBS)** | Kapalı | Sistem Gecikmesi (DPC) |
| **NVIDIA Low Latency** | Ultra | Render Kuyruğu |
| **İşaretçi Hassasiyeti** | Kapalı | Fare İvmelenmesi |
| **Güç Planı** | Nihai Performans | CPU Frekans Sabitleme |
| **Ekran Yenileme Hızı** | En Yüksek (Hz) | Görsel Girdi Tepkisi |