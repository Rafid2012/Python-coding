print("Enter 1 if you want to calculate area of circle")
print("Enter 2 if you want to calculate area of rectangle")
print("Enter 3 if you want to calculate area of square")
print("Enter 4 if you want to calculate area of triangle")
print("Enter 5 if you want to calculate area of parallelogram")
print("Enter 6 if you want to calculate area of trapezium")

a = int(input("Enter your choice: "))

if a == 1:
    r = float(input("Enter the radius of the circle: "))

    area1 = 3.14159 * r**2

    print("The area of the circle is: ",round(area1,2))

elif a == 2:
    l = float(input("Enter the lenth of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    
    area2 = l*w

    print("the area of the rectangle is: ",round(area2,2))

elif a == 3:
    sl = float(input("Enter the lenth of a side of the square: "))
    
    
    area3 = sl*sl

    print("the area of the square is: ",round(area3,2))

elif a == 4:
    b = float(input("Enter the lenth of the base of the triangle: "))
    h = float(input("Enter the hight of the triangle: "))
    
    area4 = b*h / 2

    print("the area of the triangle is: ",round(area4,2))

elif a == 5:
    b1 = float(input("Enter the lenth of the base of the parallelogram: "))
    h1 = float(input("Enter the hight of the parallelogram: "))
    
    area5 = b1*h1

    print("the area of the parallelogram is: ",round(area5,2))

elif a == 6:
    b2 = float(input("Enter the lenth of the base of the trapezium: "))
    b3 = float(input("Enter the lenth of the 2nd base of the trapezium: "))
    h2 = float(input("Enter the hight of the trapezium: "))
    
    area6 = b2+b3 / 2 * h2

    print("the area of the trapezium is: ",round(area6,2))





