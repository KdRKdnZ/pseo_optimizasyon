# Windows 10 vs Windows 11 Oyun Performansı: Teknik Karşılaştırma ve FPS Analizi

Windows 10 ve Windows 11 arasındaki oyun performansı farkı, işletim sistemlerinin çekirdek (kernel) seviyesindeki mimari değişiklikler, grafik API optimizasyonları ve donanım kaynak yönetimi ile doğrudan ilişkilidir. Modern donanımlarda bu iki işletim sistemi arasındaki kare hızı (FPS), kare zamanlaması (frame pacing) ve yükleme süreleri belirgin teknik farklılıklar gösterir.

Bu makalede, Windows 10 ve Windows 11'in oyun performansına etkisi; işlemci mimarisi, grafik teknolojileri, bellek yönetimi ve güvenlik protokolleri çerçevesinde teknik olarak incelenmiştir.

---

## 1. İşlemci Mimarisi ve Çizelgeleme (Thread Director)

İşlemci kaynaklarının oyun süreçlerine aktarılması, işletim sisteminin çizelgeleyicisine (scheduler) bağlıdır.

*   **Intel Hibrit Mimarisi (12., 13. ve 14. Nesil):** Intel'in Performans (P-Core) ve Verimlilik (E-Core) çekirdeklerini içeren hibrit mimarisinde Windows 11 açık bir üstünlüğe sahiptir. Windows 11, Intel **Thread Director** teknolojisini çekirdek düzeyinde tam entegre olarak destekler. Bu sayede oyun iş parçacıkları (threads) doğrudan P-Çekirdeklerine atanırken, arka plan işlemleri E-Çekirdeklerine yönlendirilir. Windows 10'da bu ayrım optimum düzeyde yapılamadığı için oyun kodları yanlışlıkla E-Çekirdeklerinde çalıştırılabilir ve bu durum %1 low FPS değerlerinde ani düşüşlere (stuttering/anlık takılma) yol açabilir.
*   **AMD Ryzen ve 3D V-Cache Teknolojisi:** AMD Ryzen 7000 ve özellikle 3D V-Cache (örneğin Ryzen 7 7800X3D) mimarisine sahip işlemcilerde Windows 11, yenilenen chipset sürücüleri ve oyun modu entegrasyonu sayesinde zımni bellek (L3 Cache) erişimini daha efektif yönetir. Windows 10’da bu optimizasyonlar belirli güncellemelerle sunulsa da Windows 11 mimarisi önbellek yönlendirmesinde daha kararlıdır.

---

## 2. Grafik Teknolojileri ve Depolama Mimarisi

Windows 11, oyun içi görsel işleme ve veri aktarım hatlarında yeni standartlar sunar.

### DirectStorage Teknolojisi
*   **Windows 11:** DirectStorage API'si, oyun verilerinin (kaplamalar, modeller) NVMe SSD'den Doğrudan Ekran Kartı VRAM'ine aktarılmasını sağlar. İşlemci (CPU) üzerindeki dekompresyon yükü tamamen kaldırılır. Windows 11, doğrudan depolama sürücü yığınına (storage driver stack) sahip olduğu için NVMe SSD'lerin potansiyelini tam olarak kullanır. Oyun yükleme süreleri 1 saniyenin altına inebilir.
*   **Windows 10:** DirectStorage, Windows 10’a da taşınmıştır ancak işletim sisteminin eski depolama sürücü katmanı nedeniyle veri akışı önce CPU'ya uğrar. Bu durum, Windows 11'deki kadar yüksek bant genişliği ve düşük gecikme sağlamaz.

### Auto HDR ve Pencereli Oyun Optimizasyonu
*   **Auto HDR:** Windows 11, DirectX 11 ve DirectX 12 kullanan SDR oyunları makine öğrenimi algoritmalarıyla otomatik olarak HDR formatına dönüştürür. Windows 10'da bu özellik bulunmamaktadır; kullanıcılar HDR'ı manuel olarak açmak zorundadır ve renk haritalaması tam kararlılık göstermez.
*   **Optimizations for Windowed Games:** Windows 11, "Tam Ekran Pencereli" (Borderless Windowed) modda çalışan oyunlar için DirectX 9, 10 ve 11 API'lerinde gecikmeyi düşüren, Değişken Yenileme Hızını (VRR) ve Auto HDR'ı aktif eden yeni bir çevirme modeli (Flip Model) kullanır. Windows 10'da bu modlarda girdi gecikmesi (input lag) daha yüksektir.

---

## 3. Güvenlik Protokollerinin Performansa Etkisi: VBS ve HVCI

