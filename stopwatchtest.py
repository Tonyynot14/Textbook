from stopwatch import StopWatch

# creation of stopwatch class object
clock = StopWatch()

# use of clock method start
clock.start()
sum = 0
# Random loop to test how long it takes computer to complete
for i in range(1,1000001):
    sum+=i
# use of clock method stop
clock.stop()
# use of clock method getElapsedTime to display how long between the two events
print("The amount of time for the calculation to run is",clock.getElapsedTime(), "milliseconds")