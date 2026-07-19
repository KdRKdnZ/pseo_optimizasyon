---
title: windows 11 input lag azaltma
description: windows 11 input lag azaltma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Input Lag Azaltma: En Düşük Gecikme İçin Teknik Rehber

Windows 11, modern arayüzü ve güvenlik odaklı mimarisiyle öne çıksa da, arka planda çalışan servisler, sanallaştırma tabanlı güvenlik katmanları ve varsayılan grafik yapılandırmaları nedeniyle milisaniye (ms) düzeyinde sistem gecikmesine (input lag) yol açabilir. Rekabetçi oyunlarda ve yüksek hassasiyet gerektiren profesyonel iş akışlarında bu gecikmeyi minimuma indirmek, donanım ve işletim sistemi seviyesinde optimizasyon gerektirir.

Bu rehberde, Windows 11 çekirdek (kernel) seviyesinden donanım sürücülerine kadar uygulayabileceğiniz, kanıta dayalı **Windows 11 input lag azaltma** yöntemlerini teknik detaylarıyla inceleyeceğiz.

---

## Input Lag (Gecikme) Nedir ve Windows 11'de Neden Oluşur?

Input lag, bir giriş aygıtına (klavye, fare, kontrolcü) fiziksel olarak basılması ile bu eylemin ekranda görsel bir tepkiye dönüşmesi arasında geçen süredir. Bu süreç üç ana aşamadan oluşur:

1.  **Giriş Gecikmesi (Input Latency):** Donanımın sinyali USB veri yolu üzerinden işletim sistemine iletme süresi.
2.  **İşleme Gecikmesi (Processing Latency):** Windows çekirdeğinin (kernel), grafik API'lerinin (DirectX/Vulkan) ve oyun motorunun girdiyi işleme süresi.
3.  **Görüntüleme Gecikmesi (Display Latency):** GPU'nun kareyi çizip monitöre göndermesi ve monitörün pikselleri yenileme süresi.

Windows 11, Windows 10'a kıyasla daha agresif bir pencere yöneticisine (DWM - Desktop Window Manager) ve **VBS (Virtualization-Based Security)** gibi işlemciye ek yük bindiren güvenlik katmanlarına sahiptir. Bu katmanlar, CPU-GPU arasındaki senkronizasyon döngüsünü uzatarak gecikmeyi artırır.

---

## Windows 11 İşletim Sistemi Seviyesinde Optimizasyonlar

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS) ve Oyun Modu

Donanım Hızlandırmalı GPU Zamanlaması (Hardware-Accelerated GPU Scheduling - HAGS), bellek yönetimini CPU'dan alarak doğrudan GPU'nun kendi özel zamanlama işlemcisine devreder. Bu, CPU darboğazını azaltır ve kare oluşturma kuyruğundaki (render queue) gecikmeyi minimize eder.

1.  **Ayarlar > Sistem > Monitör > Grafik** yolunu izleyin.
2.  **Varsayılan grafik ayarlarını değiştirin** seçeneğine tıklayın.
3.  **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin.
4.  Aynı menüde bulunan **Oyun Modu** (Game Mode) seçeneğini aktif edin. Oyun Modu, arka plan işlemlerinin CPU önceliğini düşürerek oyunun thread'lerine (iş parçacığı) öncelik tanır.

### Çekirdek Yalıtımı (VBS) ve Bellek Bütünlüğünü Devre Dışı Bırakma

Windows 11'de varsayılan olarak açık gelen Bellek Bütünlüğü (Hypervisor-Protected Code Integrity - HVCI), sistemi zararlı kodlardan korumak için sanallaştırma kullanır. Ancak bu güvenlik katmanı, CPU çekirdekleri arasında ek bir gecikme (inter-core latency) yaratır. Saf performans ve en düşük input lag için bu özelliğin kapatılması önerilir.

1.  Başlat menüsüne **Çekirdek Yalıtımı** (Core Isolation) yazın ve açın.
2.  **Bellek Bütünlüğü** (Memory Integrity) seçeneğini **Kapalı** duruma getirin.
3.  Bilgisayarınızı yeniden başlatın.

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma

Windows 11, pencereli modda çalışan oyunların gecikmesini azaltmak için "Pencereli oyunlar için iyileştirmeler" sunar. Ancak yerel (native) tam ekran modunda çalışan oyunlarda, Windows'un kendi sunum katmanının araya girmemesi için bu özelliğin oyun özelinde devre dışı bırakılması gerekir.

