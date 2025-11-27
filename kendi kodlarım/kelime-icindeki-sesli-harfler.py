kullanici = (input("kelime al :"))

sesli_harf = "aeiouAEIOU"
count = 0
for kelime in kullanici:
    if kelime in sesli_harf:
        count += 1
print("sesli harf sayisi: " ,count)