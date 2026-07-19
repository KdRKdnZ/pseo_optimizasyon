---
title: steam proton ayarları
description: steam proton ayarları hakkında detaylı optimizasyon ve donanım rehberi.
---

# Steam Proton Ayarları: Linux ve Steam Deck İçin Performans Rehberi

Steam Proton, Windows tabanlı oyunların Linux işletim sistemlerinde ve Steam Deck cihazlarında yüksek performansla çalışmasını sağlayan, Valve tarafından geliştirilmiş bir uyumluluk katmanıdır (compatibility layer). Temelinde Wine, DXVK (Direct3D 9/10/11'den Vulkan'a çeviri) ve VKD3D-Proton (Direct3D 12'den Vulkan'a çeviri) teknolojilerini barındırır. 

Bu rehberde, donanım kaynaklarınızı en verimli şekilde kullanmak ve oyunlardaki kare hızını (FPS) artırmak için uygulamanız gereken en gelişmiş **Steam Proton ayarları** ve başlatma seçeneklerini (launch options) inceleyeceğiz.

---

## Steam Proton Küresel Ayarları Nasıl Etkinleştirilir?

Steam üzerinde resmi olarak desteklenmeyen oyunlar da dahil olmak üzere tüm Windows kütüphanenizi Linux üzerinde çalıştırmak için öncelikle Proton'u küresel olarak etkinleştirmeniz gerekir.

