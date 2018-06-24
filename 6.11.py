def salesCommission(sales):

    if sales<=10000:
        commission = sales*(.09)
    elif  sales<=15000:
        commission = sales*(.10)
    elif sales > 10000:
        commission = sales * (.12)
    return commission



print("Sales amount \t\t Commission")
for i in range (10000,100001,5000):
    print(i,"\t\t\t",salesCommission(i))




