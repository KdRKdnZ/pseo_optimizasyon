# Wine Performans Artırma: Linux Üzerinde Maksimum Oyun ve Uygulama Başarımı

Wine (Wine Is Not an Emulator), Windows uygulamalarını ve oyunlarını Linux/POSIX uyumlu işletim sistemlerinde çalıştırmak için Direct3D çağrılarını OpenGL veya Vulkan'a çeviren bir uyumluluk katmanıdır. Doğru yapılandırılmamış bir Wine ortamı, ciddi performans kayıplarına (FPS düşüşleri, takılmalar, yüksek CPU kullanımı) neden olur.

Bu rehber, Wine ortamınızdaki darboğazları gidermek, kare hızlarını (FPS) artırmak ve sistem kaynaklarını en verimli şekilde kullanmak için uygulayabileceğiniz teknik optimizasyon adımlarını içermektedir.

---

## 1. Donanım Hızlandırma ve Çeviri Katmanları (DXVK ve VKD3D)

Varsayılan Wine Direct3D sürücüsü, DirectX çağrılarını OpenGL'e çevirir. Bu durum yüksek CPU yüküne ve düşük performansa yol açar. Performansı artırmanın en etkili yolu Vulkan tabanlı çeviriciler kullanmaktır.

### DXVK Kurulumu (DirectX 9, 10 ve 11 için)
DXVK, DirectX 9/10/11 çağrılarını Vulkan API'sine dönüştürerek grafik işlemci (GPU) üzerindeki yükü optimize eder.

1. **Winetricks ile DXVK Kurulumu:**
   ```bash
   winetricks dxvk
   ```
2. **Manuel Kurulum (Önerilen):**
   DXVK’nın en son sürümünü GitHub üzerinden indirin ve ilgili Wine ön ekine (prefix) uygulayın:
   ```bash
   export WINEPREFIX=~/.wine
   ./setup_dxvk.sh install
   ```

### VKD3D-Proton (DirectX 12 için)
DirectX 12 tabanlı oyunlarda Vulkan dönüşümü sağlamak için Valve tarafından geliştirilen VKD3D-Proton kullanılmalıdır.

```bash
winetricks vkd3d
```

---

## 2. Çekirdek ve Senkronizasyon Optimizasyonları (Esync ve Fsync)

Wine, varsayılan olarak Windows thread senkronizasyonu için `wineserver` sürecini kullanır. Bu durum işlemci üzerinde büyük bir darboğaz (bottleneck) yaratır.

### Esync (Eventfd Synchronization)
Esync, thread senkronizasyonunu doğrudan Linux çekirdeğindeki `eventfd` mekanizmasına devreder.

* **Etkinleştirme:** Ortam değişkenine `WINEESYNC=1` ekleyin.
* **Sistem Limiti Ayarı:** Esync çok fazla dosya tanımlayıcısı (file descriptor) açar. `/etc/security/limits.conf` dosyasına aşağıdaki satırları ekleyin:
  ```text
  * soft nofile 1048576
  * hard nofile 1048576
  ```

### Fsync (Futex Synchronization)
Fsync, Esync'ten daha verimlidir ve Linux 5.16+ çekirdeklerinde varsayılan olarak bulunan `futex2` sistem çağrısını kullanır. CPU kullanımını belirgin şekilde düşürür.

* **Etkinleştirme:** Ortam değişkenine `WINEFSYNC=1` ekleyin.

---

## 3. Performans Odaklı Ortam Değişkenleri (Environment Variables)

Wine çalıştırılırken komut satırına eklenen özel değişkenler ile performans doğrudan artırılabilir.

| Değişken | Değer | Açıklama |
| :--- | :--- | :--- |
| `WINEESYNC` | `1` | Esync senkronizasyonunu aktif eder. |
| `WINEFSYNC` | `1` | Fsync senkronizasyonunu aktif eder (Kerneller 5.16+). |
| `DXVK_ASYNC` | `1` | Gölgelendirici (Shader) derleme takılmalarını engeller (GPL destekli sürücülerde gerekmez). |
| `STAGING_SHARED_MEMORY` | `1` | Paylaşılan bellek kullanımını artırarak giden veri iletimini hızlandırır. |
| `__NV_PRIME_RENDER_OFFLOAD` | `1` | NVIDIA optimus dizüstü bilgisayarlarda harici GPU'yu zorunlu kılar. |
| `RADV_PERFTEST` | `gpl` | AMD GPU kullanıcıları için Graphics Pipeline Library ile shader derleme takılmalarını bitirir. |

