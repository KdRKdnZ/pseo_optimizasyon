---
title: cs2 çözünürlük önerisi
description: cs2 çözünürlük önerisi hakkında detaylı optimizasyon ve donanım rehberi.
---

# CS2 Çözünürlük Önerisi: Performans ve Rekabetçi Avantaj İçin En İyi Ayarlar

Counter-Strike 2 (CS2), Source 2 motoruna geçişle birlikte grafik işleme (rendering) mimarisini tamamen yeniledi. CS:GO'ya kıyasla GPU (Ekran Kartı) bağımlılığı artan bu yeni yapıda, doğru çözünürlüğü seçmek yalnızca saniye başına kare sayısını (FPS) değil, aynı zamanda sistem gecikmesini (input lag) ve hedef izleme (tracking) kabiliyetinizi de doğrudan etkiler. 

Bu teknik analizde, donanım mimarisi ve oyun motoru dinamiklerini göz önünde bulundurarak en optimum **cs2 çözünürlük önerisi** seçeneklerini inceleyeceğiz.

---

## Source 2 Motorunun Çözünürlük ve Render Dinamikleri

Source 2, modern bir "Deferred Shading" (Ertelenmiş Gölgelendirme) render pipeline'ı kullanır. Bu durum, çözünürlük değişimlerinin ekran kartı üzerindeki yükünü CS:GO'ya (Forward Rendering) kıyasla çok daha belirgin hale getirir.

### CPU ve GPU Darboğazı (Bottleneck) Analizi
CS2'de çözünürlüğü düşürmek (örneğin 1080p'den 960p'ye), GPU üzerindeki piksel doldurma (pixel fill-rate) ve gölgelendirici (shader) yükünü azaltır. 
* **Düşük Çözünürlüklerde (Örn: 1280x960):** Oyun CPU-bound (işlemci sınırlı) hale gelir. İşlemcinizin tek çekirdek performansı maksimum FPS sınırınızı belirler.
* **Yüksek Çözünürlüklerde (Örn: 1920x1080 ve üzeri):** Oyun GPU-bound hale gelir. Ekran kartının render süresi (frame time) uzar ve bu da gecikmeye yol açar.

### Gecikme (Input Lag) ve Frame Time İlişkisi
Mil saniye (ms) cinsinden ölçülen "Frame Time" (Kare Süresi), bir karenin çizilmesi için geçen süredir. 300 FPS'te kare süresi ~3.3 ms iken, 150 FPS'te bu süre 6.6 ms'ye çıkar. Çözünürlüğü optimize ederek elde edeceğiniz yüksek FPS, doğrudan daha düşük giriş gecikmesi (input lag) anlamına gelir.

---

## En Çok Tercih Edilen CS2 Çözünürlük Formatları ve Karşılaştırması

CS2'de çözünürlük seçimi üç ana en-boy oranına (Aspect Ratio) ayrılır: 4:3, 16:9 ve 16:10.

### 4:3 Stretched (Gerilmiş) Çözünürlükler (1280x960, 1024x768)
Profesyonel oyuncuların %70'inden fazlası 4:3 stretched formatını tercih etmektedir.

* **Teknik Mekanik:** 4:3 oranındaki görüntü, 16:9 monitörünüze yatay olarak esnetilerek sığdırılır. Bu işlem, ekrandaki karakter modellerinin yatayda **%33 oranında daha geniş** görünmesini sağlar.
* **Avantajları:** Hedefleri vurmak görsel olarak kolaylaşır; piksel sayısı azaldığı için GPU yükü düşer ve FPS ciddi oranda artar.
* **Dezavantajları:** Görüş açısı (FOV) 106 dereceden 90 dereceye düşer. Ekranın kenarlarından gelen düşmanları görmeniz zorlaşır. Yatay mouse hassasiyeti (görsel olarak) daha hızlı hissettirir.

### 16:9 Native (Doğal) Çözünürlükler (1920x1080, 2560x1440)
Oyunun görsel olarak en net ve pürüzsüz göründüğü formattır.

* **Teknik Mekanik:** Monitörün fiziksel piksel dizilimiyle birebir eşleşir (Pixel-to-Pixel Mapping).
* **Avantajları:** Maksimum FOV (106 derece) sağlar. Uzak mesafedeki düşman pikselleri (örneğin Dust II Dust 2 A uzunluk) titreme yapmaz, net okunur.
* **Dezavantajları:** Karakter modelleri daha ince görünür. Yüksek piksel sayısı nedeniyle GPU'ya binen yük maksimum seviyededir, bu da FPS düşüşüne neden olur.

### 16:10 Alternatif Çözünürlükler (1680x1050, 1440x900)
4:3'ün hızı ile 16:9'un geniş FOV'u arasında bir köprü görevi görür. FOV değeri 100 derecedir. Modeller 4:3 kadar olmasa da genişler ve görüş açısı çok fazla daralmaz.

