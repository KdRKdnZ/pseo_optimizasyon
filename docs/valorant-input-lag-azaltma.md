---
title: "valorant input lag azaltma"
description: "valorant input lag azaltma hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# Valorant Input Lag Azaltma: Sistem Gecikmesini Minimuma İndirme Rehberi

Input lag (giriş gecikmesi), farenizle yaptığınız bir hareketin veya klavyede bastığınız bir tuşun ekranda eyleme dönüşmesi arasında geçen süredir. Valorant gibi milisaniyelik reaksiyonların kritik olduğu tactical-shooter oyunlarında yüksek input lag, mermilerin gitmemesine, sprey kontrolünün bozulmasına ve rakibi önce görmenize rağmen kaybetmenize neden olur.

Sistem gecikmesi; **Çevre Birimi Gecikmesi**, **İşleme/PC Gecikmesi** ve **Ekran Gecikmesi** olmak üzere üç ana bileşenden oluşur. Bu rehberde, Valorant'ta input lag değerini donanımsal ve yazılımsal olarak en alt seviyeye çekecek teknik yöntemleri bulabilirsiniz.

---

## 1. Valorant Oyun İçi Ayarlarının Optimizasyonu

Gecikmeyi azaltmanın ilk ve en etkili adımı oyun içi motor ayarlarını doğru yapılandırmaktır.

*   **NVIDIA Reflex Low Latency:** 
    *   *Açık (On):* Sistem gecikmesini düşürür, ekran kartı sınırına takılan sistemlerde CPU ve GPU senkronizasyonunu sağlar.
    *   *Açık + Takviye (On + Boost):* GPU saat hızlarını maksimumda tutarak güç tasarrufu moduna geçmesini engeller. Ekran kartı sıcaklıklarınız normalse bu ayarı **Açık + Takviye** olarak kullanın.
*   **Ham Girdi Tamponu (Raw Input Buffer):**
    *   Ayarın **Açık** konumda olması gerekir. Bu özellik, Windows'un fare verilerini işlemesini aradan çıkararak doğrudan oyun motoruna iletir. Özellikle 1000 Hz ve üzeri tarama hızına (polling rate) sahip farelerde CPU yükünü azaltır ve gecikmeyi düşürür.
*   **Kare Hızı Sınırlama (FPS Limit):**
    *   NVIDIA Reflex aktifken FPS sınırlayıcıyı **Kapatın**. Reflex, gecikmeyi optimize etmek için kare hızını dinamik olarak yönetir. 
    *   *İstisna:* Monitörünüzün yenileme hızının çok üzerinde FPS alıyorsanız ve sistemde dalgalanma oluyorsa, monitör Hz değerinizin %10-15 üzerinde sabit bir FPS sınırı koymak (örn. 244 Hz için 280 FPS) frametime (kare süresi) tutarlılığı sağlar.
*   **V-Sync ve G-Sync / FreeSync:**
    *   **V-Sync:** Kesinlikle **Kapalı** olmalıdır. V-Sync, kareleri ekrana senkronize etmek için arabelleğe alır ve yüksek miktarda input lag oluşturur.
    *   **G-Sync/FreeSync:** Rekabetçi oyunlarda en düşük gecikme için **Kapalı** tutulması önerilir.
*   **Grafik Kalitesi Ayarları:**
    *   Görsel kaliteden ziyade kare hızını ve GPU yükünü optimize etmek için tüm grafik detaylarını (Materyal, Doku, Ayrıntı, Kalite) **Düşük** seviyeye getirin.
    *   **Bozulmasızlık (Anti-Aliasing):** Kapalı veya FXAA.
    *   **Eşyönsüz Süzme (Anisotropic Filtering):** 1x.

---

## 2. Ekran Kartı Sürücü Ayarları (NVIDIA & AMD)

Sürücü seviyesindeki gecikme engelleme teknolojileri, kare kuyruğunu (frame queue) temizleyerek tepki süresini hızlandırır.

### NVIDIA Denetim Masası
1. **Masaüstüne sağ tıklayın** ve NVIDIA Denetim Masası'nı açın.
2. **3D Ayarlarının Yönetilmesi** bölümüne gidin.
3. Aşağıdaki ayarları uygulayın:
   *   **Düşük Gecikme Oranı Modu (Low Latency Mode):** Ultra (Oyun içi NVIDIA Reflex kapalıysa etkilidir; Reflex açıkken kontrolü oyuna devreder ancak varsayılan olarak Ultra kalması önerilir).
   *   **Güç Yönetimi Modu:** Maksimum performansı tercih et.
   *   **Doku Süzme - Kalite:** Yüksek performans.
   *   **Dikey Eşitleme (V-Sync):** Kapalı.
   *   **Arka Plan Uygulamaları Maksimum Kare Hızı:** Kapalı.

### AMD Radeon Software
1. AMD Radeon Software panelini açın ve **Ayarlar > Ekran Kartları** sekmesine gelin.
2. **Radeon Anti-Lag:** Açık (NVIDIA Reflex benzeri bir gecikme düşürme teknolojisidir).
3. **Radeon Boost:** Kapalı (Çözünürlüğü dinamik değiştirdiği için kas hafızasını olumsuz etkileyebilir).
4. **Radeon Chill:** Kapalı.
5. **Wait for Vertical Refresh (Dikey Yenileme Bekleme):** Always Off (Her Zaman Kapalı).

---

## 3. Windows İşletim Sistemi Optimizasyonları

Windows'un varsayılan arka plan süreçleri ve görsel efektleri gecikmeye sebebiyet verebilir.

