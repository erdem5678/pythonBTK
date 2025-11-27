"""
uygulama 1 : yari capi verilen bir dairenin alanini ve cevresini hesaplayimniz
Alan = pi*r*r
çevre = 2*pi*r

uygulama 2 : klavyeden girilen km bilgisini mil cinsinden hesaplayiniz
 mil = km / 1.6094444
 """
pi = 3.14
r = float(input("yari cap : "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan: " + str(alan))
print("cevre: " + str(cevre))

mesafekm = input("km:")
mesafeMil = float(mesafekm) / 1.609344
mesafeMil = round(mesafeMil, 2)
print(mesafekm + " km = " + str(mesafeMil) + " mil")