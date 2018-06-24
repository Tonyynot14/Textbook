
amount = eval(input("Enter the loan amount:"))
years = eval(input("Enter number of years for loan:"))
interest=.05

print("Interest Rate\tMonthly Payment \t Total Payment")


for i in range(25):
   # total = amount*(1+(interest/12))**(12*years)
    #conTotal=amount*(math.e)**(interest*years)
    #month=total/(years*12)
    interestPerPeriod = interest/12
    payments = years*12
    a1=interestPerPeriod*(1+interestPerPeriod)**payments
    a2=(1+interestPerPeriod)**payments-1
    month=amount*(a1/a2)
    total=month*payments
    print(format(interest*100,".3f"),"% \t\t",format(month,".2f")," \t\t\t",format(total,".2f"))
    interest += .00125
