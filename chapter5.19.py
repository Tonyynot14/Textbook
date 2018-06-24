num = int(input("Enter the number of lines for the pyramid: "))
updateNum=num*2-1


def space(spaces):
    count=0
    while count<spaces:
        print(" ",end="")
        count+=1



space(updateNum)
print("1")
for j in range(2,num+1):
    space(updateNum-2)
    for i in range(j,0,-1):
        print(i,end=" ")
    for k in range(2,j+1):
        print(k,end=" ")

    print()
    updateNum -= 2
