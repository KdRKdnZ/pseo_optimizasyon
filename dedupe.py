import os
import re
import glob
import sys
import shutil
from itertools import combinations

DOCS_DIR = "docs"
REMOVED_DIR = "docs_removed"

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^\wşğüöçıi ]', ' ', text, flags=re.UNICODE)
    return set(t for t in text.split() if len(t) > 1)

def dosya_bilgisi(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    title = ""
    for line in content.splitlines():
        if line.strip().startswith("# "):
            title = line.strip("# ").strip()
            break
    if not title:
        title = os.path.splitext(os.path.basename(path))[0].replace("_", " ")
    return {
        "path": path,
        "title": title,
        "tokens": normalize(title),
        "wordcount": len(content.split()),
    }

def cakismalari_bul(esik=0.7):
    files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    # Legal ve index sayfalarını hariç tut
    muaf_dosyalar = {"gizlilik-politikasi.md", "hakkimizda.md", "iletisim.md", "index.md"}
    files = [f for f in files if os.path.basename(f) not in muaf_dosyalar]
    
    veri = [dosya_bilgisi(f) for f in files]
    sonuc = []
    
    # Zaten eşleşmiş dosyaları tekrar işlememek için takip kümesi
    islenenler = set()
    
    for a, b in combinations(veri, 2):
        if a["path"] in islenenler or b["path"] in islenenler:
            continue
        if not a["tokens"] or not b["tokens"]:
            continue
            
        ortak = a["tokens"] & b["tokens"]
        kucuk_set = min(len(a["tokens"]), len(b["tokens"]))
        if kucuk_set == 0:
            continue
            
        oran = len(ortak) / kucuk_set
        if oran >= esik:
            sonuc.append((a, b, oran))
            # Kelime sayısı az olanı elenecek olarak işaretle
            kisa = a if a["wordcount"] < b["wordcount"] else b
            islenenler.add(kisa["path"])
            
    return sorted(sonuc, key=lambda x: -x[2])

def raporla(cakismalar):
    print(f"\n[+] Total {len(cakismalar)} adet çakışan sayfa çifti tespit edildi:\n")
    for a, b, oran in cakismalar:
        kisa, uzun = (a, b) if a["wordcount"] < b["wordcount"] else (b, a)
        print(f"[%{oran*100:.0f} Örtüşme]")
        print(f"  [TINIER - Taşınacak] ({kisa['wordcount']:>4} kelime)  {kisa['path']}")
        print(f"                       \"{kisa['title']}\"")
        print(f"  [LONGER - Kalacak]  ({uzun['wordcount']:>4} kelime)  {uzun['path']}")
        print(f"                       \"{uzun['title']}\"")
        print("-" * 60)

def uygula(cakismalar):
    os.makedirs(REMOVED_DIR, exist_ok=True)
    tasinanlar = []
    
    for a, b, oran in cakismalar:
        kisa, _ = (a, b) if a["wordcount"] < b["wordcount"] else (b, a)
        if os.path.exists(kisa["path"]):
            yeni_yol = os.path.join(REMOVED_DIR, os.path.basename(kisa["path"]))
            shutil.move(kisa["path"], yeni_yol)
            tasinanlar.append(kisa['title'])
            print(f"[Taşındı] {kisa['path']} -> {yeni_yol}")
            
    with open("silinen_kelimeler.txt", "a", encoding="utf-8") as f:
        for t in tasinanlar:
            f.write(t + "\n")
            
    print(f"\n[+] {len(tasinanlar)} adet dosya '{REMOVED_DIR}/' klasörüne taşındı.")

if __name__ == "__main__":
    cakismalar = cakismalari_bul()
    if "--apply" in sys.argv:
        uygula(cakismalar)
    else:
        raporla(cakismalar)
        print("\n[!] Dosyaları 'docs_removed/' klasörüne taşımak için script'i '--apply' parametresiyle çalıştırın:")
        print("    python dedupe.py --apply")
