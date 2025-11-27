def full_name(firstname: str, lastname: str, age: int) -> str:
    return f"your name is {firstname} {lastname} and your age is {age}"

sonuc = full_name("sadik", "turan", 22)
sonuc = full_name(lastname= "bariş", firstname= "erdem", age=22)
sonuc = full_name(lastname= "turan", firstname= "sadik", age= 22)
sonuc = full_name(firstname= "sadik", lastname= "turan", age= 22)
print(sonuc)