condition = True
while condition:
    firstSide = int(input("Enter 1st side: "))
    secondSide = int(input("Enter 2nd side: "))
    thirdSide = int(input("Enter 3rd side: "))
    if not (firstSide > 0 and secondSide > 0 and thirdSide > 0):
        condition = False
    # Triangle Inequality Theorem
    else:
        triangleSides = [firstSide, secondSide, thirdSide]
        triangleSides.sort()
        if (triangleSides[0] + triangleSides[1] > triangleSides[2]):    # If it is a triangle based on Inequality theorem
            # Checking for equilateral triangle:
            if (triangleSides[0] == triangleSides[1] and triangleSides[0] == triangleSides[2]):
                print("Equilateral triangle\n")
            # Checking for isosceles triangle
            elif (triangleSides[0] == triangleSides[1] or triangleSides[0] == triangleSides[2] or triangleSides[1] == triangleSides[2]):
                print("Isosceles triangle\n")
            else:
                print("Scalene triangle\n")

        else:
            print("Not a triangle\n")
    
print("Bye")
