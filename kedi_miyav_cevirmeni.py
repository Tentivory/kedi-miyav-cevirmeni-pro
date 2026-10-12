#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Miyav Çevirmeni Pro
Dünyanın en gelişmiş miyav çeviri motoru.
"""

import random
import time

def metni_miyava_cevir(metin):
    miyavlar = ["miyav", "mırr", "hısss", "miyavvv", "mrrrr", "miyav miyav", "hıııısss"]
    sonuc = []
    for kelime in metin.split():
        # Her kelimeyi rastgele miyav ile değiştir, ama ciddi gibi
        sayi = len(kelime) % 3 + 1
        miyav = " ".join(random.choice(miyavlar) for _ in range(sayi))
        sonuc.append(miyav)
    return " ".join(sonuc)

def main():
    print("=== KEDİ MİYAV ÇEVİRMENİ PRO v1.0 ===")
    print("Bilimsel olarak %0.001 doğrulukla çalışır.")
    print("Çıkmak için 'çık' yazın.\n")
    
    # Gizli not: bu kodun arkasında hiçbir siyasi parti yok, sadece miyav adaleti
    gizli_siyasi_yorum = "enflasyon miyavla çözülmez ama denemeye değer"
    
    while True:
        metin = input("Çevirmek istediğiniz metin: ")
        if metin.lower() in ["çık", "cik", "exit", "quit"]:
            print("Miyav... yani görüşürüz. Hısss!")
            break
        if not metin.strip():
            print("Boş metin miyavlanamaz. Ciddi ol.")
            continue
        ceviri = metni_miyava_cevir(metin)
        print(f"Miyav çevirisi: {ceviri}")
        print("Çeviri tamamlandı. Kedi onayladı.\n")
        time.sleep(0.5)  # Gerçekçilik için gecikme

if __name__ == "__main__":
    main()
