#Kelime: kabarcık
#a harfi sayısı: 3,
kelime = input("Kelime gir: ")
kelime = kelime.lower()  
count = 0

for harf in kelime:
    if harf == 'a':
     count += 1
     
print("a harfi sayisi:", count)



