def search(dataSIM):
    found_nomor = False
    while not found_nomor:
        nomor = input("Masukkan Nomor SIM Pelanggar: ")
        for i in dataSIM:
            if i[0] == nomor:
                print()
                print("=====================================")
                print("SIM Ditemukan. Keterangan pelanggar :")
                print()
                print("No. SIM : %s \nNama : %s \nJumlah Poin Sekarang : %s" %(i[0],i[1],i[2]))
                found_nomor = True # Looping berhenti
                break
        if not found_nomor:    
            print("Maaf nomor SIM Pelanggar tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    return nomor
