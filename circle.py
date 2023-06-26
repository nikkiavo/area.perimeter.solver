import math

def calculate_area(radius):
    area = math.pi * radius**2
    return area

def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

# Example usage:
radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)
perimeter = calculate_perimeter(radius)

print("Area:", area)
print("Perimeter:", perimeter)