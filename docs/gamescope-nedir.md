---
title: gamescope nedir
description: gamescope nedir hakkında detaylı optimizasyon ve donanım rehberi.
---

# Gamescope Nedir? Linux ve Steam Deck İçin Mikro-Kompozitör Rehberi

**Gamescope**, Valve tarafından özellikle Linux işletim sistemi ve Steam Deck donanımı için geliştirilmiş, açık kaynaklı bir **Wayland mikro-kompozitörüdür (micro-compositor)**. Eski adı `steamcompmgr` olan bu araç, oyunların işletim sisteminin genel masaüstü pencere yöneticisinden (X11 veya standart Wayland) izole edilerek, optimize edilmiş özel bir sanal katmanda çalıştırılmasını sağlar.

Temel amacı; oyunların ekran çözünürlüğünü, yenileme hızını (Hz), kare hızını (FPS) ve ölçekleme algoritmalarını doğrudan donanım seviyesinde kontrol ederek girdi gecikmesini (input lag) minimuma indirmek ve performansı maksimuma çıkarmaktır.

---

## Gamescope'un Çalışma Prensibi ve Mimarisi

Geleneksel Linux masaüstü ortamlarında (GNOME veya KDE gibi), bir oyun çalıştırıldığında görüntünün ekrana ulaşması için X11/Wayland sunucusu, pencere yöneticisi ve kompozitör (KWin, Mutter vb.) gibi birçok katmandan geçmesi gerekir. Bu durum gecikmeye ve yırtılmalara (tearing) yol açabilir.

Gamescope, oyunu kendi içinde izole bir "kum havuzunda" (sandbox) çalıştırarak bu zinciri kırar.

### Wayland ve XWayland Entegrasyonu
Gamescope, kendisi bir Wayland kompozitörü olmasına rağmen, X11 protokolünü kullanan eski oyunları desteklemek için arka planda **XWayland** çalıştırır. Oyun, kendisini standart bir X11 ekranında sanır; ancak Gamescope bu görüntüyü yakalar, Vulkan API'sini kullanarak işler ve doğrudan ekrana (Direct Rendering Manager - DRM/KMS aracılığıyla) aktarır.

### Donanım Hızlandırmalı Ölçekleme (Hardware-Accelerated Scaling)
Gamescope, oyunun render çözünürlüğü (örneğin 720p) ile ekranın fiziksel çözünürlüğü (örneğin 1080p veya 4K) arasındaki köprüyü donanım hızlandırmalı olarak kurar. Görüntüyü ölçeklemek için CPU yerine doğrudan GPU'nun asenkron hesaplama kuyruklarını (async compute queues) kullanır. Bu sayede ana oyun motoruna ek yük bindirilmez.

---

## Gamescope'un Temel Özellikleri ve Avantajları

Gamescope, modern bir oyun deneyimi için kritik öneme sahip birçok teknik özelliği bünyesinde barındırır:

### Düşük Girdi Gecikmesi (Input Lag Reduction)
Gamescope, masaüstü ortamının getirdiği çift veya üçlü arabelleğe alma (double/triple buffering) zorunluluklarını baypas eder. **KMS (Kernel Mode Setting)** doğrudan entegrasyonu sayesinde, üretilen kareler doğrudan ekran kartının önbelleğinden monitöre gönderilir. Bu, rekabetçi oyunlarda milisaniyeler mertebesinde avantaj sağlar.

### AMD FSR (FidelityFX Super Resolution) ve Tam Ekran Ölçekleme
Gamescope, sistem genelinde **AMD FSR 1.0** ve **NVIDIA Image Scaling (NIS)** desteği sunar. Oyunun kendisinde FSR desteği olmasa bile, Gamescope aracılığıyla oyun düşük çözünürlükte çalıştırılıp yapay zeka destekli algoritmalarla yüksek çözünürlüğe net bir şekilde ölçeklenebilir. Ayrıca tamsayı ölçekleme (integer scaling) ve piksel sanatı (pixel art) oyunlar için en yakın komşu (nearest-neighbor) filtreleme seçenekleri mevcuttur.

### HDR ve Değişken Yenileme Hızı (VRR) Desteği
Linux ekosisteminde HDR (High Dynamic Range) desteğinin öncüsü Gamescope'tur. HDR10 meta verilerini doğrudan monitöre iletebilir. Aynı zamanda **G-Sync** ve **FreeSync** gibi Değişken Yenileme Hızı (VRR) teknolojilerini yerel olarak destekleyerek yırtılmasız ve akıcı bir görüntü sunar.

---

## Gamescope Nasıl Kullanılır? (Parametreler ve Komutlar)

Gamescope, terminal üzerinden veya Steam başlatma seçenekleri aracılığıyla parametrelerle yönetilir. 

### Temel Çalıştırma Komutları
Bir oyunu Gamescope ile başlatmak için terminalde şu sözdizimi kullanılır:

```bash
gamescope [seçenekler] -- [oyun_başlatma_komutu]
```

Sık kullanılan teknik parametreler şunlardır:

*   `-w`: Oyunun render edileceği genişlik (çözünürlük).
*   `-h`: Oyunun render edileceği yükseklik.
*   `-W`: Ekranın fiziksel genişliği (çıktı çözünürlüğü).
*   `-H`: Ekranın fiziksel yüksekliği.
*   `-r`: Hedef yenileme hızı (FPS/Hz sınırı).
*   `-F`: Ölçekleme yöntemi (örneğin `fsr` veya `nis`).
*   `-e`: Steam entegrasyonunu etkinleştirir (Steam Overlay desteği).

### Steam Başlatma Seçenekleri (Launch Options) Ayarı
Steam kütüphanenizdeki bir oyunu Gamescope ile optimize etmek için, oyunun özelliklerine girip **Başlatma Seçenekleri** kısmına aşağıdaki gibi bir komut ekleyebilirsiniz:

```text
gamescope -w 1280 -h 720 -W 1920 -H 1080 -f -F fsr -- %command%
```

*Bu komut; oyunu dahili olarak 720p çözünürlükte çalıştırır, AMD FSR kullanarak 1080p çözünürlüğe ölçekler ve tam ekran (`-f`) modunda başlatır.*

---

## Sonuç: Gamescope Neden Oyun Dünyasını Değiştiriyor?

Gamescope, Linux tabanlı oyunculuğun Windows karşısındaki en büyük kozlarından biridir. Valve'ın Steam Deck'te yakaladığı konsol benzeri stabilite ve performansın arkasındaki gizli kahraman Gamescope'tur. 

Gelişmiş pencere yönetimi, donanım seviyesinde FSR entegrasyonu, HDR desteği ve ultra düşük gecikme süresi ile Gamescope, yalnızca el konsollarının değil, modern Linux oyuncularının da vazgeçilmez bir optimizasyon aracıdır.