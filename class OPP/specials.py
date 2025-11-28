mylisty = [1,2,3]
# myString = 'my string'

# print(len(mylisty))
# print(len(myString))
# print(type(mylisty))
# print(type(myString))


# python specail methods
#__init__ - Her sınıfta mutlaka kullanılır
#__str__ - Nesneyi yazdırabilmek için şart
#__eq__ - İki nesneyi karşılaştırmak için
#__len__ - Koleksiyon sınıfları için
#__getitem__ - Koleksiyon sınıfları için indeksleme

# matamtik işlemler
#__add__(self, other)+obj1 + obj2 => - Toplama İşlemi
#__sub__(self, other)-obj1 - obj2 => -  Çıkarma İşlemi
#__mul__(self, other)*obj1 * obj2 => -  Çarpma İşlemi
#__truediv__(self, other)/obj1 / obj2 => - Bölme İşlemi

class movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('filim  objesi silindi')
    
m = movie('filim adi', 'yönetmen adi', 120)

# print(str(mylisty))
print(str(m))
# print(len(mylisty))
# print(len(m))