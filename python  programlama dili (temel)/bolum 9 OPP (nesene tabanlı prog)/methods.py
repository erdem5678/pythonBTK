# class
class product:

    # attribute, property
    def __init__(self, name, price, İsactive):# bir sınıfın içindeki her metotun hangi objenin çalıştıgını self sayesinde biliriz (ilk parametresi self olmalıdır)
     self.name = name 
     self.price = price
     self.İsactive = İsactive

     
# instance method
    def intro(self):
       return f"urun adi: {self.name} fiyati:{self.kdv_price()}"
   
    def kdv_price(self):
       return self.price * 1.18

# ınstance, object
p1 = product("İphone 15", 50000,True)
p2 = product("İphone pro 15", 60000, True)
p3 = product("Samsung S24", 70000,False)
p4 = product("İphone 12", 40000,True)
urunler = [p1, p2, p3]
urunler.append(p4)
for urun in urunler:
   if urun.İsactive:
      print(urun.intro())