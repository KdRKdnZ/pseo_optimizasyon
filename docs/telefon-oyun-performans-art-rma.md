---
title: "telefon oyun performansı artırma"
description: "telefon oyun performansı artırma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Telefon Oyun Performansı Artırma Rehberi: FPS Yükseltme ve Donma Önleme Yöntemleri

Mobil cihazlarda yüksek grafikli oyunların (PUBG Mobile, Call of Duty: Mobile, Genshin Impact vb.) akıcı bir şekilde çalışması, doğrudan işlemci (CPU), grafik birimi (GPU), RAM mimarisi ve yazılımsal optimizasyonlara bağlıdır. Zamanla cihazlarda yaşanan kare hızı (FPS) düşüşleri ve ısınmaya bağlı takılmalar (thermal throttling), doğru teknik müdahalelerle minimize edilebilir.

Bu rehberde, Android ve iOS cihazlarda oyun performansını en üst seviyeye çıkarmak için uygulanması gereken teknik adımlar detaylandırılmıştır.

---

## 1. İşletim Sistemi ve Donanım Seviyesinde Optimizasyon

Oyun donmalarının ana sebebi, donanım kaynaklarının oyun dışı işlemler tarafından tüketilmesidir. Sistem kaynaklarını doğrudan oyuna yönlendirmek için aşağıdaki adımlar uygulanmalıdır.

### A. "Oyun Modu" (Game Turbo / Game Space) Kullanımı
Modern akıllı telefonlarda dahili olarak bulunan Oyun Modu yazılımları, arka plan süreçlerini dondurur ve işlemci çekirdeklerini maksimum frekansa kilitler.
* **Android:** Ayarlar > Özel Özellikler > Game Turbo / Game Space yolunu izleyerek oyunu bu listeye ekleyin.
* **iOS:** Ayarlar > Odak > Oyun Odak Modu'nu aktif edin. Bu işlem, oyun sırasındaki bildirimlerin ve arka plan senkronizasyonlarının CPU üzerindeki yükünü sıfırlar.

### B. Arka Plan Süreçlerinin ve RAM’in Temizlenmesi
Arka planda çalışan sosyal medya ve mesajlaşma uygulamaları, RAM'i işgal eder ve işlemciye döngüsel yük bindirir.
* Oyuna girmeden önce tüm açık uygulamaları kapatın.
* **RAM Uzantısı (Sanal RAM) Özelliğini Kapatın:** Birçok Android cihazda bulunan "Sanal RAM" (RAM Expansion), yavaş dahili depolama birimini (UFS) RAM gibi kullanır. Depolama biriminin okuma/yazma hızı, fiziksel LPDDR RAM kadar hızlı olmadığı için mikro takılmalara (stuttering) yol açabilir. Bu özelliği kapatmak performansı artırabilir.

### C. Termal Kıstlama (Thermal Throttling) ile Mücadele
Akıllı telefonlar, aşırı ısınan CPU ve GPU'yu korumak için çalışma frekansını düşürür. Bu durum ani FPS düşüşlerine (FPS Drop) neden olur.
* **Kılıfı Çıkarın:** Oyun oynarken kılıfı çıkararak ısı dağılımını kolaylaştırın.
* **Şarjda Oynamayın:** Cihaz şarj olurken bataryanın ısınması, işlemcinin erken ısınmasına ve frekans düşürmesine sebep olur.
* **Harici Soğutucu Kullanın:** Peltier soğutma teknolojisine sahip harici telefon fanları, termal kıstlamayı engelleyerek sabit FPS almanızı sağlar.

---

## 2. Gelişmiş Android Geliştirici Seçenekleri Ayarları

Android'in gizli geliştirici menüsü üzerinden grafik işlemci ayarlarını zorlayarak performans kazanımı elde edebilirsiniz.

> **Geliştirici Seçeneklerini Açmak İçin:** Ayarlar > Cihaz Hakkında > Yapım Numarası (Build Number) üzerine 7 kez üst üste dokunun.

* **Grafik Sürücüsü Tercihleri (Graphics Driver Preferences):**
  * Geliştirici Seçenekleri > Grafik Sürücüsü Tercihleri bölümüne gidin.
  * Oynadığınız oyunu bulun ve "Sistem Grafik Sürücüsü" (System Graphics Driver) olarak değiştirin. Bu işlem, varsayılan sürücü yerine güncel sistem GPU sürücüsünün kullanılmasını sağlar.
