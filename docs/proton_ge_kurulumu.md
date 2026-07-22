# Proton GE Kurulum Rehberi: Linux'ta Steam Oyun Performansını Optimize Etme

Proton GE (GloriousEggroll), Valve tarafından geliştirilen Proton uyumluluk katmanının topluluk tarafından özelleştirilmiş ve geliştirilmiş bir sürümüdür. Resmi Proton sürümünde telif hakları veya lisans kısıtlamaları nedeniyle yer almayan Media Foundation (MF) video kodlayıcıları, en güncel DXVK/VKD3D düzeltmeleri ve oyuna özel yamalar Proton GE içerisinde sunulur. 

Bu rehberde, Linux dağıtımları üzerinde Proton GE'nin otomatik ve manuel kurulum yöntemleri, Steam konfigürasyonu ve olası sorunların giderilmesi teknik ayrıntılarıyla anlatılmaktadır.

---

## Ön Gereksinimler

*   Çalışır durumda bir Linux dağıtımı (Ubuntu, Arch Linux, Fedora, Pop!_OS vb.)
*   Yüklü ve yapılandırılmış Steam istemcisi
*   Temel terminal bilgisi (Manuel kurulum için)

---

## Yöntem 1: ProtonUp-Qt ile Otomatik Kurulum (Önerilen)

ProtonUp-Qt, Proton GE, Luxtorpeda ve Wine-GE gibi uyumluluk katmanlarını grafik arayüz (GUI) üzerinden kolayca yönetmenizi sağlayan açık kaynaklı bir araçtır.

### 1. ProtonUp-Qt Kurulumu

En pratik yükleme yöntemi Flatpak kullanmaktır. Terminali açın ve aşağıdaki komutu çalıştırın:

```bash
flatpak install flathub net.davidotek.pupgui2
```

*Alternatif olarak, Arch Linux kullanıcıları AUR üzerinden `protonup-qt` paketini yükleyebilir.*

### 2. Proton GE Sürümünün Yüklenmesi

1.  **ProtonUp-Qt** uygulamasını başlatın.
2.  Uygulama otomatik olarak Steam dizininizi tespit edecektir.
3.  Alt kısımda bulunan **"Add version"** (Sürüm Ekle) butonuna tıklayın.
4.  **Tool** açılır menüsünden **Proton-GE** seçeneğini belirleyin.
5.  **Version** kısmından en güncel kararlı sürümü (örneğin: `GE-Proton8-32`) seçin.
6.  **Install** butonuna basarak indirme ve çıkarma işlemini başlatın.

---

## Yöntem 2: Terminal Üzerinden Manuel Kurulum

Otomatik araçlar kullanmak istemeyenler için doğrudan GitHub depoları üzerinden terminal ile kurulum adımları şu şekildedir:

### 1. Uyumluluk Dizinini Oluşturun

Steam'in özel Proton sürümlerini tanıması için `compatibilitytools.d` dizininin var olması gerekir. Terminalde şu komutla dizini oluşturun:

```bash
mkdir -p ~/.steam/root/compatibilitytools.d/
```

*(Not: Bazı dağıtımlarda Steam dizini `~/.local/share/Steam/compatibilitytools.d/` yolunda olabilir.)*

### 2. En Güncel Proton GE Sürümünü İndirin

GitHub API'si kullanarak en son sürümü çekebilir veya ilgili dizine geçip arşiv dosyasını indirebilirsiniz:

```bash
cd ~/.steam/root/compatibilitytools.d/
curl -s https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest \
| grep "browser_download_url.*tar.gz" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -
```

### 3. Arşivi Çıkarın ve Geçici Dosyaları Temizleyin

İndirilen `.tar.gz` arşivini dışarı çıkarın ve ardından tar dosyasını silin:

```bash
tar -xvf GE-Proton*.tar.gz
rm GE-Proton*.tar.gz
```

---

## Steam Üzerinde Proton GE'yi Etkinleştirme

Kurulum tamamlandıktan sonra Steam'in yeni eklenen uyumluluk katmanını algılayabilmesi için **Steam'in tamamen kapatılıp yeniden başlatılması zorunludur.**

### Bütün Oyunlar İçin Varsayılan Yapma (Küresel)

1.  Steam istemcisini açın.
2.  Sol üst köşedeki **Steam > Ayarlar (Settings)** menüsüne gidin.
3.  Sol paneden **Uyumluluk (Compatibility)** sekmesine tıklayın.
4.  "Diğer tüm içerikler için Steam Play'i etkinleştir" seçeneğini aktif edin.
5.  Açılır menüden yüklediğiniz **GE-Proton (Sürüm)** seçeneğini işaretleyin.
6.  Tamam'a tıklayarak Steam'i yeniden başlatın.

### Belirli Bir Oyun İçin Etkinleştirme (Oyuna Özel)

1.  Steam Kütüphanenizde ilgili oyuna sağ tıklayın ve **Özellikler (Properties)** seçeneğini seçin.
2.  **Uyumluluk (Compatibility)** sekmesine geçin.
3.  **"Belirli bir Steam Play uyumluluk aracının kullanılmasını zorla"** kutucuğunu işaretleyin.
4.  Listeden yüklediğiniz **GE-Proton** sürümünü seçin.

---

## Teknik Kontrol ve Doğrulama

Proton GE'nin aktif olarak çalışıp çalışmadığını doğrulamak için oyun içi ara sahnelerin (özellikle `.wmv` veya `.mp4` formatındaki video çözücülerine ihtiyaç duyan) düzgün oynatılıp oynatılmadığı kontrol edilebilir.

Ayrıca oyun başlatma seçeneklerine şu parametreyi ekleyerek detaylı log alabilirsiniz:

```bash
PROTON_LOG=1 %command%
```

Bu işlem, ev dizininizde (`~/steam-45450.log` gibi) oyuna ait bir log dosyası oluşturur. Dosya içeriğinde `GE-Proton` ibaresinin yer alması sürücünün başarıyla yüklendiğini gösterir.

---

## Sık Karşılaşılan Sorunlar ve Çözümleri

### 1. Proton GE Steam Listesinde Görünmüyor
*   **Sebebi:** Steam yeniden başlatılmamış veya yanlış dizine kurulum yapılmış olabilir.
*   **Çözüm:** Flatpak kullanıyorsanız Steam dizin yolu varsayılan olarak `~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/` şeklindedir. Dosyaları bu dizine taşıyın ve Steam'i `killall -9 steam` komutu ile kapatıp açın.

### 2. Oyun Açılmıyor veya Aniden Kapanıyor
*   **Sebebi:** Eski Proton konfigürasyon artıkları (pfx dizini) çakışma yaratıyor olabilir.
*   **Çözüm:** İlgili oyunun Prefix klasörünü silin (Oyun kimliği `APPID` bilinmelidir):
    ```bash
    rm -rf ~/.steam/root/steamapps/compatdata/[APPID]/
    ```
    *Not: Bu işlem yerel kayıt dosyalarınızı silebilir. Steam Cloud senkronizasyonunun açık olduğundan emin olun.*