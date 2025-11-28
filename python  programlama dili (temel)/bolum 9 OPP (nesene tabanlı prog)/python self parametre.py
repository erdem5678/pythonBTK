class person:  # Person (kişi) sınıfını tanımla
    def __init__(self, name, age):  # Yapıcı metod - nesne oluşturulurken çalışır
        self.name = name  # İsim özelliğini ata
        self.age = age  # Yaş özelliğini ata
    
    def greet(self): # Sınıfa ait özelliklere ve yöntemlere erişmek için kullanılır
     print(f"Hello, My name is {self.name} I am  {self.age} years old")  # Selamlama mesajını yazdır
     
p1 = person("Erdem", 25)  # Person sınıfından p1 nesnesi oluştur
p1.greet()  # p1 nesnesinin greet metodunu çağır

class car:  # Car (araba) sınıfını tanımla
   def __init__(self,marka, model, year):  # Yapıcı metod
      self.marka = marka  # Marka özelliğini ata
      self.model = model  # Model özelliğini ata
      self.year = year  # Yıl özelliğini ata

   def car_info(self):  # Araba bilgilerini gösterme metodu
      print(f"{self.year} {self.marka} {self.model}")  # Yıl, marka ve model bilgisini yazdır

car1 = car("BWM", "G80", 2022)  # Car sınıfından car1 nesnesi oluştur
car1.car_info()  # car1 nesnesinin bilgilerini göster
      
class person:  # Person sınıfını tekrar tanımla (farklı yapıda)
   def __init__(self,name):  # Yapıcı metod - sadece isim alır
      self.name = name  # İsim özelliğini ata

   def greet (self):  # Kullanıcıdan mesaj alan metod
      return input("mesaj girin: ") + " " + self.name  # Kullanıcının mesajını isimle birleştir ve döndür
   
   def welcome(self):  # Hoşgeldin mesajı gösteren metod
      message = self.greet()  # greet metodunu çağır ve mesajı al
      print(message  +  "  Welcome to our website ")  # Mesajı ve hoşgeldin yazısını yazdır

p1 = person(" Erdem ")  # Person sınıfından p1 nesnesi oluştur
p1.welcome()  # p1 nesnesinin welcome metodunu çağır