1.  Oynadığınız oyunun `.exe` dosyasına sağ tıklayıp **Özellikler**'i seçin.
2.  **Uyumluluk** sekmesine gelin.
3.  **Tam ekran iyileştirmelerini devre dışı bırak** seçeneğini işaretleyin.
4.  **Uygula** ve **Tamam** butonlarına basın.

---

## Sürücü ve Donanım Seviyesinde Gecikme Azaltma

### NVIDIA Ultra Düşük Gecikme ve AMD Anti-Lag Yapılandırması

Ekran kartı sürücüleri, GPU'nun işleyeceği kareleri önceden kuyruğa alır. Bu kuyruğun sınırlandırılması, doğrudan fare hareketlerinin ekrana yansıma hızını artırır.

#### NVIDIA Kullanıcıları İçin:
1.  NVIDIA Denetim Masası'nı açın.
2.  **3D Ayarlarının Yönetilmesi** sekmesine gidin.
3.  **Düşük Gecikme Oranı Modu** (Low Latency Mode) ayarını bulun.
    *   **Ultra:** GPU'nun kare kuyruğunu sıfıra indirir ve kareyi tam zamanında (just-in-time) oluşturur. CPU sınırındaki oyunlarda gecikmeyi %20'ye kadar azaltır.
4.  Eğer oyun içi ayarlarda **NVIDIA Reflex** desteği varsa, bunu **Açık + Takviye (On + Boost)** yapın. Reflex, sürücü seviyesindeki ayarı geçersiz kılarak oyun motoru ile GPU'yu doğrudan senkronize eder.

#### AMD Kullanıcıları İçin:
1.  AMD Software: Adrenalin Edition'ı açın.
2.  **Oyun > Grafikler** sekmesine gidin.
3.  **Radeon Anti-Lag** özelliğini etkinleştirin. Bu ayar, CPU yazma hızını GPU ile hizalayarak giriş gecikmesini düşürür.

### USB Polling Rate (Raporlama Hızı) ve USB Güç Yönetimi

Fare ve klavyenizin bilgisayarla iletişim kurma sıklığı (Polling Rate), giriş gecikmesini doğrudan etkiler. 125 Hz bir fare her 8 ms'de bir veri gönderirken, 1000 Hz bir fare her 1 ms'de bir veri gönderir.

*   **Çözüm:** Giriş aygıtınızın yazılımı (Logitech G Hub, Razer Synapse vb.) üzerinden Polling Rate değerini **1000 Hz** veya donanımınız destekliyorsa **4000 Hz / 8000 Hz** değerine ayarlayın.

#### USB Güç Tasarrufunu Kapatma:
Windows'un USB portlarını güç tasarrufu moduna alması, aygıtların uyanma sürelerinde mikro gecikmelere neden olur.

1.  **Aygıt Yöneticisi**'ni açın.
2.  **Evrensel Seri Veri Yolu denetleyicileri** sekmesini genişletin.
3.  **Kök USB Hub** (USB Root Hub) aygıtlarına sağ tıklayıp **Özellikler** deyin.
4.  **Güç Yönetimi** sekmesine gidin ve **"Güç tasarrufu yapmak için bilgisayarın bu aygıtı kapatmasına izin ver"** seçeneğindeki işareti kaldırın.

### Nihai Performans Güç Planını Etkinleştirme

Windows'un standart "Yüksek Performans" planı bile işlemci çekirdeklerinin park edilmesine (core parking) ve frekans dalgalanmalarına izin verebilir. "Nihai Performans" (Ultimate Performance) modu, donanımın sürekli en yüksek güç durumunda (C-states sınırlaması olmadan) kalmasını sağlar.

1.  PowerShell veya Komut İstemi'ni (CMD) yönetici olarak açın.
2.  Aşağıdaki kodu yapıştırın ve Enter tuşuna basın:
    ```bash
    powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
    ```
3.  **Denetim Masası > Donanım ve Ses > Güç Seçenekleri** menüsüne gidin ve yeni eklenen **Nihai Performans** planını seçin.

---

## Ekran ve Grafik Ayarlarının Optimize Edilmesi

### G-Sync, FreeSync ve V-Sync Senkronizasyonu

Dikey Senkronizasyon (V-Sync), ekran yırtılmalarını önler ancak çift veya üçlü arabelleğe alma (buffering) mekanizması nedeniyle sisteme ciddi düzeyde (30-50 ms arası) input lag ekler.

