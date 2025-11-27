# indekslenemez
# sıralanamz 
#güncellenemez
#elemanlar tekrarlanamz
#eleman siler yada ekleriz

#discard()
#Sadece set (küme) yapılarında kullanılır.
#Eleman yoksa sessizce geçer, hata vermez.
#"Varsa sil, yoksa umurumda değil" der.

#remove()

#Listelerde veya setlerde kullanılır.
#Silmek istediğin eleman yoksa HATA (KeyError) verir.
#"Bu elemanı kesin sil, yoksa bağırırım" der gibi davranır.


my_set = {"ahmet","mehmet","toprak","cem","alp"}
my_set.discard("alp") # set (kullanılır)discard ile set de 11 sayısını çıkarsık 

my_set.remove("mehmet") #list, set kullanılır genelikle 
my_set.clear()
print(my_set)


set1 = {1, 2, 3, 4,6,8,9}
set2 = {2, 4, 6, 8,}

print(set1 | set2)                     
print(set2.union(set1))                
print(set1 & set2)                     
print(set1.intersection(set2))        
print(set1 - set2)                    
print(set2 - set1)                     
print(set1 ^ set2)                     
print(set1.symmetric_difference(set2))
subset_check = set1  >= set2            
print(subset_check)



