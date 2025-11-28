class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self): # Sınıfa ait özelliklere ve yöntemlere erişmek için kullanılır
     print(f"Hello, My name is {self.name} I am  {self.age} years old") 
p1 = person("Erdem", 25)
p1.greet()


class car:
   def __init__(self,marka, model, year):
      self.marka = marka
      self.model = model
      self.year = year


   def car_info(self):
      print(f"{self.year} {self.marka} {self.model}")


car1 = car("BWM", "G80", 2022)
car1.car_info()
      


class person:
   def __init__(self,name):
      self.name = name
   def greet (self):
      return input("mesaj girin: ") + " " + self.name
   def welcome(self):
      message = self.greet()
      print(message  +  "  Welcome to our website ")
p1 = person(" Erdem ")
p1.welcome()