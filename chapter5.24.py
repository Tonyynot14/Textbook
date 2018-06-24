def truncate(num,digits):
    power=10**digits
    num=int(num*power)/power

    return num



amount = eval(input("Enter the loan amount:"))
years = eval(input("Enter number of years for loan:"))
inter=eval(input("Annual interest rate:"))
interest=inter/100

interestPerPeriod = interest / 12
payments = years * 12
a1 = interestPerPeriod * (1 + interestPerPeriod) ** payments
a2 = (1 + interestPerPeriod) ** payments - 1
month = amount * (a1 / a2)
total = month * payments

print("Payment\tInterest\tPrinciple\tBalance")

for i in range(1,payments+1):
    inte=interestPerPeriod*amount
    principle=month-inte
    amount=amount-principle
    formatinte=int(inte*100)/100
    print(i,"\t\t",format(truncate(inte,2),".2f"),"\t\t",format(truncate(principle,2),".2f"),"\t\t",format(truncate(amount,2),".2f") )