# masukan = matriks dataSIM, nomorSIM
# keluaran = matriks dataSIM dengan poin dari pengguna nomorSIM yang udah dikurangi

# asumsi:
# semua memiliki nomor SIM yang berbeda
# masukan pengurangan poin selalu valid

def minusPoin(dataSIM, nomorSIM):
    print()
    for i in dataSIM:
        if i[0] == nomorSIM:
            if int(i[2]) != 0:
                mines = int(input("Masukkan jumlah pengurangan poin : "))
                i[2] = int(i[2]) - mines
                print()
                if i[2] >= 0 :
                    print("Pengurangan poin dari Tn./Ny. "+i[1]+" sebesar "+str(mines)+" berhasil.")
                    print("Poin pelanggar sekarang sebesar "+str(i[2]))
                else :
                    print("Pengurangan poin dari Tn./Ny. "+i[1]+" sebesar "+str(mines)+" berhasil.")
                    print("Poin pelanggar sekarang sebesar 0, silahkan ditindaklanjuti.")
            else:
                print("Poin pelanggar 0, silahkan ditindaklanjuti.")
    return dataSIM