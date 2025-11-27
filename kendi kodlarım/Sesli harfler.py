def sesli_harf_sayilar(metin):
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"
    sayac = 0
    for harf in metin:
        if harf in sesli_harfler:
            sayac += 1
    return sayac

metin = input("Metin girin: ")
sonuc = sesli_harf_sayilar(metin)
print("Sesli harf sayisi:", sonuc)

