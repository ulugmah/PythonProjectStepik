# Напишите программу, которая получает на вход целое число n и выводит 5 строк содержащих True или False с ответами на эти вопросы:
# 1) Является ли число четным?
# 2) Число является положительным?
# 3) Число находится в промежутке от -5 включительно до 5 включительно?
# 4) Число делится на 3 и 4, но не делится на 7?
# 5) Является ли число трехзначным?

x = int(input())
chetniy =x % 2 == 0
polojitelniy = x > 0
promejutok = -5 <= x <= 5
delitsa = x%3 == 0 and x%4 == 0 and x%7 != 0
trehznach = 100 <= abs(x) <= 999
print(chetniy)
print(polojitelniy)
print(promejutok)
print(delitsa)
print(trehznach)
