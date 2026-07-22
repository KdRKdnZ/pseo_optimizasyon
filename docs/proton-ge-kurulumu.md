---
title: "proton ge kurulumu"
description: "proton ge kurulumu hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Proton GE Kurulum Rehberi: Linux ve Steam Deck İçin Adım Adım Yöntemler

Proton GE (GloriousEggroll), Valve'ın resmi Proton yazılımının topluluk tarafından geliştirilen özel bir sürümüdür. Resmi Proton dağıtımında telif veya lisans kısıtlamaları nedeniyle yer almayan h.264, AAC ve Media Foundation gibi video/ses kodlayıcılarını (codec) barındırır. Linux dağıtımlarında ve Steam Deck üzerinde video oynatma sorunları yaşayan, performans artışı ve en güncel WINE yamalarını hedefleyen kullanıcılar için optimize edilmiştir.

Bu rehberde, Proton GE'nin otomatik ve manuel kurulum yöntemlerini, Steam entegrasyonunu ve farklı istemciler (Lutris, Heroic) üzerindeki yapılandırmasını inceleyebilirsiniz.

---

## Yöntem 1: ProtonUp-Qt ile Otomatik Kurulum (Önerilen)

ProtonUp-Qt, grafik arayüze (GUI) sahip, Proton-GE ve diğer uyumluluk katmanlarını tek tıkla indirip güncellemenizi sağlayan en pratik araçtır.

### 1. ProtonUp-Qt Kurulumu

* **Steam Deck (SteamOS) İçin:**
  1. Güç menüsünden **Masaüstü Moduna (Desktop Mode)** geçin.
  2. **Discover Software Center**'ı açın.
  3. Arama çubuğuna `ProtonUp-Qt` yazın ve **Install** butonuna tıklayın.

* **Linux Dağıtımları (Ubuntu, Fedora, Arch Linux vb.) İçin (Flatpak):**
  Terminali açın ve aşağıdaki komutu çalıştırın:
  ```bash
  flatpak install flathub net.davidotek.pupgui2
  ```

### 2. Proton GE'yi Yükleme

1. **ProtonUp-Qt** uygulamasını başlatın.
2. **Install for:** bölümünden target istemciyi seçin (Örn: *Steam* veya *Lutris*).
3. Alt kısımda bulunan **Add version** butonuna tıklayın.
4. **Tool** bölümünde *Proton-GE* seçeneğinin işaretli olduğundan emin olun.
5. **Version** kısmından en güncel sürümü (veya özel bir oyunda ihtiyaç duyulan spesifik bir sürümü) seçin.
6. **Install** butonuna basarak indirme işlemini tamamlayın.
7. İndirme bittikten sonra **Steam istemcisini yeniden başlatın**.

---

## Yöntem 2: Manuel Kurulum (Terminal / Komut Satırı)

Grafik arayüz kullanmadan, komut satırı üzerinden doğrudan GitHub depolarından çekim yapmak isteyen kullanıcılar için adımlar şunlardır:

### 1. Dizin Oluşturma

Steam'in özel uyumluluk araçlarını tanıması için `compatibilitytools.d` dizininin var olması gerekir. Terminali açarak aşağıdaki komutu girin:

* **Yerel (Native) Steam Yüklemeleri İçin:**
  ```bash
  mkdir -p ~/.steam/root/compatibilitytools.d/
  ```

* **Flatpak Steam Yüklemeleri İçin:**
  ```bash
  mkdir -p ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/
  ```

### 2. İndirme ve Arşivden Çıkarma

1. Proton GE'nin GitHub sürümler sayfasından en güncel `.tar.gz` paketini indirin veya terminal üzerinden `curl` ile çekin (Örnek sürüm: Proton-GE-Custom 9-2):

  ```bash
  cd ~/.steam/root/compatibilitytools.d/
  curl -LO https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton9-2/GE-Proton9-2.tar.gz
  ```

2. İndirilen arşivi çıkartın:
  ```bash
  tar -xvf GE-Proton9-2.tar.gz
  ```

3. Geçici arşiv dosyasını silin:
  ```bash
  rm GE-Proton9-2.tar.gz
  ```

4. Değişikliklerin algılanması için **Steam'i yeniden başlatın**.

---

## Steam Üzerinde Proton GE'yi Etkinleştirme

Kurulum tamamlandıktan sonra Proton GE sisteminizde hazır hale gelir ancak oyunlara manuel olarak atanması veya varsayılan yapılması gerekir.

### Belirli Bir Oyun İçin Proton GE Etkinleştirme

1. Steam kütüphanenizde ilgili oyuna sağ tıklayın ve **Özellikler (Properties)** seçeneğine girin.
2. Sol menüden **Uyumluluk (Compatibility)** sekmesine geçin.
3. **"Belirli bir Steam Play uyumluluk aracının kullanılmasını zorla"** (Force the use of a specific Steam Play compatibility tool) kutucuğunu işaretleyin.
4. Açılır menüden yüklediğiniz Proton GE sürümünü (Örn: `GE-Proton9-2`) seçin.

### Tüm Oyunlar İçin Varsayılan Yapma

1. Steam sol üst menüsünden **Steam > Ayarlar (Settings)** yolunu izleyin.
2. **Uyumluluk (Compatibility)** sekmesine gelin.
3. **"Diğer tüm başlıklarda Steam Play'i etkinleştir"** seçeneğini açık konuma getirin.
4. Altındaki araç seçim menüsünden yüklü Proton GE sürümünü atayın.

---

## Lutris ve Heroic Games Launcher Entegrasyonu

Proton GE sadece Steam için değil, Epic Games, GOG veya Amazon Games oyunlarını çalıştıran istemciler için de kullanılabilir.

### Heroic Games Launcher
* **Yol:** `Ayarlar > Game Defaults > Wine Version`
* ProtonUp-Qt üzerinden Heroic seçilerek Proton-GE (Wine-GE) indirildiyse, açılır menüde otomatik olarak listelenecektir.

### Lutris
* Manuel yüklemeler için arşiv dosyası aşağıdaki dizine çıkarılmalıdır:
  ```bash
  ~/.local/share/lutris/runners/wine/
  ```
* Lutris arayüzünde oyuna sağ tıklayıp **Configure > Runner options** sekmesinden **Wine version** olarak ilgili GE sürümü seçilir.

---

## Sorun Giderme ve Teknik Notlar

* **Proton GE Listede Görünmüyor:** 
  Steam çalışırken yapılan kurulumlar anında algılanmaz. Steam istemcisini tamamen kapatıp (`Steam > Çıkış`) tekrar açtığınızdan emin olun.
* **Flatpak Dizin Karışıklığı:** 
  Sisteminizde Steam Flatpak olarak kuruluysa, `.steam/root/` dizinine yapılan kurulumlar çalışmaz. Kurulumun `~/.var/app/com.valvesoftware.Steam/...` yoluna yapıldığını doğrulayın.
* **Sürüm Güncellemeleri:** 
  Proton GE otomatik güncellenmez. Oyunlarda çökme veya siyah ekran sorunları yaşandığında ProtonUp-Qt veya GitHub üzerinden en güncel sürüme yükseltme yapılması önerilir.