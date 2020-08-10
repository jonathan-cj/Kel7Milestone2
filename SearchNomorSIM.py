def search(dataSIM, nomorSIM):
    found_nomor = False
    while not found_nomor:
        nomor = input("Masukkan Nomor SIM Anda: ")
        for i in dataSIM:
            if i[0] == nomor:
                print(arrData[i])
                found_nomor = True # Looping berhenti
            else:
                print("Maaf nomor SIM Anda tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            break
    return data SIM
