

N = int(input("Введите целое число N (> 0): "))
if N <= 0:
    print("N должно быть больше 0")
else:
    s = 0.0
    for i in range(1, N + 1):
        s += 1 / i
    print("Сумма:", s)