def calculate_area(base1, base2, height):
    area = (base1 + base2) * height / 2
    return area

def calculate_perimeter(base1, base2, side1, side2):
    perimeter = base1 + base2 + side1 + side2
    return perimeter

# Example usage:
base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the height of the trapezium: "))

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))

area = calculate_area(base1, base2, height)
perimeter = calculate_perimeter(base1, base2, side1, side2)

print("Area:", area)
print("Perimeter:", perimeter)
