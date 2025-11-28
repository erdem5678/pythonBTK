# Inheritance (kalıtım) : Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# student(person), teacher(person) :Miras alması

# Animal => dog(Animal), cat(Animal)

class person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('person  Created')
        
    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')


class Student(person):
    def __init__(self,fname, lname):
        person.__init__(self,fname, lname) # burada Miras almış oldugu Person method çalışır
        print("student created")


p1 = person('Ali','Yilmaz')
s1 = Student('cinar', 'turan')


print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()