n = int(input("Введите целое число больше 999: "))
thousands_digit = (n // 1000) % 10
print("Цифра в разряде тысяч:", thousands_digit)