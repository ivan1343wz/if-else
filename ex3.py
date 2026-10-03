#3
number = int(input())
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10
print(f"цифра в позиции тысяч равна {thousands}")
print(f"цифра в позиции сотен равна {hundreds}")
print(f"цифра в позиции десятков равна {tens}")
print(f"цифра в позиции единиц равна {units}")
