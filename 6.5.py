def displaySortnedNumbers(num1,num2,num3):
    if num1>num2:
        num1,num2=num2,num1
    if num2>num3:
        num2,num3=num3,num2
    if num1>num2:
        num1,num2=num2,num1
    return num1,num2,num3


number1 =int(input("Enter the first number:"))
number2 =int(input("Enter the second number:"))
number3 =int(input("Enter the third number:"))

print("The sorted numbers are", displaySortnedNumbers(number1,number2,number3))