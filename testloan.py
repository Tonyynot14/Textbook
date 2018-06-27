from testloanclass import Loan


def main():
    annualInterestRate = eval(
        input("Enter the yearly interest rate, for example, 7.25 should be percent not decimal: "))

    numberOfYears = eval(input("Enter the number of years for the loan as a integer: "))

    loanAmount = eval(input("Enter loan amount: "))

    borrower = input("Enter a borrower's name: ")

    loan = Loan(annualInterestRate,numberOfYears,loanAmount,borrower)

    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(),".2f"))
    print("The total payment is", format(loan.getTotalPayment(),".2f"))


main()
