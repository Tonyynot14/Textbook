class Loan:
    # intializer for class, remember to spell right or whole class does not work
    def __init__(self, annualInterestRate = 2.5,numberOfYears = 1,loanAmount = 1000,borrower=" "):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount =loanAmount
        self.__borrower = borrower
    # Accessor functions, to be able to get any private data part in object
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getNumberOfYears(self):
        return self.__numberOfYears
    def getLoanAmount(self):
        return self.__loanAmount
    def getBorrower(self):
        return self.__borrower

    # Mutator functions/methods
    def setAnnualInterestRate(self,annualInterestrate):
        self.__annualInterestRate = annualInterestrate

    def setNumberOfYears(self,numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self,loanAmount):
        self.__loanAmount =loanAmount

    def setBorrower(self,borrower):
        self.__borrower =borrower


# Formula to calculate monthly payment
    def getMonthlyPayment(self):
        # Divide by 1200 because you divide by 12 and 100 to get a decimal value for 12 months
        monthlyInterestRate = self.__annualInterestRate/1200
        monthlyPayment =self.__loanAmount*monthlyInterestRate/(1-(1/(1+monthlyInterestRate)**(self.__numberOfYears*12)))
        return monthlyPayment
# The total payments for the life of the loan
    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment()*self.__numberOfYears*12
        return totalPayment
