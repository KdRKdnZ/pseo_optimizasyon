---
title: Intensive care ünitesinde kullanılan monitörlerin teknik verileri
description: Intensive care ünitesinde kullanılan monitörlerin teknik verileri hakkında detaylı optimizasyon ve donanım rehberi.
---

# Intensive Care Ünitesinde Kullanılan Monitörlerin Teknik Verileri

Yoğun bakım ünitelerinde (ICU - Intensive Care Unit) kullanılan hasta başı monitörleri, kritik durumdaki hastaların fizyolojik parametrelerini kesintisiz olarak takip eden, yüksek hassasiyetli medikal cihazlardır. Bir yazılım mimarı ve donanım uzmanı gözüyle bakıldığında bu cihazlar; düşük gürültülü analog ön uçlar (AFE), yüksek çözünürlüklü analog-dijital dönüştürücüler (ADC), gerçek zamanlı işletim sistemleri (RTOS) ve kesintisiz veri entegrasyonu sağlayan haberleşme protokollerinin birleştiği gömülü sistemlerdir.

---

## Donanım Mimarisi ve Sensör Teknolojileri

Yoğun bakım monitörlerinin donanım mimarisi, insan vücudundan alınan mikrovolt ($\mu V$) ve milivolt ($mV$) seviyesindeki analog sinyallerin gürültüden arındırılarak dijitalleştirilmesi esasına dayanır.

```
[Hasta] -> [Sensörler/Elektrotlar] -> [Analog Ön Uç (AFE)] -> [ADC (24-bit)] -> [MCU/DSP] -> [RTOS / Ekran / Ağ]
```

### EKG (Elektrokardiyografi) ve Sinyal İşleme Blokları

EKG modülü, kalbin elektriksel aktivitesini ölçmek için 3, 5 veya 12 kanallı (lead) kablo konfigürasyonları kullanır.

*   **Giriş Empedansı:** Hasta güvenliği ve sinyal kalitesi için giriş empedansı $> 100 \, M\Omega$ seviyesindedir.
*   **Ortak Mod Bastırma Oranı (CMRR):** Şebeke gürültüsünü (50 Hz / 60 Hz) filtrelemek için CMRR değeri en az $100 \, dB$ (ideal olarak $> 120 \, dB$) olmalıdır.
*   **Örnekleme Hızı (Sampling Rate):** Sinyal analizi ve pacemaker (kalp pili) tespiti için kanal başına minimum $500 \, Hz$ ile $8000 \, Hz$ arasında örnekleme yapılır.
*   **ADC Çözünürlüğü:** Genellikle ardışık yaklaşımlı (SAR) veya Delta-Sigma ($\Delta\Sigma$) mimarisine sahip **24-bit ADC**'ler (örneğin, Texas Instruments ADS1298 serisi) kullanılır. Bu, $nV$ (nanovolt) seviyesindeki değişimlerin bile çözümlenmesini sağlar.

### SpO2 (Nabız Oksimetresi) ve Optik Alıcılar

SpO2 modülü, kandaki oksihemoglobin ($HbO_2$) ve deoksihemoglobin ($Hb$) oranını ölçmek için Beer-Lambert kanununu kullanır.

*   **Işık Dalga Boyları:** Kırmızı ışık ($660 \, nm$) ve Kızılötesi (Infrared) ışık ($940 \, nm$) LED'leri kullanılır.
*   **Ölçüm Aralığı ve Hassasiyet:** $\%70$ - $\%100$ aralığında ölçüm doğruluğu $\pm \%2$ tolerans sınırındadır. Perfüzyon indeksi (PI) $\%0.05$ gibi çok düşük seviyelerde bile cihazın kararlı çalışması gerekir.
*   **Sürücü Devresi:** LED akımları, ortam ışığının etkisini (ambient light cancellation) yok etmek için yüksek frekanslarda ($1 \, kHz$ - $4 \, kHz$) modüle edilerek sürülür.

### İnvaziv ve Non-İnvaziv Kan Basıncı (IBP/NIBP) Sensörleri

*   **NIBP (Non-İnvaziv):** Osilometrik yöntemle çalışır. Manşet içi basınç sensörü $0$ ila $300 \, mmHg$ aralığında ölçüm yapar. Basınç çözünürlüğü $1 \, mmHg$, doğruluğu ise $\pm 3 \, mmHg$ seviyesindedir. Donanımsal aşırı basınç koruma valfi (overpressure protection) $300 \, mmHg$ (yetişkin için) değerinde mekanik olarak devreye girer.
*   **IBP (İnvaziv):** Doğrudan arter içine yerleştirilen kateter uçlu piezo-rezistif basınç transdüserleri kullanılır. Ölçüm aralığı $-50$ ila $+300 \, mmHg$ arasındadır. Frekans yanıtı (frequency response) DC ile $40 \, Hz$ arasındadır ve örnekleme hızı en az $100 \, Hz$'dir.

---

## Veri İletişim Protokolleri ve Yazılım Mimarisi

Yoğun bakım monitörleri, ürettikleri kritik verileri hastane bilgi yönetim sistemlerine (HBYS) ve merkezi izleme istasyonlarına (Central Station) gecikmesiz aktarmak zorundadır.

### HL7 (Health Level Seven) Entegrasyonu

Monitörler, hasta demografik bilgilerini almak ve hayati bulguları (vitals) dışa aktarmak için **HL7 v2.x** veya modern sistemlerde **HL7 FHIR (Fast Healthcare Interoperability Resources)** standartlarını kullanır.

