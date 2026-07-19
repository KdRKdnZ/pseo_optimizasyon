---
title: windows 11 memory integrity kapatılır mı
description: windows 11 memory integrity kapatılır mı hakkında detaylı optimizasyon ve donanım rehberi.
---

# Windows 11 Memory Integrity Kapatılır mı? Teknik Analiz ve Performans Etkileri

Windows 11 ile birlikte varsayılan olarak aktif gelen **Bellek Bütünlüğü (Memory Integrity)**, işletim sisteminin çekirdek (kernel) seviyesindeki güvenliğini sağlamak için tasarlanmış donanım tabanlı bir güvenlik özelliğidir. Ancak bu özellik, özellikle oyuncular, eski donanım kullananlar ve sanallaştırma yazılımları ile çalışan profesyoneller arasında "performans kaybına yol açtığı" gerekçesiyle tartışma konusudur.

Bu teknik analizde, bir yazılım mimarı ve donanım uzmanı gözüyle Bellek Bütünlüğü'nün ne olduğunu, kapatılmasının güvenliğe ve performansa etkilerini kanıta dayalı verilerle inceleyeceğiz.

---

## Windows 11 Bellek Bütünlüğü (Memory Integrity) Nedir?

Bellek Bütünlüğü, Microsoft'un **Çekirdek Yalıtımı (Core Isolation)** teknolojisinin bir parçasıdır ve teknik literatürde **HVCI (Hypervisor-Protected Code Integrity)** olarak adlandırılır. 

Sistem, Windows mimarisinin en hassas bölgesi olan çekirdeği (Ring 0) korumak için **VBS (Virtualization-Based Security - Sanallaştırma Tabanlı Güvenlik)** teknolojisini kullanır. CPU'nun sanallaştırma uzantılarını (Intel VT-x veya AMD-V) kullanarak işletim sisteminden izole edilmiş, güvenli bir bellek alanı oluşturur. 

Bu izole alanda çalışan kod bütünlüğü kontrol mekanizması, sisteme yüklenmeye çalışan sürücülerin (drivers) imzalı ve güvenli olup olmadığını denetler. Amaç, kötü amaçlı yazılımların (malware) veya fidye yazılımlarının (ransomware) çekirdek seviyesine sızarak sistemi tamamen ele geçirmesini engellemektir.

---

## Windows 11 Memory Integrity Kapatılmalı mı?

Bu sorunun kesin bir "evet" veya "hayır" cevabı yoktur; karar, bilgisayarı kullanım amacınıza ve donanım konfigürasyonunuza bağlıdır.

### Hangi Durumlarda Kapatılmalıdır?
*   **Eski Donanım ve Sürücü Uyumsuzluğu:** Bilgisayarınıza bağlı eski bir yazıcı, tarayıcı veya özel bir donanım varsa ve bu donanımın sürücüleri dijital olarak imzalanmamışsa, Bellek Bütünlüğü bu sürücülerin yüklenmesini engeller. Bu durumda özelliği kapatmak zorunlu hale gelir.
*   **Maksimum Oyun Performansı Arayışı:** CPU darboğazı (bottleneck) yaşanan sistemlerde, arka plandaki sanallaştırma yükünü azaltarak FPS dalgalanmalarını minimuma indirmek için kapatılabilir.
*   **Üçüncü Taraf Sanallaştırma Yazılımları:** VMware, VirtualBox veya Android emülatörleri (BlueStacks vb.) kullanırken performans düşüşü veya mavi ekran (BSOD) hataları alıyorsanız, HVCI çakışmalarını önlemek için kapatılması önerilir.

### Hangi Durumlarda Kesinlikle Açık Kalmalıdır?
*   **Kurumsal ve Finansal Kullanım:** Bankacılık işlemleri yapılan, hassas verilerin barındığı iş bilgisayarlarında kesinlikle açık kalmalıdır.
*   **Modern Donanım Sahipleri:** Intel 11. nesil / AMD Ryzen 5000 serisi ve üzeri güncel işlemcilere sahipseniz, donanımsal optimizasyonlar sayesinde performans kaybı neredeyse sıfır olduğundan kapatılması anlamsızdır.

---

## Bellek Bütünlüğünü Kapatmanın Avantajları ve Dezavantajları

Sistem mimarisi düzeyinde yapılacak bu değişikliğin getireceği artı ve eksileri bilmek, doğru kararı vermenizi sağlar.

### Avantajlar (Performans ve Uyumluluk)
*   **CPU Üzerindeki Yükün Azalması:** HVCI aktifken, her kod yürütme işleminde CPU çekirdeği sanal güvenli bölge ile normal bölge arasında geçiş yapar (context switching). Kapatıldığında bu ek yük ortadan kalkar.
*   **Eski Sürücülerin Çalışması:** "Sürücü yüklenemedi" veya "Bu sürücü bu cihazda engellendi" gibi Windows Defender uyarıları ortadan kalkar.
*   **Giriş Gecikmesinin (Input Lag) Azalması:** Özellikle rekabetçi e-spor oyunlarında (Valorant, CS2, Apex Legends) milisaniyelik tepki süresi iyileşmeleri gözlemlenebilir.

