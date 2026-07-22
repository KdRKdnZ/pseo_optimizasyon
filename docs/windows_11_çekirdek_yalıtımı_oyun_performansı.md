# Windows 11 Çekirdek Yalıtımı ve Oyun Performansı: FPS Etkisi ve Teknik İnceleme

Windows 11 işletim sisteminde varsayılan olarak açık gelen **Çekirdek Yalıtımı (Core Isolation)** ve bunun alt özelliği olan **Bellek Bütünlüğü (Memory Integrity / HVCI)**, işletim sistemini alt düzey çekirdek saldırılarına karşı koruyan gelişmiş güvenlik katmanlarıdır. Ancak bu güvenlik mimarisi, donanım kaynakları üzerinde ek bir yük yaratarak oyun performansını, ortalama FPS değerlerini ve kare zamanlamalarını (frametime) doğrudan etkiler.

Bu makalede, Windows 11 Çekirdek Yalıtımı'nın çalışma mantığı, oyunlardaki teknik etkisi, hangi donanımlarda ne kadar performans kaybına yol açtığı ve nasıl optimize edileceği teknik detaylarıyla açıklanmaktadır.

---

## Çekirdek Yalıtımı ve Bellek Bütünlüğü (HVCI) Nedir?

Çekirdek Yalıtımı, Windows 11'in **Sanal Arama Tabanlı Güvenlik (VBS - Virtualization-Based Security)** mimarisini kullanır. İşlemcinin sanallaştırma yeteneklerini (Intel VT-x / AMD-V) kullanarak işletim sisteminin çekirdeğinden (Kernel) izole edilmiş güvenli bir bellek bölgesi oluşturur.

Bu yapının en kritik bileşeni **Bellek Bütünlüğü (HVCI - Hypervisor-Protected Code Integrity)** özelliğidir. HVCI'ın teknik işlevi şunlardır:

1. **Kötü Amaçlı Sürücü Engelleme:** Çekirdek modunda çalışmaya çalışan tüm sürücülerin ve kodların imzasını denetler.
2. **Kendi Kendine Değişen Kodları Engelleme:** Bellekteki çalıştırılabilir kodların yetkisiz şekilde değiştirilmesini önler.
3. **Hipervizör Denetimi:** Windows Hipervizör'ü aracılığıyla çekirdek belleğini koruma altında tutar.

---

## Çekirdek Yalıtımı Oyun Performansını Nasıl Etkiler?

Bellek Bütünlüğü açık olduğunda, işlemci (CPU) her bir bellek erişiminde ve çekirdek seviyesindeki işlemde ek denetimler yapmak zorundadır. Bu durum donanım seviyesinde şu iki temel soruna yol açar:

### 1. İşlemci Gecikmesi (CPU Overhead) ve İşlem Yükü
Bellek Bütünlüğü, işlemcinin komut yürütme süreçlerine ek adımlar ekler. Özellikle Intel'in **MBEC (Mode-Based Execute Control)** veya AMD'nin benzeri donanımsal hızlandırma teknolojilerine sahip olmayan eski nesil işlemcilerde, bu ek denetimler tamamen yazılımsal olarak emüle edilir. Bu durum CPU kullanımını artırır ve oyunların gereksinim duyduğu işleme gücünü çalar.

### 2. %1 ve %0.1 FPS Düşüşleri (Micro-Stuttering)
Oyunlarda sadece ortalama FPS değil, karelerin ekrana geliş sıklığı ve kararlılığı (**Frametime**) hayati önem taşır. Çekirdek Yalıtımı'nın anlık bellek taramaları, arka planda milisaniyelik gecikmelere (latency spike) neden olur. Bu durum oyun oynarken ekranın anlık olarak takılmasına (**micro-stuttering**) ve %1 Low FPS değerlerinin ciddi şekilde düşmesine yol açar.

---

## Donanım Nesillerine Göre Performans Etki Analizi

Çekirdek Yalıtımı'nın performansa etkisi kullanılan işlemci mimarisine göre değişiklik gösterir:

* **Yeni Nesil İşlemciler (Intel 11. Nesil ve Üzeri / AMD Ryzen 5000 ve Üzeri):**
  Bu işlemciler MBEC teknolojisini donanımsal olarak desteklediği için performans kaybı görece daha düşüktür. Ortalama FPS kaybı **%3 ile %7** arasında değişir.
