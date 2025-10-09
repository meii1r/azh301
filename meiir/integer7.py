# Ввод двузначного числа
num = int(input("Введите двузначное число: "))

# Получение цифр
tens = num // 10
units = num % 10

# Сумма и произведение
sum_digits = tens + units
prod_digits = tens * units

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", prod_digits)