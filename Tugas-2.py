
daftarkontak = ("Daftar Kontak:\n"
"Nama: Fawwaz\n"
"No Telepon: 08123456789"
)
def welcome():
    inn = input("Pilih menu:")
    def DaftarKontak():
        print (daftarkontak)
    def TambahKontak():
        person_name = input("Please enter the person name::")
        mobile_number = input("Please enter the mobile number:")

#Main
print(
    "Selamat Datang!\n"
    "--- Menu --- \n"
    "1. Daftar Kontak\n"
    "2. Tambah Kontak\n"
    "3. Keluar\n")
while(True):
    inn=welcome
    if inn == "1":
        DaftarKontak()
    elif inn == "2":
        TambahKontak()
    elif inn=='3':
        print("Program selesai, sampai jumpa!!!")
        break
    else:
        print(input("Pilih menu:"))
    



