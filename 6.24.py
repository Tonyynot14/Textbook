def prime(num):
    divisibleNums=1
    for i in range(2,num):
        if num%i==0:
            divisibleNums+=1

    if divisibleNums>1:
        return False
    else:
        return True



def palindromic(num):
    updateNum=num
    final=""
    while updateNum>0:
        final+=str(updateNum%10)
        updateNum=updateNum//10
    final=int(final)
    if num==final:
        return True
    else:
        return False

#input needs to be how many numbers to display
def palindromicPrime(positives):
    count=2
    while positives>0:
        if palindromic(count) and prime(count):
            print(format(count,"5d"),end=" ")
            positives-=1
            if positives%10==0:
                print()

        count+=1





palindromicPrime(100)

