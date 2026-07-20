import os
import asyncio
from google import genai

client = genai.Client()

def dosya_oku(dosya_adi):
    if not os.path.exists(dosya_adi):
        return []
    with open(dosya_adi, 'r', encoding='utf-8') as f:
        return [satir.strip() for satir in f if satir.strip()]

def uretilenlere_ekle(kelime):
    with open('uretilenler.txt', 'a', encoding='utf-8') as f:
        f.write(kelime + '\n')

async def makale_uret(kelime, semaphore):
    async with semaphore:
        try:
            print(f"Üretiliyor: {kelime}")
            response = await client.aio.models.generate_content(
                model='gemini-3.5-flash',
                contents=f"'{kelime}' hakkında teknik, SEO uyumlu ve doğrudan bilgi veren detaylı bir makale yaz. Markdown formatında olsun ve içerik direkt h1 başlığı ile başlasın. Gereksiz giriş cümleleri kullanma."
            )
            
            dosya_adi = kelime.replace(" ", "_").lower() + ".md"
            dosya_yolu = os.path.join("docs", dosya_adi)
            
            with open(dosya_yolu, "w", encoding="utf-8") as f:
                f.write(response.text)
            
            uretilenlere_ekle(kelime)
            print(f"Başarılı: {kelime}")
            
        except Exception as e:
            print(f"Hata ({kelime}): {e}")

async def main():
    os.makedirs("docs", exist_ok=True)
    
    sablonlar = dosya_oku("sablonlar.txt")
    ekran_kartlari = dosya_oku("ekran_kartlari.txt")
    manuel_kelimeler = dosya_oku("kelimeler.txt")
    uretilenler = set(dosya_oku("uretilenler.txt"))
    
    tum_kelimeler = []
    
    for gpu in ekran_kartlari:
        for sablon in sablonlar:
            tum_kelimeler.append(sablon.replace("{gpu}", gpu))
            
    tum_kelimeler.extend(manuel_kelimeler)
    
    islem_yapilacaklar = [k for k in tum_kelimeler if k not in uretilenler]
    
    if not islem_yapilacaklar:
        print("Sistem kontrol edildi: Üretilecek yeni anahtar kelime bulunamadı.")
        return

    print(f"Toplam {len(islem_yapilacaklar)} YENİ makale üretilecek (Eskiler atlandı)...")
    
    semaphore = asyncio.Semaphore(5)
    gorevler = [makale_uret(k, semaphore) for k in islem_yapilacaklar]
    await asyncio.gather(*gorevler)

if __name__ == "__main__":
    asyncio.run(main())
