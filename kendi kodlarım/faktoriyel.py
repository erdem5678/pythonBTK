n = int(input("Sayi girin: ")) 
sonuc = 1
for i in range(1 ,n+1):
    sonuc*=i
    print(f"{n}! =" ,sonuc)