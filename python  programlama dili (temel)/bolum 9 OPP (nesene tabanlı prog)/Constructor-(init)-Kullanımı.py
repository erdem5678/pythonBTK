class Ogrenci:
    def __init__(self, isim, notlar):
        self.isim = isim
        self.notlar = notlar

    def ortalama(self):
        return sum(self.notlar) / len(self.notlar)

# Nesneler
ogr1 = Ogrenci("Ali", [80, 90, 85])
ogr2 = Ogrenci("Ayşe", [95, 90, 92])

# Ortalamaları yazdır
print(f"{ogr1.isim} ortalamasi: {ogr1.ortalama()}")
print(f"{ogr2.isim} ortalamasi: {ogr2.ortalama()}")