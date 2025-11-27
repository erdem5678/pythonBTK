# file = open(r"C:\Users\baris\OneDrive\Desktop\python BTK\bolum 8 dosya yönetimi\log.txt",encoding="utf-8")
# print(file.read())

# file.close()
try:
    with open("log.txt",encoding="utf-8") as file:# with bloğu kullanıldığında dosya otomatik kapanır.
      for i in file:
        print(i, end="")# end="" ile satır atlamasını engelledik
except FileNotFoundError as e: # "dosya yoksa hata veriyor
   print("dosya okuma hatasi  ")
    # print(file.read(10))# 10 karakter okur
    # print(file.tell())# cursorun konumunu verir
    # print(file.read())
    # print(file.tell())