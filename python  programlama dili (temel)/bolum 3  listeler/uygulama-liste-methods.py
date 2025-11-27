customers = ["satikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

#1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık sipariși listeye ekleyiniz.
customers.append("sadikturan") 
order_totals.append(5000)
#2- Son eklenensiparişi siliniz.

customers.pop() #sonuc = custommers
order_totals.pop()#sonuc = order_totals

#3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
#'‹username›' isimli müşterinin sipariș toplamı '<10000›' liradır.(döngüler)

# sonuc = f"{customers[0]} isimli müşterinin sipariș toplami{order_totals[0] + order_totals[4]}liradir"
# sonuc = f"{customers[1]} isimli müşterinin sipariș toplami{order_totals[1]}liradir"

#4- Müşterileri alfabetik olarak sıralayınız.

customers.sort() #print(customers) böyle çaşır

#5- Sipariș toplamlarını azalan şekilde sıralayınız.

order_totals.sort()
order_totals.reverse() # liste elmanlarını tersden sıralar 

#6- En düşük sipariş hangisidir?

sonuc = min(order_totals)
soncu = max(order_totals)

#7-'sadikturan' isimli kullanıcının kaç tane sipariși vardır?

sonuc = customers.count('sadikturan')

#8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.

customers.remove('ahmetyilmaz')

#9- Listelerdeki tüm içerikleri siliniz.

customers.clear()
order_totals.clear()

#10- Kullanıcıdan aldığınız kullanıcı adı ve sipariș toplamlarını listeye
username = input('muster ad: ')
toplam = input('toplam: ')
customers.append(username)
order_totals.append(toplam)
print(customers)
print(order_totals)
#['barış ']
#['5000']
#print(sonuc)