* **4x MSAA'yı Zorla (Force 4x MSAA):**
  * OpenGL ES 2.0 oyunlarında kenar yumuşatmayı donanımsal olarak zorlar. Grafik kalitesini artırır ancak GPU yükünü ve pil tüketimini artırabilir. Güçlü bir GPU'ya sahipseniz aktifleştirin, orta segment cihazlarda kapalı tutun.
* **Arka Plan İşlem Sınırı (Background Process Limit):**
  * Bu ayarı "En fazla 1 işlem" veya "En fazla 2 işlem" olarak sınırlandırarak arka plan yükünü tamamen kesebilirsiniz.

---

## 3. Depolama Teknolojisi ve Önbellek Temizliği

Depolama biriminin okuma/yazma hızı, oyun içi harita yüklemeleri (asset loading) ve kaplama (texture) işleme süreçlerini doğrudan etkiler.

* **Depolama Alanında En Az %20 Boş Yer Bırakın:** UFS depolama birimleri dolmaya yaklaştıkça okuma/yazma performansları düşer. Bu durum, oyunda harita yüklenirken anlık takılmalara yol açar.
* **Oyun Önbelleğini (Cache) Temizleyin:** 
  * *Ayarlar > Uygulamalar > [Oyun Adı] > Depolama > Önbelleği Temizle* adımlarını uygulayın. Hatalı tutulan önbellek dosyaları işleme süreçlerini yavaşlatır.

---

## 4. Oyun İçi Grafik Ayarlarının Optimize Edilmesi

Maksimum FPS ve düşük gecikme süresi için ideal grafik konfigürasyonu şu şekilde olmalıdır:

| Grafik Ayarı | Tavsiye Edilen Değer | Teknik Sebebi |
| :--- | :--- | :--- |
| **Grafik Kalitesi (Graphics)** | Düşük (Low) / Akıcı (Smooth) | GPU üzerindeki piksel işleme yükünü azaltır. |
| **Kare Hızı (Frame Rate)** | Aşırı (Extreme) / 90 FPS / 120 FPS | Cihazın desteklediği en yüksek değere ayarlanmalıdır. |
| **Gölgeler (Shadows)** | Kapalı (Off) | Gölgeler, GPU işleme gücünü en çok tüketen unsurdur. |
| **Stil / Renk Modu** | Klasik veya Renkli | Gerçekçi veya Sinematik modlar ekstra filtre işleme gerektirir. |
| **Anti-Aliasing (Kenar Yumuşatma)**| Kapalı / 2x | Doku kenarlarını yumuşatırken ekstra GPU belleği kullanır. |
| **Grafikleri Otomatik Ayarla** | Kapalı | Oyun içi ani grafik düşüşlerini ve dalgalanmalarını engeller. |

---

## 5. Ağ ve Ping Optimizasyonu (Online Oyunlar İçin)

Online oyunlardaki anlık takılmalar ve gecikmeler (lag) genellikle sistem performansıyla değil, ağ bant genişliği ve bağlantı kalitesiyle ilgilidir.

* **5 GHz Wi-Fi Bandına Geçin:** 2.4 GHz Wi-Fi bantları ev aletlerinden ve diğer ağlardan kolayca etkilenir. 5 GHz veya Wi-Fi 6 bağlantısı daha düşük paket kaybı (packet loss) ve jitter sunar.
* **DNS Sunucusunu Değiştirin:** Cloudflare (`1.1.1.1`) veya Google DNS (`8.8.8.8`) kullanarak alan adı çözümleme sürelerini kısaltın ve veri yönlendirmesini optimize edin.
* **Otomatik Güncellemeleri Kapatın:** Google Play Store veya App Store'un arka planda uygulama güncellemesini engelleyin.

---

## Özet Performans Kontrol Listesi

1. Oyuna girmeden önce **Oyun Modu**'nu başlatın.
2. Cihaz **şarjda değilken** ve **kılıfsız** oynayın.
3. Oyun içi ayarlardan **Grafikleri Düşük**, **Kare Hızını En Yüksek** seviyeye getirin.
4. Depolama alanının en az **%20'sinin boş** olduğundan emin olun.
5. Kullanılmayan arka plan uygulamalarını kapatın ve **Sanal RAM** özelliğini devreden çıkarın.