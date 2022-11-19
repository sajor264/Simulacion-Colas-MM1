attentionRate = {}
transMatrix = []

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
    for queue in range(queueQuantity):
        attentionRate[queue] = float(lines.pop())
    # Creamos la Matriz
    for line in lines:
        tempList = []
        for e in line.split():
            tempList.append(float(e))
        transMatrix.insert(0, tempList)
    return arrivalRate, queueQuantity


if __name__ == "__main__":
    # Inputs
    fileName = str(input("Ingrese el nombre del archivo: "))
    exTime = int(input("Cantidad de tiempo minimo de ejecucion: "))

    # Procesa la informacion del txt y la asigna a las variables
    arrivalRate, queueQuantity = processData(fileName)

    # print(arrivalRate)
    # print(queueQuantity)
    # print(attentionRate)
    # print(transMatrix)