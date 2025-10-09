A = int(input("Введите число A: "))
B = int(input("Введите число B (B > A): "))

sum_squares = 0
for i in range(A, B + 1):
    sum_squares += i ** 2

print("Сумма квадратов от", A, "до", B, "равна", sum_squares)