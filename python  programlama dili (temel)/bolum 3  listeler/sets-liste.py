meyveler ={"elma", "armut","kiraz",}
meyveler2 = {"elma", "armut","kiraz","kavun"}
 
# sonuc = meyveler[0] # bu kullanım yanlıştır set metohunda index yoktur 

for x in meyveler: # set içindeki  elemanlara for döngüsü ile erişilir 
      print(x)

sonuc = "elma" in meyveler # elma elamanını meyveler için var mı diye kontrol eder varsa True yoksa False döner


meyveler.add("karpuz") # add metodu ile meyveler listesine karpuz ekledik 
meyveler.update(meyveler2) # meyveler 2 listesini güncelledik  ve böylece 2 listede aynı olan elemanlar tekara yazılmayacak 
meyveler.remove("elma")# remov ile elma elemanını sildik "raise an error"
meyveler.discard("armut")# bu metoda  remove gibi aynı işi yaparv
meyveler.pop() # rasgele eleman silinir
meyveler.clear() # tüm seti siler "set()"
sonuc = meyveler
print(sonuc)