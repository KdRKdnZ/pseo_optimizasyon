import os
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

async def makale_uret(kelime, semaphore):
    async with semaphore:
        async with limiter:
            backoff = 5
            while True:
                try:
                    log.info(f"Üretiliyor: {kelime}")
                    response = await client.aio.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=f"'{kelime}' hakkında teknik, SEO uyumlu ve doğrudan bilgi veren detaylı bir makale yaz. Markdown formatında olsun, içerik direkt h1 başlığı ile başlasın. Gereksiz giriş cümleleri kullanma."
                    )

                    dosya_adi = kelime.replace(" ", "_").lower() + ".md"
                    dosya_yolu = os.path.join("docs", dosya_adi)
                    gecici_yol = dosya_yolu + ".tmp"

                    with open(gecici_yol, "w", encoding="utf-8") as f:
                        f.write(response.text)
                    os.replace(gecici_yol, dosya_yolu)

                    with open('uretilenler.txt', 'a', encoding='utf-8') as f:
                        f.write(kelime + '\n')

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
    uretilenler = set(dosya_oku("uretilenler.txt"))
    
    tum_kelimeler = []
    for gpu in ekran_kartlari:
        for sablon in sablonlar:
            tum_kelimeler.append(sablon.replace("{gpu}", gpu))
            
    tum_kelimeler.extend(manuel_kelimeler)
    
    islem_yapilacaklar = [k for k in tum_kelimeler if k not in uretilenler]
    
    if not islem_yapilacaklar:
        log.info("Sistem kontrol edildi: Üretilecek yeni anahtar kelime bulunamadı.")
        return

    log.info(f"Toplam {len(islem_yapilacaklar)} YENİ makale üretilecek.")
    
    semaphore = asyncio.Semaphore(1)
    gorevler = [makale_uret(k, semaphore) for k in islem_yapilacaklar]
    await asyncio.gather(*gorevler)

if __name__ == "__main__":
    asyncio.run(main())
