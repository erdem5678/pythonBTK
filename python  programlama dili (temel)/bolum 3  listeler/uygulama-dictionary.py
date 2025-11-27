# Aşagıdaki ögrenci bilgilerini dictionary listesinde saklaynız.
      # 101 yiğit bilgi 2010 (40,80,90)
      # 102 Ada bilge 2012 (80,80,80)
      # 103 çınar turan 2017 (70,70,70)
ogrenciler = {
    101: {
    "ad": "yiğit",
    "soyad":"bilge",
    "dogumYili": 2010,
    "notlar":(40,80,90)

    },
    102:{
   "ad": "Ada",
    "soyad":"bilge",
    "dogumYili": 2012,
    "notlar":(80,80,80)
    },
    103:{
    "ad": "çinar",
    "soyad":"turan",
    "dogumYili": 2017,
    "notlar": (70,70,70)
    }
}

# klavyeden girilen ögrenci numarasına göre aşagıdaki çümleyi yazdırınınız  
     # 101 numaralı yiğit bilge isimindeki ögrencinin yaşı 14 ve not ortalaması 70
ogrenciNo = int(input('ogrenci no: ')) #print(ogrenciler[ogrenciNo])
ogrenci = ogrenciler[ogrenciNo]
ortalama = (ogrenci["notlar"][0] + ogrenci["notlar"][1] + ogrenci["notlar"][2]) / 3
print(f"{ogrenciNo} numarali {ogrenci["ad"]}{ogrenci["soyad"]}  isimindeki ögrencinin yaşi {2024 - ogrenci["dogumYili"]} ve not ortalamasi {ortalama}")