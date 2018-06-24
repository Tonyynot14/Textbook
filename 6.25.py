# Creator: Tony Wade

# function returns true if prime and false if the number is not prime.
def prime(num):
    divisibleNums = 1
    for i in range(2, num):
        if num % i == 0:
            divisibleNums += 1

    if divisibleNums > 1 or num <= 1:
        return False
    else:
        return True


# function to change number into string to concatenate then returns flip of number.
# Use modular division base 10 system to get each number
# then update number by floor division by ten to get to the next number
def flip(num):
    updateNum = num
    final = ""
    while updateNum > 0:
        final += str(updateNum % 10)
        updateNum = updateNum // 10
    final = int(final)
    return final


# checks if the flip of the number is the same as number. Returns true or false based on this test
def palindromic(num):
    updateNum = num
    final = flip(num)
    # while updateNum>0:
    #   final+=str(updateNum%10)
    #  updateNum=updateNum//10
    if num == final:
        return True
    else:
        return False


# A emirp is a prime number that the flip is prime as well but not a palindromic number. Uses previous functions palindromic and prime and flip to achiecve this goal.
def emirp(positives):
    count = 10
    while positives > 0:
        if prime(count) and prime(flip(count)) and not (palindromic(count)):
            print(format(count, "5d"), end=" ")
            positives -= 1
            if positives % 10 == 0:
                print()

        count += 1


emirp(100)
