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
    def __init__(self,fname, lname, number):
        person.__init__(self,fname, lname) # burada Miras almış oldugu Person method çalışır
        self.studentNumber = number
        print("student created")

    # override (geçersiz kılma)
    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(person):
    def __init__(self,fname, lname, branch):
        super().__init__(fname, lname) # burada Miras almış oldugu Person method çalışır
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
    


p1 = person('Ali','Yilmaz')
s1 = Student('cinar', 'turan', 1256)
t1 = Teacher('bariş','erdem','siber güvenlik')
t1.who_am_i()

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()

