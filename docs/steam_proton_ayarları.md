# Steam Proton Ayarları: Linux ve Steam Deck İçin Detaylı Yapılandırma Rehberi

Steam Proton, Valve tarafından geliştirilen ve Windows tabanlı oyunların Linux işletim sistemlerinde ve Steam Deck'te doğrudan çalıştırılmasını sağlayan Wine tabanlı bir uyumluluk katmanıdır (compatibility layer). Proton; **DXVK** (DirectX 9/10/11'i Vulkan'a çeviren yapı) ve **VKD3D-Proton** (DirectX 12'yi Vulkan'a çeviren yapı) teknolojilerini kullanarak yüksek performanslı bir oyun deneyimi sunar.

Bu rehberde, Steam Proton ayarlarının nasıl optimize edileceği, özel başlatma seçenekleri, GE-Proton (GloriousEggroll) kurulumu ve performans artırma yöntemleri teknik detaylarıyla ele alınmaktadır.

---

## 1. Steam Proton'u Global Olarak Etkinleştirme

Steam üzerinde henüz desteklenmeyen tüm Windows oyunlarını Linux üzerinde çalıştırabilmek için öncelikle Proton'un tüm kütüphanede aktif edilmesi gerekir.

1. **Steam** istemcisini açın.
2. Sol üst menüden **Steam > Ayarlar (Settings)** yolunu izleyin.
3. Sol panelden **Uyumluluk (Compatibility)** sekmesine gelin.
4. **"Diğer tüm başlıklar için Steam Play'i etkinleştir" (Enable Steam Play for all other titles)** seçeneğini aktif edin.
5. **"Diğer başlıkları şununla çalıştır:" (Run other titles with:)** açılır menüsünden en güncel kararlı Proton sürümünü (örneğin *Proton 8.0-x* veya *Proton Experimental*) seçin.
6. Değişikliklerin uygulanması için Steam'i yeniden başlatın.

---

## 2. Oyuna Özel Proton Sürümü Yapılandırma

Bazı oyunlar belirli Proton sürümlerinde daha kararlı çalışır. Belirli bir oyun için Proton sürümünü değiştirmek için:

1. Kütüphanenizdeki oyuna sağ tıklayıp **Özellikler (Properties)** seçeneğine tıklayın.
2. **Uyumluluk (Compatibility)** sekmesine geçin.
3. **"Belirli bir Steam Play uyumluluk aracının kullanılmasını zorla" (Force the use of a specific Steam Play compatibility tool)** kutucuğunu işaretleyin.
4. Açılan listeden hedeflenen Proton sürümünü seçin.

---

## 3. Proton Sürümleri Arasındaki Farklar

* **Proton (Kararlı Sürüm - Örn: Proton 8.0):** Valve tarafından tam testlerden geçmiş, yüksek kararlılık sunan sürümdür.
* **Proton Experimental:** En son düzeltmeleri, güncel DXVK sürümlerini ve henüz test aşamasında olan oyun yamalarını içerir. Yeni çıkan oyunlar için ilk tercih olmalıdır.
* **Proton Hotfix:** Valve'ın yeni çıkan popüler oyunlardaki kritik hataları (crash, siyah ekran) hızlıca çözmek için yayınladığı geçici sürümdür.
* **GE-Proton (Custom/GloriousEggroll):** Topluluk tarafından geliştirilen özel sürümdür. Valve'ın lisans sorunları nedeniyle resmi Proton'a ekleyemediği h.264 video kodeklerini (Cutscene/Sinematik sorunlarını çözer), özel DXVK yamalarını ve FSR güncellemelerini içerir.

---

## 4. Özel Sürüm: GE-Proton Kurulumu ve Yapılandırması

Resmi Proton sürümlerinde açılmayan veya sinematik videoları oynamayan oyunlar için GE-Proton kurulmalıdır.

### ProtonUp-Qt ile Kolay Kurulum (Tavsiye Edilen)
1. Steam Deck (Desktop Mode) veya Linux dağıtımınızın uygulama mağazasından (Discover / Software Center) **ProtonUp-Qt** uygulamasını indirin.
2. Uygulamayı açın ve **"Add version"** butonuna tıklayın.
3. Tool kısmından **GE-Proton**'u, Version kısmından en güncel sürümü seçip **Install** butonuna basın.
4. Kurulum bittikten sonra Steam'i yeniden başlatın.
5. Oyunun **Uyumluluk** ayarlarından yüklediğiniz `GE-ProtonXX-XX` sürümünü seçin.

