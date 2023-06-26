def calculate_area(base, height):
    area = 0.5 * base * height
    return area

def calculate_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

# Example usage:
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = calculate_area(base, height)
perimeter = calculate_perimeter(side1, side2, side3)

print("Area:", area)
print("Perimeter:", perimeter)