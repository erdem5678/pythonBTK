while True: 
        try:
                x = int(input("x: "))
                y = int(input("y: "))
                print(x / y)
                
        except(ZeroDivisionError, ValueError) as file: 
                # with open("hata_kayitlari.txt", "a", encoding="utf-8") as f:
                #  f.write(f"Hata: {str(file)}\n")
                #  f.write("-------------\n")
                print("x ve ye sayi olmaz. sifir olamaz")
                print(file)

        except Exception as e:
                print("bilinmeyen bir hatta oluştu")
                print(e)

        else:
                break              #print("her şey yolunda ")
        finally:
                print("finally bloğu çalişti")
#finally = Python’da try/except yapısının “HER TÜRLÜ DURUMDA çalışan” kısmıdır.
#Hata olsun, olmasın, return olsun, break olsun… mutlaka çalışır