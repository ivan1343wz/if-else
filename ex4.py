#4
import math

def calculate_rectangle_area(width, height):
    return width * height
def calculate_circle_area(radius):
    return math.pi * radius ** 2
width, height = map(float, input("введите ширину и высоту с пробел:").split())
rectangle_area = calculate_rectangle_area(width, height)
print(f"площадь прямоугольника: {rectangle_area:.2f}")
radius = float(input("введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print(f"площадь круга: {circle_area:.2f}")
