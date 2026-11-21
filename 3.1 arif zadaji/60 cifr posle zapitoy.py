from decimal import Decimal, getcontext

getcontext().prec = 60

a = Decimal(input())
b = Decimal(input())
formula = a.sqrt() + b
print(formula)