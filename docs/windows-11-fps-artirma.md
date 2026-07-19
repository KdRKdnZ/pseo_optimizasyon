---
title: windows 11 fps artırma
description: windows 11 fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 FPS Artırma Rehberi: Donanım ve İşletim Sistemi Optimizasyonu

Windows 11, modern mimarisi ve güvenlik odaklı yapısıyla öne çıksa da, varsayılan olarak açık gelen birçok arka plan servisi ve güvenlik katmanı oyun performansını doğrudan olumsuz etkiler. Bu rehberde, işletim sistemi çekirdeği (kernel) seviyesinden donanım sürücülerine kadar uygulayabileceğiniz, kanıtlanmış **Windows 11 FPS artırma** yöntemlerini teknik detaylarıyla inceleyeceğiz.

---

## Çekirdek Seviyesinde Windows 11 FPS Artırma Yöntemleri

Windows 11'in oyunlarda Windows 10'a kıyasla daha düşük performans göstermesinin temel nedeni, varsayılan olarak etkinleştirilen sanallaştırma tabanlı güvenlik önlemleridir. Bu ayarları optimize ederek CPU üzerindeki yükü azaltabilirsiniz.

### Sanallaştırma Tabanlı Güvenliği (VBS) ve Bellek Bütünlüğünü Kapatın

Virtualization-Based Security (VBS) ve Hypervisor-Protected Code Integrity (HVCI / Bellek Bütünlüğü), sistemi zararlı yazılımlardan korumak için CPU üzerinde sanal bir güvenli bölge oluşturur. Ancak bu işlem, özellikle CPU darboğazı yaşanan oyunlarda %5 ila %15 arasında FPS kaybına yol açar.

1. Başlat menüsüne **Çekirdek Yalıtım** (Core Isolation) yazın ve açın.
2. **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** duruma getirin.
3. Bilgisayarınızı yeniden başlatın.

*Kanıt:* Microsoft, oyun performansını optimize etmek isteyen kullanıcılar için bu ayarın kapatılmasını resmi olarak önermektedir.

### Donanım Hızlandırmalı GPU Zamanlamasını (HAGS) Aktif Edin

Hardware-Accelerated GPU Scheduling (HAGS), video belleğini (VRAM) yönetme görevini işletim sisteminden alarak doğrudan GPU'nun kendi zamanlayıcısına devreder. Bu, kare oluşturma gecikmesini (render latency) düşürür ve minimum FPS değerlerini (1% ve 0.1% Low) yukarı taşır.

1. **Ayarlar > Sistem > Ekran > Grafik** yolunu izleyin.
2. **Varsayılan grafik ayarlarını değiştir** seçeneğine tıklayın.
3. **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin.

### Oyun Modu (Game Mode) ve Grafik Önceliklerini Yapılandırın

Windows 11 Oyun Modu, oyun çalışırken arka plan işlemlerinin (Windows Update, bildirimler vb.) CPU iş parçacıklarını (threads) işgal etmesini engeller.

* **Oyun Modunu Açma:** **Ayarlar > Oyun > Oyun Modu** bölümüne gidin ve aktif edin.
* **Uygulama Özelinde GPU Atama:** Grafik ayarları ekranından oynadığınız oyunu seçip **Seçenekler**'e tıklayarak **Yüksek Performans** (Harici GPU) olarak ayarlayın.

---

## Donanım ve Sürücü Optimizasyonu ile Maksimum Performans

Yazılımsal ayarların yanı sıra, donanımın işletim sistemiyle olan iletişim protokollerini optimize etmek gecikmeleri (latency) minimize eder.

### Ekran Kartı Sürücülerini DDU ile Temiz Kurun

Üst üste yüklenen GPU sürücüleri, Windows kayıt defterinde (Registry) çakışmalara ve dolayısıyla anlık takılmalara (stuttering) neden olur.

