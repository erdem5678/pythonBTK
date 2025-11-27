def bilet_sistemi():
    eco_biletler = [1,2,3,4,5]
    vip_biletler = [6,7,8,9,10]

    while True:
        ad = input("Adiniz: ")
        ucak_sinifi = input("Bilet türü (eco,vip): ").lower()
        adet = int(input("Bilet adeti: "))

        if ucak_sinifi == "ecc":
            if len(eco_biletler) >= adet:
                print(f"{ad}, {adet} adet ekonomi bileti alindi.")
                for i in range(adet):
                    eco_biletler.pop(0) # bileti listeden kaldırır
            else:
                print("Yeterli ekonomi Bİleti yok.Diger uçuş 2 saat sonra.")

        elif ucak_sinifi == "vip":
            if len(vip_biletler) >= adet:
                print(f"{ad},{adet} adet vip bileti aldi")
                for i in range(adet):
                    vip_biletler.pop(0)

        else:
            print("Yeterli VIP bileti yok. Diger uçuş 2 saat sonra.")
    else:
        print("Gecerli bilet türü girin. 'eco' veya 'VIP'")
bilet_sistemi()  
