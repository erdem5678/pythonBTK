# string concat
ad = "Baris"
soyad = "caliskan"
yas = 20
msj = "My name is " + ad + " " + soyad + " . " + "I am " + str(yas) + " years ols."
# string format
msj = " My name {} {} . I am {} years old. ".format(ad , soyad, yas)
msj = " My name {0} {1} . I am {2} years old. ".format(ad , soyad, yas)
msj = " My name {a} {s} . I am {y} years old. ".format(a = ad , s = soyad, y =yas)
# f -string
msj = f" My name {ad} {soyad} . I am {yas} years old. "
print(msj)