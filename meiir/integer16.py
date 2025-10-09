# Вводим трехзначное число
num = int(input("Введите трехзначное число: "))

# Получаем сотни, десятки и единицы
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Меняем местами десятки и единицы
new_num = hundreds * 100 + units * 10 + tens

print("Результат:", new_num)