*   **En Düşük Gecikmeli Yapılandırma:**
    1.  Monitörünüzün **G-Sync** veya **FreeSync** özelliğini monitör arayüzünden ve GPU denetim masasından açın.
    2.  Oyun içi ayarlarda **V-Sync seçeneğini kapatın**.
    3.  NVIDIA Denetim Masası'nda genel ayarlardan **Dikey Senkronizasyon'u "Açık"** yapın.
    4.  Oyun içi kare hızını (FPS), monitörünüzün maksimum yenileme hızının (Hz) **3 FPS altına** sabitleyin (Örn: 144 Hz monitör için 141 FPS limitleyin). Bu kombinasyon, G-Sync'in aktif kalmasını sağlarken V-Sync'in gecikme yaratmasını engeller.

---

## Gelişmiş Gecikme Analizi: HPET ve MSI Mode

### HPET (High Precision Event Timer) Durumu

Yüksek Hassasiyetli Olay Zamanlayıcısı (HPET), eski sistemlerde zaman senkronizasyonu için kullanılırdı. Modern işlemcilerde ise doğrudan CPU üzerinde yer alan TSC (Time Stamp Counter) kullanılır. HPET'in açık kalması, işletim sisteminin sürekli olarak harici zamanlayıcıya sorgu göndermesine ve gecikmeye yol açar.

HPET'i Windows çekirdeğinde devre dışı bırakmak için:

1.  Komut İstemi'ni (CMD) yönetici olarak çalıştırın.
2.  Aşağıdaki komutu girerek HPET sorgularını devre dışı bırakın:
    ```bash
    bcdedit /set useplatformclock no
    ```
3.  Ardından dinamik tick özelliğini kapatarak kararlı bir zamanlama elde edin:
    ```bash
    bcdedit /set disabledynamictick yes
    ```
4.  Bilgisayarınızı yeniden başlatın.

### MSI (Message Signaled Interrupts) Modunu Etkinleştirme

Geleneksel donanım sürücüleri, hat tabanlı (Line-based) kesme (interrupt) sinyalleri kullanır. Bu durum, birden fazla donanımın aynı kesme hattını paylaşmasına ve işlemci kuyruğunda gecikmelere yol açar. Ekran kartınızı ve ağ bağdaştırıcınızı **MSI (Message Signaled Interrupts)** moduna geçirmek, kesme sinyallerinin doğrudan CPU'ya iletilmesini sağlayarak sistem kararlılığını ve tepkiselliğini artırır.

1.  Ücretsiz bir araç olan **MSI Utility v3** programını güvenilir bir kaynaktan indirin ve yönetici olarak çalıştırın.
2.  Listeden ekran kartınızı (GPU) bulun.
3.  Sağ taraftaki **MSI** kutucuğunun işaretli olduğundan emin olun.
4.  **Interrupt Priority** (Kesme Önceliği) kısmını ekran kartınız için **High** (Yüksek) olarak ayarlayın.
5.  Sağ üstteki **Apply** butonuna tıklayın ve sistemi yeniden başlatın.

---

## Windows 11 Gecikme Optimizasyon Özeti

| Yapılan Ayar | Etki Alanı | Beklenen Gecikme Azalması |
| :--- | :--- | :--- |
| **NVIDIA Reflex / Ultra Low Latency** | GPU Render Kuyruğu | Yüksek (10 - 25 ms) |
| **Bellek Bütünlüğünü Kapatma (VBS)** | CPU Çekirdek Gecikmesi | Orta (3 - 8 ms) |
| **1000+ Hz Polling Rate** | USB Giriş Gecikmesi | Yüksek (1 - 7 ms) |
| **HPET & Dynamic Tick Devre Dışı** | Sistem Zamanlayıcı Kararlılığı | Düşük (Mikro takılmalar önlenir) |
| **MSI Modu (GPU Önceliği)** | Donanım Kesme Gecikmesi | Orta (Sistem tepkiselliği artar) |

Bu optimizasyon adımları, Windows 11'in arka plan mimarisini saf performans moduna geçirerek donanımınızın gerçek potansiyelini ortaya çıkarır. Yapılan değişikliklerin ardından sistem kararlılığını test etmek için **LatencyMon** yazılımı ile DPC gecikmelerini analiz edebilirsiniz.