* **Eski Nesil İşlemciler (Intel 10. Nesil ve Öncesi / AMD Ryzen 3000 ve Öncesi):**
  Donanımsal MBEC desteği yetersiz veya eksik olduğu için HVCI yükü yazılımsal olarak işlenir. Bu sistemlerde performans kaybı **%10 ile %25** seviyelerine çıkabilir.

### Oyun Türlerine Göre Performans Kaybı Tablosu

| Oyun Tipi | Örnek Oyunlar | Ortalama FPS Etkisi | %1 Low FPS (Kare Kararlılığı) Etkisi |
| :--- | :--- | :--- | :--- |
| **CPU Limitli / Rekabetçi (Esports)** | CS2, Valorant, Rainbow Six Siege | %8 - %15 Düşüş | Ciddi Takılmalar (%15 - %20 Düşüş) |
| **AAA / GPU Limitli** | Cyberpunk 2077, Alan Wake 2 | %2 - %5 Düşüş | Hissedilebilir Anlık Takılmalar |
| **Açık Dünya / İşlemci Yoğun** | GTA V, Starfield, Flight Simulator | %10 - %18 Düşüş | Yüksek Kare Zamanı Dalgalanması |

---

## Windows 11 Çekirdek Yalıtımı Oyun İçin Kapatılmalı mı?

Karar, bilgisayarın kullanım amacına göre verilmelidir:

### Kapatmanız Gereken Durumlar (Oyuncu Profili):
* Sisteminizde öncelik maksimum FPS, düşük sistem gecikmesi (input lag) ve pürüzsüz oyun deneyimi ise,
* Rekabetçi FPS oyunları (CS2, Valorant vb.) oynuyorsanız,
* Giriş veya orta seviye bir işlemciye/sisteme sahipseniz,
* Bilgisayarınızı yalnızca oyun ve genel günlük işler için kullanıyorsanız.

### Açık Kalması Gereken Durumlar (Güvenlik Profili):
* Bilgisayarınızda kritik finansal veriler, şirket bilgileri veya hassas dosyalar barındırıyorsanız,
* Bilinmeyen kaynaklardan sıklıkla dosya/yazılım indiriyorsanız,
* Kurumsal bir ağa bağlı çalışıyorsanız.

---

## Windows 11 Çekirdek Yalıtımı (Bellek Bütünlüğü) Nasıl Kapatılır?

Oyun performansını artırmak için Bellek Bütünlüğü özelliğini adım adım devre dışı bırakabilirsiniz:

1. **Başlat** menüsünü açın ve **Windows Güvenliği** yazarak uygulamayı açın.
2. Sol menüden **Aygıt Güvenliği** sekmesine tıklayın.
3. **Çekirdek Yalıtımı** başlığı altındaki **Çekirdek Yalıtımı Detayları** bağlantısına tıklayın.
4. **Bellek Bütünlüğü (Memory Integrity)** seçeneğini **Kapalı** konuma getirin.
5. Değişikliklerin geçerli olması için **bilgisayarınızı yeniden başlatın**.

```text
Grafik Arayüz Yolu:
Windows Güvenliği -> Aygıt Güvenliği -> Çekirdek Yalıtımı Detayları -> Bellek Bütünlüğü [KAPALI]
```

### Registry (Kayıt Defteri) Üzerinden Kapatma (Alternatif Yöntem)

Grafik arayüzden kapatılamayan durumlar için Kayıt Defteri kullanılabilir:

1. `Win + R` tuşlarına basın, `regedit` yazıp Enter'a basın.
2. Şu yola gidin:  
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity`
3. Sağ taraftaki **Enabled** DWORD değerine çift tıklayın ve değerini `0` yapın.
4. Bilgisayarınızı yeniden başlatın.

---

## Özet ve Teknik Değerlendirme

Windows 11'in Çekirdek Yalıtımı özelliği, siber güvenlik açısından üst düzey koruma sağlasa da, işletim sistemi ile donanım arasında ekstra bir sanallaştırma katmanı oluşturduğu için sanal bir performans bütçesi tüketir. 

Özellikle sistem kaynaklarının sınırda olduğu donanımlarda ve milisaniyelik tepkilerin önemli olduğu e-spor oyunlarında, **Bellek Bütünlüğü'nün kapatılması oyun performansında gözle görülür bir artış, daha kararlı kare zamanlamaları ve daha yüksek %1 FPS değerleri sağlar.** Sıradan bir ev kullanıcısı ve oyuncu için bu özelliğin kapatılması kabul edilebilir bir güvenlik riskidir.