**Örnek Çalıştırma Komutu:**
```bash
WINEFSYNC=1 RADV_PERFTEST=gpl DXVK_FRAME_RATE=144 wine oyun.exe
```

---

## 4. Özel Wine Sürümlerinin Kullanımı (Wine-GE ve Proton-GE)

Ana dal (upstream) WineHQ sürümü saf uyumluluğa odaklanır ve performans yamalarını geç alır. Oyun ve ağır grafik uygulamaları için özelleştirilmiş Wine derlemeleri kullanılmalıdır.

* **Wine-GE (GloriousEggroll):** Esync, Fsync, FSR (FidelityFX Super Resolution) ve Valve'ın Proton güncellemelerini içeren en optimize Wine sürümüdür.
* **Lutris veya Heroic Games Launcher** kullanarak bu runner'ları tek tıkla yükleyebilir ve prefix'lerinize atayabilirsiniz.

---

## 5. Feral GameMode Entegrasyonu

Feral GameMode, arka planda çalışan ve oyun başladığında Linux işletim sistemini geçici olarak performans moduna alan bir daemon'dır.

### Yaptığı Optimizasyonlar:
* CPU Governor modunu `performance` olarak ayarlar.
* I/O önceliğini yükseltir.
* GPU aşırı hızlandırma (Overclock) profillerini etkinleştirir (NVIDIA/AMD).
* Ekran koruyucuyu devre dışı bırakır.

### Kurulum ve Kullanım:
Ubuntu/Debian için:
```bash
sudo apt install gamemode
```

Wine ile çalıştırma:
```bash
gamemoderun wine uygulama.exe
```

---

## 6. AMD FSR (FidelityFX Super Resolution) Yapılandırması

Wine-GE veya Wine-Staging sürümlerinde, Vulkan destekleyen her oyunda çözünürlük ölçekleme (FSR) zorlanabilir. Bu işlem, düşük çözünürlükte render alıp görüntüyü netleştirerek devasa FPS artışı sağlar.

* **WINE_FULLSCREEN_FSR=1**: FSR'yi etkinleştirir.
* **WINE_FULLSCREEN_FSR_STRENGTH=2**: Keskinleştirme gücünü ayarlar (0: En keskin, 5: En yumuşak).

**Kullanım Örneği:**
1. Oyun içi çözünürlüğü monitörünüzün doğal çözünürlüğünden bir alt kademeye getirin (Örn: 4K monitörde 1440p seçin).
2. Oyunu şu komutla başlatın:
```bash
WINE_FULLSCREEN_FSR=1 WINE_FULLSCREEN_FSR_STRENGTH=2 wine oyun.exe
```

---

## 7. Şema ve Bellek Limitlerini Düzenleme (Registry Ayarları)

Wine regedit üzerinden belirli grafik ayarları değiştirilerek Bellek (VRAM) yönetimi optimize edilebilir.

1. `wine regedit` komutunu çalıştırın.
2. `HKEY_CURRENT_USER\Software\Wine\Direct3D` dizinine gidin (Yoksa oluşturun).
3. Aşağıdaki `String` (SZ) değerlerini ekleyin/düzenleyin:

* **VideoMemorySize:** Ekran kartınızın MB cinsinden VRAM miktarı (Örn: 8GB için `8192`). Wine'ın VRAM'i yanlış tespit etmesini engeller.
* **CSMT (Command Stream Multithreading):** `enabled` yapın. Direct3D komutlarını ayrı bir thread'e taşıyarak CPU darboğazını çözer.

---

## Performans Kontrol Listesi (Özet)

1. [ ] Ekran kartı sürücülerinizin (NVIDIA/Mesa) güncel olduğundan emin olun.
2. [ ] Wine Prefix'ine **DXVK** veya **VKD3D** entegre edin.
3. [ ] Çekirdek düzeyinde **Fsync** destekli bir kernel (5.16+) ve Wine-GE sürümü kullanın.
4. [ ] Oyunları **GameMode** (`gamemoderun`) ile başlatın.
5. [ ] Masaüstü Ortamınızın (GNOME/KDE) "Compositor" (Pencere Yöneticisi) özelliğini oyun sırasında devre dışı bırakın (V-Sync gecikmesini ve FPS düşüşünü önler).