#6
import math

x_degrees = float(input())
x_radians = (x_degrees * math.pi) / 180
result = math.sin(x_radians) + math.cos(x_radians) + (math.tan(x_radians))**2
print(result)
