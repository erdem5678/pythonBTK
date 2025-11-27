# print(10/0)

# x = 10
# if x > 5:
#     raise ValueError("x 5 den büyük olamaz")

def renklendir(text, renk):
     renkler = ("blue", "red", "with", "black","orange")
     if type(text) is not str:
       raise TypeError("text str tpinde olmalidir")
    
     if type(renk) is not str:
        raise TypeError("renk str tipinde olmalidir")
    
     if renk not in renkler:
        raise ValueError("gecersiz renk")
    
     print(f"{text} {renk} olarak yazildi")

try:

    renklendir("selam", "blue")
    renklendir("merhaba", "green")
except (TypeError, ValueError) as ex:
    print(ex)