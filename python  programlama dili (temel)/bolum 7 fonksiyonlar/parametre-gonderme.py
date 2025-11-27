def selamlama(isim):
    return "Merhaba, " + isim

# print(selamlama("bariş"))
# print(selamlama("erdem"))

def toplam(sayi1, sayi2):
    return sayi1 + sayi2

# print(toplam(10,20))
# print(toplam(10,30))


def yasHesaplama(doğumYili):
    return 2025 - doğumYili

def emekliligeKacYilKladi(dogumYili, isim):
    yas = yasHesaplama(dogumYili)

    kalanSure = 65 - yas
    if kalanSure > 0 :
        return f"{isim}, emekliliginize {kalanSure} yil kladi"
    else:
        return f"{isim}, zaten {abs(kalanSure)} emekli olduunuz" # abs metodu negatif bir sayı pozitfi vermesi için kullanılır 

print(emekliligeKacYilKladi(2006, "bariş"))#(int(input("yil girimniz: ")), "bariş"))
print(emekliligeKacYilKladi(1968, "erdem"))
print(emekliligeKacYilKladi(1996, "can"))
