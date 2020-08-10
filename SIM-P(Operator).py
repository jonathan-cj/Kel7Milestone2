import csv, time
import kurangiPoin as kurang 
import SearchNomorSIM as cari
import ResetPoin as reset

mark = "9999"
database = "Data Pengendara SIM-P.csv"
arrData = [("9999",0,0) for i in range(100)]

def insertArr(arr,file):
    reader = csv.reader(file,delimiter=',')
    j = 0
    for i in reader :
        if i != [] :
            arr[j] = i
            j += 1

def writeFile(file,arr):
    writer = csv.writer(file,delimiter=',')
    i = 0
    while arr[i][0] != mark:
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

'''

MAIN PROGRAM

'''

loadFile()

print("Selamat datang, Petugas!")

done = False
while not done :
    print()
    time.sleep(1)
    print("Berikut fungsi yang dapat diakses: \n1.Kurang Point\n2.Reset Poin\n3.Exit")
    print()
    opt = int(input("Masukan pilihan anda:"))

    if opt == 1 :
        time.sleep(2)
        nomorSIM = cari.search(arrData)
        
        print("=====================================")
        arrData = kurang.minusPoin(arrData,nomorSIM)
    
    elif opt == 2 :
        time.sleep(2)
        nomorSIM = cari.search(arrData)

        print("=====================================")
        arrData = reset.resetPoin(arrData,nomorSIM)

    elif opt == 3 :
        print("Apakah anda ingin menyimpan perubahan? (Y/N)")
        opt = input()
        print()
        if opt == 'Y' :
            saveFile()
            print("Perubahan berhasil disimpan!")
        done = True

print("Terima kasih sudah menggunakan SIM-P!")
close = input()


