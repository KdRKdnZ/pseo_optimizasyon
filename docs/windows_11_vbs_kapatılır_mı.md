# Windows 11 VBS Kapatılmalı mı? Performans ve Güvenlik Analizi

**VBS (Virtualization-based Security - Sanallaştırma Tabanlı Güvenlik)**, Windows 11 ile birlikte varsayılan olarak açık gelen ve işletim sisteminin çekirdeğini zararlı yazılımlardan korumayı hedefleyen donanım seviyesinde bir güvenlik özelliğidir. 

Ancak VBS, arka planda sürekli olarak sanallaştırma katmanı çalıştırdığı için işlemci ve bellek kaynaklarını tüketir. Bu durum, özellikle oyunlarda ve yüksek işlem gücü gerektiren uygulamalarda **%5 ile %25 arasında performans kayıplarına** yol açabilir.

---

## VBS (Sanallaştırma Tabanlı Güvenlik) Nedir ve Nasıl Çalışır?

VBS, donanım sanallaştırma özelliklerini (Intel VT-x / AMD-V) kullanarak güvenli bir bellek bölgesi oluşturur. Bu yalıtılmış bölge, işletim sistemi çekirdeğinden (Kernel) tamamen bağımsızdır. 

VBS'in en önemli bileşeni **HVCI (Hypervisor-Enforced Code Integrity - Bellek Bütünlüğü)** özelliğidir. HVCI, sisteme sızmaya çalışan imzasız veya zararlı sürücülerin bellek alanına kod enjekte etmesini engeller.

---

## Windows 11'de VBS Kapatılır mı?

**Evet, Windows 11'de VBS kapatılabilir.** VBS'in kapatılıp kapatılmaması kullanıcının önceliklerine bağlıdır:

### VBS'i Kapatması Gereken Kullanıcılar:
* **Oyuncular (Gamers):** Maksimum FPS, daha düşük gecikme (frame time) ve kararlı kare hızları isteyenler.
* **Eski veya Orta Segment Donanıma Sahip Olanlar:** İşlemci çekirdek sayısı ve önbelleği sınırlı olan sistemlerde VBS yükü belirgin şekilde hissedilir.
* **Benchmark ve Hız Aşırtma (Overclock) Yapanlar:** Donanımın ham gücünü ölçmek isteyenler.

### VBS'i Açık Bırakması Gereken Kullanıcılar:
* **Kurumsal ve Şirket Bilgisayarları:** Kritik verilerin işlendiği ve siber saldırı riskinin yüksek olduğu ortamlar.
* **Günlük/Ofis Kullanıcıları:** Oyun oynamayan, önceliği sistem güvenliği ve veri bütünlüğü olan kullanıcılar.

---

## VBS Kapatmanın Avantajları ve Dezavantajları

| Avantajlar (VBS Kapalı) | Dezavantajlar (VBS Kapalı) |
| :--- | :--- |
| **FPS Artışı:** Oyunlarda ortalama %5 - %20 FPS artışı sağlanır. | **Çekirdek Koruması Azalır:** Kernel seviyesindeki zararlı yazılımlara karşı koruma kalkar. |
| **İşlemci Yükü Azalır:** Arka plan arka plan sanallaştırma işlemleri durur. | **Credential Guard Devre Dışı:** Oturum açma kimlik bilgilerinin çalınma riski artar. |
| **Daha Düşük Gecikme:** Sistem tepkiselliği ve kare zamanlaması (frame delivery) iyileşir. | **Sürücü Doğrulama Esnetilir:** Güvenli olmayan sürücülerin çalışmasına izin verilmiş olur. |

---

## Windows 11 VBS Nasıl Kapatılır? (Adım Adım)

VBS'i kapatmak için en etkili ve güvenli iki yöntem aşağıdadır.

### Yöntem 1: Windows Güvenliği Arayüzü İle Kapatma (Önerilen)

1. **Başlat** menüsüne tıklayın ve **Windows Güvenliği** yazıp uygulamayı açın.
2. Sol menüden **Cihaz Güvenliği** sekmesine geçin.
3. **Çekirdek Yalıtım (Core Isolation)** başlığı altındaki **Çekirdek yalıtım ayrıntıları** bağlantısına tıklayın.
4. **Bellek Bütünlüğü (Memory Integrity)** seçeneğini **KAPALI** konumuna getirin.
5. Değişikliklerin etkili olması için **bilgisayarınızı yeniden başlatın**.

```markdown
Windows Güvenliği > Cihaz Güvenliği > Çekirdek Yalıtım Ayrıntıları > Bellek Bütünlüğü -> Kapalı
```

### Yöntem 2: Komut İstemi (CMD) Kullanarak VBS'i Tamamen Devre Dışı Bırakma

Arayüzden kapatılmasına rağmen VBS'in arka planda tetiklendiği durumlar için:

1. **Başlat** menüsüne `cmd` yazın, **Komut İstemi**'ne sağ tıklayıp **Yönetici olarak çalıştır**'ı seçin.
2. Aşağıdaki komutu yapıştırın ve **Enter** tuşuna basın:

```bash
bcdedit /set hypervisorlaunchtype off
```

3. İşlem tamamlandıktan sonra bilgisayarınızı yeniden başlatın.

*(Tekrar açmak isterseniz aynı komutta `off` yerine `auto` yazmanız yeterlidir.)*

---

## VBS'in Kapalı Olduğu Nasıl Kontrol Edilir?

VBS'in gerçekten devre dışı kalıp kalmadığını doğrulamak için:

1. `Windows + R` tuşlarına basarak **Çalıştır** penceresini açın.
2. `msinfo32` yazıp **Enter**'a basın (Sistem Bilgisi penceresi açılacaktır).
3. **Sistem Özeti** sekmesinde aşağı kaydırın ve **Sanal Büyüklük Tabanlı Güvenlik** öğesini bulun.
4. Karşısında **"Etkin değil"** yazıyorsa VBS başarıyla kapatılmış demektir.

---

## Özet ve Teknik Değerlendirme

Windows 11'de VBS'i kapatmak **sisteme veya donanıma hiçbir zarar vermez**. Windows 10 varsayılan olarak VBS kapalı şekilde çalışıyordu ve milyonlarca kullanıcı bu şekilde sistemi güvenle kullandı. 

Eğer sisteminizi kişisel kullanım, oyun ve genel eğlence amacıyla kullanıyorsanız; kaliteli bir antivirüs yazılımı ve bilinçli internet kullanımıyla **VBS'i kapatıp sistem performansını artırmak teknik olarak mantıklı ve mantıklı bir tercihtir.**