---

## Profesyonel Oyuncuların CS2 Çözünürlük Tercihleri Neden Farklı?

Profesyonel arenada çözünürlük seçimi sadece performans değil, bilişsel algı ve kas hafızası ile ilgilidir.

| Çözünürlük | En-Boy Oranı | FOV (Görüş Açısı) | Model Genişliği | FPS Performansı |
| :--- | :--- | :--- | :--- | :--- |
| **1280x960** | 4:3 (Stretched) | 90° | En Geniş (%33 Genişletilmiş) | En Yüksek |
| **1024x768** | 4:3 (Stretched) | 90° | Geniş (Düşük Piksel Netliği) | Maksimum (Eski PC'ler için) |
| **1680x1050** | 16:10 (Stretched)| 100° | Orta Genişlik | Dengeli |
| **1920x1080** | 16:9 (Native) | 106° | Standart | Standart |

### Görüş Açısı (FOV) ve Piksel Yoğunluğu Dengesi
Source 2 motorunda, 4:3 çözünürlükte dikey FOV sabit kalırken yatay FOV daralır. Profesyonel oyuncular, dikkat dağınıklığını önlemek ve tamamen ekranın merkezine (crosshair bölgesine) odaklanmak için dar FOV (90°) tercih ederler.

### Kas Hafızası ve Sub-Tick Sistemi
CS2'nin yeni **sub-tick** sunucu altyapısı, fare hareketlerinizin sunucuya iletilme hassasiyetini artırmıştır. 4:3 stretched çözünürlükte yatay farenizin ekran üzerindeki piksel atlama hızı değişse de, oyun içi 3D dönme açınız (yaw değeri) değişmez. Bu nedenle kas hafızanız zarar görmez.

---

## Donanımınıza Göre CS2 Çözünürlük Önerisi

Sistem bileşenlerinizin gücüne göre en kararlı performansı alabileceğiniz çözünürlük kombinasyonları aşağıda listelenmiştir.

### Giriş Seviyesi Sistemler İçin Öneri
*(Örn: GTX 1050 Ti / GTX 1650, Intel i3/i5 eski nesil)*

* **Öneri:** **1024x768 (4:3 Stretched)** veya **1280x720 (16:9)**
* **Gerekçe:** Bu sistemlerde öncelik GPU yükünü sıfırlayarak 144 FPS barajını aşmaktır. 1024x768 piksel yoğunluğu düşük olsa da render süresini minimumda tutar.

### Orta Seviye Sistemler İçin Öneri
*(Örn: RTX 2060 / RTX 3060, AMD Ryzen 5 3600 / 5600)*

* **Öneri:** **1280x960 (4:3 Stretched)**
* **Gerekçe:** CS2 için şu anki "altın standarttır". Hem modeller genişler hem de işlemci odaklı performans maksimize edilir. Görüntü çamurlu hissettirmez.

### Üst Seviye Sistemler İçin Öneri
*(Örn: RTX 4070 ve üzeri, AMD Ryzen 7 7800X3D)*

* **Öneri:** **1920x1080 (16:9 Native)** veya **1440x1080 (4:3 Custom Stretched)**
* **Gerekçe:** Güçlü bir GPU ve X3D önbellekli bir işlemciye sahipseniz, 1080p'de 400+ FPS alabilirsiniz. Bu durumda 16:9'un sunduğu maksimum FOV ve piksel netliği avantajından yararlanmak rekabetçi üstünlük sağlar.

---

## CS2'de 4:3 Stretched (Gerilmiş) Çözünürlük Nasıl Yapılır?

Oyunu 4:3 seçtiğinizde yanlarda siyah barlar (black bars) kalıyorsa, ekran kartı sürücünüzden ölçeklendirme ayarını değiştirmeniz gerekir.

### NVIDIA Ekran Kartları İçin:
1. Masaüstüne sağ tıklayın ve **NVIDIA Denetim Masası**'nı açın.
2. Sol menüden **"Masaüstü boyutunu ve konumunu ayarla"** sekmesine gidin.
3. Ölçeklendirme modunu **"Tam Ekran" (Full-screen)** olarak seçin.
4. "Ölçeklendirmeyi şunun üzerinde gerçekleştir:" seçeneğini **"GPU"** olarak ayarlayın.
5. "Oyunlar ve programlar tarafından belirlenen ölçeklendirme modunu geçersiz kıl" kutucuğunu işaretleyin ve uygulayın.

### AMD Ekran Kartları İçin:
1. Masaüstüne sağ tıklayıp **AMD Software: Adrenalin Edition**'ı açın.
2. **Ayarlar (Dişli Çark) > Ekran** sekmesine gidin.
3. **"GPU Ölçekleme" (GPU Scaling)** seçeneğini aktif hale getirin.
4. **"Ölçekleme Modu" (Scaling Mode)** ayarını **"Tam Panel" (Full Panel)** olarak değiştirin.