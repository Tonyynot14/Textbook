def sumDigits(num):
    sum = 0
    while num>0:

        sum += num%10
        num=num//10
    return sum

num = int(input("Enter a number you would like to sum: "))

value = sumDigits(num)

print("The sum of ",num, "is",value)