### Manuel Kurulum Yolu
Sistem terminalini kullanarak tar.gz arşivini ilgili dizine çıkarabilirsiniz:

```bash
mkdir -p ~/.steam/root/compatibilitytools.d/
tar -xf GE-Proton*.tar.gz -C ~/.steam/root/compatibilitytools.d/
```

---

## 5. Gelişmiş Başlatma Seçenekleri (Launch Options) ve Çevre Değişkenleri

Oyunların performansını artırmak, grafik sorunlarını çözmek veya NVIDIA teknolojilerini aktif etmek için **Özellikler > Genel > Başlatma Seçenekleri (Launch Options)** alanına teknik komutlar eklenebilir.

Komutların sonuna `%command%` ifadesinin eklenmesi zorunludur.

### Performans ve Grafik Komutları

* **NVIDIA DLSS ve NVAPI Etkinleştirme:**
  ```bash
  PROTON_ENABLE_NVAPI=1 PROTON_HIDE_NVIDIA_GPU=0 %command%
  ```

* **GameMode Etkinleştirme (Feral GameMode ile CPU/GPU Performansını Önceliklendirme):**
  ```bash
  gamemoderun %command%
  ```

* **DirectX 11 Oyunlarında DXVK İşlemcisini Değiştirme (D3D11 -> Vulkan):**
  ```bash
  PROTON_USE_DXVK=1 %command%
  ```

* **Geniş Ekran / HUD Görüntüleme (MangoHud ile FPS, Sıcaklık ve Kullanım Değerleri):**
  ```bash
  mangohud %command%
  ```

* **E-Sync ve F-Sync Yapılandırması (CPU İş Parçacığı Yükünü Azaltma):**
  *E-Sync/F-Sync varsayılan olarak açıktır. Bazı eski oyunlarda kilitlenmeye sebep olursa kapatmak için:*
  ```bash
  PROTON_NO_ESYNC=1 PROTON_NO_FSYNC=1 %command%
  ```

* **Sistem Belleği (RAM) Kaynaklı Çökmeleri Önleme (AMD/Intel GPU):**
  ```bash
  vk_x11 %command%
  ```

---

## 6. Anti-Cheat (Hile Karşıtı) Yazılım Ayarları

Easy Anti-Cheat (EAC) ve BattEye kullanan çevrimiçi oyunların (Apex Legends, Elden Ring vb.) Proton üzerinde çalışması için ek çalışma zamanı paketleri gereklidir.

1. Steam kütüphanenizde arama alanına `Proton` yazın.
2. Araçlar (Tools) kategorisinde bulunan şu iki paketi yükleyin:
   * **Steam Linux Runtime - Sniper / Soldier**
   * **Proton EasyAntiCheat Runtime**
   * **Proton BattEye Runtime**

> **Not:** Kernel düzeyinde çalışan hile karşıtı yazılımlar (örneğin Riot Vanguard - Valorant) Proton üzerinde **çalışmaz**.

---

## 7. Proton Önbellek (Shader Pre-Caching) Temizliği ve Optimize Edilmesi

Oyunlardaki anlık takılmaları (stuttering) önlemek için Steam, gölgelendirici (shader) verilerini önceden derler. Disk alanını yönetmek veya bozuk önbelleği temizlemek için:

1. **Steam > Ayarlar > Shader Pre-Caching** bölümüne gidin.
2. **"Enable Shader Pre-Caching"** seçeneğinin açık olduğundan emin olun.
3. Takılma yaşanan bir oyunda önbelleği sıfırlamak için şu dizindeki ilgili oyun koduna (AppID) ait klasörü silin:
   `~/.steam/steam/steamapps/shadercache/[Oyun_AppID]`

---

## 8. Doğrulama ve Uyumluluk Takibi: ProtonDB

Bir oyunu çalıştırmadan veya ayar yapmadan önce **ProtonDB (protondb.com)** veritabanı kontrol edilmelidir. Topluluk tarafından sağlanan bu platformda oyunlar şu seviyelerle derecelendirilir:

* **Native:** Linux desteği var.
* **Platinum:** Hiçbir ayar gerektirmeden kusursuz çalışır.
* **Gold:** Ufak başlatma komutları (Launch Options) ile sorunsuz çalışır.
* **Silver:** Ufak grafiksel hatalar veya performans kayıpları içerebilir.
* **Borked:** Oyun mevcut Proton sürümleriyle çalışmıyor.

Özel bir başlatma parametresi aramadan önce ProtonDB üzerindeki kullanıcı raporlarında paylaşılan özel parametrelerin kullanılması en hızlı çözümdür.