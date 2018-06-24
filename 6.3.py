def reverse(num):
    newNumber=""
    while num>0:
        newNumber  += str(num%10)
        num = num//10
    newNumber=int(newNumber)
    return newNumber


def isPalindrome(number):
    if number ==reverse(number):
        return True
    else:
        return False

number=int(input("Enter a number to reverse:"))

print(reverse(number))

if isPalindrome(number):
    print("This number is a Palindrome")