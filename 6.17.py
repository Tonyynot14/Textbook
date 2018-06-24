def isValid(side1,side2,side3):
    sideAdd1 = side1+side2
    sideAdd2 = side1+side3
    sideAdd3 = side2+side3

    if sideAdd1 > side3 and sideAdd2 >side2 and sideAdd3 >side1:
        return True
    else:
        return False


def area(side1,side2,side3):
    s = (side1+side2+side3)/2
    areaTri = (s*(s-side1)*(s-side2)*(s-side3))**(1/2)
    return areaTri


side1,side2,side3 = eval(input("Enter thre sides in double:"))
if isValid(side1,side2,side3):
    print("The Area of the triangle is ", area(side1,side2,side3))
else:
    print("Input is invalid")