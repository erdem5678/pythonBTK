# class
class product:
    # method
    # attribute, property
    def __init__(self, name, price, İsactive):# bir sınıfın içindeki her metotun hangi objenin çalıştıgını self sayesinde biliriz (ilk parametresi self olmalıdır)
     self.name = name # burada name attribute olarak tanımlanır
     self.price = price# burada price attribute olarak tanımlanır
     self.İsactive = İsactive# burada İsactive attribute olarak tanımlanır


# ınstance, object
p1 = product("İphone 15", 50000,True)# bir product sınıfından p1 adında bir nesne(ınstance) oluşturdukx
p2 = product("İphone pro 15", 60000, True)
p3 = product("Samsung S24", 70000,False)

urunler = [p1, p2, p3]# ürünleri bir listeye atadık

for urun in urunler:# urun p1, p2, p3 ü temsil eder
   if urun.İsactive:# urun aktif ise
      print(f"urun adi: {urun.name} urun fiyati:{urun.price}")

# sonuc = p1.name
# sonuc = p1.price
# sonuc = p1.İsactive
# print(sonuc)