def calculate_area(side_length):
    area = side_length ** 2
    return area

def calculate_perimeter(side_length):
    perimeter = 4 * side_length
    return perimeter

# Example usage:
side_length = float(input("Enter the side length of the square: "))

area = calculate_area(side_length)
perimeter = calculate_perimeter(side_length)

print("Area:", area)
print("Perimeter:", perimeter)
