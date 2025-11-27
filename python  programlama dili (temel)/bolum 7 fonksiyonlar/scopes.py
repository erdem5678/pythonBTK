# local scope
# Bir fonksiyonun içinde tanımlanan değişkenlerin alanı.
# Sadece o fonksiyonun içinde geçerlidir, dışarıdan erişemezsin.
# Fonksiyon bittiğinde değişken “yok olur”.

# global scope
# Dosyanın her yerinden erişilebilen değişkenlerin bulunduğu alan.
# Fonksiyonların dışında tanımlanan her şey globaldir.
# Bir fonksiyonun içine girip, global x demedikçe global değişkeni değiştiremezsin.
# Programın her köşesinden görünür.

x = "global scope"

def my_func():
    x = "local scope"
    print(x)

my_func()
print(x)


name = "Cinar"

def cahnge_name(new_name):
    global name # burada çınarı günceller ve ada yapar
    name = new_name
    print(name)
cahnge_name("ada")
print(name)

name = "glabal string"
def grreeting():
    name = "Cinar"

    def hello():
        name = "Ada"
        print("hello", name)
    hello()
grreeting()



x = 50
def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")
test()
print(x)