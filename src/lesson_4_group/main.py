uangMasuk = []
uangKeluar = []
jumlahUangMasuk = 0
jumlahUangKeluar = 0

def showUangMasuk():
    if(len(uangMasuk) != 0):
        print('')
        print("List Uang Masuk : ")
        for uang in uangMasuk:
            print(f"- {uang}")
    else:
        print('\nUang Masuk anda = 0')

def showUangKeluar():
    if(len(uangKeluar) != 0):
        print('')
        print("List Uang Keluar : ")
        for uang in uangKeluar:
            print(f"- {uang}")
    else:
        print('\nUang Keluar anda = 0')

def calcUangMasuk():
    for uang in uangMasuk:
        global jumlahUangMasuk
        jumlahUangMasuk += uang

def inputUangMasuk():
    saldo = int(input('Masukkan nominal uang masuk : '))
    uangMasuk.append(saldo)

def inputUangKeluar():
    saldo = int(input('Masukkan nominal uang keluar : '))
    uangKeluar.append(saldo)

def calcUangKeluar():
    for uang in uangKeluar:
        global jumlahUangKeluar
        jumlahUangKeluar += uang

def operations(menu):
    if menu == 0:
        showUangMasuk()
            
        tambah = input('Tambah uang masuk? (y/n) ')
        if(tambah.lower() == 'y'):
            inputUangMasuk()
            
            while True:
                lanjut = input('tambahkan uang masuk lagi? (y/n) ')
                
                if(lanjut.lower() == 'y') : 
                    inputUangMasuk()
                else : break    
        
        showUangMasuk()
        
    elif menu == 1:
        
        showUangKeluar()
            
        tambah = input('Tambah uang keluar? (y/n) ')
        if(tambah.lower() == 'y'):
            inputUangKeluar()
            
            while True:
                lanjut = input('tambahkan uang keluar lagi? (y/n) ')
                
                if(lanjut.lower() == 'y') : 
                    inputUangKeluar()
                else : break    
    
        showUangKeluar()
        
    elif menu == 2:
        calcUangMasuk()
        print(f"\nJumlah Uang Masuk : {jumlahUangMasuk}")
    elif menu == 3:
        calcUangKeluar()
        print(f"Jumlah Uang Keluar : {jumlahUangKeluar}")
    elif menu == 4:
        calcUangMasuk()
        calcUangKeluar()
        print(
            f"Jumlah Sisa Uang (uang masuk {jumlahUangMasuk} - uang keluar) {jumlahUangKeluar} : {jumlahUangMasuk - jumlahUangKeluar}"
        )
    else:
        print("pilih menu dengan benar!!!")

    backToMenu = int(input("Tekan 0 Untuk kembali ke menu utama "))
    if backToMenu == 0:
        print("")
        showMenu()

def showMenu():
        print('\n--------------------')
        print('APLIKASI PENCATATAN KEUANGAN')
        print('--------------------\n')
        print("SILAHKAN PILIH MENU")
        print("0 : Masuk")
        print("1 : Keluar")
        print("2 : Sum Masuk")
        print("3 : Sum Keluar")
        print("4 : Sum ALL")
        selectedMenu = int(input("Pilih Menu: "))
        operations(selectedMenu)
        
showMenu()
