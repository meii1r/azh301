# Вводим трехзначное число
n = int(input())

# Получаем последнюю цифру (первую справа)
last_digit = n % 10

# Получаем оставшиеся две цифры
rest = n // 10

# Формируем новое число
new_number = int(str(last_digit) + str(rest))

print(new_number)