email = "info@sadikturan.com"
parola = "123456"

email = (input("email gir: "))
parola = (input("parola  gir: "))

if(email == "info@sadikturan.com"):
    if(parola == "123456"):
        print("login olsundu ")
    else:
        print("parola yanliş")
else:
    print("email yanliş")