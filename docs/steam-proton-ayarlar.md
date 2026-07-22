---
title: "steam proton ayarları"
description: "steam proton ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Steam Proton Ayarları: Linux ve Steam Deck Oyun Performansı Rehberi

Steam Proton, Valve tarafından geliştirilen ve Windows tabanlı oyunların Linux dağıtımlarında ve Steam Deck üzerinde yüksek performansla çalışmasını sağlayan Wine tabanlı bir uyumluluk katmanıdır (compatibility layer). DirectX komutlarını Vulkan API'sine dönüştürerek neredeyse sıfıra yakın performans kaybı ile oyun oynamayı mümkün kılar.

Bu rehberde, Steam Proton optimize ayarlarını, başlatma parametrelerini (launch options), Proton-GE kurulumunu ve performans artırma tekniklerini teknik ayrıntılarıyla inceleyeceğiz.

---

## 1. Global (Genel) Steam Proton Ayarlarını Etkinleştirme

Steam üzerinde resmi desteği olmayan oyunlar da dahil olmak üzere tüm Windows kütüphanesini Linux üzerinde çalıştırmak için global Proton ayarının yapılması gerekir.

1. **Steam** istemcisini açın.
2. Sol üst menüden **Steam > Ayarlar (Settings)** yolunu izleyin.
3. Sol panelden **Uyumluluk (Compatibility)** sekmesine gelin.
4. **"Desteklenen içerikler için Steam Play'i etkinleştir"** seçeneğini aktif edin.
5. **"Diğer tüm içerikler için Steam Play'i etkinleştir"** seçeneğini işaretleyin.
6. **"Çalıştır:"** açılır menüsünden en güncel kararlı Proton sürümünü (örneğin *Proton 9.0* veya *Proton Experimental*) seçin.
7. İstemciyi yeniden başlatın.

---

## 2. Oyuna Özel Proton Sürümü Tanımlama

Her oyun tüm Proton sürümleriyle aynı kararlılıkta çalışmaz. Belirli bir oyuna özel Proton sürümü atamak için:

1. Kütüphanenizdeki oyuna sağ tıklayıp **Özellikler (Properties)** seçeneğine tıklayın.
2. **Uyumluluk (Compatibility)** sekmesine geçin.
3. **"Belirli bir Steam Play uyumluluk aracının kullanımını zorla"** kutucuğunu işaretleyin.
4. Alt kısımdaki listeden ilgili oyun için en uygun olan Proton sürümünü seçin.

---

## 3. Proton Sürümleri ve Teknik Farkları

| Proton Sürümü | Kullanım Amacı | Avantajları |
| :--- | :--- | :--- |
| **Proton Stable (örn. 8.0/9.0)** | Genel oyun kullanımı | Valve tarafından yoğun testlerden geçmiş, en kararlı sürümdür. |
| **Proton Experimental** | Yeni çıkan ve sorunlu oyunlar | En son DXVK, VKD3D ve Wine güncellemelerini içerir. Hızlı yama alır. |
| **Proton Hotfix** | Belirli oyun güncellemeleri | Oyun güncellemeleri sonrası oluşan anlık kırılmaları düzeltmek için Valve tarafından yayınlanır. |
| **Proton GE (GloriousEggroll)** | Özel video kodlayıcıları ve performans | Valve'ın telif hakları nedeniyle ekleyemediği h264/AAC gibi medya kodlayıcılarını (cutscene/sinematikler için) ve özel oyun yamalarını içerir. |

---

## 4. Performans ve Hata Ayıklama İçin Başlatma Seçenekleri (Launch Options)

Oyun performansını artırmak, grafik sürücüsü çakışmalarını çözmek veya shader kasılmalarını (stuttering) engellemek için oyuna özel başlatma komutları kullanılır.

Bu ayarları uygulamak için: **Oyun Özellikleri > Genel > Başlatma Seçenekleri** kutusuna aşağıdaki kod dizilimlerini ekleyebilirsiniz.

### Temel Komut Yapısı
Tüm komutlar, parametrenin sonuna `%command%` eklenerek yazılmalıdır.

### Önemli Başlatma Parametreleri:

*   **GameMode Etkinleştirme (CPU/GPU Önceliği):**
    Feral GameMode entegrasyonu ile işlemci ölçeklemesini performans moduna alır.
    ```bash
    gamemoderun %command%
    ```

