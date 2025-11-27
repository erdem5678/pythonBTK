# class
class product:
    pass
    # method
    # attribute, property
# ınstance, object
p1 = product()
p2 = product()

sonuc = type(p1)
sonuc2 = type(p2)
print(sonuc)
print(sonuc2)

sonuc = p1
sonuc = p2 #0x0000024651768CD0> indicates at which address in memory it was created
print(sonuc)