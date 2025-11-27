# value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x,y)

# reference
 
a = ["elma", "armut"]
b = ["elma", "armut"]

a = b # adres koplama
a[0] = "uzum"
print(a,b)

# liste koplaylama

listeA = [10,20]
listeB = listeA.copy() # 1 yöntem kopyalama için 
listeB = list(listeA) # 2 yöntem

listeB[0] = 30
print(listeA,listeB) #  [10, 20] [30, 20] 