1. En güncel NVIDIA, AMD veya Intel sürücüsünü indirin.
2. **DDU (Display Driver Uninstaller)** yazılımını indirin ve sistemi **Güvenli Mod**'da başlatarak mevcut sürücüleri tamamen kazıyın.
3. Sistemi normal modda başlatıp yeni sürücüyü "Temiz Kurulum" seçeneğiyle yükleyin.

### Nihai Performans (Ultimate Performance) Güç Planını Devreye Alın

Standart "Yüksek Performans" planı, CPU çekirdeklerinin park edilmesini (core parking) tamamen engellemez. "Nihai Performans" modu ise donanımın mikro saniyeler düzeyindeki güç geçiş gecikmelerini sıfıra indirir.

1. **CMD**'yi (Komut İstemi) yönetici olarak çalıştırın.
2. Aşağıdaki kodu yapıştırıp Enter tuşuna basın:
   ```cmd
   powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
   ```
3. **Denetim Masası > Güç Seçenekleri** bölümüne giderek yeni eklenen **Nihai Performans** planını seçin.

---

## Gelişmiş Sistem ve Kayıt Defteri (Registry) Ayarları

Sistem mimarisine doğrudan müdahale ederek, Windows 11'in oyun dışı kaynak tüketimini en aza indirebilirsiniz.

### Kayıt Defteri ile Ağ Gecikmesini (Ping) ve İşlemci Önceliğini Optimize Edin

Aşağıdaki adımlar, oyun paketlerinin ağ kartı tarafından işlenme önceliğini artırır ve CPU'nun oyun motoruna daha fazla kaynak ayırmasını sağlar.

1. `Win + R` tuşlarına basıp `regedit` yazarak Kayıt Defteri Düzenleyicisi'ni açın.
2. Şu yola gidin: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile`
3. **NetworkThrottlingIndex** değerini çift tıklayın ve taban değerini *Onaltılık* seçip değer verisini `ffffffff` yapın (Ağ sınırlamasını devre dışı bırakır).
4. **SystemResponsiveness** değerini `0` yapın (Sistem kaynaklarının %100'ünü oyunlara ayırır).

### Geçici Dosyaları ve Gölgelendirici Önbelleğini (Shader Cache) Temizleyin

Bozulmuş gölgelendirici önbellekleri, oyunlarda ani FPS düşüşlerine (FPS drop) neden olur.

1. **Ayarlar > Sistem > Depolama > Geçici Dosyalar** yolunu izleyin.
2. **DirectX Gölgelendirici Önbelleği** (DirectX Shader Cache) seçeneğini işaretleyip **Dosyaları kaldırın** butonuna basın.

---

## Windows 11 FPS Artırma Sonuç Analizi

Aşağıdaki tabloda, uygulanan optimizasyonların sistem bileşenlerine ve oyun performansına olan ortalama etkisi (sentetik ve gerçek dünya testleri baz alınarak) gösterilmiştir:

| Yapılan Optimizasyon | Etkilenen Bileşen | Ortalama FPS Artışı | Etki Alanı |
| :--- | :--- | :--- | :--- |
| **VBS / HVCI Kapatma** | CPU (İşlemci) | %+5 - %+15 | CPU Sınırındaki Oyunlar (Valorant, CS2) |
| **HAGS Aktivasyonu** | GPU (Ekran Kartı) | %+3 - %+8 | VRAM Sınırındaki Ağır Grafikli Oyunlar |
| **Nihai Performans Modu** | CPU / Anakart | %1 Low FPS Kararlılığı | Anlık Takılmaların (Stutter) Önlenmesi |
| **DDU ile Temiz Kurulum** | GPU Sürücüsü | %+5 + Kararlılık | Sürücü Çakışması Kaynaklı Drop Çözümü |

Bu optimizasyonlar, Windows 11'in modern güvenlik mimarisinden ödün vererek donanımınızın saf gücünü doğrudan oyun motoruna aktarmasını sağlar. Donanım limitlerinizi zorlamadan en kararlı performansı elde etmek için bu adımları sırasıyla uygulamanız önerilir.