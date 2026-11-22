# Дано дробное число x. Выведите вторую цифру после точки.
num = float(input())
antwort = int(abs(num) * 100 % 10)
print(antwort)