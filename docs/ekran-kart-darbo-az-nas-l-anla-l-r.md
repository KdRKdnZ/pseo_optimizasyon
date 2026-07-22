---
title: "ekran kartı darboğazı nasıl anlaşılır"
description: "ekran kartı darboğazı nasıl anlaşılır hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Ekran Kartı Darboğazı Nasıl Anlaşılır? (GPU Bottleneck Tespiti ve Çözümü)

Ekran kartı (GPU) darboğazı, grafik işlemcinin sistemdeki diğer bileşenlerin (özellikle işlemci) gönderdiği verileri işleme hızına yetişememesi ve %100 yük altında çalışarak sistemin maksimum kare hızını (FPS) sınırlandırması durumudur. 

Oyun performansında ekran kartının %99-%100 kullanım oranına ulaşması genel olarak **ideal kabul edilen** bir durum olsa da, sistemin vadettiği potansiyel FPS değerine ulaşılamıyorsa veya grafik ayarları düşürülmesine rağmen performans artmıyorsa GPU kaynaklı bir darboğaz söz konusudur.

Bu rehberde, ekran kartı darboğazını teknik olarak nasıl tespit edeceğinizi, CPU darboğazından nasıl ayıracağınızı ve çözüm yöntemlerini adım adım inceleyeceğiz.

---

## 1. Ekran Kartı Darboğazının Temel Belirtileri

Sisteminizde ekran kartı darboğazı olup olmadığını oyun esnasındaki şu davranışlardan anlayabilirsiniz:

* **%99 - %100 GPU Kullanımı:** Oyun sırasında ekran kartı kullanımı sürekli olarak %98-%100 bandında seyrederken, işlemci (CPU) kullanımı %20-%60 gibi daha düşük seviyelerde kalır.
* **Grafik Ayarları Düşürüldüğünde FPS’in Artması:** Grafik kalitesini (DirectX/Vulkan ayarları, doku kalitesi, gölgeler) "Ultra" konumundan "Düşük" konuma getirdiğinizde FPS değerinde belirgin bir artış yaşanır.
* **Çözünürlük Hassasiyeti:** Çözünürlüğü 4K'dan 1080p'ye çektiğinizde FPS doğrudan yükseliyorsa, sınırlayıcı unsur ekran kartıdır.
* **Stabil Yüksek Kare Süresi (Frametime):** CPU darboğazının aksine, GPU darboğazında anlık takılmalar (micro-stuttering) az olur. Oyun takılmadan akar ancak alınan toplam FPS ekran kartının gücüyle sınırlıdır.

---

## 2. Yazılımsal Tespiti: MSI Afterburner ile Canlı İzleme

Ekran kartı darboğazını kesin olarak teşhis etmek için oyun içi OSD (On-Screen Display) verilerini analiz etmek gerekir.

### Gerekli Araçlar:
* **MSI Afterburner** ve **RivaTuner Statistics Server (RTSS)**

### Adım Adım Teşhis Prosedürü:

1. **MSI Afterburner** yazılımını indirin ve kurun.
2. Ayarlar (Çark simgesi) > **İzleme (Monitoring)** sekmesine gidin.
3. Aşağıdaki değerleri "Bilgi Ekranında Göster (OSD)" olarak işaretleyin:
   * **GPU Kullanımı (GPU Usage)**
   * **GPU Sıcaklığı (GPU Temperature)**
   * **CPU Kullanımı (CPU Usage - Tüm Çekirdekler)**
   * **Kare Hızı (FPS)**
   * **Kare Süresi (Frametime - ms)**
4. Donanım yükü yüksek bir oyuna (örn: *Cyberpunk 2077, Red Dead Redemption 2, Unreal Engine 5 tabanlı oyunlar*) girin.

### Veri Analizi Tablosu:

