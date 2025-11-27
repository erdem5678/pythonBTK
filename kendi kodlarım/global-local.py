global_deger = 10

def fonksiyon():
    local_deger = 20
    print("locak değer: ", local_deger)

print("global değer: ", global_deger)
fonksiyon()
print("fonksiyon sonrasi global: ", global_deger)
