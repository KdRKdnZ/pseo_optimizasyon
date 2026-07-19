---
title: android fps artırma
description: android fps artırma hakkında detaylı optimizasyon ve donanım rehberi.
---

# Android FPS Artırma: Donanım ve Yazılım Tabanlı Performans Optimizasyonu Rehberi

Android işletim sisteminde saniye başına düşen kare sayısı (FPS - Frames Per Second), doğrudan CPU/GPU mimarisi, termal yönetim (thermal throttling) ve yazılımsal renderlama boru hattının (rendering pipeline) verimliliğine bağlıdır. Bu teknik rehberde, Android cihazlarda oyun ve arayüz performansını maksimuma çıkarmak için uygulayabileceğiniz donanım ve yazılım seviyesindeki optimizasyon yöntemlerini inceleyeceğiz.

---

## Android Grafik İşleme Mimarisi ve FPS İlişkisi

Android'de bir görüntünün ekrana çizilmesi süreci **Choreographer**, **SurfaceFlinger** ve **Hardware Composer (HWC)** bileşenleri tarafından yönetilir. Sistem, her 16.6 milisaniyede bir (60 Hz ekranlar için) yeni bir kare üretmek zorundadır. Bu sürenin aşılması, "jank" adı verilen kare düşmelerine ve dolayısıyla düşük FPS hissiyatına neden olur.

FPS düşüşlerinin temel nedenleri şunlardır:
*   **CPU Darboğazı (Bottleneck):** Oyun içi fizik motoru ve yapay zeka hesaplamalarının tek bir çekirdeğe yüklenmesi.
*   **GPU Sınırları:** Piksel doldurma oranının (pixel fill rate) ve gölgelendirici (shader) hesaplamalarının yetersiz kalması.
*   **Termal Kısıtlama (Thermal Throttling):** SoC (System on Chip) sıcaklığının kritik eşiğe ulaşması sonucu DVFS (Dynamic Voltage and Frequency Scaling) protokolünün saat hızlarını düşürmesi.

---

## Geliştirici Seçenekleri ile Android FPS Artırma

Android'in çekirdek ayarlarında yapılacak değişiklikler, grafik işlemci üzerindeki yükü hafifleterek doğrudan FPS artışı sağlar. Bu ayarlara erişmek için **Ayarlar > Telefon Hakkında > Derleme Numarası** seçeneğine 7 kez dokunarak "Geliştirici Seçenekleri"ni aktif etmeniz gerekir.

### HW Bindirmelerini Devre Dışı Bırak (Disable HW Overlays)
Ekran kompozisyonu (ekrandaki farklı katmanların birleştirilmesi) varsayılan olarak CPU ve GPU arasında paylaştırılır. **"HW bindirmelerini devre dışı bırak"** seçeneği aktif edildiğinde, ekran kompozisyonu tamamen GPU'ya devredilir. 
*   **Etkisi:** CPU üzerindeki yükü azaltır, arayüz geçişlerini ve oyun içi FPS kararlılığını artırır.
*   **Dezavantajı:** GPU sürekli aktif olduğu için güç tüketimi (pil kullanımı) bir miktar artabilir.

### Grafik Sürücüsü Tercihleri (Graphics Driver Preferences)
Android 10 ve üzeri sürümlerde, her uygulama için kullanılacak grafik sürücüsü manuel olarak seçilebilir.
*   **Optimizasyon:** Oynadığınız oyunu listeden bulun ve "Varsayılan" yerine **"Sistem Grafik Sürücüsü" (System Graphics Driver)** olarak ayarlayın. Bu, oyunun donanım üreticisinin (Qualcomm, MediaTek) en güncel API optimizasyonlarını doğrudan kullanmasını sağlar.

### Pencere ve Geçiş Animasyon Ölçekleri
Sistem arayüzünün render edilme süresini kısaltmak için animasyon sürelerini optimize edin:
*   **Pencere animasyon ölçeği:** 0.5x (veya Kapalı)
*   **Geçiş animasyonu ölçeği:** 0.5x (veya Kapalı)
*   **Animatör süre ölçeği:** 0.5x (veya Kapalı)
Bu ayar doğrudan oyun içi FPS'i artırmasa da, arayüz gecikmesini (input lag) azaltarak cihazın tepki süresini optimize eder.

---

## İşletim Sistemi ve Çekirdek (Kernel) Seviyesinde Optimizasyonlar

Yazılım katmanında arka plan süreçlerinin yönetilmesi, CPU döngülerinin tamamen oyuna ayrılmasını sağlar.

