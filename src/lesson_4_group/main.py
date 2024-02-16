uangMasuk = [200, 500, 1000]
uangKeluar = [40, 100]
jumlahUangMasuk = 0
jumlahUangKeluar = 0


def calcUangMasuk():
    for uang in uangMasuk:
        global jumlahUangMasuk
        jumlahUangMasuk += uang


def calcUangKeluar():
    for uang in uangKeluar:
        global jumlahUangKeluar
        jumlahUangKeluar += uang


def operations(menu):
    if menu == 0:
        print("List Uang Masuk : ")
        for uang in uangMasuk:
            print(f"- {uang}")
    elif menu == 1:
        print("List Uang keluar : ")
        for uang in uangKeluar:
            print(f"- {uang}")
    elif menu == 2:
        print(f"Jumlah Uang Masuk : {jumlahUangMasuk}")
    elif menu == 3:
        print(f"Jumlah Uang Keluar : {jumlahUangKeluar}")
    elif menu == 4:
        print(
            f"Jumlah Sisa Uang (uang masuk - keluar) : {jumlahUangMasuk - jumlahUangKeluar}"
        )
    else:
        print("pilih menu dengan benar!!!")

    print('Tekan 0 Untuk kembali ke menu')
    backToMenu = int(input(" "))
    if backToMenu == 0:
        showMenu()


def showMenu():
        print("SILAHKAN PILIH MENU")
        print("0 : Masuk")
        print("1 : Keluar")
        print("2 : Sum Masuk")
        print("3 : Sum Keluar")
        print("4 : Sum ALL")
        selectedMenu = int(input("Pilih Menu: "))
        operations(selectedMenu)

def init():
    calcUangMasuk()
    calcUangKeluar()
    showMenu()


init()