1. Steam istemcisini açın ve sol üstteki **Steam > Ayarlar (Settings)** menüsüne gidin.
2. Sol panelden **Steam Play** (veya yeni arayüzde **Compatibility**) sekmesine tıklayın.
3. **"Enable Steam Play for all other titles"** (Diğer tüm oyunlar için Steam Play'i etkinleştir) seçeneğini işaretleyin.
4. **"Run titles with"** (Oyunları şununla çalıştır) açılır menüsünden en güncel kararlı Proton sürümünü (Örn: *Proton 8.0* veya *Proton Experimental*) seçin.
5. Değişikliklerin uygulanması için Steam'i yeniden başlatın.

---

## En İyi Performans İçin Steam Proton Başlatma Seçenekleri

Proton, oyun bazında optimize edilebilen dinamik çevre değişkenleri (environment variables) ile çalışır. Bir oyunun performansını artırmak, takılmaları (stuttering) önlemek veya uyumluluk sorunlarını çözmek için oyun özelliklerindeki **Başlatma Seçenekleri (Launch Options)** kısmına aşağıdaki parametreleri ekleyebilirsiniz.

Bir başlatma seçeneği eklemek için: Steam kütüphanenizde oyuna sağ tıklayın, **Özellikler > Genel** sekmesine gelin ve en alttaki **Başlatma Seçenekleri** kutusuna kodları girin. Kodların sonuna `%command%` eklemeyi unutmayın.

### 1. CPU ve İş Parçacığı (Thread) Optimizasyonları

Modern çok çekirdekli işlemcilerin gücünden tam olarak yararlanmak ve senkronizasyon darboğazlarını önlemek için şu parametreleri kullanın:

*   **Esync ve Fsync Etkinleştirme:**
    Linux çekirdeğinin (kernel) eventfd (Esync) veya futex (Fsync) senkronizasyon mekanizmalarını kullanmasını sağlar. Bu, CPU yükünü azaltır ve FPS'i artırır. Modern Linux dağıtımlarında ve SteamOS'te Fsync varsayılan olarak desteklenir.
    ```bash
    PROTON_USE_FSYNC=1 %command%
    ```
    *Eğer sisteminiz Fsync desteklemiyorsa Esync kullanabilirsiniz:*
    ```bash
    PROTON_USE_ESYNC=1 %command%
    ```

### 2. Grafik ve Vulkan (DXVK / VKD3D) Optimizasyonları

DirectX çağrılarını Vulkan'a dönüştürürken gölgelendirici (shader) derleme aşamasında yaşanan takılmaları önlemek için bu ayarlar kritiktir.

*   **GPL (Graphics Pipeline Library) Etkinleştirme:**
    NVIDIA (sürücü 520+) ve AMD (Mesa 23+) kartlarda gölgelendirici derleme takılmalarını (shader compilation stutter) neredeyse tamamen ortadan kaldırır.
    ```bash
    RADV_PERFTEST=gpl %command%  # Sadece AMD ekran kartları için
    ```
*   **Vulkan Gölgelendirici Önbelleği (Shader Cache) Sınırlandırma:**
    Disk yazma hızından kaynaklı anlık takılmaları önlemek için DXVK önbelleğini optimize edin:
    ```bash
    dxvk.enableGraphicsPipelineLibrary = True
    ```

### 3. Donanım Üreticisine Özel Başlatma Seçenekleri

#### NVIDIA Ekran Kartları İçin:
NVIDIA sürücülerinin iş parçacığı optimizasyonunu zorlamak için:
```bash
__GL_THREADED_OPTIMIZATIONS=1 %command%
```

#### AMD Ekran Kartları İçin:
AMD'nin açık kaynaklı Vulkan sürücüsü olan RADV'yi etkinleştirmek ve yüksek performans moduna almak için:
```bash
AMD_VULKAN_DIRTY_TRACKING_PAGE_SIZE=1 %command%
```

### 4. Feral GameMode Entegrasyonu
Sistem kaynaklarını (CPU valisi, I/O önceliği, GPU saat hızları) oyun moduna geçirmek için Feral GameMode aracını başlatma seçeneklerine ekleyin (Sisteminizde `gamemode` paketinin kurulu olması gerekir):
```bash
gamemoderun %command%
```

---

## Proton GE (GloriousEggroll) Kurulumu ve Kullanımı

Resmi Proton sürümlerinin lisans kısıtlamaları nedeniyle içeremediği bazı video kodekleri (Media Foundation) ve uç nokta optimizasyonları, topluluk yapımı **Proton GE (GloriousEggroll)** sürümünde mevcuttur. Özellikle oyun içi videoların oynatılamadığı veya ses sorunlarının yaşandığı oyunlarda Proton GE kullanımı şarttır.

### Proton GE Nasıl Kurulur?

1. Masaüstü moduna geçin (Steam Deck için güç menüsünden "Switch to Desktop" seçeneğini kullanın).
2. **Discover Software Center** (Yazılım Merkezi) uygulamasını açın.
3. Arama çubuğuna **ProtonUp-Qt** yazın ve uygulamayı yükleyin.
4. ProtonUp-Qt uygulamasını çalıştırın.
5. **"Add version"** (Sürüm ekle) butonuna tıklayın.
6. Compatibility tool olarak **Proton-GE**'yi seçin ve en güncel sürümü indirip yükleyin.
7. Steam'i yeniden başlatın.
8. Sorun yaşadığınız oyuna sağ tıklayıp **Özellikler > Uyumluluk** sekmesinden yeni yüklediğiniz **Proton-GE** sürümünü seçin.

---

## Donanım Tabanlı Proton Optimizasyonları

### Steam Deck Özel Ayarları
Steam Deck donanımı sınırlı güç bütçesine (TDP) sahip olduğundan, Proton ayarlarıyla donanım yükünü dengelemek pil ömrünü ve akıcılığı doğrudan etkiler.

*   **FSR (FidelityFX Super Resolution) Aktivasyonu:**
    Oyun içi çözünürlüğü 1280x800 pikselin altına (Örn: 960x600) düşürün. Steam Deck hızlı erişim menüsünden (üç nokta butonu) Performans sekmesine gelin ve **Scaling Filter** ayarını **FSR** olarak seçin. Bu işlem, Proton'un oyunu yapay zeka destekli keskinleştirme ile ekrana sığdırmasını sağlayarak GPU yükünü azaltır.
*   **Kare Hızı ve Yenileme Hızı Kilitleme:**
    Ekran yenileme hızını 40Hz'e, kare hızını da 40 FPS'e sabitlemek, 60 FPS'e kıyasla %30'a varan pil tasarrufu sağlar ve kare üretim sürekliliğini (frame pacing) optimize eder.

---

## Sık Karşılaşılan Proton Hataları ve Çözümleri

### 1. Oyun Hiç Başlamıyor veya Siyah Ekranda Kalıyor
Bu durum genellikle DirectX 12 veya video kodek uyumsuzluğundan kaynaklanır.
*   **Çözüm:** Başlatma seçeneklerine `PROTON_USE_WINED3D=1 %command%` yazarak Vulkan çevirisini devre dışı bırakıp eski OpenGL tabanlı WineD3D sürücüsünü zorlayabilirsiniz (Not: Performans düşebilir). Alternatif olarak oyunu **Proton GE** ile çalıştırmayı deneyin.

### 2. Bozuk Proton "Prefix" Dosyalarını Temizleme
Oyun güncellemelerinden sonra Proton yapılandırma klasörü (Prefix) bozulabilir.
*   **Çözüm:** Steam kütüphanesinde oyuna sağ tıklayın, **Yönet > Yerel dosyalara göz at** seçeneği ile oyunun kurulu olduğu dizini kontrol edin. Ardından, oyunun kimlik numarasını (AppID) `steamapps/compatdata/[AppID]` dizininden bulun ve bu klasörü silin. Steam, oyunu bir sonraki başlatışınızda temiz bir Proton Prefix'i oluşturacaktır.