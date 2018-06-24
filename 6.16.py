#need to know if year is leap year for number of days
def isLeapYear(year):
    return year%400==0 or (year%4==0 and year%100!=0)

def numberOfDaysInAYear(year):
    days = 365
    if isLeapYear(year):
        days+=1
    return days

print("Year\t\tDays")
for i in range(2010,2021):
    print(i,"\t\t",numberOfDaysInAYear(i))