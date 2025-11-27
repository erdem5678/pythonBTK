# def display_user(*args):
#     print(type(args)) #<class 'tuple'> ()
#     print(args)

# display_user()


def display_user(**kwargs):
    # print(type(kwargs))# <class 'dict'> {}
    # print(kwargs)

    for key, value in kwargs.items():
        print(f" {key}: {value}")
        print("\n")
display_user(Username="bariserdem")
display_user(Username="bariserdem", email="info@bariserdem.com")
display_user(Username="bariserdem", email="info@bariserdem.com", country="Türkiye")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50,60,key1="value1",key2="value2")

#kwargs = named arguments = anahtar-değer (key-value)
#şeklinde gelen argümanları sözlük olarak toplar.
#args nasıl tuple topluyorsa,
#kwargs da dictionary toplar.