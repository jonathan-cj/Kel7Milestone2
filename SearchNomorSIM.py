# Menghitung jumlah baris pada array arrData
baris = 0
for i in arrData:
    baris += 1

col_nomor = [x[0] for x in arrData] # Membuat list yang berisi 1 kolom nomor SIM saja

# Proses Pencarian Nomor SIM
nomor = input("Masukkan Nomor SIM Anda: ")

#Fungsi untuk search apakah nomor SIM sesuai
def search():
    for x in range(0,baris): # Looping untuk baris ke-0 sampai jumlah baris pada arrData
        if nomor == col_nomor[x]: # Jika input nomor SIM samadengan data pada col_nomor baris ke-x
            print(arrData[x]) # Mencetak pada layar semua data pada baris ke-x
            return True
    return False

# Pengulangan jika nomor SIM tidak sesuai
while search() == False:
    print("Maaf nomor SIM Anda tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    nomor = input("Masukkan Nomor SIM Anda: ")
    search()