---
title: "RX 570 undervolt ayarları"
description: "RX 570 undervolt ayarları hakkında detaylı teknik rehber, performans analizi ve karşılaştırma."
---

# RX 570 Undervolt Ayarları Rehberi: Sıcaklık ve Güç Tüketimini Düşürme

AMD Radeon RX 570, Polaris mimarisinin en popüler ekran kartlarından biridir. Ancak fabrika çıkışlı voltaj değerleri (stock voltage) genellikle gereğinden yüksek ayarlanmıştır. Bu durum kartın yüksek sıcaklıklara ulaşmasına, fan gürültüsüne ve termal darboğaza (thermal throttling) girmesine neden olur. 

**Undervolt (voltaj düşürme)** işlemi; ekran kartının çekirdek frekansını koruyarak veya artırarak, çekirdeğe verilen voltajı azaltma işlemidir. Doğru yapılan bir undervolt ile RX 570 kartınızda **5-15°C sıcaklık düşüşü**, **%15-25 güç tasarrufu** ve daha kararlı bir FPS eğrisi elde edebilirsiniz.

---

## Gereksinimler ve Ön Hazırlık

İşleme başlamadan önce sisteminizde aşağıdaki yazılımların güncel olduğundan emin olun:

1. **Sürücü:** AMD Radeon Software Adrenalin Edition (Güncel sürüm).
2. **Stres Testi Yazılımı:** FurMark veya MSI Kombustor.
3. **İzleme Yazılımı:** HWiNFO64 veya MSI Afterburner (Sıcaklık ve güç tüketimini anlık takip etmek için).

> **Not:** Undervolt işlemi donanıma kalıcı zarar vermez. Kararsız bir değer girildiğinde sürücü çöker (WattMan hatası) ve sistem fabrika ayarlarına geri döner.

---

## AMD Radeon Software ile Adım Adım RX 570 Undervolt

Undervolt işlemi için üçüncü taraf yazılımlar yerine AMD'nin kendi sürücüsü olan Radeon Software kullanılması tavsiye edilir.

### 1. Ayar Menüsüne Erişim
1. Masaüstüne sağ tıklayıp **AMD Radeon Software**'i açın.
2. Üst menüden **Performans** tabına, ardından **Ayarlanıyor (Tuning)** sekmesine tıklayın.
3. Manuel Ayarlama seçeneğini **Özel (Custom)** olarak değiştirin.

### 2. GPU Ayarları ve Voltaj Kontrolü
1. **GPU Ayarlaması (GPU Tuning)** seçeneğini aktif edin.
2. **Gelişmiş Kontrol (Advanced Control)** anahtarını açık konuma getirin.
3. **Voltaj Kontrolü (Voltage Control)** anahtarını **Manuel** yapın.

Bu aşamada karşınıza `State 0` ile `State 7` arasında değişen durum frekansları ve voltaj değerleri (mV cinsinden) çıkacaktır.

---

## Önerilen RX 570 Undervolt Değerleri (P-State Tablosu)

RX 570 kartlarında silikon kalitesi (silicon lottery) değişkendir. Aşağıdaki tablo, çoğu RX 570 (4GB ve 8GB) modeli için geçerli olan **stabil ve optimize edilmiş referans değerlerdir**.

Fabrika çıkışında `State 7` voltajı genellikle **1150 mV** seviyesindedir. Hedefimiz bu değeri performans kaybı olmadan **1000 mV - 1050 mV** bandına çekmektir.

| P-State | Frekans (MHz) | Stok Voltaj (mV) | **Önerilen Undervolt Voltajı (mV)** |
| :--- | :--- | :--- | :--- |
| **State 1** | 300 | 750 | 750 (Sabit Bırakın) |
| **State 2** | 600 | 800 | 800 (Sabit Bırakın) |
| **State 3** | 900 | 900 | 875 |
| **State 4** | 1145 | 1000 | 925 |
| **State 5** | 1200 | 1075 | 960 |
| **State 6** | 1240 | 1125 | 990 |
| **State 7** | 1244 - 1280 | 1150 | **1015 - 1030** |

> **İpucu:** Eğer kartınız fabrikasyon çıkışlı overclocklu ise (Örn: 1300 MHz), `State 7` için voltajı **1030 mV - 1050 mV** arasında tutmanız gerekebilir.

