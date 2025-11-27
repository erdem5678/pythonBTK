class Araba():   
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model

    def bilgi_yaz(self):
         return f"Marka : {self.marka} modeli:{self.model}"
    
araba1 = Araba("Toyota","Corolla")
araba2 = Araba("Ford","focus")

print(araba1.bilgi_yaz())
print(araba2.bilgi_yaz())