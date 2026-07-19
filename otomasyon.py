import os
import asyncio
import logging
from slugify import slugify
from google import genai
from google.genai import types

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
client = genai.Client()

PROMPT_TEMPLATE = """
Sen kıdemli bir yazılım mimarı, donanım uzmanı ve SEO yazarısın.
Aşağıdaki anahtar kelime için teknik doğruluğu yüksek, kanıta dayalı ve SEO uyumlu Türkçe bir Markdown makale oluştur.
Gereksiz giriş cümleleri kullanma, doğrudan konuya gir ve H1, H2, H3 başlık hiyerarşisine kesinlikle uy.

Anahtar Kelime: {keyword}
"""

async def generate_article(keyword, semaphore):
    async with semaphore:
        logging.info(f"İşleniyor: {keyword}")
        
        # Hata durumunda 5 kez artan sürelerle (10s, 20s, 30s...) tekrar dener
        for attempt in range(5):
            try:
                response = await client.aio.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=PROMPT_TEMPLATE.format(keyword=keyword),
                    config=types.GenerateContentConfig(temperature=0.3)
                )
                await asyncio.sleep(4) # Standart rate-limit koruması
                return keyword, response.text
            except Exception as e:
                wait_time = (attempt + 1) * 10
                logging.warning(f"API Yoğunluğu. {wait_time} saniye bekleniyor... (Deneme {attempt+1}/5)")
                await asyncio.sleep(wait_time)
        
        logging.error(f"Başarısız ({keyword}): Sunucu yanıt vermiyor.")
        return keyword, None

async def main():
    if not os.path.exists('kelimeler.txt'):
        return

    with open('kelimeler.txt', 'r', encoding='utf-8') as f:
        keywords = [line.strip() for line in f if line.strip()]

    os.makedirs('docs', exist_ok=True)
    semaphore = asyncio.Semaphore(3)
    tasks = [generate_article(kw, semaphore) for kw in keywords]
    
    for future in asyncio.as_completed(tasks):
        kw, content = await future
        if content:
            slug = slugify(kw)
            file_path = f"docs/{slug}.md"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"---\ntitle: {kw}\ndescription: {kw} hakkında detaylı optimizasyon ve donanım rehberi.\n---\n\n")
                f.write(content)
            logging.info(f"Kaydedildi: {file_path}")

if __name__ == "__main__":
    asyncio.run(main())
