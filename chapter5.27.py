


for j in range(10000,100001,+10000):
    sum=0
    count=0
    for i in range(1,j,2):
        count+=1
        if count%2==0:
            sum-=1/i
        else:
            sum += 1 / i
    pi=sum*4

    print(j,"as the interactions =",pi)


