class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Example usage:
length = int(input("enter the length :  "))
width = int(input("enter the width :  "))
rectangle = Rectangle(length, width)

area = rectangle.calculate_area()

print(f"Length of the rectangle: {length}")
print(f"Width of the rectangle: {width}")
print(f"Area of the rectangle: {area}")
