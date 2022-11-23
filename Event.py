class Event:

    def __init__(self):
        self.setExecTime(0)
        self.setW(0)
        self.setWq([])
    
    # GETTERS
    def getExecTime(self):
        return self.__execTime

    def getW(self):
        return self.__w

    def getWq(self):
        return self.__wq


    # SETTERS
    def setExecTime(self, execTime):
        self.__execTime = execTime

    def setW(self, w):
        self.__w = w

    def setWq(self, wq):
        self.__wq = wq


    # FUNCTIONS
    def addExecTime(self, time):
        tempExecTime = self.getExecTime()
        tempExecTime += time
        self.setExecTime(tempExecTime)

    def addWTime(self, time):
        tempW = self.getW()
        tempW += time
        self.setW(tempW)

    def addWqTime(self, time, pos):
        tempWq = self.getWq()
        tempWq[pos] += time
        self.setWq(tempWq)