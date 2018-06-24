def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    futureValue = investmentAmount*(1+monthlyInterestRate)**(12*years)
    return futureValue




future = round(futureInvestmentValue(10000,.05/12,5),2)
print("The future value is",future)