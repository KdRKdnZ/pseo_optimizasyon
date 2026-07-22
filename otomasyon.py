import os
import re
import socket
import asyncio
import logging
import httpx
from google import genai
from google.genai import errors as genai_errors
from aiolimiter import AsyncLimiter

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("pseo")

client = genai.Client()
limiter = AsyncLimiter(10, 60)
RETRYABLE_HTTP_CODES = {429, 500, 503, 504}

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def dosya_oku(dosya_adi):
    if not os.path.exists(dosya_adi):
        return []
    with open(dosya_adi, 'r', encoding='utf-8') as f:
        return [satir.strip() for satir in f if satir.strip()]

async def internet_var_mi() -> bool:
    try:
        await asyncio.get_running_loop().run_in_executor(
            None, socket.getaddrinfo, "8.8.8.8", 443
        )
        return True
    except OSError:
        return False

async def internet_gelene_kadar_bekle():
    while not await internet_var_mi():
        log.warning("Ağ bağlantısı yok, 15sn sonra tekrar kontrol edilecek.")
        await asyncio.sleep(15)

async def makale_uret(kelime, slug, semaphore):
    async with semaphore:
        async with limiter:
            backoff = 5
            while True:
                try:
                    log.info(f"Üretiliyor: {kelime} (Slug: {slug})")
                    response = await client.aio.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=f"'{kelime}' hakkında teknik, SEO uyumlu ve doğrudan bilgi veren detaylı bir makale yaz. Markdown formatında olsun, içerik direkt h1 başlığı ile başlasın. Gereksiz giriş cümleleri kullanma."
                    )

                    dosya_adi = f"{slug}.md"
                    dosya_yolu = os.path.join("docs", dosya_adi)
                    gecici_yol = dosya_yolu + ".tmp"

                    # Front matter ve içerik birleştirme
                    front_matter = f"---\ntitle: \"{kelime}\"\ndescription: \"{kelime} hakkında detaylı teknik rehber, performans analizi ve karşılaştırma.\"\n---\n\n"
                    tam_icerik = front_matter + response.text

                    with open(gecici_yol, "w", encoding="utf-8") as f:
                        f.write(tam_icerik)
                    os.replace(gecici_yol, dosya_yolu)

                    with open('uretilenler.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{slug}:{kelime}\n")

                    log.info(f"Başarılı: {kelime}")
                    return

                except genai_errors.APIError as e:
                    kod = getattr(e, "code", getattr(e, "status_code", None))
                    if kod in RETRYABLE_HTTP_CODES:
                        log.warning(f"{kelime}: API {kod}, {backoff}sn bekleniyor")
                        await asyncio.sleep(backoff)
                        backoff = min(backoff * 2, 90)
                        continue
                    log.error(f"{kelime}: Kalıcı API hatası ({kod}) - {e}")
                    return

                except (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout, socket.gaierror, OSError) as e:
                    log.warning(f"{kelime}: Ağ hatası ({type(e).__name__}: {e}), bağlantı bekleniyor...")
                    await internet_gelene_kadar_bekle()
                    continue

                except Exception as e:
                    log.error(f"{kelime}: Beklenmeyen hata {type(e).__name__}: {e}")
                    return

async def main():
    os.makedirs("docs", exist_ok=True)
    
    sablonlar = dosya_oku("sablonlar.txt")
    ekran_kartlari = dosya_oku("ekran_kartlari.txt")
    manuel_kelimeler = dosya_oku("kelimeler.txt")
    
    # Mevcut slug hafızasını oku
    uretilen_sluglar = set()
    if os.path.exists("uretilenler.txt"):
        with open("uretilenler.txt", "r", encoding="utf-8") as f:
            for satir in f:
                satir = satir.strip()
                if ":" in satir:
                    uretilen_sluglar.add(satir.split(":")[0])
                elif satir:
                    uretilen_sluglar.add(slugify(satir))

    # Docs klasöründeki mevcut .md dosyalarını da kontrol et
    for dosya in os.listdir("docs"):
        if dosya.endswith(".md"):
            uretilen_sluglar.add(dosya[:-3])
    
    tum_kelimeler = []
    for gpu in ekran_kartlari:
        for sablon in sablonlar:
            tum_kelimeler.append(sablon.replace("{gpu}", gpu))
            
    tum_kelimeler.extend(manuel_kelimeler)
    
    # Semantik Deduplication Kontrolü
    islem_yapilacaklar = []
    eklenen_sluglar = set()
    
    for k in tum_kelimeler:
        slug = slugify(k)
        if slug not in uretilen_sluglar and slug not in eklenen_sluglar:
            islem_yapilacaklar.append((k, slug))
            eklenen_sluglar.add(slug)
    
    if not islem_yapilacaklar:
        log.info("Sistem kontrol edildi: Üretilecek yeni anahtar kelime bulunamadı.")
        return

    log.info(f"Toplam {len(islem_yapilacaklar)} YENİ benzersiz makale üretilecek.")
    
    semaphore = asyncio.Semaphore(1)
    gorevler = [makale_uret(k, slug, semaphore) for k, slug in islem_yapilacaklar]
    await asyncio.gather(*gorevler)

if __name__ == "__main__":
    asyncio.run(main())
