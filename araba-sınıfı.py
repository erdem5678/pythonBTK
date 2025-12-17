class Araba:
    def __init__(self, marka, model):
        # Araba özelliklerini başlat
        self.marka = marka
        self.model = model
        self.hiz = 0  # Başlangıç hızı 0

    def hizlan(self, miktar):
        # Hızı artır
        if miktar <= 0:
            print("Hiz değeri 0'dan küçük olamaz")
            return  # Fonksiyondan çık
        
        self.hiz += miktar  # Hıza miktar ekle
        print(f"Hiz: {self.hiz} km/h")
    

    def brake(self, miktar):

        # Fren yap (hızı azalt)
        if miktar <= 0:
            print("Fren değeri 0'dan küçük olamaz")
            return  # Fonksiyondan çık
        self.hiz -= miktar  # Hızdan miktar çıkar


        # Hız negatif olmasın kontrolü
        if self.hiz < 0:
            self.hiz = 0
        print(f"Hiz: {self.hiz} km/h")
    


    def __str__(self):
        # Araba bilgilerini string olarak döndür
        return f"{self.marka} {self.model} - Hız: {self.hiz} km/h"



# Test kodları - Araba oluştur ve kullan
car = Araba("BMW", "M3")
car.hizlan(20)   
car.hizlan(0)    
car.hizlan(30) 
car.brake(20)   
car.brake(10)   
print(car)       