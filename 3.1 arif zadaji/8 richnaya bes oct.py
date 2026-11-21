number = int(input())

# Если число равно 0, сразу выводим 0
if number == 0:
    print(0)
else:
    octal = ""
    while number > 0:
        # Находим остаток от деления на 8
        remainder = number % 8
        # Добавляем остаток в начало строки
        octal = str(remainder) + octal
        # Уменьшаем число в 8 раз (целочисленное деление)
        number //= 8

    print(octal)