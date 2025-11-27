""" 
dosya açmak ve oluşturmak için open() fonksiyonu kullanilir.


kulanimi              : open(dosya_adi,dosya_erişimi_modu)
dosya_erişim_modu     : dosyayi hangi amaçla açtigimizi belirtilir.
"r"                   : okuma modu. belirtilen konumda dosya olmalidir
seek                  : cursor konumu 

"""
# 3 read den sonra bir şey yazdırmıyor çünkü cursor en sona gelmiş durumda.
f = open("log.txt",encoding="utf-8")# varsayılan okuma modudur.
print(f.read())
print(f.read())