def selamlama(isim = "kullanici", mesaj = "iyi günler"): # buna default parametre atması denir
    return f"{mesaj} {isim}"

sonuc = selamlama("bariş", "merhaba") 
sonuc = selamlama("bariş", "selam") 
sonuc = selamlama("bariş") 
sonuc = selamlama()

def usAlma(taban,us=2):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(5)

def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a,b,fn = toplama):
    return fn(a,b)

sonuc = islem(10,20,cikarma)
sonuc = islem(10,20)
sonuc = islem(10,20,toplama)

print(sonuc)