Windows 11 ile birlikte varsayılan olarak gelen bazı güvenlik katmanları oyun performansını olumsuz etkileyebilir.

*   **VBS (Virtualization-based Security) ve HVCI (Hypervisor-Enforced Code Integrity):** Windows 11 temiz kurulumlarında VBS ve HVCI özellikleri varsayılan olarak açık gelir. Bu özellikler bellekte güvenli bir alan oluşturarak zararlı kodların yürütülmesini engeller.
*   **Performans Kaybı:** VBS açık olduğunda, işlemcinin sanallaştırma komut setleri sürekli çalışır. Bu durum ekran kartı ve işlemci arasındaki veri akışında bant genişliği kısıtlamasına yol açarak oyunlarda **%3 ile %15 arasında FPS kaybına** neden olabilir.
*   **Çözüm:** Windows 11 üzerinde maksimum oyun performansı elde etmek için VBS ve HVCI özelliklerinin kayıt defteri (Registry) veya Windows Güvenliği ayarlarından kapatılması önerilir. Windows 10'da bu özellik varsayılan olarak kapalıdır.

---

## 4. Bellek (RAM) ve Arka Plan Kaynak Yönetimi

| Metrik | Windows 10 | Windows 11 |
| :--- | :--- | :--- |
| **Boşta RAM Kullanımı (Sistem Boşta)** | ~2.5 GB - 3.0 GB | ~3.5 GB - 4.5 GB |
| **Arka Plan Süreç Önceliği** | Standart İş Parçacığı Önceliği | Gelişmiş Ön Plan / Oyun Modu Önceliği |
| **DirectX 12 Ultimate Desteği** | Var | Tam Entegre ve İyileştirilmiş |
| **Pencereli Mod Girdi Gecikmesi** | Yüksek | Düşük (Flip Model Optimizasyonu) |

Windows 11, görsel arayüzü (Fluent Design) ve yeni arka plan servisleri nedeniyle Windows 10'a kıyasla sistem boşta iken yaklaşık 1 GB daha fazla RAM tüketir. **16 GB veya 32 GB RAM** kullanan sistemlerde bu durum oyun performansını etkilemez. Ancak **8 GB RAM** kapasitesine sahip sistemlerde Windows 10, bellek taşmalarını (pagefile kullanımı) önlediği için daha stabil bir oyun deneyimi sunar.

---

## 5. Gerçek Dünya FPS ve Benchmark Karşılaştırması

İki işletim sistemi arasındaki FPS değerleri, donanımın jenerasyonuna göre değişiklik gösterir:

1.  **Modern Donanım (Intel 13./14. Nesil, Ryzen 7000/9000, RTX 4000 / RX 7000 Serisi):**
    *   **Ortalama FPS:** Windows 11, Windows 10'a göre %1 ile %3 arasında daha yüksek ortalama FPS değerleri verir.
    *   **%1 Low / %0.1 Low FPS:** Windows 11'in daha gelişmiş işlemci çizelgeleyicisi sayesinde anlık FPS düşüşleri daha az yaşanır. Frame time grafiği daha düzgündür.
2.  **Eski Donanım (Intel 10./11. Nesil ve Altı, Ryzen 3000 Serisi ve Altı, GTX 10 / RX 500 Serisi):**
    *   **Ortalama FPS:** Windows 10, Windows 11 ile ya başa baş performans gösterir ya da %2 ila %5 arasında daha yüksek FPS sunar.
    *   **Neden:** Eski donanımlarda Windows 11'in ek güvenlik ve görsel arayüz yükleri işlemciye ek yük getirir.

---

## Sonuç: Hangi İşletim Sistemi Tercih Edilmeli?

*   **Windows 11 Tercih Edilmeli:**
    *   Intel 12. nesil ve üzeri (hibrit mimarili) işlemci kullananlar.
    *   NVMe Gen4 veya Gen5 SSD sahibi olup DirectStorage destekli oyunları oynayanlar.
    *   HDR monitör kullanan ve Auto HDR teknolojisinden yararlanmak isteyenler.
    *   Oyunları "Borderless Windowed" (Pencereli Tam Ekran) modunda oynayanlar.
    *   *Not: En yüksek FPS için VBS (Sanal Tabanlı Güvenlik) devre dışı bırakılmalıdır.*

*   **Windows 10 Tercih Edilmeli:**
    *   Intel 11. nesil veya AMD Ryzen 3000 serisi ve öncesi işlemci kullananlar.
    *   Sisteminde 8 GB RAM bulunan oyuncular.
    *   E-spor oyunlarında (CS2, Valorant vb.) VBS ayarlarıyla uğraşmadan en düşük işletim sistemi gecikmesini (system latency) hedefleyenler.