num = int(input("Enter a number and I will tell you the prime factors: "))
numDivid = num
highest=0

for j in range(2,num):
    #print count or the prime factor need num to update
    while numDivid%j==0:
        highest=j
        numDivid=numDivid/j

numDivid=num
for i in range(2,highest+1):
    #print count or the prime factor need num to update
    while numDivid%i==0:
        if i!=highest:
            print(i,",",sep="",end = " ")
        else:
            print(i)
        numDivid = numDivid / i



