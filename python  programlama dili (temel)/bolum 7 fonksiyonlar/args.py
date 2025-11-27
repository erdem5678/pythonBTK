# sayilar = (10,20,30,40)


# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

def toplam(*args): #Fonksiyona kaç tane argüman geleceğini bilmediğinde kullanırsın. 
#Hepsini tuple olarak toplar.
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i 
    return sonuc
sonuc = toplam(10,20,30,40,50)
print(sonuc)

#*args → sınırsız sayıda değer alır
#Hepsini tek bir tuple içine doldurur
#Sırasıyla (index ile) erişirsin