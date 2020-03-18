# # PR 6 DESEMBER 2019
row1Film1Siang = [0,0,0,0,0,0,0,0,0,0]
row2Film1Siang = [0,0,0,0,0,0,0,0,0,0]
row1Film1Malam = [0,0,0,0,0,0,0,0,0,0]
row2Film1Malam = [0,0,0,0,0,0,0,0,0,0]

row1Film2Siang = [0,0,0,0,0,0,0,0,0,0]
row2Film2Siang = [0,0,0,0,0,0,0,0,0,0]
row1Film2Malam = [0,0,0,0,0,0,0,0,0,0]
row2Film2Malam = [0,0,0,0,0,0,0,0,0,0]

AllHistoryPurc = []

def pilihanjadwalFilm1Siang(row1Film1Siang,row2Film1Siang):
    for row1 in row1Film1Siang:
        print(row1, end=" ")
    print()
    for row2 in row2Film1Siang:
        print(row2, end=" ")

def pilihanjadwalFilm1Malam(row1Film1Malam,row2Film1Malam):
    for row1 in row1Film1Malam:
        print(row1, end=" ")
    print()
    for row2 in row2Film1Malam:
        print(row2, end=" ")

def pilihanjadwalFilm2Siang(row1Film2Siang,row2Film2Siang):
    for row1 in row1Film2Siang:
        print(row1, end=" ")
    print()
    for row2 in row2Film2Siang:
        print(row2, end=" ")

def pilihanjadwalFilm2Malam(row1Film2Malam,row2Film2Malam):
    for row1 in row1Film2Malam:
        print(row1, end=" ")
    print()
    for row2 in row2Film2Malam:
        print(row2, end=" ")

# # FUNCTION PILIHAN JADWAL
def pilihan_jadwal():
    HistoryPembelian = []
    pilihan = int(input('Silahkan pilih film: '))
    if pilihan == 1:
        print("Pilih jadwal film Beranak Dalam Kubur: ")
        print("1. Siang")
        print("2. Malam")
        pilihan_jadwal1 = int(input("pilih: "))
        if pilihan_jadwal1 == 1:
            HistoryPembelian = purchase_seat(row1Film1Siang,row2Film1Siang,"Beranak Dalam Kubur", "Siang")
            AllHistoryPurc.extend(HistoryPembelian)
            pilihanjadwalFilm1Siang(row1Film1Siang,row2Film1Siang)
            print()
        elif pilihan_jadwal1 == 2:
            HistoryPembelian = purchase_seat(row1Film1Malam,row2Film1Malam, "Beranak Dalam Kubur", "Malam")
            pilihanjadwalFilm1Malam(row1Film1Malam,row2Film1Malam)
            AllHistoryPurc.extend(HistoryPembelian)
            print()
        else:
            print('-Silahkan pilih jadwal sesuai dengan angka tertera.-')
            print()
    elif pilihan == 2:
        print("Pilih jadwal film Maju Kena Mundur Kena: ")
        print("1. Siang")
        print("2. Malam")
        pilihan_jadwal2 = int(input("pilih: "))
        if pilihan_jadwal2 == 1:
            HistoryPembelian = purchase_seat(row1Film2Siang, row2Film2Siang, "Maju Kena Mundur Kena", "Siang")
            pilihanjadwalFilm2Siang(row1Film2Siang, row2Film2Siang)
            AllHistoryPurc.extend(HistoryPembelian)
        elif pilihan_jadwal2 == 2:
            HistoryPembelian = purchase_seat(row1Film2Malam, row2Film2Malam, "Maju Kena Mundur Kena", "Malam")
            pilihanjadwalFilm2Malam(row1Film2Malam, row2Film2Malam)
            AllHistoryPurc.extend(HistoryPembelian)
        else:
            print('-Silahkan pilih jadwal sesuai dengan angka tertera.-')
            print()
    elif pilihan < 0 and pilihan > 2:
        print()
        print('\n''-Hanya ada 2 Film, silahkan pilih film yang tersedia-')

# # FUNCTION MENU
def menu0():
    print(" ")
    print("Menu:")
    print('1. Pesan Tiket')
    print('2. Lihat History')
    print('3. Keluar')


# # FUNCTION PURCHASE SEAT
def purchase_seat(row1,row2,judulfilm,waktu):
    print()
    newinput = int(input("Beli tiket berapa kali? "))
    purc_history = [] 
    x = 0
    while x < newinput:
        History = []
        History.append(judulfilm)
        History.append(waktu)
        rowx = int(input("Row: "))
        rowy = int(input("Seat: "))
        if rowx == 1:
            if row1[rowy] == 0:
                row1[rowy-1] = 'x'
                History.append(rowx)
                History.append(rowy)
                x += 1 
            else:
                print('tempat duduk tidak tersedia')
                History = []
        elif rowx == 2:
            if row2[rowy] == 0:
                row2[rowy-1] = 'x'
                x += 1
                History.append(rowx)
                History.append(rowy)
            else:
                print('tempat duduk tidak tersedia')
                History = []
        else:
            print('row hanya ada 2, silahkan coba lagi')
        purc_history.append(History)
        History = []
    return purc_history

# # LOOPING MENU
a = True
while a == True:
    menu0()
    inputan = int(input('Tentukan pilihan?: '))
    if inputan == 1:
        print("List film:")
        print("1. Beranak Dalam Kubur")
        print("2. Maju Kena Mundur Kena")
        pilihan_jadwal()
    elif inputan == 2:
        print ()
        tampung = 0
        if len(AllHistoryPurc) == 0:
            print('History pembelian belum ada, silahkan pesan tiket terlebih dahulu (pilih 1)')
        while(tampung<len(AllHistoryPurc)):
            if (len(AllHistoryPurc[tampung]) == 4):
                print('History Pembelian:\n Film {} Jadwal {} Row {} Seat {}' .format(AllHistoryPurc[tampung][0], AllHistoryPurc[tampung][1], AllHistoryPurc[tampung][2],
                AllHistoryPurc[tampung][3]))
                tampung += 1
            else:
                tampung += 1
    elif inputan == 3:
        print('--Terima Kasih--')
        a = False
    else:
        print('-Hanya ada 3 pilihan, silahkan pilih sesuai dengan nomor yang tertera-')