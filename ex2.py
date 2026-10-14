#2
#
weight = float(input("введите ваш вес в килограммах "))
height = float(input("введите ваш рост в метрах (например, 1.78)"))
bmi = weight / (height ** 2)
print(f"ваш индекс массы тела равен {bmi:.1f}")
