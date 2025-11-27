programlama_dilleri = ["python", "c#", "java" , "javascript"]

sonuc = programlama_dilleri
sonuc = type(programlama_dilleri)
sonuc = programlama_dilleri[0:2] # ilk index geçerlidir ancak sonki index geçrli degildir 
print(sonuc)
sonuc = programlama_dilleri[:2]
sonuc = programlama_dilleri[:]
sonuc = programlama_dilleri [-3:-1]
sonuv = programlama_dilleri[-3:]
print(sonuc)
# güncelleme
programlama_dilleri[-1] = "c++"

sonuc = programlama_dilleri
sonuc = len(programlama_dilleri)
sonuc = programlama_dilleri + ["php", "go"]

sonuc = "python" in programlama_dilleri
sonuc = "HTML" in programlama_dilleri #koşul ifadeleri  liste içinde elaman   sorgulamaya yarar

del programlama_dilleri[0]

for dil in programlama_dilleri: # ["python", "c#", "java" , "javascript"] döngül ile e listedeki elemanları ekrana yazdırdık 
    print(dil)
#print(sonuc)