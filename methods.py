# # class
# class Person:
#     # class attributes
#     address = ' no information ' 


#     # constuctor(yapıcı metod)
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.year = year

# # instance methods
#     def intro(self):
#         print('Hello there. I am ' + self.name)
# # instance methods
#     def calculateAge(self):
#         return 2019 - self.year


# # objet, (instance)
# p1 = Person(name= 'Ali', year= 1990)
# p2 = Person(name='bariş',year=2006)

# p1.intro()
# p2.intro()

# print(f'adim: {p1.name} yaş: {p1.calculateAge()}')
# print(f'adim: {p1.name} yaşim: {p2.calculateAge()}')


class Circle:
    # class object attribute
    pi = 3.14 # her bir  method için ortak oldugu içi burada tanımlnadı 

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle() # yaricap = 1
c2 = Circle(5)
print(f'c1 cevresi: {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}')
print(f'c2 cevresi: {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}')


