A = int(input("Введите число A: "))
B = int(input("Введите число B (B > A): "))
summa = 0

for i in range(A, B + 1):
    summa += i

print("Сумма всех целых чисел от A до B включительно:", summa)