# Tony Wade
# Hans Luhn IBM proposed algorithm for validating credit card numbers

# Even places from right to left doubled and added together, if the double is more
# 10 then add the two digits together
def sumOfDoubleEvenPlace(number):
    summ = 0
    for i in range(1, getSize(number) + 1):
        digit = number % 10
        if i % 2 == 0:
            digit = digit*2
            digit = getDigit(digit)
            summ += digit
        number = number // 10

    return summ

# If the number doubled is over ten return the addtion of the two numbers, max value would be 18.
def getDigit(number):
    if number >= 10:
        # 9*2 is 18 so will never be more than two digits, so I added the remainder of 10 to floor divison of 10
        number= number % 10 + number// 10
    return number

# Odd place from right to left summed together and return the sum
def sumOfOddPlace(number):
    summ = 0
    for i in range(1,getSize(number)+1):
         digit = number%10
         if i%2 != 0:
                 summ += digit
         number = number//10

    return summ


# This function tells whether the card is prefix matches the d value which can be 4, 5, 37 , or 6
def prefixMatched(number,d):

    k = getSize(d)

    prefix = getPrefix(number,k)

    if prefix == d:
        return True
    else:return False


# Get how many digits is in the number can be
def getSize(d):
    digit = str(d)
    long = len(digit)
    return long
# Returns the prefix of the number, k specifies the numbers of places the prefix is. Should ever only be 1 or 2
def getPrefix(number,k):
    length = getSize(number)
    number=number//(10**(length-k))
    return number

# this function test whether the card is 13-16 digits long, then test the prefix to see what kind of card it is.
# As long as the card is one of the 4 major card providers you add up the double even place and odd place numbers
#and if that sum is divisble by 10 then the card is valid
def isValid(number):
    if getSize(number) >=13 and getSize(number)<=16:
        if prefixMatched(number,4):
            card = "Visa"
        elif prefixMatched(number,5):
            card = "MasterCard"
        elif prefixMatched(number,37):
            card = "American Express"
        elif prefixMatched(number, 6):
            card = "Discover"
        else: card == "none"

        if card != "none":
            summedEvenOdd = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
            if summedEvenOdd%10 == 0:
                print(card)
                return True
            else:return False





print(isValid(4388576018410707))
