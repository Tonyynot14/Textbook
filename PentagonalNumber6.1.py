#function to find pentagonal number of value N
def getPentagonalNumber(n):
    solution = n*(3*n-1)/2
    return solution


for i in range(101):
    print(int(getPentagonalNumber(i)),end="")
    if i%10==0:
        print()
