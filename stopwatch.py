import time
# class for a stopwatch, have to use start and stop function to get time between events. While running class
# start before the event and stop after and use the getElapsedTime function to see the difference between
# the two times
class StopWatch:
    def __init__(self,startTime = time.time(), stopTime = time.time()):
        self.__startTime = startTime
        self.StopTime = stopTime
    def getStartTime(self):
        return self.__startTime
    def getStopTime(self):
        return self.__stopTime
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__stopTime = time.time()
    def getElapsedTime(self):
        elapsed = self.__stopTime-self.__startTime
        return elapsed