A = int(input("Введите число A: "))
B = int(input("Введите число B (B > A): "))
proz = 1

for i in range(A, B + 1):
    proz *= i

print("Сумма всех целых чисел от A до B включительно:", proz)