### Dezavantajlar (Güvenlik Riskleri)
*   **Çekirdek Seviyesinde Savunmasızlık:** Bellek Bütünlüğü kapalıyken, kötü niyetli bir yazılım sisteme sızarsa doğrudan Kernel seviyesine (Ring 0) erişebilir. Bu durum, antivirüs yazılımlarının bile tespit edemeyeceği rootkit'lerin sisteme yerleşmesine yol açabilir.
*   **Sistem Kararsızlığı:** İmzalanmamış ve optimize edilmemiş kararsız sürücülerin sisteme yüklenmesi, sık sık mavi ekran (BSOD) hataları almanıza neden olabilir.

---

## Bellek Bütünlüğü Kapatıldığında Performans Ne Kadar Artar? (Kanıta Dayalı Veriler)

Donanım testleri ve benchmark sonuçları, Bellek Bütünlüğü'nün (HVCI) performans üzerindeki etkisinin işlemci mimarisine doğrudan bağlı olduğunu göstermektedir.

| İşlemci Nesli / Mimarisi | Donanımsal Destek (MBEC / GMET) | Ortalama Performans Kaybı (Aktifken) | Kapatıldığında Elde Edilen Kazanç |
| :--- | :--- | :--- | :--- |
| **Intel 8. - 10. Nesil / AMD Zen+** | Yok veya Sınırlı | %8 - %15 | **%10 - %15 FPS Artışı / Daha kararlı frametime** |
| **Intel 11. Nesil ve Üzeri / AMD Zen 3+** | Var (Hardware-level MBEC) | %1 - %3 | **Hissedilemeyecek kadar az (%1-2)** |

*Not: Intel, 7. nesil ve öncesi işlemcileri resmi olarak Windows 11 destek listesine almamıştır. Bu bypass edilmiş sistemlerde Bellek Bütünlüğü açılırsa performans kaybı %25'e kadar çıkabilir.*

**Özet Donanım Analizi:** Eğer işlemciniz **Intel MBEC (Mode-Based Execution Control)** veya **AMD GMET** teknolojisini donanımsal olarak destekliyorsa, Bellek Bütünlüğü'nü kapatmak size oyunlarda kayda değer bir FPS artışı sağlamayacaktır. Ancak eski nesil bir işlemciye sahipseniz, kapatmak sisteminizi gözle görülür şekilde rahatlatacaktır.

---

## Windows 11 Bellek Bütünlüğü Nasıl Kapatılır?

Bellek Bütünlüğü özelliğini Windows arayüzünü kullanarak güvenli bir şekilde kapatmak için aşağıdaki adımları takip edin:

### Yöntem 1: Windows Güvenliği Arayüzü ile Kapatma

1.  Klavyenizden `Windows + S` tuşlarına basın ve arama çubuğuna **Windows Güvenliği** yazarak uygulamayı açın.
2.  Sol menüden **Cihaz Güvenliği (Device Security)** seçeneğine tıklayın.
3.  Sağ tarafta bulunan **Çekirdek Yalıtım Detayları (Core Isolation Details)** bağlantısına tıklayın.
4.  **Bellek Bütünlüğü (Memory Integrity)** seçeneğinin yanındaki anahtarı **Kapalı (Off)** konumuna getirin.
5.  Kullanıcı Hesabı Denetimi (UAC) uyarısını onaylayın.
6.  Değişikliklerin geçerli olması için **bilgisayarınızı yeniden başlatın**.

```
[Başlat] -> [Windows Güvenliği] -> [Cihaz Güvenliği] -> [Çekirdek Yalıtımı] -> [Bellek Bütünlüğü: KAPALI]
```

### Yöntem 2: Kayıt Defteri (Registry) ile Kapatma (Gelişmiş Kullanıcılar)

Eğer arayüz üzerinden kapatma seçeneği grileşmişse veya hata alıyorsanız, Kayıt Defteri üzerinden bu işlemi gerçekleştirebilirsiniz:

1.  `Windows + R` tuşlarına basın, `regedit` yazın ve Enter'a basın.
2.  Aşağıdaki yolu takip edin:
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity`
3.  Sağ tarafta bulunan **Enabled** değerine çift tıklayın.
4.  Değeri **0** yapın (Aktif etmek için tekrar 1 yapabilirsiniz).
5.  Bilgisayarınızı yeniden başlatın.

---

## Sıkça Sorulan Sorular (FAQ)

### Bellek bütünlüğü kapalıyken bilgisayar virüs kapar mı?
Sadece bu özelliğin kapalı olması bilgisayarınıza virüs bulaştırmaz. Ancak, bilgisayarınıza bir şekilde virüs veya zararlı yazılım bulaşırsa, bu yazılımın sistemin en derin seviyesi olan çekirdeğe sızması ve kendini gizlemesi çok daha kolay olur. Güvenilir sitelerden indirme yapıyor ve bilinçli bir kullanıcıysanız, risk düşüktür.

### Valorant veya Vanguard için bellek bütünlüğü şart mı?
Riot Games'in hile karşıtı yazılımı **Vanguard**, çekirdek seviyesinde (Kernel-level Driver) çalışır. Vanguard, Bellek Bütünlüğü açıkken de kapalıyken de çalışabilir. Ancak Windows 11'de TPM 2.0 ve Secure Boot zorunluluğu gibi, gelecekte Vanguard'ın HVCI'yi de zorunlu tutma ihtimali bulunmaktadır. Şu an için kapatılması oyuna girmenize engel değildir.

### Bellek bütünlüğünü kapatmak garanti dışı bırakır mı?
Hayır. Bellek Bütünlüğü tamamen yazılımsal ve Windows işletim sisteminin sunduğu bir ayardır. Kapatılması donanımınıza zarar vermez ve bilgisayarınızın garantisini etkilemez.