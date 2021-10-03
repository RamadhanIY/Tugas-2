#Data
listkontak = ["Fawwaz"]
listnumber = ["08123456789"]

#System
def DaftarKontak():
        print ("Daftar Kontak: ")
        for i in range(len(listkontak)):
            print ("Nama : {}".format(listkontak[i]))
            print ("Nomor telepon: {}". format(listnumber[i]))

def TambahKontak():
        listkontak.append(input("Please enter the person name:"))
        listnumber.append(input("Please enter the mobile number:"))
        print("Kontak berhasil ditambahkan")


#Main
print(
    "Selamat Datang!\n"
    "--- Menu --- \n"
    "1. Daftar Kontak\n"
    "2. Tambah Kontak\n"
    "3. Keluar\n")
while(True):
    inn = input("Pilih menu:")
    if  inn == "1":
        DaftarKontak()
    elif inn == "2":
        TambahKontak()
    elif inn=='3':
        print("Program selesai, sampai jumpa!!!")
        break
    else:
        print("Menu tidak tersedia.")
    



