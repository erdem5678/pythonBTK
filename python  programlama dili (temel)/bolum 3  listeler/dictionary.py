sehirler = ['kocaeli', 'istanbul']
plakalar = [41,34]

# key value

print(plakalar[0], sehirler[0])
print(plakalar[1], sehirler[1])

print(plakalar[sehirler.index('istanbul')])# sehiler degişkenin icinde index ile istanbul plakasını cekiyoruz  
print(plakalar[sehirler.index('kocaeli')])

# dictionary

plakalar ={
    'kocaeli': 41, 
   'istanbul': 34,
     'izmir':36
}

plakalar['izmir'] = 35 # dictionary öge ekleme 

print(plakalar['kocaeli'])
print(plakalar['istanbul'])
print(plakalar['izmir'])
