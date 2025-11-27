
def multiplication_table(n):
    print(f"MULTIPLICATION TABLE OF {n}")
    for i in range(1, 13):
        print(f"{i} x {n} = {i * n}")

# Kullanıcıdan sayı alma
number = int(input("Enter a number: "))
multiplication_table(number)
