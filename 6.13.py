def m(i):
    sum=0
    print("i\t\t\t m(j)")
    for j in range(1,i+1):
        sum+=j/(j+1)
        print(j,"\t\t",format(sum,"8.4f"))




m(20)