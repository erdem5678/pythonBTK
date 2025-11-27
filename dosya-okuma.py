# f = open("open.txt","r")
# print(f.read())
for i in range(1,5):
 with open("open.txt", "a") as f:
    f.write(f"{i}. {input("kelime girin: ")}\n")
# dosyayı okuma gösterme 
with open("open.txt", encoding="utf-8") as f:
    f = f.read()
    print(f)
aranan = input("aranan kişi kim: ")
if aranan in f:
   print(f"{aranan} kişi var ")
else:
   print(f"{aranan} kişi yok ")


#open and read the file after the appending:
# with open("open.txt") as f:
#   print(f.read()) 