### Game Mode API ve Game Dashboard Kullanımı
Modern Android sürümlerinde (Android 12+) yerleşik olarak bulunan Game Mode API, oyunların sistem kaynaklarına erişim önceliğini belirler.
*   **Performans Modu:** CPU ve GPU saat hızlarını maksimum frekansta kilitler, arka plan ağ trafiğini kısıtlar ve bildirimlerin oluşturduğu kesme (interrupt) isteklerini engeller.

### Arka Plan İşlem Sınırı ve RAM Yönetimi
LPDDR bellek üzerindeki yükü azaltmak, oyun içi kaplamaların (textures) belleğe daha hızlı yüklenmesini sağlar.
*   Geliştirici seçeneklerinden **"Arka plan işlem sınırı"** ayarını "En çok 2 işlem" olarak sınırlayın.
*   **RAM Plus / Sanal RAM Özelliğini Kapatın:** Depolama birimini (UFS) RAM gibi kullanan bu teknoloji, UFS'in okuma/yazma hızları fiziksel RAM'e göre çok yavaş olduğu için oyunlarda anlık takılmalara (stuttering) yol açar. **Android FPS artırma** sürecinde sanal RAM'in kapatılması kararlılığı artırır.

---

## İleri Düzey ve Root Gerektiren FPS Artırma Yöntemleri

Cihazınızda Root (Magisk) yetkisi veya ADB (Android Debug Bridge) erişimi varsa, donanım limitlerini zorlayacak derin optimizasyonlar yapabilirsiniz.

### ADB ile Çözünürlük ve DPI Değiştirme
GPU üzerindeki piksel yükünü azaltmanın en etkili yolu render çözünürlüğünü düşürmektir. 1080p (FHD) bir ekranı 720p (HD) çözünürlüğe çekmek, GPU'nun işlemesi gereken piksel sayısını %50'den fazla azaltır.

Bilgisayarınızdan ADB terminalini açın ve şu komutları uygulayın:
```bash
# Çözünürlüğü 720p seviyesine düşürme
adb shell wm size 720x1600

# Yoğunluğu (DPI) çözünürlüğe uygun olarak ayarlama
adb shell wm density 280
```
*Not: Orijinal ayarlara dönmek için `adb shell wm size reset` ve `adb shell wm density reset` komutlarını kullanabilirsiniz.*

### Vulkan API Kullanımını Zorlama
OpenGL ES yerine modern **Vulkan API** kullanımı, CPU yükünü (overhead) azaltarak çoklu çekirdek performansını optimize eder. Root yetkisine sahip cihazlarda `build.prop` dosyasına aşağıdaki satırlar eklenerek Vulkan renderlama motoru zorlanabilir:

```properties
debug.hwui.renderer=skiavk
debug.renderengine.backend=vulkan
```

---

## Termal Yönetim ve Donanım Sınırlamalarını Aşma

En güçlü mobil işlemci bile termal limitlere ulaştığında performansını düşürmek zorundadır. Donanım uzmanı gözüyle termal yönetimi optimize etmek için şu adımları izleyin:

### Termal Kısıtlama (Thermal Throttling) Mekanizması
Android cihazlar, batarya ve SoC sıcaklığı 45°C üzerine çıktığında frekans düşürür. Bunu engellemek için:
*   **Harici Soğutma:** Peltier teknolojisine sahip yarı iletken telefon soğutucuları kullanın. Bu cihazlar SoC sıcaklığını aktif olarak 15-20°C düşürerek cihazın sürekli maksimum frekansta (sustained performance) çalışmasını sağlar.
*   **Şarj Esnasında Oyun Oynamama:** Şarj entegresi (PMIC) şarj sırasında yüksek ısı üretir. Bu ısı, SoC ısısıyla birleştiğinde termal kısıtlamayı kaçınılmaz kılar.

---

## Android FPS Artırma Yöntemleri Karşılaştırma Tablosu

| Yöntem | Performans Etkisi | Güç Tüketimi (Pil) | Risk Seviyesi |
| :--- | :--- | :--- | :--- |
| **HW Bindirmelerini Kapatma** | Orta (%5 - %10) | Hafif Artış | Çok Düşük |
| **Sanal RAM (RAM Plus) Kapatma** | Yüksek (Anlık takılmaları önler) | Değişmez | Çok Düşük |
| **ADB ile Çözünürlük Düşürme** | Çok Yüksek (%20 - %40) | Azalır (Pil tasarrufu sağlar) | Orta |
| **Vulkan API Zorlaması (Root)** | Yüksek (%15 - %25) | Optimize Olur | Yüksek |
| **Harici Peltier Soğutucu Kullanımı**| En Yüksek (Sürekli kararlı FPS) | Değişmez | Yok |