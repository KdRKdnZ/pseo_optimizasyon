# CS2 En İyi Çözünürlük Önerileri: FPS, Görüş Açısı (FOV) ve Teknik Karşılaştırma Rehberi

Counter-Strike 2 (CS2) oyununda doğru çözünürlük ve en-boy oranı (aspect ratio) seçimi; kare hızınızı (FPS), gecikme sürenizi (input lag), rakip modellerinin boyutunu ve ekrandaki toplam görüş alanınızı (FOV) doğrudan etkiler. CS2, Source 2 motoruna geçiş yaptığı için CS:GO'ya kıyasla piksel netliği ve ışıklandırma konusunda daha hassastır. 

Bu rehberde, donanımınıza ve oyun tarzınıza en uygun CS2 çözünürlüğünü seçmeniz için teknik analizleri ve profesyonel oyuncu konfigürasyonlarını bulabilirsiniz.

---

## En-Boy Oranı (Aspect Ratio) Karşılaştırması: 16:9 vs 4:3 vs 16:10

CS2'de çözünürlük tercihinden önce en-boy oranının mekanik etkilerini anlamak gerekir.

```
+------------------+-----------------------+------------------------+
| Özellik          | 16:9 (Yerel / Native) | 4:3 (Stretched / Esnetilmiş) |
+------------------+-----------------------+------------------------+
| Görüş Açısı (FOV)| 106° (Geniş)          | 90° (Dar)              |
| Oyuncu Modelleri | Standart Genişlik     | %33 Daha Geniş         |
| Yatay Fare Hızı  | Standart (1:1)        | Hissedilen Hız Daha Yüksek |
| FPS Verimi       | Düşük / Orta          | Yüksek                 |
| Görsel Netlik    | Çok Yüksek            | Orta / Düşük           |
+------------------+-----------------------+------------------------+
```

### 1. 16:9 (Yerel - Native Çözünürlük)
*   **Görüş Açısı (FOV):** 106 derecedir. Ekranın sağ ve sol kenarlarında daha fazla alan görünür.
*   **Avantajı:** "Tünel görüşü" riskini azaltır. Yan taraflardan gelen düşmanları kaçırma ihtimaliniz düşer. CS2'nin yenilenen grafikleri ve sis bombaları (smoke) en net bu oranda görünür.
*   **Dezavantajı:** Karakter modelleri 4:3 oranına göre daha incedir; hedefe kilitlenmek (aim odaklanması) daha fazla görsel hassasiyet gerektirir.

### 2. 4:3 Esnetilmiş (Stretched)
*   **Görüş Açısı (FOV):** 90 derecedir. Yan taraflar kırpılarak görüntü ekrana yayılır.
*   **Avantajı:** Oyuncu modelleri yatayda %33 oranında genişler. Bu durum hit-box (isabet alanı) boyutunu fiziksel olarak değiştirmese de görsel olarak hedef almayı kolaylaştırır. Piksel sayısı düştüğü için ekran kartına binen yük azalır ve FPS artar.
*   **Dezavantajı:** Yatay düzlemdeki hareketler daha hızlı hissettirir, bu da spray kontrolünü ve yatay takibi zorlaştırabilir. Görüş alanı daraldığı için kenarlardaki rakipleri göremeyebilirsiniz.

### 3. 4:3 Siyah Kenarlıklar (Black Bars)
*   Görüntü esnetilmez, sağ ve sol tarafta siyah bantlar oluşur. Modeller genişlemez, ancak odaklanmayı artırdığı ve eski e-spor alışkanlıklarına dayandığı için tercih edilir.

---

## En Çok Tercih Edilen CS2 Çözünürlükleri ve Teknik Analizi

### 1. 1280x960 (4:3 Stretched) – *En Çok Tercih Edilen Espor Çözünürlüğü*
*   **Tür:** 4:3
*   **Netlik:** Orta
*   **FPS Performansı:** Yüksek
*   **Açıklama:** CS:GO ve CS2 profesyonel sahnesinin en popüler çözünürlüğüdür. Performans ile görsel netlik arasındaki en dengeli noktadır. Karakter modelleri yeterince genişler ve uzak mesafedeki rakipler seçilebilir kalır.

