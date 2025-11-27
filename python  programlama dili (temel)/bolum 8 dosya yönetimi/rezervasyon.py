def bilet_sistemi():
    eco_biletler = [1, 2, 3, 4, 5]
    vip_biletler = [6, 7, 8, 9, 10]


    while eco_biletler or vip_biletler:
        ad = input("Adiniz: ")
        ucak_sinif = input("Bilet türü (eco, vip): ").lower()
        adet = int(input("Bilet adedi: "))

        if ucak_sinif == "eco" and not eco_biletler:
            print("Ekonomi biletleri tükendi. Diger uçuş 2 saat sonra.")
            continue
        elif ucak_sinif == "vip" and not vip_biletler:
            print("VIP biletleri tükendi. Diger uçuş 2 saat sonra.")
            continue


        if ucak_sinif == "eco":
            if len(eco_biletler) >= adet:
                print(f"{ad}, {adet} adet ekonomi bileti alindi.")
                for i in range(adet):
                    eco_biletler.pop(0)
                with open("rezervasyonlar.txt", "a",encoding="utf-8") as dosya:
                    dosya.write(f"{ad} - ECO - {adet}\n")
            else:
                print("Yeterli ekonomi bileti yok. Diğer uçuş 2 saat sonra.")
    
        elif ucak_sinif == "vip": 
            if len(vip_biletler) >= adet:
                print(f"{ad}, {adet} adet VIP bileti alindi.")
                for i in range(adet):
                 vip_biletler.pop(0)  # Biletleri listeden kaldır
            with open("rezervasyonlar.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"{ad} - VIP - {adet}\n")
        else:
            print("Yeterli VIP bileti yok. Diğer uçuş 2 saat sonra.")
    else:
        print("Geçersiz bilet türü. Lütfen 'eco' veya 'vip' girin.")

    print("\nTüm biletler tükendi. Sistem kapanyor.")
    
    # Bilet sorgulama
    print("\n--- Rezervasyon Sorgulama ---")
    ad_sorgu = input("Sorgulamak istediğiniz ad: ")
    ucak_sinif_sorgu = input("Sorgulamak istediğiniz sinif (VIP/ECO): ").lower()

    var_mi = False
    with open("rezervasyonlar.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            satir_ad, satir_sinif, satir_adet = [x.strip() for x in satir.split("-")]# satiri parçalara ayır ve boşlukları temizle
            if satir_ad == ad_sorgu and satir_sinif == ucak_sinif_sorgu:# eşleşme kontrolü
                var_mi = True
                break

    if var_mi:
        print(f"{ad_sorgu} adli kullanicinin {ucak_sinif_sorgu} sinifinda rezervasyonu mevcut.")
    else:
        print(f"{ad_sorgu} adli kullanicinin {ucak_sinif_sorgu} sinifinda rezervasyonu bulunamadi.")

bilet_sistemi()
