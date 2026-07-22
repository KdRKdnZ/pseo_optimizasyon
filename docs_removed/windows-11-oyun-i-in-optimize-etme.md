---
title: "windows 11 oyun için optimize etme"
description: "windows 11 oyun için optimize etme hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 Oyun Optimizasyonu Rehberi: FPS Artırma ve Gecikme Düşürme

Windows 11, güncel mimarisi ve DirectStorage gibi teknolojileriyle oyunlar için gelişmiş bir altyapı sunar. Ancak varsayılan ayarlar, güvenlik ve genel kullanım odaklı olduğu için maksimum donanım performansını engeller. Bu rehberde, Windows 11 işletim sistemini teknik yöntemlerle tam performanslı bir oyun platformuna dönüştürme adımlarını inceleyeceğiz.

---

## 1. Çekirdek Sistem ve Grafik Ayarlarının Optimize Edilmesi

### Oyun Modu (Game Mode) Aktifleştirme
Windows 11 Oyun Modu, sistem kaynaklarını (CPU ve GPU) doğrudan çalışan oyuna önceliklendirecek şekilde ayarlar ve arka plan işlemlerini kısıtlar.

* **Adım:** `Ayarlar` > `Oyun` > `Oyun Modu` sekmesine gidin.
* **İşlem:** "Oyun Modu" seçeneğini **Açık** konuma getirin.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
HAGS (Hardware-Accelerated GPU Scheduling), bellek yönetim yükünü CPU'dan alıp doğrudan GPU'ya devreder. Bu işlem, özellikle orta ve üst segment ekran kartlarında gecikmeyi (latency) düşürür.

* **Adım:** `Ayarlar` > `Sistem` > `Ekran` > `Grafikler` > `Varsayılan grafik ayarlarını değiştir` yolunu izleyin.
* **İşlem:** **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** hale getirin ve bilgisayarı yeniden başlatın.

### Değişken Yenileme Hızı (VRR) ve Optimizations for Windowed Games
Pencereli modda çalışan oyunlarda gecikmeyi azaltmak ve G-Sync/FreeSync performansını artırmak için bu iki ayar kritik öneme sahiptir.

* Aynı grafik menüsünde yer alan **Değişken Yenileme Hızı (VRR)** ve **Pencereli oyunlar için optimizasyonlar** seçeneklerini **Açık** yapın.

---

## 2. Güvenlik Özelliklerini Performans İçin Yapılandırma (VBS & HVCI)

Windows 11'de varsayılan olarak gelen Sanallaştırma Tabanlı Güvenlik (VBS) ve Çekirdek Yalıtımı (HVCI), bellek erişimlerini sürekli denetlediği için oyunlarda %5 ile %15 arasında FPS kaybına neden olabilir.

