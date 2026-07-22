---
title: "windows 11 fps artırma"
description: "windows 11 fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 FPS Artırma Rehberi: Teknik ve Donanım Düzeyinde Optimizasyon

Windows 11, modern mimarisi ve güvenlik odaklı yapısıyla öne çıksa da varsayılan ayarları performans odaklı oyun senaryoları için her zaman ideal değildir. İşletim sisteminin arka plan süreçleri, güvenlik protokolleri ve görsel efektleri, CPU ve GPU kaynaklarını tüketerek kare hızı (FPS) kayıplarına ve "stuttering" (anlık takılma) sorunlarına yol açabilir. 

Aşağıdaki adımlar, Windows 11 üzerinde maksimum oyun performansı elde etmek için uygulanması gereken teknik optimizasyonları içermektedir.

---

## 1. Windows 11 Yerleşik Oyun Özelliklerini Yapılandırma

Windows 11, oyun performansını doğrudan etkileyen çekirdek ayarlara sahiptir. Bu ayarların doğru yapılandırılması, donanım sürücülerinin işletim sistemiyle senkronize çalışmasını sağlar.

### Oyun Modu'nu (Game Mode) Aktifleştirme
Oyun Modu, oyun çalışırken arka plan işlemlerinin kaynak kullanımını kısıtlar ve CPU önceliğini oyuna verir.

1. `Windows + I` tuşlarına basarak **Ayarlar**'ı açın.
2. **Oyun** > **Oyun Modu** sekmesine gidin.
3. **Oyun Modu** seçeneğini **Açık** konuma getirin.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS, bellek yönetim yükünü CPU'dan alarak doğrudan GPU'ya devreder. Özellikle orta ve üst segment ekran kartlarında (NVIDIA GTX 1000 serisi ve üzeri, AMD RX 5000 serisi ve üzeri) FPS artışı ve gecikme (latency) düşüşü sağlar.

1. **Ayarlar** > **Sistem** > **Ekran** > **Grafikler** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** bağlantısına tıklayın.
3. **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** yapın.
4. **Pencereli oyunlar için optimizasyonlar** seçeneğini de aktifleştirin.
5. Bilgisayarı yeniden başlatın.

---

## 2. Güvenlik Tabanlı Performans Kayıplarını Önleme (VBS ve HVCI)

Windows 11'de varsayılan olarak açık gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Bellek Bütünlüğü (HVCI), sistem güvenliğini artırırken oyunlarda %5 ile %25 arasında FPS kaybına neden olabilir. Tamamen oyun odaklı sistemlerde bu özelliklerin kapatılması ciddi performans artışı sağlar.

### Bellek Bütünlüğünü (Memory Integrity) Devre Dışı Bırakma

1. Başlat menüsüne **Windows Güvenliği** yazın ve açın.
2. **Cihaz Güvenliği** > **Çekirdek Yalıtımı Detayları** sekmesine girin.
3. **Bellek Bütünlüğü** (Memory Integrity) ayarını **Kapalı** duruma getirin.
4. Sisteminizi yeniden başlatın.

---

## 3. Güç Tüketimi ve CPU Frekans Sabitleme

Windows 11 varsayılan "Dengeli" güç planı, CPU çekirdek frekanslarını sürekli dalgalandırır. Bu durum ani FPS düşüşlerine (Frame Drop) sebep olur. "Nihai Performans" modu ile CPU'nun sürekli yüksek frekansta çalışması sağlanır.

### Nihai Performans (Ultimate Performance) Modunu Etkinleştirme

