# Вводим трехзначное число
num = int(input("Введите трехзначное число: "))

# Извлекаем сотни, десятки и единицы
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

# Меняем местами сотни и десятки
new_num = tens * 100 + hundreds * 10 + units

print("Результат:", new_num)