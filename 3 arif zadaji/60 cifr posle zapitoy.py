# Попробуйте Decimal в деле! Вашей программе на вход подаются два числа с плавающей точкой a и b.
# formula = a.sqrt() + b
# Посчитайте для них формулу точностью 60 знаков.
from decimal import Decimal, getcontext

getcontext().prec = 60

a = Decimal(input())
b = Decimal(input())
formula = a.sqrt() + b
print(formula)