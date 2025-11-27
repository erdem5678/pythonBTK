# "w" : (write) yazma modu 
#   ** dosyayı komudu oluşturur
#   ** eger konumda aynı dosyayı siler ve yeni oluşturur.

with open("dosya.txt","w",encoding="utf-8") as file:# dosya oluşturur

  file.write("çalişkan erdem\n")# dosyaya yazar
  file.write("bariş erdem \n")# dosyaya yazar

file.close()# dosyayı kapatır


with open("dosya.txt","r",encoding="utf-8") as file:# dosya oluşturur
   for i in file:
    print(i, end="")# end="" ile satır atlamasını engelledik