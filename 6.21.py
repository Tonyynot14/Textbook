def sqrt(n):

    lastGuess=n+5
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    e=.00001
    count=0

    while lastGuess-nextGuess>e:
        lastGuess =nextGuess
        nextGuess = (lastGuess+(n/lastGuess))/2




    print (nextGuess)

sqrt(9)