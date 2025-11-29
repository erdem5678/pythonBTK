class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.pages_read = 0

# methodlar:
    def read(self, pages_count):
        self.pages_read += pages_count # Okunan sayfa sayısını toplama ekle


 # Toplam sayfadan fazla okunmasın (sayfa sınırını kontrol et)
        if self.pages_read > self.pages:
            self.pages_read = self.pages

# Kalan sayfa sayısını hesapla
        kalan_sayfa = self.pages - self.pages_read
        print(f"{pages_count} sayfa okunudu. kalan:{kalan_sayfa}")

# kitap bittiyse bildir
        if kalan_sayfa == 0:
            print("kitap bitti")

# Nesne string'e çevrildiğinde kitap bilgilerini göster
    def __str__(self):
        return f"kiyap: {self.title } - yazar: {self.author}"
    
# len() fonksiyonu ile toplam sayfa sayısını döndür   
    def __len__(self):
        return self.pages


# test kodu
print("--- Book 1 ---")
b = book("1984", "Albus Dumbeledor", 309)
print(b)
print(f"toplam sayfa : {len(b)}")

# okuma işlemi
b.read(50)
b.read(100)
b.read(150)

print("\n--- Book 2 ---")
#başka kitap
b2 = book("suç ve ceza", "Dostoyevski", 500)
print(b2)
print(f"toplam sayfa : {len(b2)}")

b2.read(250)
b2.read(250)
    


