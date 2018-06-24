tuition=10000
increase=1.05
fourYear =0
for i in range(1,14):
    tuition=tuition*increase
    if i==10:
        print("The tuition in 10 years is",format( tuition,".2f"))
    if i>=10:
        fourYear+=tuition
        #print(fourYear)

print ("The price for four years after 10 years of increase is",format(fourYear,".2f"))