---
title: proton ge kurulumu
description: proton ge kurulumu hakkında detaylı optimizasyon ve donanım rehberi.
---

# Proton GE Kurulumu: Linux ve Steam Deck İçin Adım Adım Rehber

Proton GE (GloriousEggroll), Valve'ın resmi Proton uyumluluk katmanının topluluk tarafından geliştirilen ve optimize edilen özel bir çatalıdır (fork). Resmi Proton sürümlerinde lisans kısıtlamaları nedeniyle yer almayan video çözücüleri (Media Foundation), en güncel DXVK (Direct3D to Vulkan) ve VKD3D yamalarını barındırır. Bu rehberde, Linux masaüstü sistemlerde ve Steam Deck üzerinde **Proton GE kurulumu** işlemlerini en güvenli ve performanslı yöntemlerle ele alacağız.

---

## Proton GE Nedir ve Neden Kullanılmalıdır?

Resmi Proton sürümleri, kararlılık odaklı olduğu için upstream (kaynak) Wine güncellemelerini ve deneysel yamaları sisteme geç entegre eder. Proton GE ise şu avantajları sağlar:

*   **Gelişmiş Video Oynatma:** Birçok oyunda karşılaşılan siyah ekran veya "Media Foundation" kaynaklı video oynatılamama sorunlarını çözer.
*   **Güncel Sürücüler ve API'ler:** DXVK, VKD3D-Proton ve FAudio bileşenlerinin en son kararlı veya beta sürümlerini içerir.
*   **Performans Yamaları:** CPU darboğazlarını azaltan Fsync ve Esync optimizasyonları varsayılan olarak etkindir.

---

## Yöntem 1: ProtonUp-Qt ile Otomatik Proton GE Kurulumu (Önerilen)

ProtonUp-Qt, grafik arayüze (GUI) sahip, bağımlılıkları otomatik yöneten ve hem Steam Deck hem de standart Linux dağıtımlarında çalışan en kararlı araçtır.

### Steam Deck Üzerinde Kurulum

1.  Steam Deck'inizin güç menüsünden **Desktop Mode (Masaüstü Modu)** seçeneğine geçiş yapın.
2.  Görev çubuğundaki mavi çanta simgesine tıklayarak **Discover Software Center**'ı açın.
3.  Arama çubuğuna `ProtonUp-Qt` yazın ve uygulamayı yükleyin.
4.  Uygulamayı başlatın. **Add Version** butonuna tıklayın.
5.  Açılan pencerede *Compatibility Tool* olarak **GE-Proton** seçeneğini, *Version* kısmında ise en güncel sürümü seçip **Install** butonuna basın.
6.  Kurulum tamamlandıktan sonra Steam'i yeniden başlatın.

### Masaüstü Linux (Ubuntu, Fedora, Arch) Üzerinde Kurulum

Masaüstü Linux dağıtımlarında Flatpak aracılığıyla kurulum yapmak, sandbox güvenliği açısından en doğru mimari yaklaşımdır.

Terminali açın ve aşağıdaki komutla ProtonUp-Qt'yi yükleyin:

```bash
flatpak install flathub net.davidotek.pupgui2
```

Uygulamayı çalıştırdıktan sonra yukarıdaki Steam Deck adımlarını takip ederek dilediğiniz GE-Proton sürümünü tek tıkla sisteminize entegre edebilirsiniz.

---

## Yöntem 2: Manuel Proton GE Kurulumu (Gelişmiş Kullanıcılar)

Otomatik araçları kullanmak istemeyen veya sunucu/headless ortamlarda çalışan sistem yöneticileri için manuel kurulum en şeffaf yöntemdir.

### Gerekli Dizin Yapısının Oluşturulması

Steam'in özel uyumluluk araçlarını tanıyabilmesi için `compatibilitytools.d` dizininin mevcut olması gerekir. Eğer bu dizin yoksa terminalden oluşturun:

**Standart Steam Kurulumları İçin:**
```bash
mkdir -p ~/.steam/root/compatibilitytools.d/
```

**Flatpak Steam Kurulumları İçin:**
```bash
mkdir -p ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/
```