*   **DXVK Async Shader Derleme (Takılmaları Önleme):**
    Shader derleme kaynaklı takılmaları (stutter) en aza indirir. *(Not: Bazı online oyunlarda anti-cheat uyarısı verebilir)*
    ```bash
    RADV_PERFTEST=gpa,nggc DXVK_ASYNC=1 %command%
    ```

*   **DirectX 11'den Vulkan'a Geçişi Zorlama (DXVK):**
    Eski kartlarda veya performans sorunlarında DirectX yerine Vulkan katmanını zorlar.
    ```bash
    PROTON_USE_WINED3D=1 %command%
    ```

*   **DirectX 12 Ray Tracing Desteğini Açma (VKD3D):**
    NVIDIA veya AMD kartlarda Linux üzerinde Işın İzleme teknolojisini aktif eder.
    ```bash
    VKD3D_CONFIG=dxr VKD3D_FEATURE_LEVEL=12_1 %command%
    ```

*   **FPS Limitini Mantıksal Olarak Sınırlandırma:**
    Gpu yükünü azaltmak ve gecikmeyi önlemek için DXVK seviyesinde FPS kilitler.
    ```bash
    DXVK_FRAME_RATE=60 %command%
    ```

*   **Proton Hata Günlüğü (Log) Oluşturma:**
    Açılmayan oyunların hatasını tespit etmek için kullanıcı dizininde `steam-APPID.log` dosyası oluşturur.
    ```bash
    PROTON_LOG=1 %command%
    ```

*   **Birden Fazla Parametreyi Birlikte Kullanma Örneği:**
    ```bash
    gamemoderun MANGOHUD=1 DXVK_FRAME_RATE=144 %command%
    ```

---

## 5. Proton-GE (GloriousEggroll) Kurulumu ve Yapılandırması

Valve’ın resmi Proton sürümünde açılmayan ara sahneler (sinematikler) veya düşük performans gösteren oyunlar için Proton-GE kurulmalıdır.

### ProtonUp-Qt İle Kolay Kurulum (Tavsiye Edilen)
1. Linux dağıtımınızın yazılım merkezinden veya Flatpak üzerinden **ProtonUp-Qt** uygulamasını indirin.
2. Uygulamayı açın ve **"Add version"** butonuna tıklayın.
3. Tool olarak **GE-Proton** seçin ve en son sürümü yükleyin.
4. Steam'i yeniden başlatın. Oyun uyumluluk menüsünde `GE-Proton (vX-XX)` görünecektir.

### Manuel Kurulum (Terminal)
```bash
mkdir -p ~/.steam/root/compatibilitytools.d/
cd ~/.steam/root/compatibilitytools.d/
wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton9-4/GE-Proton9-4.tar.gz
tar -xvf GE-Proton9-4.tar.gz
```

---

## 6. Anti-Cheat (EAC / BattEye) Destekli Oyunlar İçin Yapılandırma

Easy Anti-Cheat (EAC) ve BattEye kullanan Apex Legends, Elden Ring, Arma 3 gibi oyunların Linux üzerinde çalışması için ilgili runtime paketlerinin Steam üzerinden indirilmesi gerekir.

1. Steam Kütüphanesi arama çubuğuna **"Steam Linux Runtime"** yazın.
2. Aşağıdaki araçları aratıp yükleyin:
   * **Proton Easy Anti-Cheat Runtime**
   * **Proton BattEye Runtime**
3. Oyunu başlatmadan önce Proton Experimental veya en güncel Proton-GE sürümünün seçili olduğundan emin olun.

---

## 7. Proton Performansı Optimization Checklist (Özet)

*   [ ] **Grafik Sürücüleri:** NVIDIA kullanıcıları için proprietary (mülk) sürücülerin (`nvidia-driver`), AMD kullanıcıları için güncel `Mesa` sürücülerinin kurulu olduğundan emin olun.
*   [ ] **Shader Pre-Caching:** `Steam > Ayarlar > Shader Gölgelendirme Ön Belleği` özelliğini açık tutun. Bu, oyun içi takılmaları engeller.
*   [ ] **ProtonDB Kontrolü:** Oyun açılmıyorsa veya performans düşükse, [ProtonDB.com](https://www.protondb.com) adresinden oyunun kodunu aratıp topluluk tarafından verilen özel başlatma parametrelerini uygulayın.
*   [ ] **Dosya Sistemi:** Oyunların yüklü olduğu diskin **ext4** veya **btrfs** biçiminde olması önerilir. NTFS sürücülerinde Proton izin sorunları nedeniyle çökmeler yaşanabilir.