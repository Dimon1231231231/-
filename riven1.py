import math

S = float(input("Введіть площу трикутника S: "))
a = float(input("Введіть різницю (основа більша за висоту на a): "))

# Основа b = h + a, площа S = (b * h) / 2 => S = ((h + a) * h) / 2
# 2S = h^2 + a*h
# h^2 + a*h - 2S = 0

discriminant = a**2 + 8 * S
h = (-a + math.sqrt(discriminant)) / 2  # беремо додатний корінь

print(round(h, 2))