Aşağıda, bir hasta başı monitörünün merkezi sisteme gönderdiği örnek bir HL7 v2.5 OBX (Observation/Result) segment yapısı gösterilmiştir:

```text
MSH|^~\&|MONITOR_ICU_04|HOSPITAL_A|CENTRAL_STATION|HOSPITAL_A|20231027143000||ORU^R01^ORU_R01|MSG00001|P|2.5
PID|1||12345678901^^^MRN||YILMAZ^AHMET||19750512|M
OBX|1|NM|8867-4^Heart rate^LN||72|bpm/min|60-100|N|||F|||20231027143000
OBX|2|NM|2708-6^Oxygen saturation^LN||98|%|95-100|N|||F|||20231027143000
```

*   **IEEE 11073 (PHD):** Cihazlar arası birlikte çalışabilirlik (interoperability) için tıbbi cihaz haberleşme standardı olan **ISO/IEEE 11073** ailesi kullanılır. Bu standart, verilerin semantik olarak doğru yorumlanmasını garanti eder.

### Gerçek Zamanlı İşletim Sistemleri (RTOS) ve Güvenilirlik

Yoğun bakım monitörlerinde genel amaçlı işletim sistemleri (Windows, standart Linux) yerine deterministik çalışan **RTOS (Real-Time Operating System)** mimarileri tercih edilir. Yaygın olarak kullanılan RTOS'lar şunlardır:
*   **VxWorks**
*   **QNX Neutrino**
*   **FreeRTOS** (Daha düşük maliyetli/mikrodenetleyici tabanlı modüllerde)

#### RTOS Tercih Nedenleri ve Teknik Parametreler:
1.  **Görev Önceliği (Task Prioritization):** EKG aritmi analizi ve alarm üretimi en yüksek önceliğe (highest priority) sahipken, ekran arayüzünün güncellenmesi daha düşük önceliklidir.
2.  **Gecikme Süresi (Latency):** Kesme gecikmesi (interrupt latency) ve bağlam geçiş süresi (context switching time) mikro saniyeler ($\mu s$) seviyesindedir.
3.  **Watchdog Timer (Bekçi Köpeği):** Yazılımsal veya donanımsal kilitlenmeleri önlemek için bağımsız bir donanımsal Watchdog entegresi bulunur. Sistem $100 \, ms$ boyunca "I am alive" sinyali gönderemezse otomatik olarak yeniden başlar.

---

## Elektriksel Güvenlik ve Standartlar

Yoğun bakım monitörleri, doğrudan hastanın kalbine ve dolaşım sistemine bağlı olabildiğinden, elektriksel güvenlik gereksinimleri en üst seviyededir.

### IEC 60601-1 ve Elektromanyetik Uyumluluk (EMC)

*   **IEC 60601-1 (Tıbbi Elektrikli Ekipman Genel Güvenlik Kuralları):** Cihazlar bu standarda uygun olmak zorundadır.
*   **Koruma Sınıfı:** **Sınıf I** (topraklamalı koruma) veya **Sınıf II** (çift yalıtımlı) koruma sınıfındadır.
*   **Uygulanan Kısım Tipi (Applied Part Type):** EKG ve IBP gibi doğrudan kalbe temas eden modüller **Type CF (Cardiac Float)** sınıfındadır. Type CF için izin verilen maksimum hasta kaçak akımı (patient leakage current) normal şartlarda $< 10 \, \mu A$, tek hata durumunda (single fault condition) ise $< 50 \, \mu A$'dir.
*   **Defibrilatör Koruması:** Monitör girişleri, hastaya elektroşok (defibrilasyon) uygulandığında oluşacak yüksek gerilime ($5000 \, V$, $360 \, Joule$) dayanıklı olmalıdır. Giriş hatlarında gaz deşarj tüpleri (GDT) ve hızlı yanıt veren TVS diyotları kullanılır.

---

## Teknik Veri Karşılaştırma Tablosu

Aşağıdaki tablo, standart bir yoğun bakım monitörünün modül bazlı kritik teknik parametrelerini özetlemektedir:

| Parametre | Ölçüm Aralığı | Çözünürlük | Doğruluk / Tolerans | Bant Genişliği / Frekans |
| :--- | :--- | :--- | :--- | :--- |
| **EKG (ECG)** | $15 - 350 \, bpm$ | $1 \, bpm$ | $\pm \%1$ veya $\pm 1 \, bpm$ | Diagnostik: $0.05 - 150 \, Hz$ <br> Monitör: $0.5 - 40 \, Hz$ |
| **SpO2** | $\%0 - \%100$ | $\%1$ | $\pm \%2$ ($\%70-\%100$ arası) | Örnekleme: $50 - 100 \, Hz$ |
| **NIBP** | $10 - 270 \, mmHg$ | $1 \, mmHg$ | $\pm 3 \, mmHg$ | Osilometrik sönümleme hızı |
| **IBP** | $-50 - 300 \, mmHg$ | $1 \, mmHg$ | $\pm \%2$ veya $\pm 1 \, mmHg$ | DC - $40 \, Hz$ |
| **Solunum (Resp)** | $0 - 150 \, rpm$ | $1 \, rpm$ | $\pm 2 \, rpm$ | Empedans Pnömoğrafisi: $0.2 - 2.5 \, \Omega$ |
| **Sıcaklık (Temp)** | $0 - 50 \, ^\circ C$ | $0.1 \, ^\circ C$ | $\pm 0.1 \, ^\circ C$ | YSI 400 serisi uyumlu termistör |