| Parametre | GPU Darboğazı Senaryosu | CPU Darboğazı Senaryosu | Dengeli Sistem |
| :--- | :--- | :--- | :--- |
| **GPU Kullanımı** | **%98 - %100** | %50 - %85 (Dalgalı) | %95 - %99 |
| **CPU Kullanımı** | %20 - %60 | %80 - %100 (Çekirdek bazlı) | %40 - %70 |
| **Kare Süresi Grafik** | Düz / Stabil (Yüksek ms) | Sık Sıçramalı (Spike) | Düz / Stabil (Düşük ms) |
| **Grafik Düşürme Etkisi**| FPS Doğrudan Artar | FPS Değişmez / Çok Az Artar | FPS Artar |

---

## 3. GPU Darboğazı ve CPU Darboğazı Arasındaki Fark

İki durum sıkça karıştırılsa da teknik yük dağılımı tamamen farklıdır:

* **GPU Darboğazı:** Ekran kartınız tam kapasitede çalışıyordur. İşlemci rahat durumdadır. Oyun akıcıdır fakat FPS belli bir sınırın üzerine çıkamaz. Bu durum donanım sağlığı ve oyun deneyimi açısından **tehlikeli değildir**, sisteminizin tüm grafik gücünü kullandığını gösterir.
* **CPU Darboğazı:** İşlemci ekran kartına kare çizim komutlarını (Draw Calls) yetiştiremez. GPU kullanımı %60-80'lere düşer. Oyunda **anlık takılmalar (stuttering) ve ani FPS düşüşleri (drop)** yaşanır. Bu, istenmeyen darboğaz türüdür.

---

## 4. Ekran Kartı Darboğazı Nasıl Giderilir?

Eğer ekran kartınız sisteminizin zayıf halkası haline geldiyse ve hedeflediğiniz FPS değerini alamıyorsanız uygulayabileceğiniz teknik çözümler şunlardır:

### Yazılımsal ve Grafiksel Çözümler

1. **Yapay Zeka Ölçeklendirme Teknolojilerini Kullanın:**
   * **NVIDIA DLSS**, **AMD FSR** veya **Intel XeSS** teknolojilerini devreye sokun. Bu teknolojiler oyunu daha düşük bir çözünürlükte işleyip yapay zeka ile ekran çözünürlüğünüze yükselterek GPU yükünü %30-%50 oranında azaltır.
2. **Yükü İşlemciye Kaydıran Ayarları Düşürün:**
   * Ray Tracing (Işın İzleme)
   * Volumetric Fog (Hacimsel Sis)
   * Shadow Quality (Gölge Kalitesi)
   * Ambient Occlusion (Ortam Kapatma)
3. **Çözünürlüğü Veya Render Skalasını Düşürün:**
   * Monitör çözünürlüğünüz yüksekse (örneğin 4K), oyun içi çözünürlüğü 1440p veya 1080p seviyesine çekerek GPU üzerindeki yükü doğrudan hafifletebilirsiniz.
4. **GPU Overclock (Hız Aşırtma):**
   * MSI Afterburner üzerinden GPU Çekirdek Saat Hızı (Core Clock) ve Bellek Saat Hızını (Memory Clock) güvenli sınırlar içinde artırarak %5-%10 arası performans kazanımı sağlayabilirsiniz.

### Donanımsal Çözümler

* **VRAM Yetersizliğini Kontrol Edin:** Eğer GPU kullanımı %100 iken VRAM sınırına ulaşılıyorsa (örn: 8GB VRAM'in 7.9GB'ı doluysa), Kaplama (Texture) kalitesini düşürmek performansı doğrudan artırır.
* **GPU Yükseltmesi:** Yazılımsal çözümler yetersiz kaldığında tek kesin çözüm, daha yüksek işlem gücüne ve VRAM kapasitesine sahip bir ekran kartına geçiş yapmaktır.

---

## Özet

Ekran kartı darboğazı, **oyun esnasında GPU kullanımının %99 - %100 olması** ve grafik ayarları düşürüldüğünde FPS’in yükselmesi ile kolayca anlaşılır. CPU darboğazının aksine oyunda takılmalara yol açmaz, yalnızca alabileceğiniz maksimum kare hızını belirler. **DLSS/FSR kullanımı** ve ağır grafik ayarlarının optimize edilmesi, yeni bir ekran kartı almadan bu darboğazı hafifletmenin en etkili yoludur.