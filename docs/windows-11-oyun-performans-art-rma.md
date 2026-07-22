---
title: "windows 11 oyun performansı artırma"
description: "windows 11 oyun performansı artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Oyun Performansı Artırma Rehberi: FPS ve Sistem Optimizasyonu

Windows 11, modern mimarisi ve oyun odaklı teknolojileriyle gelişmiş bir işletim sistemi olmasına rağmen, varsayılan güvenlik ve arka plan ayarları oyunlarda kare hızı (FPS) kayıplarına ve girdi gecikmesine (input lag) neden olabilir. Bu rehber, Windows 11 işletim sisteminde maksimum oyun performansı elde etmek için uygulanması gereken teknik optimizasyon adımlarını içermektedir.

---

## 1. Çekirdek Güvenlik Özelliklerini Devre Dışı Bırakma (VBS ve HVCI)

Windows 11'de varsayılan olarak açık gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Çekirdek Yalıtımı (HVCI), sistem güvenliğini sağlarken işlemci (CPU) ve bellek (RAM) üzerinde ciddi bir yük oluşturur. Yapılan testler, VBS'nin kapatılmasının oyunlarda %5 ile %25 arasında FPS artışı sağladığını göstermektedir.

### VBS ve Bellek Bütünlüğünü Kapatma Adımları:
1. Başlat menüsüne **"Çekirdek Yalıtımı"** (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Başlat menüsüne `cmd` yazıp **Yönetici Olarak Çalıştır**'a tıklayın.
4. Komut satırına aşağıdaki komutu girin ve `Enter` tuşuna basın:
   ```cmd
   bcdedit /set hypervisorlaunchtype off
   ```
5. Değişikliklerin etkinleşmesi için bilgisayarı yeniden başlatın.

---

## 2. Windows Oyun Modu ve Donanım Hızlandırmalı GPU Zamanlamasını (HAGS) Etkinleştirme

Windows 11'in **Oyun Modu**, sistem kaynaklarını (CPU çekirdekleri ve RAM) arka plan işlemlerinden alıp doğrudan oyuna yönlendirir. **HAGS** ise grafik kartının kendi belleğini (VRAM) işletim sistemi yerine doğrudan yönetmesini sağlayarak render gecikmesini düşürür.

### Oyun Modunu Açma:
* `Ayarlar > Oyun > Oyun Modu` sekmesine gidin ve **Açık** konuma getirin.

### HAGS'i (Hardware-Accelerated GPU Scheduling) Açma:
1. `Ayarlar > Sistem > Ekran > Grafik` yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** hale getirin.
4. Bilgisayarınızı yeniden başlatın.

---

## 3. "Nihai Performans" Güç Planını Etkinleştirme

Windows 11 varsayılan olarak "Dengeli" güç planı ile gelir. Bu plan, işlemci frekansını sürekli dalgalandırarak micro-stuttering (anlık takılmalar) oluşmasına yol açabilir. İşlemcinin sürekli yüksek frekansta kalması için **Nihai Performans** (Ultimate Performance) moduna geçilmelidir.

1. Komut İstemcisini (CMD) **Yönetici olarak** açın.
2. Aşağıdaki komutu yapıştırın ve çalıştırın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Denetim Masası > Donanım ve Ses > Güç Seçenekleri` bölümüne gidin.
4. Listeden **Nihai Performans** seçeneğini işaretleyin.

---

## 4. Ekran Kartı Sürücü ve Kontrol Paneli Optimizasyonu

Güncel olmayan veya yanlış yapılandırılmış grafik sürücüleri performans darboğazlarına (bottleneck) neden olur.

### Sürücü Güncellemesi:
* NVIDIA veya AMD sürücülerinizi resmi sitelerinden güncelleyin. Temiz bir kurulum için **DDU (Display Driver Uninstaller)** kullanarak eski sürücü kalıntılarını kaldırmanız tavsiye edilir.

### NVIDIA Denetim Masası Ayarları:
* **3D Ayarlarının Yönetilmesi** sekmesine gidin:
  * **Güç Yönetimi Modu:** Maksimum performansı tercih et
  * **Düşük Gecikme Oranı Modu (Low Latency Mode):** On veya Ultra
  * **Doku Süzme - Kalite:** Yüksek Performans
  * **Dikey Eşitleme (V-Sync):** Kapalı (G-Sync kullanılıyorsa oyun içi Kapalı, NVCP üzerinden Açık yapılmalıdır).

### AMD Software Adrenalin Edition Ayarları:
* `Ekran Kartları` sekmesinden **Radeon Anti-Lag** özelliğini açın.
* **Radeon Boost** özelliğini dinamik çözünürlük desteği gerektiren oyunlar için aktif edin.
* **Ekran Kartı Profili** olarak "Performans" seçeneğini belirleyin.

---

## 5. Arka Plan Uygulamalarını ve Overlay (Katman) Yazılımlarını Kapatma

Oyun oynarken arka planda çalışan yazılımlar işlemci çekirdeklerini ve RAM bant genişliğini tüketir.

### Xbox Game Bar ve Yakalamaları Kapatma:
1. `Ayarlar > Oyun > Xbox Game Bar` yolunu izleyin ve seçeneği **Kapalı** yapın.
2. `Ayarlar > Oyun > Yakalamalar` sekmesinden **Arka planda kaydetme** özelliğini kapatın.

### Başlangıç Uygulamalarını Devre Dışı Bırakma:
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. **Başlangıç Uygulamaları** sekmesine gelin.
3. Discord, Spotify, Steam gibi bilgisayar açıldığında otomatik başlayan tüm gereksiz uygulamaları **Devre Dışı Bırak** olarak ayarlayın.

### Katmanları (Overlay) Kapatma:
* **Discord:** `Kullanıcı Ayarları > Oyun Arayüzü > Oyun içi arayüzü etkinleştir` (Kapalı)
* **GeForce Experience / AMD Software:** Oyun içi bilgi ekranı katmanlarını kapatın.

---

## 6. Görsel Efektleri ve RAM Kullanımını Optimize Etme

Windows 11'in gölge ve animasyon efektleri GPU/CPU üzerinde ek yük yaratır. Oyun performansı için işletim sistemini temel düzeyde çalıştırmak en iyi sonucu verir.

1. `Windows + R` tuşlarına basın, `sysdm.cpl` yazıp `Enter` tuşuna basın.
2. **Gelişmiş** sekmesinden Performans başlığı altındaki **Ayarlar** butonuna tıklayın.
3. **En iyi performans için ayarla** seçeneğini seçin.
4. Metin fontlarının bozulmaması için yalnızca **"Ekran yazı tipi kenarlarını düzelt"** seçeneğini işaretleyin ve kaydedin.

---

## 7. Depolama (SSD/NVMe) ve TRIM Optimizasyonu

Oyun yükleme sürelerini azaltmak ve açık dünya oyunlarındaki kaplama yükleme (texture streaming) takılmalarını önlemek için depolama birimlerinin optimize edilmesi gerekir.

### TRIM Komutunun Kontrolü:
1. CMD'yi **Yönetici olarak** açın.
2. Aşağıdaki komutu girin:
   ```cmd
   fsutil behavior query DisableDeleteNotify
   ```
3. Sonuç `0` olarak dönüyorsa TRIM aktiftir ve SSD'niz optimum performansla çalışıyordur. Eğer `1` ise aşağıdaki komutla aktifleştirin:
   ```cmd
   fsutil behavior set DisableDeleteNotify 0
   ```

### Sürücüleri İyileştirme:
* `Windows + S` tuşlarına basıp **"Sürücüleri Birleştir ve İyileştir"** aracını açın. SSD sürücünüzü seçip **İyileştir** butonuna tıklayarak TRIM işlemini manuel olarak tetikleyin.

---

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Beklenen Etki | Risk / Yan Etki |
| :--- | :--- | :--- |
| **VBS / HVCI Kapatma** | Yüksek FPS Artışı (%5 - %25) | Kurumsal düzeyde güvenlik azalır (Bireysel kullanıcı için güvenlidir) |
| **HAGS ve Oyun Modu** | Render gecikmesinde düşüş, stabil FPS | Yok |
| **Nihai Performans Planı** | Anlık takılmaların (stuttering) önlenmesi | Masaüstünde güç tüketimi biraz artabilir |
| **NVIDIA/AMD Sürücü Ayarları** | Daha yüksek ortalama FPS ve düşük input lag | Grafik kalitesinde çok az düşüş olabilir |
| **Arka Plan Katmanları Kapatma** | Minimum CPU kullanımı ve %1 Low FPS artışı | Oyun içi sohbet katmanları görünmez |

Bu adımlar eksiksiz uygulandığında, Windows 11 üzerinde hem sistem gecikmesi minimum seviyeye inecek hem de donanımınızın sunduğu ham performans en yüksek FPS değerleriyle ekrana yansıyacaktır.