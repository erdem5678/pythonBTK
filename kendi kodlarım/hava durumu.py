def hava(sicaklik):
    if sicaklik <= 0 :
        return "donuyor"
    elif sicaklik <= 15 :
        return "soguk"
    elif sicaklik <=25 :
        return "ilik"
    else:
        return "sicak"

girdi = int(input("lufen sicaklik girin: "))
sonuc = hava(girdi)
print(f"girdiniz sivaklik durumu: {sonuc}")