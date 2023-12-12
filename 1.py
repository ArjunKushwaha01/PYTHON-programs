import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = 5
circle = Circle(radius)

area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print(f"Radius of the circle: {radius}")
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter of the circle: {perimeter:.2f}")
