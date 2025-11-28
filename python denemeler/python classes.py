class person:
    def __init__(self,name,age): # __init__()Yeni bir nesne oluşturmak için sınıf her kullanıldığında yöntem otomatik olarak adlandırılır.
        self.name = name
        self.age = age
# Kullanmak __init__()İlk değerlere sahip nesneler oluşturmayı kolaylaştırır:
p1 = person ("Erdem", 20)
print(p1.name)
print(p1.age)


# O olmadan bir sınıf oluşturun __init__(): :
class person:
    pass #__init__()Yöntem, her nesne için özellikleri manuel olarak ayarlamanız gerekir:
p1 = person()
p1.name = "Erdem"
p1.age = 20
print(p1.name)
print(p1.age)



class person:
#Ayrıca parametreler için varsayılan değerleri de ayarlayabilirsiniz __init__()Yöntem:
    def __init__(self,name,age = 18):
        self.name = name
        self.age = age
p1 = person("Erdem")
p2 = person ("Baris", 35)
print(p1.name,p1.age)
print(p2.name,p2.age)


# birden fazla paramtre oluşturma 
class person:
    def __init__(self, name, age,city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
p1 = person("Can", 28, "Bodrum", "Türkiye")
print(p1.name, p1.age, p1.city, p1.country)
# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)