### Çekirdek Yalıtımını (HVCI) Devre Dışı Bırakma
1. Başlat menüsüne `Çekirdek Yalıtımı` (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** konuma getirin.
3. Bilgisayarı yeniden başlatın.

### VBS'i Kayıt Defteri (Registry) Üzerinden Kapatma
Güvenlik katmanını tamamen pasife çekmek için:
1. `Win + R` tuşlarına basıp `regedit` yazın.
2. `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\DeviceGuard` yoluna gidin.
3. `EnableVirtualizationBasedSecurity` DWORD değerini çift tıklayıp verisini `0` yapın.

---

## 3. Güç Yönetimi ve İşlemci Çekirdek Park Etme (Core Parking)

### "Nihai Performans" (Ultimate Performance) Güç Planı
Varsayılan güç planları işlemci frekansını sürekli dalgalandırır. Bu durum micro-stuttering (anlık takılma) sorununa yol açar.

1. Komut İstemi'ni (CMD) Yönetici olarak çalıştırın.
2. Şu kodu yapıştırın ve Enter'a basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. `Denetim Masası` > `Güç Seçenekleri` menüsüne gidin ve **Nihai Performans** planını seçin.

### CPU Core Parking ve Throttling İptali
İşlemci çekirdeklerinin uyku moduna geçmesini (parking) engellemek için regedit üzerinden ayarlama yapılabilir:

1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\5433366f-541e-40d0-9756-bb1426f0e596\0cc12a64-325d-447e-b4d0-235084910e3d` yoluna gidin.
2. `Attributes` değerini `0` yapın.
3. Güç seçeneklerinde "İşlemci performans çekirdeği park etme minimum durumu" ayarı görünecektir, bunu `%100` yapın.

---

## 4. Arka Plan Hizmetleri ve Telemetri Temizliği

### Windows Xbox Game Bar ve Yakalamaları Kapatma
Arka planda sürekli ekran kaydı alan Game Bar, NVMe SSD ve GPU band genişliğini tüketir.

* `Ayarlar` > `Oyun` > `Görüntüler (Captures)` sekmesine gidin.
* **Arka planda kaydet** seçeneğini **Kapalı** yapın.
* `Oyun` > `Xbox Game Bar` sekmesinden denetleyici butonları ile açma ayarını kapatın.

### Gerekli Olmayan Hizmetleri Devre Dışı Bırakma
`services.msc` komutu ile Hizmetler penceresini açın ve şu hizmetleri "Devre Dışı" olarak ayarlayın:
* **SysMain (Superfetch):** SSD kullanıyorsanız gereksiz disk okuması yapar.
* **Connected User Experiences and Telemetry:** Arka planda veri toplayarak CPU ve ağ tüketir.
* **Windows Arama (Windows Search):** Disk indekslemesi yaparak arka plan kaynaklarını kullanır (İsteğe bağlı).

---

## 5. Grafik Sürücüsü ve Kayıt Defteri (Registry) İnce Ayarları

### Clean Install (DDU) ile Sürücü Güncelleme
Sürücü çakışmalarını önlemek için Display Driver Uninstaller (DDU) yazılımını Güvenli Mod'da çalıştırarak mevcut sürücüleri tamamen kaldırın ve NVIDIA/AMD'nin en güncel WHQL sürücüsünü kurun.

### Registry İle Oyun Önceliğini Artırma (SystemResponsiveness)
Windows'un multimedya ve oyun akışlarına sistem kaynaklarının %100'ünü ayırmasını sağlamak için:

1. `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile` yoluna gidin.
2. `SystemResponsiveness` DWORD değerini `0` (Hexadecimal) yapın.
3. `NetworkThrottlingIndex` değerini `ffffffff` (Hexadecimal) yapın (Ağ bant genişliği kısıtlamasını kaldırır).

`SystemProfile` altındaki `Tasks\Games` klasörüne gidin:
* `GPU Priority` -> `8`
* `Priority` -> `6`
* `Scheduling Category` -> `High`
* `SFIO Priority` -> `High`

---

## 6. Ağ (Network) ve Ping Optimizasyonu

Çevrim içi oyunlarda paket kaybı ve yüksek ping değerlerini düşürmek için Nagle Algoritmasını devre dışı bırakın.

1. `Win + R` > `regedit` ile şu yola gidin:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\`
2. Kullanılan ağ bağdaştırıcısının GUID klasörünü bulun (içinde IP adresinizin olduğu klasör).
3. Klasör içine sağ tıklayıp iki adet yeni **DWORD (32-bit)** değeri oluşturun:
   * `TcpAckFrequency` -> Değer: `1`
   * `TCPNoDelay` -> Değer: `1`

 bu işlem, TCP paketlerinin birleştirilmeden doğrudan gönderilmesini sağlar ve komut gecikmesini (input lag) düşürür.

---

## 7. Geçici Dosyaların ve Temizliğin Otomatikleştirilmesi

Sistem birikintileri RAM ve disk önbelleğini olumsuz etkiler.

* `Ayarlar` > `Sistem` > `Depolama` yolunu izleyin.
* **Depolama Algılaması (Storage Sense)** özelliğini **Açık** konuma getirin.
* Geçici dosyaları temizleme sıklığını "Her hafta" veya "Her gün" olarak yapılandırın.

---

## Özet Performans Kontrol Listesi

| Yapılacak İşlem | Hedef | Beklenen Etki |
| :--- | :--- | :--- |
| **Game Mode & HAGS** | CPU/GPU Yük Dengesi | Daha kararlı FPS, Düşük Input Lag |
| **VBS / HVCI Kapatma** | İşlemci Güvenlik Katmanı | %5-%15 FPS Artışı |
| **Nihai Performans** | Güç Yönetimi | Anlık Takılmaların (Stutter) Önlenmesi |
| **Nagle Algoritması Pasif**| Ağ Protokolü | Düşük Ping / Daha Hızlı Tepki Süresi |
| **Registry Games Tweaks** | İşlemci Önceliği | Oyun İşlemlerine Maksimum Thread Ayırma |

Bu teknik konfigürasyonlar, Windows 11'in arka plan yükünü minimuma indirerek donanımınızın saf işleme gücünü doğrudan render süreçlerine aktarmasını sağlar. Her majör Windows güncellemesinden sonra bu ayarların sıfırlanıp sıfırlanmadığı kontrol edilmelidir.