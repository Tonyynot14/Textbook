def spacing(num):
    for i in range(num):
        print("  ",end="")



def displayPattern(n):
    space=n
    for i in range(n+1):
        spacing(space)
        for j in range(i,0,-1):

            print(j,end=" ")
        space-=1
        print()



displayPattern(6)

