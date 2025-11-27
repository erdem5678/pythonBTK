import sqlite3  # SQLite veritabanı işlemleri için gerekli modül içe aktarılıyor
connection = sqlite3.connect("chinook.db")# 'chinook.db' adlı veritabanına bağlantı oluşturuluyor
cursor = connection.cursor() # SQL komutlarını çalıştırmak için cursor (imleç) oluşturuluyor

sql = "INSERT INTO genres(name) VALUES('Macera')"
cursor.execute(sql) 
connection.commit() # sorguyu veri tabanıan gönderiyoruz 

# cursor.execute("SELECT * FROM customers WHERE city = 'Oslo'") # Oslo şehrindeki müşterileri sorgulayan SQL komutu çalıştırılıyor
# text = cursor.fetchall() # coklu kayıt almak isdedigimiz de bunu kullanırız 
# text = cursor.fetchone() # fetchone() → Sadece ilk bulunan kaydı çeker
# print(text)
# for customer in text:
#    print(customer[1] + " " + customer[2])

connection.close() # Bağlantı kapatılıyor
print("Veritabani bağlantisi yapildi")
