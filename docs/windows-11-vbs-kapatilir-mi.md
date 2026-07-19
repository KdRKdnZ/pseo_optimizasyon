---
title: windows 11 vbs kapatılır mı
description: windows 11 vbs kapatılır mı hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 VBS Kapatılır mı? Performans ve Güvenlik Analizi

Windows 11 ile birlikte varsayılan olarak aktif gelen **VBS (Virtualization-Based Security - Sanallaştırma Tabanlı Güvenlik)**, işletim sisteminin güvenliğini donanım seviyesinde izole ederek korumayı amaçlayan kritik bir mimari özelliktir. Ancak bu güvenlik katmanı, özellikle oyun performansında ve işlemci yoğun iş yüklerinde belirli bir overhead (ek yük) yaratır. 

Bu teknik analizde, bir yazılım mimarı ve donanım uzmanı gözüyle "Windows 11 VBS kapatılır mı?" sorusunu yanıtlayacak, performans test verilerini inceleyecek ve kapatma işleminin risk-kazanç analizini yapacağız.

---

## VBS (Virtualization-Based Security) Nedir ve Nasıl Çalışır?

VBS, Windows 11'in güvenli bir bellek bölgesi oluşturmak ve bu bölgeyi normal işletim sisteminden izole etmek için donanım sanallaştırma özelliklerini (Intel VT-x veya AMD-V) kullanma teknolojisidir. 

Windows, bu izole edilmiş ortamı korumak için bir hipervizör (Hyper-V) çalıştırır. Bu sayede, işletim sisteminin çekirdeği (kernel) ele geçirilse bile, saldırganlar bu izole edilmiş güvenli bölgedeki verilere erişemez.

### HVCI (Çekirdek Yalıtımı) ve VBS İlişkisi

VBS mimarisinin en önemli bileşeni **HVCI (Hypervisor-Protected Code Integrity)**, Türkçe adıyla **Bellek Bütünlüğü (Core Isolation)** özelliğidir. HVCI, Windows çekirdeğine yüklenmeye çalışan tüm sürücülerin ve kodların güvenilirliğini doğrular. 

*   **Çalışma Mantığı:** Kod bütünlüğü kontrolleri, normal Windows işletim sisteminin dışında, VBS tarafından yönetilen güvenli sanal kapsayıcıda gerçekleştirilir.
*   **Donanım Gereksinimi:** Bu işlem, işlemcinin **SLAT (Second Level Address Translation)** ve **MBEC (Mode-Based Execution Control)** gibi donanımsal sanallaştırma uzantılarını yoğun şekilde kullanmasını gerektirir.

---

## Windows 11 VBS Kapatılmalı mı? (Karar Matrisi)

VBS'in kapatılıp kapatılmaması gerektiği, bilgisayarınızı kullanım amacınıza ve donanım bileşenlerinize doğrudan bağlıdır. Aşağıdaki tablo, karar vermenizi kolaylaştıracaktır:

| Kullanıcı Profili | VBS Durumu | Nedeni |
| :--- | :--- | :--- |
| **Safkan Oyuncu (Gamer)** | **Kapatılmalı** | FPS düşüşlerini engellemek ve %1 / %0.1 Low FPS değerlerini kararlı hale getirmek için. |
| **Eski Nesil CPU Kullanıcısı** | **Kapatılmalı** | Intel 10. Nesil / AMD Ryzen 3000 öncesi işlemcilerde VBS'in getirdiği performans kaybı %15'e kadar çıkabilir. |
| **Yazılım Geliştirici / Güçlü PC** | **Açık Kalmalı** | Docker, WSL2 gibi sanallaştırma araçları zaten Hyper-V kullanır. Modern CPU'larda (Intel 13/14. Nesil, Ryzen 7000/9000) performans kaybı %2-3 civarındadır. |
| **Kurumsal / Ofis Kullanıcısı** | **Kesinlikle Açık Kalmalı** | Kimlik avı, fidye yazılımları (ransomware) ve kernel seviyesi açıklara karşı en güçlü savunma hattıdır. |

---

## VBS Kapatmanın Performansa Etkisi: Test Sonuçları

