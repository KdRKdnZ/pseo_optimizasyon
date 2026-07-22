# Windows 11 Bellek Bütünlüğü Kapatılır mı? Performans ve Güvenlik Rehberi

Evet, Windows 11'de **Bellek Bütünlüğü (Memory Integrity)** özelliği kapatılabilir. Ancak bu işlem, sistem performansı ile siber güvenlik arasında doğrudan bir tercih yapmanızı gerektirir. 

Bellek Bütünlüğü'nün kapatılması özellikle oyunlarda **FPS artışı** ve eski sürücülerle uyumluluk sağlarken, sistemi zararlı yazılımlara ve kök dizin (rootkit) saldırılarına karşı daha savunmasız hale getirir.

---

## Bellek Bütünlüğü (HVCI) Nedir ve Nasıl Çalışır?

Bellek Bütünlüğü, teknik adıyla **HVCI (Hypervisor-protected Code Integrity)**, Windows 11'deki **Çekirdek Yalıtımı (Core Isolation)** mimarisinin bir parçasıdır. Sanallaştırma Tabanlı Güvenlik (VBS - Virtualization-based Security) teknolojisini kullanır.

Temel görevi şudur:
* Windows çekirdeğine (kernel) yüklenmeye çalışan kodların güvenilir ve imzalı olup olmadığını denetler.
* Kötü amaçlı yazılımların, yüksek yetkili Windows süreçlerine enjekte edilmesini engeller.
* Donanım düzeyinde sanallaştırma kullanarak güvenli bir bellek alanı oluşturur.

---

## Windows 11 Bellek Bütünlüğünü Kapatmak Ne İşe Yarar?

Bellek Bütünlüğü varsayılan olarak açık gelir. Ancak kapatıldığında sistemde şu değişiklikler gözlemlenir:

### 1. Performans ve FPS Artışı
HVCI, arka planda sürekli bir doğrulama işlemi yaptığı için CPU ve bellek üzerinde ekstra bir yük oluşturur. 
* **Oyun Performansı:** Özellikle eski nesil işlemcilerde (Intel 10. Nesil öncesi veya AMD Ryzen 3000 öncesi) Bellek Bütünlüğü kapatıldığında oyunlarda **%5 ile %15 arasında FPS artışı** görülebilir.
* **Girdi Gecikmesi (Input Lag):** İşlemci üzerindeki yük azaldığı için kare zamanlamaları (frametime) daha kararlı hale gelir.

### 2. Sürücü (Driver) Uyumsuzluklarının Çözülmesi
Eski donanımlara (eski ses kartları, Wi-Fi adaptörleri veya anti-cheat yazılımları) ait sürücüler dijital olarak imzalanmamış olabilir. Bellek Bütünlüğü açıkken Windows bu sürücülerin çalışmasını engeller. Özellik kapatıldığında bu donanımlar sorunsuz çalışmaya başlar.

---

## Bellek Bütünlüğünü Kapatmanın Riskleri Nelerdir?

Bellek Bütünlüğü kapatıldığında sisteminizin savunma zırhından önemli bir katman kaldırılmış olur:

* **Çekirdek Düzeyinde Saldırılar:** Saldırganlar, yönetici yetkisi elde etseler bile bellek bütünlüğü açıkken Windows çekirdeğine sızamazlar. Kapatıldığında ransomware (fidyeci yazılımlar) ve rootkit'lerin sisteme yerleşmesi kolaylaşır.
* **Sıfır Gün (Zero-Day) Açıkları:** Donanım seviyesindeki güvenlik devre dışı kaldığı için henüz yamalanmamış Windows güvenlik açıkları istismara açık hale gelir.

---

## Karşılaştırma Tablosu: Açık mı, Kapalı mı?

| Kriter | Bellek Bütünlüğü AÇIK | Bellek Bütünlüğü KAPALI |
| :--- | :--- | :--- |
| **Güvenlik Seviyesi** | Maksimum (Endüstri Standardı) | Orta (Klasik Antivirüs Düzeyi) |
| **Oyun / FPS Performansı**| Normal / Hafif Düşüş | Optimize / Yüksek FPS |
| **Eski Sürücü Desteği** | Kısıtlı | Tam |
| **CPU Yükü** | Yüksek (Sanallaştırma Katmanı) | Düşük |

---

## Windows 11 Bellek Bütünlüğü Nasıl Kapatılır? (Adım Adım)

Bellek Bütünlüğü özelliğini devre dışı bırakmak için aşağıdaki adımları uygulayabilirsiniz:

1. **Windows Güvenliği'ni Açın:** Başlat menüsüne `Windows Güvenliği` yazın ve uygulamayı açın.
2. **Aygıt Güvenliği Menüsüne Gidin:** Sol panelde bulunan **"Aygıt Güvenliği"** sekmesine tıklayın.
3. **Çekirdek Yalıtımı Detaylarına Girin:** "Çekirdek Yalıtımı" başlığı altındaki **"Çekirdek yalıtımı detayları"** bağlantısına tıklayın.
4. **Özelliği Kapatın:** **"Bellek Bütünlüğü"** ayarını `Kapalı` konumuna getirin.
5. **Sistemi Yeniden Başlatın:** Değişikliklerin geçerli olması için bilgisayarınızı yeniden başlatın.

> **İpucu:** Eğer ayar gri renkteyse ve değiştirilemiyorsa, sisteminizde kayıt defteri (Regedit) veya Grup İlkesi (GPO) üzerinden kısıtlama olabilir.

---

## Sonuç ve Tavsiye: Kapatmalı mısınız?

* **Kapatmalısınız, eğer:** Bilgisayarınızı ağırlıklı olarak oyun oynamak için kullanıyorsanız, güncel olmayan sürücüler nedeniyle "Mavi Ekran (BSOD)" hataları alıyorsanız ve işlemciniz eski nesil ise.
* **Açık Tutmalısınız, eğer:** Bilgisayarınızda kritik finansal veriler, şirket bilgileri tutuyorsanız, güvenliği doğrulanmamış dosya/yazılım indiriyorsanız ve güncel bir işlemciye (Intel 12.+ Nesil / AMD Ryzen 5000+) sahipseniz.

*Güvenlik riskini minimize etmek için Bellek Bütünlüğü'nü kapattığınızda güvenilir bir antivirüs yazılımı kullanmanız ve bilmediğiniz kaynaklardan dosya çalıştırmamanız önerilir.*