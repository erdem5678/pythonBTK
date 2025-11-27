# identity
x = [2,4,6]
y = [2,4,6]
z = y

print(x == y)
print(x is y) # nesen benzerliigi var mı  False
print(x is not y) # obje benzerligi var mı  True


print( z is y) # True nesen benzerlgi var 
print(z is not y) # False obje benzerligi yok 

# # membership


print(20 in x) # x içinde 20 yok False
print(20 not in x) # True gönder x içinde 20 yok çünükü
print(6 in x) # x içinde 6 var True 
