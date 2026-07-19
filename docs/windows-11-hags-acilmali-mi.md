---
title: windows 11 hags açılmalı mı
description: windows 11 hags açılmalı mı hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 HAGS Açılmalı mı? Performans ve Teknik Analiz

Windows 10 ile hayatımıza giren ve Windows 11 ile varsayılan olarak optimize edilen **HAGS (Hardware-Accelerated GPU Scheduling / Donanım Hızlandırmalı GPU Zamanlaması)**, modern işletim sistemlerinde grafik işlem biriminin (GPU) bellek yönetimini optimize etmeyi amaçlayan kritik bir API seviyesi özelliğidir. 

Peki, **windows 11 hags açılmalı mı?** Bu sorunun yanıtı, kullandığınız donanım mimarisine, oynadığınız oyunların grafik motoruna ve sisteminizdeki darboğaz (bottleneck) durumuna göre değişiklik gösterir. Bu teknik analizde, HAGS'ın çalışma prensibini, avantajlarını, dezavantajlarını ve hangi senaryolarda açılması gerektiğini kanıtlara dayanarak inceleyeceğiz.

---

## HAGS (Donanım Hızlandırmalı GPU Zamanlaması) Nedir?

Geleneksel Windows Görüntü Sürücüsü Modelinde (WDDM), grafik önceliklendirme ve zamanlama görevleri öncelikle CPU tarafından yönetilir. CPU, GPU'ya gönderilecek komutları sıraya koyar, bu da yüksek kare hızlarında (FPS) CPU üzerinde ek bir yük (overhead) yaratır.

HAGS aktif edildiğinde, bu zamanlama ve bellek yönetimi görevleri doğrudan GPU'nun kendi üzerinde bulunan özel bir **zamanlama işlemcisine (dedicated scheduling processor)** devredilir. Böylece aradaki "aracı" (CPU) ortadan kalkar ve GPU kendi iş yükünü kendisi yönetmeye başlar.

---

## HAGS Açmanın Avantajları Nelerdir?

### 1. CPU Darboğazını (Bottleneck) Azaltır
Eğer sisteminizde güçlü bir ekran kartı (örneğin RTX 3070) ve buna kıyasla daha zayıf veya eski nesil bir işlemci (örneğin Ryzen 5 2600) varsa, CPU grafik komutlarını yetiştirmekte zorlanır. HAGS, zamanlama yükünü CPU'dan alarak işlemci üzerindeki yükü hafifletir ve CPU kaynaklı darboğazları minimize eder.

### 2. Giriş Gecikmesini (Input Latency) Düşürür
Komut kuyruğunun CPU yerine doğrudan GPU tarafından yönetilmesi, karelerin ekrana çizilme süresini (frame time) kısaltır. Bu durum, özellikle rekabetçi FPS oyunlarında daha düşük giriş gecikmesi (input lag) ve daha akıcı bir oyun deneyimi sağlar.

### 3. DLSS 3 (Frame Generation) İçin Zorunludur
NVIDIA'nın Ada Lovelace (RTX 40 serisi) mimarisiyle sunduğu **DLSS 3 Frame Generation (Kare Oluşturma)** teknolojisinin çalışabilmesi için Windows 11'de HAGS özelliğinin kesinlikle açık olması gerekir. HAGS kapalıyken yapay zeka destekli ara kare oluşturma teknolojisi aktif edilemez.

---

## HAGS Açmanın Dezavantajları ve Olası Sorunlar

HAGS her ne kadar modern bir teknoloji olsa da, bazı senaryolarda kararsızlıklara yol açabilir:

*   **Eski Oyunlarda Kararsızlık:** DirectX 11 ve daha eski API'leri kullanan bazı oyunlarda HAGS, mikro takılmalara (stuttering) veya ani FPS düşüşlerine (frametime spikes) neden olabilir.
*   **Yayıncı Yazılımları ile Çakışma:** OBS Studio veya Streamlabs gibi GPU tabanlı kodlama (NVENC) kullanan yayın yazılımlarında, HAGS açıkken sahne geçişlerinde veya yoğun grafik anlarında drop (kare kaybı) yaşandığı rapor edilmiştir. GPU, kendi zamanlamasını önceliklendirdiği için arka plandaki yayın yazılımına yeterli kaynak ayırmayabilir.

---

## Windows 11'de HAGS Nasıl Açılır?

Windows 11'de HAGS özelliğini aktif etmek için aşağıdaki adımları takip edebilirsiniz:

1.  Masaüstüne sağ tıklayın ve **Görüntü Ayarları** seçeneğine gidin.
2.  Açılan pencerenin alt kısmında yer alan **Grafikler** seçeneğine tıklayın.
3.  Üst kısımda bulunan **Varsayılan grafik ayarlarını değiştir** bağlantısına tıklayın.
4.  **Donanım hızlandırmalı GPU zamanlaması** seçeneğini **Açık** konuma getirin.
5.  Değişikliklerin geçerli olması için bilgisayarınızı yeniden başlatın.

---

## Karar Matrisi: HAGS'ı Kimler Açmalı, Kimler Kapatmalı?

Aşağıdaki tablo, donanım ve kullanım senaryonuza göre HAGS ayarını nasıl yapılandırmanız gerektiğini göstermektedir:

| Donanım / Kullanım Senaryosu | HAGS Durumu | Nedeni |
| :--- | :--- | :--- |
| **NVIDIA RTX 40 Serisi GPU** | **Kesinlikle Açılmalı** | DLSS 3 Frame Generation teknolojisini kullanabilmek için zorunludur. |
| **Giriş/Orta Segment CPU + Güçlü GPU** | **Açılmalı** | CPU darboğazını azaltır, ortalama FPS değerini %2 ila %7 arasında artırır. |
| **Üst Segment CPU + Üst Segment GPU** | **Açılmalı (Test Ederek)** | FPS artışı minimal olur ancak daha stabil frametime (kare süresi) elde edilir. |
| **OBS ile Aktif Yayın Yapanlar** | **Kapatılmalı veya Test Edilmeli** | Yayında kare kaçırma (render lag) sorunlarına yol açabilir. |
| **Eski Nesil GPU (GTX 10 Serisi / RX 500 Serisi)** | **Kapatılmalı** | Eski mimarilerde donanımsal zamanlayıcı zayıf olduğundan performansı düşürebilir. |

---

## Sonuç: Windows 11 HAGS Açılmalı mı?

Modern bir Windows 11 sisteminde, güncel bir ekran kartı (NVIDIA RTX veya AMD RX 5000/6000/7000 serisi) kullanıyorsanız **HAGS özelliğini kesinlikle açmalısınız.** Özellikle DX12 ve Vulkan kullanan modern oyunlarda HAGS, daha stabil kare süreleri ve daha düşük gecikme süresi sunar.

Ancak, sisteminizde ağırlıklı olarak eski nesil (DX11/DX9) oyunlar oynuyorsanız, OBS ile profesyonel yayın yapıyorsanız ve oyunlarda ani takılma (stutter) sorunları yaşıyorsanız, HAGS özelliğini kapatıp sisteminizi test etmek en sağlıklı yaklaşım olacaktır.