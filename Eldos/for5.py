# Введите цену за 1 кг конфет
price_per_kg = float(input("Введите цену за 1 кг конфет: "))

# Вывести стоимость 0.1, 0.2, ..., 1 кг конфет
for i in range(1, 11):
    weight = i * 0.1
    cost = weight * price_per_kg
    print(f"{weight:.1f} кг конфет стоит {cost:.2f}")