### Donanım Hızlandırmalı GPU Zamanlaması (HAGS)
Windows 10 (2004 ve üzeri) ve Windows 11'de bulunan bu özellik, GPU belleğini yönetme görevini CPU'dan alıp GPU'ya devreder.
*   **Yol:** `Ayarlar > Sistem > Ekran > Grafik Ayarları`
*   **Eylem:** **Donanım Hızlandırmalı GPU Zamanlaması** seçeneğini **Açık** konuma getirin ve bilgisayarı yeniden başlatın. *(Not: Bazı alt segment sistemlerde ters etki yapabileceğinden test edilmesi önerilir).*

### Tam Ekran İyileştirmelerini Devre Dışı Bırakma
Windows'un pencereli tam ekran modunu zorlamasını engeller.
1. `VALORANT-Win64-Shipping.exe` dosyasını bulun (Varsayılan: `C:\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64`).
2. Dosyaya sağ tıklayıp **Özellikler** > **Uyumluluk** sekmesine geçin.
3. **"Tam ekran iyileştirmelerini devre dışı bırak"** seçeneğini işaretleyin.
4. **"Yüksek DPI ayarlarını değiştir"** butonuna tıklayın ve **"Yüksek DPI ölçekleme davranışını geçersiz kıl"** seçeneğini işaretleyip **Uygulama** seçeneğini seçin.

### Fare İvmesini Kapatma (Pointer Precision)
Windows'un fare hareketlerinize yapay hızlandırma eklemesini engeller.
1. `Denetim Masası > Fare > İşaretçi Seçenekleri` yolunu izleyin.
2. **"İşaretçi hassasiyetini arttır"** seçeneğindeki işareti **kaldırın**.
3. Çizgiyi tam ortadaki 6/11 konumunda bırakın.

### Windows Oyun Modu (Game Mode)
*   `Ayarlar > Oyun > Oyun Modu` sekmesinden **Oyun Modu'nu Açık** hale getirin. Bu işlem, Windows'un arka plan güncellemelerini ve kaynak kullanımını kısıtlayarak işlemci önceliğini Valorant'a verir.

---

## 4. Donanım ve Çevre Birimi Ayarları

### Fare Polling Rate (Tarama Hızı)
Farenizin bilgisayara saniyede kaç kez konum bildirdiğini belirler.
*   **1000 Hz:** Standart ve en kararlı değerdir (1ms gecikme).
*   **2000 Hz / 4000 Hz / 8000 Hz:** Güçlü bir CPU'nuz (Ryzen 7000 serisi veya Intel 13./14. Nesil) varsa kullanılmalıdır. Zayıf CPU'larda mikro takılmalara (stuttering) yol açabilir. Oyun içinde *Ham Girdi Tamponu* kesinlikle açık olmalıdır.

### Monitör Overdrive ve Yenileme Hızı
*   **Ekran Yenileme Hızı:** Windows Ekran Ayarları ve Monitör OSD menüsünden monitörünüzün desteklediği en yüksek Hz değerinin (144Hz, 240Hz, 360Hz vb.) seçili olduğundan emin olun.
*   **Response Time / Overdrive:** Monitörünüzün OSD menüsünden piksel yanıt süresini hızlandıran ayarı bulun (Fast/Faster). En yüksek moda ("Extreme/Ultra Fast") alırken dikkat edin; piksel tersine gölgelenme (Inverse Ghosting / Overshoot) yapıyorsa bir alt seviyeye çekin.

---

## 5. İleri Seviye Sistem Ayarları (BIOS ve Registry)

### HPET (High Precision Event Timer) Devre Dışı Bırakma
HPET, Windows'un zamanlama mimarisidir ve bazı sistemlerde gecikmeyi artırabilir.

1. Komut İstemi'ni (CMD) **Yönetici olarak** çalıştırın.
2. Şu komutu girin ve Enter'a basın:
   ```cmd
   bcdedit /set useplatformclock false
   ```
3. Ardından dinamik kene özelliğini kapatmak için şu komutu girin:
   ```cmd
   bcdedit /set disabledynamictick yes
   ```
4. Bilgisayarı yeniden başlatın.

### BIOS Ayarları
*   **XMP / DOCP:** RAM'lerinizin vaat edilen yüksek frekans ve düşük gecikme (CL) değerlerinde çalıştığından emin olmak için BIOS üzerinden XMP/DOCP profilini aktif edin. RAM gecikmesi, doğrudan sistem input lag'ini etkiler.
*   **C-States (Power Saving):** BIOS üzerindeki işlemci güç tasarruf modlarını (C-States, C1E) kapatmak, işlemcinin sürekli maksimum frekansta kalmasını sağlayarak voltaj dalgalanmalarından kaynaklanan gecikmeleri önler.

---

## Özet Kontrol Listesi

| Alan | Yapılması Gereken Eylem | Hedef Etki |
| :--- | :--- | :--- |
| **Oyun İçi** | NVIDIA Reflex: Açık + Boost | GPU kuyruk gecikmesini sıfırlama |
| **Oyun İçi** | Ham Girdi Tamponu: Açık | Doğrudan fare girdisi işleme |
| **Sürücü** | Düşük Gecikme Modu: Ultra / Anti-Lag | Kare işleme süresini düşürme |
| **Windows** | Tam Ekran İyileştirmelerini Kapat | DWM (Desktop Window Manager) gecikmesini baypas etme |
| **Donanım** | XMP/DOCP Açık, High Hz Aktif | Sistem genel bant genişliğini artırma |