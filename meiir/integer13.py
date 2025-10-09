# Дано трехзначное число
n = int(input("Введите трехзначное число: "))

# Получаем первую цифру, остальные две цифры
first_digit = n // 100
last_two_digits = n % 100

# Формируем новое число
result = last_two_digits * 10 + first_digit

print(result)