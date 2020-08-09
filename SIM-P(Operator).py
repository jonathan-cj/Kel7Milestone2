import csv, kurangiPoin

mark = "9999"
database = "database.csv"
arrData = [() for i in range(100)]

def insertArr(arr,file):
    reader = csv.reader(file,delimiter=';')
    j = 0
    for i in reader :
        if i != [] :
            arr[j] = i
            j += 1

def writeFile(file,arr):
    writer = csv.writer(file,delimiter=';')
    i = 0
    while arr[i][0] == mark:
        if arr[i] != () :
            writer.writerow(arr[i])
        i += 1

'''

FUNGSI

'''

def loadFile():
    fileDatabase = open(database,'r')

    insertArr(arrData, fileDatabase)

    fileDatabase.close()

def saveFile():
    fileDatabase = open(database,'w', newline='')

    writeFile(fileDatabase,arrData)

    fileDatabase.close()