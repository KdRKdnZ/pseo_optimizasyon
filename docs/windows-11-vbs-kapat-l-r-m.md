---
title: "windows 11 vbs kapatılır mı"
description: "windows 11 vbs kapatılır mı hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Windows 11 VBS Kapatılır mı? Performans ve Güvenlik Rehberi

Evet, Windows 11'de VBS (**Virtualization-based Security / Sanallaştırma Tabanlı Güvenlik**) kapatılabilir. Ancak bu işlemi yapmadan önce VBS'nin ne olduğunu, ne işe yaradığını ve kapatıldığında sisteminizde ne gibi değişiklikler olacağını teknik olarak anlamanız gerekir.

Bu rehberde, VBS'nin çalışma mantığını, oyun performansına etkilerini ve adım adım nasıl kapatılacağını bulabilirsiniz.

---

## VBS (Virtualization-based Security) Nedir?

VBS, Windows 11'in (ve Windows 10'un) Donanım Sanallaştırma özelliklerini (Intel VT-x / AMD-V) kullanarak normal işletim sisteminden izole edilmiş, güvenli bir bellek bölgesi oluşturmasını sağlayan bir güvenlik mimarisidir. 

VBS'nin temel amacı, zararlı yazılımların (malware) ve çekirdek seviyesindeki (kernel-level) saldırıların işletim sistemine sızmasını engellemektir. VBS altyapısı üzerinde çalışan en önemli bileşen **HVCI (Hypervisor-Enforced Code Integrity / Çekirdek Yalıtımı - Bellek Bütünlüğü)** özelliğidir.

---

## Windows 11'de VBS Kapatılmalı mı?

VBS'nin kapatılması tamamen **kullanım amacınıza** bağlıdır:

### Neden Kapatılmalı? (Performans Odaklı Yaklaşım)
* **Oyun Performansı (FPS Artışı):** VBS ve HVCI arka planda sürekli olarak bellek doğrulaması yaptığı için işlemciye (CPU) ek yük bindirir. VBS kapatıldığında, özellikle e-spor oyunlarında ve CPU limitli senaryolarda **%5 ile %25 arasında FPS artışı** ve daha kararlı "Frametime" (kare süreleri) elde edilir.
* **Eski Donanımlarda Rahatlama:** Özellikle 10. nesil öncesi Intel veya Ryzen 3000 serisi öncesi AMD işlemcilerde VBS'nin performans yükü daha fazla hissedilir.

### Neden Açık Kalmalı? (Güvenlik Odaklı Yaklaşım)
* **Siber Güvenlik:** VBS, Mimikatz gibi araçlarla yapılan kimlik bilgisi hırsızlığını (Credential Theft) ve Kernel düzeyindeki exploit'leri engeller.
* **Kurumsal Kullanım:** İş bilgisayarlarında ve hassas veri barındıran sistemlerde VBS hayati bir güvenlik katmanıdır.

---

## Windows 11 VBS Nasıl Kapatılır? (Adım Adım)

VBS'yi tamamen devre dışı bırakmak için uygulayabileceğiniz 3 farklı yöntem bulunmaktadır.

### Yöntem 1: Windows Güvenliği Arayüzü ile Kapatma (En Kolay)

1. `Windows + I` tuşlarına basarak **Ayarlar**'ı açın.
2. Sol menüden **Gizlilik ve Güvenlik** > **Windows Güvenliği** sekmesine gidin.
3. **Cihaz Güvenliği** seçeneğine tıklayın.
4. **Çekirdek Yalıtımı (Core Isolation)** başlığı altındaki **Çekirdek yalıtımı ayrıntıları** linkine tıklayın.
5. **Bellek Bütünlüğü (Memory Integrity)** seçeneğini **Kapalı** konuma getirin.
6. Bilgisayarınızı yeniden başlatın.

---

### Yöntem 2: Kayıt Defteri (Regedit) ile Kapatma

Eğer ilk yöntemle VBS tamamen kapanmadıysa Kayıt Defteri üzerinden zorlayabilirsiniz:

1. `Windows + R` tuşlarına basın, `regedit` yazıp Enter'a basın.
2. Şu yola gidin:
   `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\DeviceGuard`
3. Sağ tarafta bulunan `EnableVirtualizationBasedSecurity` değerine çift tıklayın.
4. Değer verisini `0` olarak değiştirin.
5. **Tamam**'a tıklayın ve bilgisayarınızı yeniden başlatın.

---

### Yöntem 3: Komut İstemi (CMD) ile Sanallaştırmayı Devre Dışı Bırakma

VBS'yi çalıştıkran Hypervisor katmanını komut satırı ile kapatabilirsiniz:

1. Başlat menüsüne `cmd` yazın, sağ tıklayıp **Yönetici olarak çalıştır**'ı seçin.
2. Aşağıdaki komutu yapıştırın ve Enter'a basın:
   ```cmd
   bcdedit /set hypervisorlaunchtype off
   ```
3. İşlem tamamlandıktan sonra bilgisayarınızı yeniden başlatın.

*(Not: Hyper-V, WSL2 (Windows Subsystem for Linux) veya BlueStacks/LDPlayer gibi emülatörler kullanıyorsanız, bu komut onları çalışmaz hale getirebilir.)*

---

## VBS'nin Kapalı Olduğu Nasıl Kontrol Edilir?

İşlemin başarılı olup olmadığını doğrulamak için:

1. `Windows + R` tuşlarına basın, `msinfo32` yazıp Enter'a basın (Sistem Bilgisi).
2. Açılan pencerede **Sistem Özet** sekmesinde kalın.
3. Sağ taraftaki listeden **Sanallaştırma tabanlı güvenlik** öğesini bulun.
4. Karşısında **"Etkin değil" (Not enabled)** yazıyorsa VBS başarıyla kapatılmıştır.

---

## Özet ve Karar Tablosu

| Kullanıcı Profili | Önerilen VBS Durumu | Nedeni |
| :--- | :--- | :--- |
| **Oyuncular (Gamers)** | **Kapalı** | Maksimum FPS, düşük gecikme ve takılmasız oyun deneyimi için. |
| **Geliştiriciler / Yazılımcılar** | **Açık** | Sanallaştırma (Docker, WSL2) ve güvenlik gereksinimleri için. |
| **Günlük / Ofis Kullanıcıları** | **Açık** | İnternet üzerindeki zararlı yazılımlara karşı maksimum koruma için. |

**Sonuç:** Bilgisayarınızı ağırlıklı olarak oyun oynamak için kullanıyorsanız ve sisteminizde kritik kurumsal veriler bulunmuyorsa, Windows 11'de VBS'yi kapatmak kayda değer bir performans kazancı sağlayacaktır.