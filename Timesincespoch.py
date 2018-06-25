# Time Functions , shows in UTC time which is 4 hours difference than est

import time

# Test if leap year returns true or false. If divisible by 400 or divisible by 4 but not 100 makes it a leap year
def leap(year):
    return year%400 == 0 or(year%4 == 0 and year%100 != 0)

# Many many days are in each month, once you get to the year you can tell the date by the number
def month(days,year):
    # Test if the year is a leap year then supplies what day it would be based on days in a leap year
    if leap(year):
        if day<=31:
            month = "January"
        elif days<=60:
            month = "February"
        elif days<=91:
            month = "March"
        elif days <= 121:
            month = "April"
        elif days<=152:
            month = "May"
        elif days<=182:
            month = "June"
        elif days<=213:
            month = "July"
        elif days<=244:
            month = "August"
        elif days<=274:
            month = "September"
        elif days<=305:
            month = "October"
        elif days<=335:
            month = "Novemeber"
        elif days <=366:
            month = "December"
    # If not leap year then it is has one less day in February
    else:
        if days <= 31:
            month = "January"
        elif days <= 59:
            month = "February"
        elif days <= 90:
            month = "March"
        elif days <= 120:
            month = "April"
        elif days <= 151:
            month = "May"
        elif days <= 181:
            month = "June"
        elif days <= 212:
            month = "July"
        elif days <= 243:
            month = "August"
        elif days <= 273:
            month = "September"
        elif days <= 304:
            month = "October"
        elif days <= 334:
            month = "Novemeber"
        elif days <= 365:
            month = "December"
    return month

# Test what day it is based on days in a year
def date(days,year):
    days = days
    if leap(year):
        if day<=31:
            days =days
        elif days<=60:
            days = days-31
        elif days<=91:
            days = days-60
        elif days <= 121:
            days = days-91
        elif days<=152:
            days = days-121
        elif days<=182:
            days = days-152
        elif days<=213:
            days = days-182
        elif days<=244:
            days = days-213
        elif days<=274:
            days = days-244
        elif days<=305:
            days = days-274
        elif days<=335:
            days = days-305
        elif days <= 366:
            days = days-335
    else:
        if days <=31:
            days = days
        elif days <= 59:
            days = days-31
        elif days <=90:
            days = days-59
        elif days <=120:
            days = days-90
        elif days <= 151:
            days = days-120
        elif days <= 181:
            days = days-151
        elif days <= 212:
            days = days-181
        elif days <= 243:
            days = days-212
        elif days <= 273:
            days = days-212
        elif days <= 304:
            days = days-273
        elif days <= 334:
            days = days-304
        elif days <= 365:
            days =days-334
    return days

#Makes clock show hour in am or pm
def amPmTime(hour):
    if hour>12:
        hour-=12
    return hour


#displays time in military time and date in month day, year
def dateTime():
    currentTime=time.time()

    totalSeconds = int(currentTime)


    currentSecond = totalSeconds%60

    totalMinutes = totalSeconds//60

    currentMinute = totalMinutes%60

    totalHours = totalMinutes//60

    currentHour = totalHours%24

    totalDays=totalHours/24

    #year will update after ever loop
    year= 1970
    while totalDays>366:
        if year%400==0 or(year%4==0 and year%100!=0):
            totalDays-=366
        else:
            totalDays-=365
        year+=1
    totalDays+=1
    totalDays=int(totalDays)




# Formatting for display of time
    if currentHour >=12  and currentHour < 24:

        print(amPmTime(currentHour),":",currentMinute,":",currentSecond," PM ",month(totalDays,year)," ",date(totalDays,year),", ",year,sep="")

# Formatting for display of time
    else:
        if currentHour == 0:
            currentHour = 12
        print(amPmTime(currentHour), ":", currentMinute, ":", currentSecond, " AM ", month(totalDays, year), " ",
              date(totalDays, year), ", ", year, sep="")


dateTime()