### 2. 1920x1080 (16:9 Native) – *Maksimum Görsel Netlik ve Bilgi*
*   **Tür:** 16:9
*   **Netlik:** Mükemmel
*   **FPS Performansı:** Donanıma Bağlı
*   **Açıklama:** Güçlü bir sisteminiz (RTX 3060 / RX 6600 ve üzeri) ve yüksek yenileme hızlı (240Hz+) bir monitörünüz varsa, CS2'nin Source 2 avantajlarından tam yararlanmanızı sağlar. Keskin hatlar sayesinde uzaktaki piksel farklarını algılamak kolaylaşır.

### 3. 1440x1080 (4:3 Custom Stretched) – *Netlik + Geniş Model Dengesi*
*   **Tür:** 4:3 (Özel Çözünürlük)
*   **Netlik:** Yüksek
*   **FPS Performansı:** Orta-Yüksek
*   **Açıklama:** 1080p monitörlerde 1280x960'ın sunduğu blurlanma (bulanıklık) sorununu çözer. 4:3 en-boy oranının model genişletme avantajını, 1080p Dikey piksel kalitesiyle birleştirir.

### 4. 1024x768 (4:3 Stretched) – *Maksimum FPS ve Performans*
*   **Tür:** 4:3
*   **Netlik:** Düşük
*   **FPS Performansı:** Çok Yüksek
*   **Açıklama:** Düşük segment GPU/CPU kombinasyonuna sahip sistemler için idealdir. Ekran kartı yükünü minimuma indirerek sistem gecikmesini (system latency) düşürür. Ancak uzak mesafelerdeki grafikler pikselleşebilir.

---

## Özel Çözünürlük Oluşturma (1440x1080 Yapılandırması)

1080p monitörünüzde en net 4:3 deneyimi için `1440x1080` özel çözünürlüğünü tanımlamanız önerilir.

### NVIDIA Denetim Masası Adımları:
1. Masaüstüne sağ tıklayıp **NVIDIA Denetim Masası**'nı açın.
2. **Çözünürlük Değiştirme** sekmesine gidin ve **Özelleştir** butonuna tıklayın.
3. **Özel Çözünürlük Oluştur** seçeneğine basın.
4. Yatay Piksel: `1440` / Dikey Hatlar: `1080` değerlerini girin ve Test edin.
5. **Masaüstü Boyutunu ve Konumunu Ayarla** sekmesine geçin.
6. Ölçeklendirme modunu **Tam Ekran (Full-screen)** yapın ve ölçeklendirmenin **GPU** üzerinde gerçekleştirilmesini seçin.

### AMD Radeon Software Adımları:
1. **AMD Software** uygulamasını açın.
2. **Ayarlar (Dişli simgesi) > Ekran** sekmesine gidin.
3. **Özel Çözünürlükler** bölümünden "Yeni Oluştur"a tıklayın.
4. Çözünürlük değerlerini `1440x1080` olarak ayarlayıp kaydedin.
5. Ölçekleme Modunu **Tam Panel (Full Panel)** olarak değiştirin.

---

## Donanım ve Sistem Özelliklerine Göre Çözünürlük Seçim Tablosu

| Sistem Özelliği / Hedef | Önerilen Çözünürlük | En-Boy Oranı | Ölçekleme |
| :--- | :--- | :--- | :--- |
| **Giriş Seviyesi PC** (Düşük FPS) | 1024x768 veya 1152x864 | 4:3 | Stretched |
| **Orta Seviye PC** (Rekabetçi Odaklı) | 1280x960 | 4:3 | Stretched |
| **Üst Seviye PC** (Netlik + Performans) | 1440x1080 (Özel) | 4:3 | Stretched |
| **Yüksek Sistem / Yayıncılar** | 1920x1080 | 16:9 | Native |

---

## CS2 İçin Teknik Özet ve Karar

*   **FPS Artışı ve Kolay Hedef Alma İçin:** `1280x960 (4:3 Stretched)` veya `1440x1080 (4:3 Stretched)` seçilmelidir.
*   **Maksimum Görüş Alanı ve Grafik Netliği İçin:** `1920x1080 (16:9 Native)` tercih edilmelidir.
*   **Gecikme (Input Lag) Optimize Edilmesi:** Çözünürlük düşürüldükçe GPU kullanım oranı azalır, bu da GPU kaynaklı giriş gecikmesini minimize eder. Ancak CS2 CPU ağırlıklı bir oyun olduğu için işlemci darboğazı olan sistemlerde çözünürlük düşürmek FPS'i doğrudan katlamayabilir.