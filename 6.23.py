def convertMillis(totalMillis):
    millis = totalMillis%1000
    totalSeconds = totalMillis//1000
    seconds = totalSeconds%60
    totalMinutes = totalSeconds//60
    minutes = totalMinutes%60
    totalHours = totalMinutes//60
    hours = totalHours%60

    format =str(totalHours)+":"+str(minutes)+":"+str(seconds)
    return format



print (convertMillis(555550000))