### Tarball İndirme ve Çıkartma

1.  [GloriousEggroll GitHub Releases](https://github.com/GloriousEggroll/proton-ge-custom/releases) sayfasına gidin.
2.  En son kararlı sürümün `.tar.gz` uzantılı arşiv dosyasının bağlantısını kopyalayın.
3.  Terminal üzerinden ilgili dizine geçiş yaparak dosyayı indirin ve çıkartın:

```bash
# Uyumluluk dizinine geçiş yapın
cd ~/.steam/root/compatibilitytools.d/

# En güncel sürümü indirin (Örnektir, sürüm numarasını güncelleyin)
wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton9-10/GE-Proton9-10.tar.gz

# Arşivi çıkartın
tar -xf GE-Proton9-10.tar.gz

# İndirilen arşiv dosyasını silerek diskte yer açın
rm GE-Proton9-10.tar.gz
```

---

## Steam Üzerinde Proton GE'yi Etkinleştirme

Kurulum tamamlandıktan sonra Steam'in yeni uyumluluk aracını tarayabilmesi için **Steam istemcisini tamamen kapatıp yeniden başlatmanız** gerekir.

### Global Olarak Etkinleştirme (Tüm Windows Oyunları İçin)

1.  Steam > **Ayarlar** (Settings) > **Uyumluluk** (Compatibility) menüsüne gidin.
2.  "Diğer tüm oyunlar için Steam Play'i etkinleştir" seçeneğini aktif hale getirin.
3.  Açılır menüden yüklediğiniz **GE-Proton** sürümünü seçin.

### Oyun Özelinde Etkinleştirme (Önerilen)

Bazı oyunlar resmi Proton sürümleriyle daha kararlı çalışırken, bazıları yalnızca Proton GE ile açılır. Bu nedenle optimizasyonu oyun bazlı yapmak en sağlıklı yöntemdir.

1.  Steam kütüphanenizden ilgili oyuna sağ tıklayıp **Özellikler** (Properties) seçeneğine tıklayın.
2.  **Uyumluluk** (Compatibility) sekmesine gelin.
3.  "Belirli bir Steam Play uyumluluk aracının kullanılmasını zorunlu tut" seçeneğini işaretleyin.
4.  Listeden yüklediğiniz **GE-Proton** sürümünü seçin.

---

## Donanım ve Performans Optimizasyonu İçin İpuçları

Proton GE'den maksimum verim almak için aşağıdaki ortam değişkenlerini (Environment Variables) oyunların başlatma seçeneklerine ekleyebilirsiniz.

### Shader Önbelleği ve Akıcılık Optimizasyonu

Oyun içi takılmaları (stuttering) önlemek ve Vulkan shader derleme sürecini optimize etmek için oyuna sağ tıklayıp **Özellikler > Genel > Başlatma Seçenekleri** kısmına şu parametreleri ekleyin:

```bash
radv_perftest=gpl %command%
```
*Not: Bu komut, AMD GPU kullanan sistemlerde (Steam Deck dahil) Graphics Pipeline Library (GPL) özelliğini zorlayarak shader derleme takılmalarını neredeyse sıfıra indirir.*

---

## Sıkça Karşılaşılan Sorunlar ve Çözümleri

### Proton GE Steam Listesinde Görünmüyor
*   **Çözüm:** Steam'i arka planda tamamen kapattığınızdan emin olun (`killall steam` komutunu kullanabilirsiniz). Ayrıca manuel kurulum yaptıysanız, klasör hiyerarşisinin `compatibilitytools.d/GE-ProtonX-XX/` şeklinde olduğunu, arada fazladan bir alt klasör bulunmadığını kontrol edin.

### Oyun Başlatılamıyor (Prefix Bozulması)
*   **Çözüm:** Proton sürüm değişikliklerinde eski Wine prefix'i (oyun özelindeki sanal Windows dizini) çakışma yaratabilir. Oyunun `compatdata` klasörünü silerek temiz bir başlangıç yapın. Oyunun Steam ID'sini bulun ve şu dizinden ilgili klasörü silin:
    `~/.steam/root/steamapps/compatdata/[Oyun_ID]/`