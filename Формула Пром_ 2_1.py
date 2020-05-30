import math

a = float(input("a = "))
b = float(input("b = "))

x1 = math.sqrt(a * b) / (math.exp(a) * b) + a * math.exp(2 * a / b)
print(x1)
