def m(i):
    sum = 0
    for j in range(1,i+1):
        sum+=((-1)**(j+1))/(2*j-1)
    new =sum*4
    print(format(j,"3d"),format(new,"12.4f"))



for i in range(1,901+1,100):
    m(i)