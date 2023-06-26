# Created by Nikki Abrasado 15/5/23
# Updated last 8/6/23

 
# Ask user what shape they would like

answer = input("What shape do you need to know the area/perimeter of? Select the letter matching to the shape"
               "you would like to use:\n"
               "a) Rectangle\n"
               "b) square\n"
               "c) Circle\n"
               "d) triangle\n"
               "e) parallelogram\n"
               "f) trapezium\n"
               "Select an option (a, b, c, d, e, f): ")

# Check the user's answer and redirect to the corresponding file
if answer == "a":
    exec(open("rectangle.py").read())  # Execute the code in rectangle.py
elif answer == "b":
    exec(open("square.py").read())  # Execute the code in square.py
elif answer == "c":
    exec(open("circle.py").read())  # Execute the code in circle.py
elif answer == "d":
    exec(open("triangle.py").read())  # Execute the code in triangle.py
elif answer == "e":
    exec(open("parallelogram.py").read())  # Execute the code in parallelogram.py
elif answer == "f":
    exec(open("trapezium.py").read())  # Execute the code in file_c.py
else:
    print("Invalid option. Please input letters ranging from a-f to pick the shape")




