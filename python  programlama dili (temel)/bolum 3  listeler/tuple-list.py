my_list = [1,2,3]
my_tuple = (1,2,3,1)#1,2,3,1 olarakda tuple da kullanıla bilir ve degiştirilemz !!!

print(type(my_list)) # hangi sınıfa oldugunu bakıyoruz 
print(type(my_tuple))

my_list[0] = 2 #sonuc = my_list
# my_tuple[0] = 2 # TypeError: 'tuple' object does not support item assignment tuple degiştirilemez

my_list.append(3) # liste sonuna  3 ekler
sonuc = my_tuple.count(1) # tuple içinde 1 elamının kaç deva döndügünü bakar 

my_tuple2 = tuple([2,3,4]) # dönüşüm 
my_list2  = list((2,3,4)) # dönüşüm 
print(type(my_tuple2)) # <class 'tuple'>
print(type(my_list2))# <class 'list'>