---

## VRAM (Bellek) ve Güç Limiti Ayarları

### Bellek Ayarlaması (VRAM Tuning)
- **VRAM Tuning** anahtarını aktif edin.
- Bellek voltaj kontrolünü manuel yapın. 
- Bellek voltajı (Memory Voltage) varsayılan olarak **950 mV** değerindedir. RX 570 modellerinde bellek voltajını düşürmek yerine **950 mV** seviyesinde sabitlemek sistem kararlılığı için en güvenli yoldur.
- Bellek frekansını stok değerinde (Genellikle 1750 MHz veya 2000 MHz) bırakın.

### Güç Limiti (Power Limit)
- **Güç Ayarlaması (Power Tuning)** anahtarını açın.
- Güç Limitini **+%10 ile +%20** arasında bir değere getirin.
- *Neden?* Güç limitini artırmak voltajı yükseltmez; kartın yüksek yük altında güç limitine takılıp frekans düşürmesini (throttling) engeller.

---

## Kararlılık (Stability) Testi Nasıl Yapılır?

Ayarları uyguladıktan sonra konfigürasyonun stabil çalışıp çalışmadığı test edilmelidir.

1. **FurMark Testi:** FurMark uygulamasını başlatın. 1080P çözünürlükte en az **15-20 dakika** çalıştırın.
   - Ekranda çizgi, kilitlenme, yeşil kareler (artifact) oluşmamalıdır.
   - Sıcaklık değerlerini takip edin. Hedef sıcaklık yük altında **65°C - 72°C** arasıdır.
2. **Oyun Testi:** Ağır grafikli bir oyuna (Red Dead Redemption 2, Cyberpunk 2077, Metro Exodus vb.) girerek en az 30 dakika oynayın. Sentetik testlerde kapanmayan kartlar oyun içinde çökebilir.

### Test Sonucuna Göre Aksiyon Alma:
- **Sistem Çökerse / Oyun Kapanırsa:** Voltajı adım adım **+10 mV** veya **+15 mV** artırın (Örn: 1015 mV -> 1030 mV).
- **Sistem Stabil ve Sıcaklık Düşükse:** Voltajı daha da düşürmeyi deneyebilirsiniz (**-10 mV** azaltarak sınır noktayı bulun).

---

## Olası Sorunlar ve WattMan Hatası Çözümü

Undervolt denemelerinde sistem kararsızlaştığında ekran kararabilir ve AMD sürücüsü **"Sistem bir WattMan hatası nedeniyle varsayılan ayarlara geri döndü"** uyarısı verebilir.

1. **Profil Kaydetme:** Her stabil ayardan sonra Radeon Software üzerinden sağ üstteki simgeden profilinizi bilgisayarınıza `.xml` dosyası olarak kaydedin. Sıfırlanma durumunda profili tek tıkla geri yükleyebilirsiniz.
2. **Windows Hızlı Başlatmayı Kapatma:** Windows'un "Hızlı Başlat" (Fast Startup) özelliği, bilgisayar her açıldığında AMD sürücü ayarlarını sıfırlayabilir. Güç Seçenekleri üzerinden bu özelliği devre dışı bırakın.
3. **MPO (Multi-Plane Overlay) Devre Dışı Bırakma:** AMD kartlarda anlık siyah ekran sorunlarını önlemek için Windows MPO özelliğini regedit üzerinden kapatabilirsiniz.

---

## Özet ve Beklenen Sonuçlar

Başarılı bir RX 570 undervolt işlemi sonrasında elde edilecek ortalama kazanımlar şunlardır:

* **Çekirdek Voltajı:** 1150 mV $\rightarrow$ 1020 mV
* **Güç Tüketimi:** ~135W $\rightarrow$ ~95W - 105W
* **Çalışma Sıcaklığı:** 78°C $\rightarrow$ 64°C - 68°C
* **Fan Devri:** %70 (Gürültülü) $\rightarrow$ %40 - %50 (Sessiz)

Undervolt, bileşen ömrünü uzatan ve ekran kartının tam performansla, ısınmadan çalışmasını sağlayan en etkili donanım optimizasyonudur.