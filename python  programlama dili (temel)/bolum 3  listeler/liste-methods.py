sayilar = [4,6,8,2,56,77,90,4,4,]
isimler = ['ahmet', 'canan' , ' zeynep', ' gokhan', ' ali', 'canan']

sonuc = min(sayilar)
sonuc = min(isimler)
sonuc  = max(sayilar)
sonuc = max(isimler)

# ekleme

sayilar.append(12)
isimler.append('cinar')
sonuc = sayilar
sonuc = isimler

sayilar.insert(0,100) # verilen index numrasına 100 elmanına ekler 
sayilar.insert(-1,100)
sayilar.insert(-3,100)
sayilar.insert(len(sayilar),100) # lisstenin sonu 100 ekler 
sonuc = sayilar


# silme

sayilar.pop() # son elmenı siler 
sayilar.pop(0) # listedeki ilk elmanı siler çünkü index numarısı verilmiştir 
isimler.remove('canan')
del isimler[1] # del ile listedelki index numarısı 1 olan canan kişisini sildim 

# sıralama
sayilar.sort() # sayıları küçükten büyge sıralar 
isimler.sort() #isimleri alfabatik sıraya göre sıralar
sayilar.reverse()# listeyi tersden sıraladı 

sonuc = sayilar.count(4) # sayilar listesinde 4 elmanı kaç deva geçiyor  3
sonuc = isimler.count('canan') # isimler listesinde canan elmanı kaç deva geçiyor 2 

print(sonuc)