# bir ögrencinin 2 yazılı bir sözl notunu alarak ortalma hesaplayınız ve hesaplanan ortalmayı göre not aralıgını karşılık gelen degerlendrimeyi yazdırınız 
#   0-24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5

yazili1 = float(input("yaziki 1: "))
yazili2 = float(input("yaziki 2: "))
proje = float(input("proje: "))
ortalama = (yazili1 + yazili2 + proje) / 3

if(ortalama >= 0) and (ortalama < 25):
    print(f"ortalmaniz: {round(ortalama)} ve dedgerlendirme notu : 0") # round metordu ile  ayı bir sonraki sayı yuvarlya biliriz  "86.66" "87" olması gibi 
elif (ortalama >= 25) and (ortalama < 45):
    print(f"ortalmaniz:  {round(ortalama)}  ve dedgerlendirme notu : 1")
elif (ortalama >= 45) and (ortalama < 55):
    print(f"ortalmaniz:  {round(ortalama)}  ve dedgerlendirme notu : 2")
elif (ortalama >= 55) and (ortalama < 70):
    print(f"ortalmaniz:  {round(ortalama)}  ve dedgerlendirme notu : 3")
elif (ortalama >= 70) and (ortalama < 85):
    print(f"ortalmaniz:  {round(ortalama)} ve dedgerlendirme notu : 4")
elif (ortalama >=85) and (ortalama <= 100):
    print(f"ortalmaniz:  {round(ortalama)}  ve dedgerlendirme notu : 5")
else:
    print("yanlis not bilgisi")