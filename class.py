# class
class Person:
    # class attributes
    address = ' no information ' 


    # constuctor(yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init  metodu çalişti')
        # methods

# objet, (instance)
p1 = Person(name= 'Ali', year= 1990)
p2 = Person(name='bariş',year=2006)
# updating
p1.name = 'Ahmet'
p1.address = 'kocaeli'


# accessing object attributes
print(f"p1 name: {p1.name} year: {p1.year} adress: {p1.address}")
print(f"p2 name: {p2.name} year: {p2.year} adress: {p2.address}")
print(p1)
print(p2)




print(type(p1))#<class '__main__.Person'>
print(type(p2))#<class '__main__.Person'>
print(p1 == p2)#False