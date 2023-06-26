def calculate_area(base, height):
    area = base * height
    return area

def calculate_perimeter(side1, side2):
    perimeter = 2 * (side1 + side2)
    return perimeter

# Example usage:
base = float(input("Enter the base length of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))

area = calculate_area(base, height)
perimeter = calculate_perimeter(side1, side2)

print("Area:", area)
print("Perimeter:", perimeter)
