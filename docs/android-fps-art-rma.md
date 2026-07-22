---
title: "android fps artırma"
description: "android fps artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Android FPS Artırma: Donanım ve Yazılım Odaklı Teknik Rehber

Android cihazlarda oyunlarda alınan saniye başına kare sayısı (FPS), işlemci (CPU), grafik işlemci (GPU), bellek (RAM) mimarisi ve yazılımsal optimizasyonların doğrudan bir bileşenidir. Düşük FPS ve anlık takılmalar (micro-stuttering); termal kısıtlama (thermal throttling), yetersiz GPU işleme veya arka plan kaynak tüketiminden kaynaklanır. 

Aşağıdaki adımlar, Android işletim sisteminde donanım performansını maksimuma çıkarmak ve FPS değerlerini stabilize etmek için uygulanan teknik yöntemleri içermektedir.

---

## 1. Geliştirici Seçenekleri Üzerinden Sistem Optimizasyonu

Android’in gizli geliştirici menüsü, GPU işleme süreçlerini doğrudan kontrol etmenizi sağlar.

*   **Geliştirici Seçeneklerini Aktifleştirin:** `Ayarlar > Telefon Hakkında > Yapım Numarası (Build Number)` kısmına 7 kez üst üste dokunun.
*   **Donanım Katmanlarını Devre Dışı Bırakın (Disable HW Overlays):** Bu seçeneği açık konuma getirin. Normal şartlarda ekran bileşimi için CPU ve GPU ortak çalışır. Bu ayar açıldığında, ekran katmanlama işlemleri doğrudan GPU’ya aktarılır ve CPU üzerindeki yük azaltılarak oyunlara daha fazla işlem gücü ayrılır.
*   **Oyun Sürücüsü Tercihi (Game Driver Preference):** Android 10 ve üzerinde bulunan bu ayarda, oynadığınız oyunu bulun ve varsayılan yerine **"Sistem Grafik Sürücüsü" (System Graphics Driver)** olarak değiştirin. Bu, oyunun doğrudan güncel GPU sürücüsünü kullanmasını sağlar.
*   **Arka Plan İşlem Sınırı:** `Ayarlar > Geliştirici Seçenekleri > Arka Plan İşlem Sınırı` sekmesinden değeri **"En fazla 2 işlem"** olarak ayarlayarak CPU'nun oyun haricindeki iş parçacıklarına (threads) kaynak ayırmasını engelleyin.

---

## 2. Sanal RAM (Sanal Bellek Genişletme) Özelliğini Kapatın

Son yıllarda Xiaomi, Samsung ve Oppo gibi üreticilerin sunduğu "RAM Genişletme / RAM Plus" özelliği, dahili depolama alanının (UFS) bir kısmını SWAP belleği olarak kullanır. 

UFS depolama birimleri (UFS 2.2, 3.1 veya 4.0 bile olsa), fiziksel LPDDR RAM modüllerinden çok daha yavaştır. Oyun sırasında sistem sanal RAM’den veri okumaya çalıştığında I/O (Giriş/Çıkış) darboğazı yaşanır ve bu durum **ani FPS düşüşlerine (FPS drop)** sebep olur.

*   **Çözüm:** `Ayarlar > Bellek / RAM` sekmesine gidin ve Sanal RAM / RAM Plus özelliğini **tamamen kapatıp** cihazı yeniden başlatın.

---

## 3. Termal Kısma (Thermal Throttling) İle Mücadele

Android cihazlar, SoC (System on Chip) sıcaklığı güvenli sınırı (genellikle 40-45°C) aştığında frekans düşürür (Underclocking). Bu durum doğrudan FPS'in yarı yarıya düşmesine yol açar.

