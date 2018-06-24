def distance(x1,y1,x2,y2):
    pointToPoint = (((x1-x2)**2)+((y1-y2)**2))**.5
    return pointToPoint


x1,y1 = eval(input("Enter the X and Y coordinate of point one:"))
x2,y2 = eval(input("Enter the X and Y coordinate of point two:"))


ptDistance = distance(x1,y1,x2,y2)


print("The distance between point 1 and point 2 is", ptDistance)