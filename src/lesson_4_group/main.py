uangMasuk = [200,500,1000]
uangKeluar = [40,100]
jumlahUangMasuk = 0
jumlahUangKeluar = 0

def calcUangMasuk():
    for uang in uangMasuk:
        jumlahUangMasuk+=uang

def calcUangKeluar():
    for uang in uangKeluar:
        jumlahUangKeluar+=uang

def listMenu():
    try:
        print('SILAHKAN PILIH MENU')
        print('0 : Masuk')
        print('1 : Keluar')
        print('2 : Sum Masuk')
        print('3 : Sum Keluar')
        print('4 : Sum ALL')
        selectedMenu = int(input('Pilih Menu: '))

        if(selectedMenu == 0):
            print('List Uang Masuk : ')
            for uang in uangMasuk:
                print(f"- {uang}")
        elif(selectedMenu == 1):
            print('List Uang keluar : ')
            for uang in uangKeluar:
                print(f'- {uang}')
        elif(selectedMenu == 2):
            print(f'Jumlah Uang Masuk : {jumlahUangMasuk}')
        elif(selectedMenu == 3):
            print(f'Jumlah Uang Keluar : {jumlahUangKeluar}')
        elif(selectedMenu == 4):
            print(f'Jumlah Sisa Uang (uang masuk - keluar) : {jumlahUangMasuk - jumlahUangKeluar}')
    except:
        print('tolong pilih menu dengan benar!')

def init():
    calcUangMasuk()
    calcUangKeluar()
    menu = listMenu()

init()