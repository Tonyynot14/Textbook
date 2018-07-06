from stopwatch import StopWatch

clock = StopWatch()

clock.start()
sum = 0
for i in range(1,1000001):
    sum+=i
clock.stop()

print("The amount of time for the calculation to run is",clock.getElapsedTime(), "milliseconds")