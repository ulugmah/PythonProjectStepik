# Вашей программе на вход даются 3 строки. Выведите обратно строку наименьшей длины.
# В случае, если длина у нескольких строк совпадает – выведите ту, которая была введена позже остальных.
# Напоминаем, что посчитать длину строки можно с помощью len.
pervaya =str(input(""))
vtoraya =str(input(""))
tretaya =str(input(""))
if len(pervaya) <len(vtoraya):
    print(pervaya)
elif len(vtoraya)<len(tretaya):
    print(vtoraya)
else:
    print(tretaya)