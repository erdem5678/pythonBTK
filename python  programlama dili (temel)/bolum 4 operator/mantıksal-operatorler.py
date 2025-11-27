# (yas >= 18) => true,false
#(mezuniyet == 'lise') yada (mezuniyet == 'ünüversite') =>  true,false
# sonuc = (yas >= 18) ve (mezuniyet == 'lise' ve ya  mezuniyet == 'ünüversite')

x = 11

sonuc = (x > 5) and (x < 10)

# 1- and 
# True, False => True
# True, False => False
# False, False => False

# 2 - or
# True, True => True
# True, False, False => True
# False, False => False

sonuc = (x > 0) and (x % 2 == 0) # x pozitif çiftf yası
sonuc = (x > 0) or (x % 2 == 0) # x pozitif yada çift sayı

# 3- not

# False => True
# True => False
sonuc = not(x > 0)
print(sonuc)
