def leftOfTheLine(x0,y0,x1,y1,x2,y2):
    direction = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
    if direction>0:
        return True
    else:
        return False


def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    direction = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
    print (y0)
    if direction < 0:
        return True
    else:
        return False

def onTheSameLine(x0, y0, x1, y1, x2, y2):
    direction = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if direction == 0:
        return True
    else:
        return False

def onTheLineSegment(x0, y0, x1, y1, x2, y2):

   # find lowest and highest point so that you know the range of points of the line segment
    if x0>x1:
        highestx=x0
    else:
        highestx=x1

    if y0>y1:
        highesty=y0
    else:
        highesty=y1
    if x0 < x1:
        lowestx = x0
    else:
        lowestx = x1

    if y0 < y1:
        lowesty = y0
    else:
        lowesty = y1


    direction = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    if onTheSameLine(x0, y0, x1, y1, x2, y2) and (x2<highestx and y2<highesty and x2>lowestx and y2>lowesty):
        return True
    else:
        return False




x0,y0,x1,y1,x2,y2=eval(input("Enter the coordinates for p0,p1,and p2:"))

if leftOfTheLine(x0,y0,x1,y1,x2,y2):
    print("p2 is on the left side of the line ")
elif rightOfTheLine(x0,y0,x1,y1,x2,y2):
    print("p2 is on the right side of the line ")

elif onTheSameLine(x0,y0,x1,y1,x2,y2):
    print("p2 is on the same line ")
    if(onTheLineSegment(x0,y0,x1,y1,x2,y2)):
        print("p2 is also within the line segment connecting the two lines")


