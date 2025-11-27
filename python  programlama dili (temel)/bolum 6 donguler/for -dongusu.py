# for => liste

sayilar = [1,2,3,4,5,6,8,91,21]
isimler = ["Ali","Canan","Zeynep"]
adsoyad = "satik turan"

for x in sayilar:
    print(x)

for x in sayilar:
    print("Merhaba BTK Akedimi")

for isim in isimler:
    print(isim)

for i in adsoyad:
    print(i)

my_tuple = [(1,2),(2,3),(4,5)]

for i in my_tuple:#(1, 2)(2, 3)(4, 5)
  print(i)

for a,b in my_tuple:#1 2 -  2 3 -  4 5
    print(a,b)

my_dict = {"41":"kocaeli","53":"Rize","35":"izmir"}

for x in my_dict:
    print(my_dict[x])
    print(x)

for x in my_dict.values():
    print(x)

for x in my_dict.values():
    print(x)

for x,y in my_dict.items():
    print(x,y)