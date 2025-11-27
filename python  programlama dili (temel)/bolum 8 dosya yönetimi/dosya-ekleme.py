# open(dosya_adi,dosya_modu)
# dosya_erişim_modu => dosyayi hangi amaçla açtıigimzi belirtir.



# "r" (read) okuma. dosya konumda yoksa hata verir
# "w" (wriyte yazma modu)
    # ** dosyayi konumda oluşturur
    # ** eger konumda aynı dosyayi siler ve yeni oluşturur.
# "a" (append ekleme modu) dosya konumda yoksa oluşturur
# "r+" hem okuma hem yazma modunda açılır .dosya konumda yoksa hata verir.

with open("dosya.txt","r+",encoding="utf-8") as file:# dosya oluşturur
    # file.seek(20)# cursoru 20. karaktere götürür
    print(file.read())# cursordan sonrasını okur
    file.write("birinci satir\n")# dosyaya yazar