Yapılan bağımsız donanım testleri ve mimari analizler, VBS (özellikle HVCI/Bellek Bütünlüğü) aktif olduğunda işlemci üzerinde ek bir bağlam geçişi (context switch) yükü oluştuğunu göstermektedir.

*   **Oyunlarda FPS Etkisi:** CPU darboğazı (CPU bottleneck) olan oyunlarda (örneğin; *CS2, Valorant, Shadow of the Tomb Raider*) VBS kapatıldığında ortalama **%5 ile %15 arasında FPS artışı** gözlemlenmiştir.
*   **Giriş/Çıkış (I/O) Performansı:** NVMe SSD okuma/yazma hızlarında, özellikle rastgele 4K dosya erişimlerinde VBS açıkken %5'e varan mikro gecikmeler (latency) yaşanabilmektedir.
*   **Sentetik Testler (Cinebench/Geekbench):** Tek çekirdek performansında fark ihmal edilebilir düzeydeyken, çoklu çekirdek (multi-thread) testlerinde VBS kapalıyken %3-5 daha yüksek skorlar elde edilmektedir.

---

## Windows 11 VBS Nasıl Kapatılır? (Adım Adım Rehber)

VBS'i kapatmaya karar verdiyseniz, bunu işletim sistemi düzeyinde güvenli bir şekilde gerçekleştirmek için aşağıdaki üç yöntemden birini kullanabilirsiniz.

### Yöntem 1: Windows Güvenliği Arayüzü ile Kapatma (En Güvenli Yol)

1.  Windows Arama çubuğuna **"Çekirdek Yalıtımı" (Core Isolation)** yazın ve açın.
2.  **"Bellek Bütünlüğü" (Memory Integrity)** seçeneğinin yanındaki anahtarı **Kapalı** konumuna getirin.
3.  Bilgisayarınızı yeniden başlatın.

### Yöntem 2: Kayıt Defteri (Registry) ile Kapatma

Eğer arayüzden kapatılmasına izin verilmiyorsa, Windows Kayıt Defteri üzerinden VBS'i tamamen devre dışı bırakabilirsiniz:

1.  `Win + R` tuşlarına basın, `regedit` yazıp Enter'a basın.
2.  Aşağıdaki yola gidin:
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard`
3.  Sağ tarafta bulunan **"EnableVirtualizationBasedSecurity"** değerine çift tıklayın.
4.  Değer verisini `0` yapın.
5.  Bilgisayarınızı yeniden başlatın.

### Yöntem 3: Grup İlkesi Düzenleyicisi (GPEDIT) ile Kapatma (Windows Pro/Enterprise)

1.  `Win + R` tuşlarına basın, `gpedit.msc` yazın ve açın.
2.  Şu yolu izleyin: **Bilgisayar Yapılandırması > Yönetim Şablonları > Sistem > Device Guard**.
3.  **"Sanallaştırma Tabanlı Güvenliği Aç" (Turn on Virtualization Based Security)** ilkesine çift tıklayın.
4.  Seçeneği **Devre Dışı Bırakıldı (Disabled)** olarak ayarlayın.
5.  Uygula ve Tamam dedikten sonra bilgisayarı yeniden başlatın.

---

## Sonuç: VBS Kapatmak Mantıklı mı?

Bir sistem mimarı olarak önerim; **eğer önceliğiniz saf oyun performansı ise ve güncel olmayan bir donanıma sahipseniz, Windows 11 VBS özelliğini kapatmak mantıklıdır.** Elde edeceğiniz %10'luk performans artışı, oyun içi akıcılığı (özellikle 1% low FPS değerlerini) doğrudan olumlu etkileyecektir.

Ancak, bilgisayarınızda finansal işlemler yapıyor, kurumsal veriler barındırıyor veya güncel bir işlemci (Intel Core i7 13700K / AMD Ryzen 7 7800X3D ve üzeri) kullanıyorsanız, **VBS'i açık bırakmanız önerilir.** Modern işlemcilerdeki donanımsal optimizasyonlar sayesinde güvenlikten ödün vermeden performans kaybını hissetmeyeceksiniz.