# error (Hata = Kodun yanlış olduğu için Python’un durup seni uyarmasıdır.)
# SyntaxError => Yazım hatası.
# NameError => Değişken yok.
# TypeError => Tür uyumsuzluğu.
# ValueError => Tür doğru ama değer yanlış.
# error handing



try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x + y)
except:
    print("hata oluştu")