*   **Kılıf Kullanımı:** Yüksek grafikli oyunlar oynarken cihazın ısı dağıtımını engelleyen silikon veya deri kılıfları çıkarın.
*   **Harici Soğutucu Kullanımı:** Peltier tabanlı harici telefon soğutucuları, SoC sıcaklığını 10-15°C düşürerek CPU ve GPU'nun maksimum çekirdek frekanslarında (Boost Clock) uzun süre kalmasını sağlar.
*   **Şarjda Oyun Oynamayın:** Şarj işlemi sırasında pilin ısınması, chipset ısı sınırını hızla aşarak cihazın termal kısıtlamaya girmesine neden olur.

---

## 4. Ekran Yenileme Hızı ve Grafik API Seçimi

FPS performansının ekrana doğru yansıması ve grafik işleme verimliliği için şu ayarlar yapılmalıdır:

### Ekran Yenileme Hızı (Refresh Rate)
`Ayarlar > Ekran > Yenileme Hızı` sekmesinden ekranı **120 Hz** veya **90 Hz** sabitleyin. Bazı cihazlarda bulunan "Dinamik/Adaptif" modlar, oyun sırasında frekansı 60 Hz'e düşürebilir.

### Vulkan API Kullanımı
Oyun içi grafik ayarlarında OpenGL ES yerine **Vulkan** API seçeneği varsa bunu tercih edin. Vulkan, CPU üzerindeki sürücü yükünü (overhead) azaltarak çok çekirdekli işlemcilerde daha yüksek ve kararlı FPS sunar.

---

## 5. Üreticiye Özel Oyun Modlarının Yapılandırılması

Çoğu Android üreticisi donanım seviyesinde kaynak tahsisi yapan yazılımlara sahiptir:

*   **Samsung (Game Booster & Game Plugins):** Galaxy Store üzerinden *Game Plugins* ve onun altındaki *Perf Z* ile *Game Booster Plus* modüllerini indirin. Buradan oyun profillerini "Maksimum Performans" konumuna getirin.
*   **Xiaomi / Poco (Game Turbo):** Game Turbo içerisinden "Performans Modu"nu açın, Wi-Fi optimizasyonu ve dokunma yanıt hızını artırın.
*   **Performans Modu:** Cihazın genel pil ayarlarından "Güç Tasarrufu" veya "Dengeli" mod yerine **"Performans Modu"**nu seçin.

---

## 6. İleri Düzey (Root Gerektiren) FPS Optimizasyonları

Root yetkisi bulunan cihazlarda kernel seviyesinde müdahalelerle performans artırılabilir:

*   **Custom Kernel ve Overclock:** FrancoKernel veya ElementalX gibi özel çekirdekler yüklenerek CPU/GPU frekans sınırları artırılabilir ve thermal throttling limitleri esnetilebilir.
*   **LKT / FDE.AI Magisk Modülleri:** Yapay zeka tabanlı bu modüller, arka plan servislerini tamamen dondurarak RAM ve CPU kaynaklarını %100 oranında ön plandaki oyuna tahsis eder.
*   **Thermal Config Düzenleme:** `/system/vendor/etc/thermal-engine.conf` dosyasındaki sıcaklık limitleri değiştirilerek işlemcinin ısındığında frekans düşürmesi engellenebilir (Harici soğutma ile kullanılması önerilir).

---

## Teknik Özet ve Kontrol Listesi

| Parametre | İdeal Ayar | Etkisi |
| :--- | :--- | :--- |
| **HW Katmanları** | Devre Dışı (Disabled) | Ekran yükünü GPU'ya vererek CPU'yu rahatlatır. |
| **Sanal RAM (RAM Plus)** | Kapalı (Off) | I/O darboğazını önler, anlık takılmaları keser. |
| **Grafik API** | Vulkan | İşlemci yükünü azaltır, FPS kararlılığı sağlar. |
| **Pil Modu** | Performans Modu | SoC çekirdeklerinin düşük frekansa geçmesini önler. |
| **Sıcaklık Yönetimi** | < 40°C (Harici Soğutma) | Thermal Throttling engelleyip sabit FPS sağlar. |