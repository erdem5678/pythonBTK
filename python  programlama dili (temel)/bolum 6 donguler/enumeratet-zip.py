#enumerate
markalar = ["open","bwm","togg"]

index = 1
for marka in markalar:
    print(f"{index}-{marka}")
    index += 1

obj1 = enumerate(markalar,1)
print(type(obj1))
print(list(obj1))

for index,marka in enumerate(markalar):
    print(f"{index}-{marka}")


# zip

numara = [100,200,300]
ogreci = ["Ali","Ayse","canan","Mehmet"]

print(list(zip(numara,ogreci)))

for no,isim in zip(numara,ogreci):
    print(no,isim)