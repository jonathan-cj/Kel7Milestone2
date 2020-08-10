def resetPoin(dataSIM,nomorSIM):
    print()
    for i in dataSIM:
        if i[0] == nomorSIM:
            opt = 'N'
            if int(i[2]) != 0:
                print("Poin pemilik SIM belum 0, apakah anda yakin ?(Y/N)")
                opt = input()
                print()

            if int(i[2]) == 0 or opt == 'Y':
                i[2] = '100'
                print("Poin dari  poin dari Tn./Ny."+i[1]+" berhasil direset menjadi 100")
    return dataSIM
            