words = ["bariş","caliskan","Erdem"]
uzunkelime = ""
max_len = 0

for kelime in words:
    if len(kelime) > max_len:
        max_len = len(kelime)
        uzunkelime = kelime
print(uzunkelime)