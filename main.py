import numpy as np
from Event import Event

attentionRate = {}
transMatrix = []
queues = {}

def processData(fileName):
    lines = []
    # Abrimos el archivo
    file = open(fileName, "r")
    tempLines = file.readlines()
    # Convertimos el txt a un arreglo dividido
    # por saltos de lines y asignamos valores
    for line in tempLines: 
        lines.insert(0, line.rstrip())
    arrivalRate = float(lines.pop())
    queueQuantity = int(lines.pop())
    # Le asignamos la tasa de atencion a cada cola
    for queue in range(1, queueQuantity + 1):
        attentionRate[queue] = float(lines.pop())
        queues[queue] = []
    # Creamos la Matriz
    for line in lines:
        tempList = []
        for e in line.split():
            tempList.append(float(e))
        transMatrix.insert(0, tempList)
    return arrivalRate, queueQuantity

def getTasa(var):
    return -np.log(np.random.rand())/var

def entryProb(probList):
    randNumber = np.random.rand()
    current = 0
    selectedProb = 0
    index = 0
    for prob in probList:
        current += prob
        if randNumber <= current:
            return index
        index += 1

def getNextOnQueue(queue):
    selected = queue[0]
    for event in queue:
        if event.getExecTime() <= selected.getExecTime():
            selected = event
    return selected

def adjustQueueTime(queue, time):
    for event in queue:
        event.addExecTime(time)
        event.addWTime(time)

def getL():
    total = 0
    for queue in queues:
        total += len(queues[queue])
    return total

def getLq():
    dic = {}
    for queue in queues:
        dic[queue] = len(queues[queue])
    return dic

def getW():
    total = 0
    for queue in queues:
        for event in queues[queue]:
            total += event.getW()
    return total

if __name__ == "__main__":
    np.random.seed(0)

    # Inputs
    fileName = str(input("Ingrese el nombre del archivo: "))
    exTime = int(input("Cantidad de tiempo minimo de ejecucion: "))

    # Procesa la informacion del txt y la asigna a las variables
    arrivalRate, queueQuantity = processData(fileName)

    # Se crea y se colocan los eventos en las colas
    actualTime = 0
    while actualTime <= exTime:
        event = Event()
        actualTime += getTasa(arrivalRate)
        event.setExecTime(actualTime)
        queue = entryProb(transMatrix[0])
        queues[queue].append(event)
    
    # Se simulan las colas
    executed = True
    while executed:
        executed = False
        for queue in queues:
            event = getNextOnQueue(queues[queue])
            if event.getExecTime() <= exTime:
                executed = True
                queues[queue].remove(event)
                nextQueue = entryProb(transMatrix[queue])
                if nextQueue != 0:
                    time = getTasa(attentionRate[queue])
                    event.addExecTime(time)
                    queues[nextQueue].append(event)
                    adjustQueueTime(queues[queue], time)
    # Obtenemos L y Lq
    L = getL()
    Lq = getLq()
    W = getW()

    print("L: " + str(L))
    print("Lq: " + str(Lq))
    print("W: " + str(W))