1. Başlat menüsüne sağ tıklayıp **Terminal (Yönetici)** veya **PowerShell (Yönetici)** seçeneğini çalıştırın.
2. Aşağıdaki komutu yapıştırın ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Win + R` tuşlarına basıp `powercfg.cpl` yazarak **Güç Seçenekleri**'ni açın.
4. **Nihai Performans** planını seçin.

---

## 4. Sistem Görsel Efektlerini ve Telemetriyi Optimize Etme

Windows 11'in animasyonları, saydamlık efektleri ve arka plan servisleri RAM ve CPU kaynaklarını işgal eder.

### Görsel Efektleri Kapatma
1. `Win + R` tuş kombinasyonu ile Çalıştır penceresini açın, `sysdm.cpl` yazıp Enter'a basın.
2. **Gelişmiş** sekmesinden **Performans** bölümündeki **Ayarlar** düğmesine tıklayın.
3. **En iyi performans için ayarla** seçeneğini işaretleyin.
4. Okunabilirliği bozmamak adına yalnızca **"Ekran yazı tipi kenarlarını düzelt"** seçeneğini işaretli bırakıp **Uygula**'ya tıklayın.

### Başlangıç ve Arka Plan Uygulamalarını Kısıtlama
1. `Ctrl + Shift + Esc` ile **Görev Yöneticisi**'ni açın.
2. Sol menüden **Başlangıç Uygulamaları** sekmesine gelin.
3. Discord, Spotify, Steam gibi sistem açılışında yük getiren ve arka planda çalışan gereksiz tüm uygulamaları **Devre Dışı Bırakın**.

---

## 5. Grafik Sürücüsü ve Sürücü Düzeyinde Ayarlar

Grafik kartı sürücülerinin güncelliği kadar denetim masası ayarları da kritik önem taşır.

### NVIDIA Denetim Masası Optimizasyonu
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin ve şu ayarları uygulayın:
   * **Güç Yönetimi Modu:** Maksimum performansı tercih et
   * **Düşük Gecikme Oranı Modu (Low Latency Mode):** Açık veya Ultra
   * **Doku Süzme - Kalite:** Yüksek Performans
   * **Dikey Eşitleme (V-Sync):** Kapalı (G-Sync/FreeSync kullanılıyorsa oyun içi kapatılıp buradan yönetilebilir)

### AMD Software: Adrenalin Edition Optimizasyonu
1. AMD Yazılımını açın ve **Ekran Kartları** sekmesine gidin.
2. Profil olarak **eSpor** veya **Özel** seçin.
3. **Radeon Anti-Lag:** Açık
4. **Radeon Boost:** İhtiyaca göre Açık (Çözünürlüğü dinamiğe alarak FPS artırır)
5. **Ekran Kartı Durumu (Power Limit):** Güç limitini %5-10 artırmak çekirdek saat hızlarını stabil tutar.

---

## 6. Geçici Dosyalar ve Geçici Bellek (Cache) Temizliği

Sistemde biriken önbellek dosyaları disk I/O performansını olumsuz etkileyebilir.

1. `Win + R` tuşlarına basıp sırasıyla şu komutları çalıştırın ve açılan klasörlerdeki tüm dosyaları silin:
   * `temp`
   * `%temp%`
   * `prefetch`
2. **Depolama Mantığı (Storage Sense)** özelliğini aktifleştirmek için:
   * **Ayarlar** > **Sistem** > **Depolama** sekmesinden **Depolama Mantığı**'nı **Açık** konuma getirin.

---

## 7. Tam Ekran İyileştirmelerini Devre Dışı Bırakma (Oyun Özelinde)

Bazı eski veya rekabetçi oyunlarda (CS2, Valorant vb.) Windows'un hibrit tam ekran modu gecikmeye ve FPS düşüşüne neden olabilir.

1. Oyunun çalıştırılabilir ana dosyasına (`.exe`) sağ tıklayıp **Özellikler**'e girin.
2. **Uyumluluk** sekmesine gelin.
3. **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4. **Yüksek DPI ayarlarını değiştir** butonuna basarak **Yüksek DPI ölçeklendirme davranışını geçersiz kıl** seçeneğini aktif edin ve **Uygula**'ya tıklayın.

---

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Beklenen Etki | Risk / Yan Etki |
| :--- | :--- | :--- |
| **HAGS ve Oyun Modu** | Donanım verimliliği, yüksek FPS | Yok |
| **VBS / HVCI Kapatma** | %5 - %20 FPS Artışı | Düşük güvenlik riski (Bireysel kullanıcılar için ihmal edilebilir) |
| **Nihai Performans Modu** | Mikro takılmaların (Stuttering) engellenmesi | Hafif güç tüketimi artışı |
| **Görsel Efekt Kısma** | İşlemci ve RAM yükünün hafiflemesi | Minimal arayüz estetiği kaybı |
| **Sürücü Optimizasyonu** | Düşük girdi gecikmesi (Input Lag) | Yok |

Bu teknik konfigürasyonlar, Windows 11'in donanım kaynaklarını gereksiz işlemlerle tüketmesini engelleyerek, mevcut sisteminizin sunabileceği maksimum kare hızını (FPS) ve en düşük gecikme değerini almanızı sağlar.