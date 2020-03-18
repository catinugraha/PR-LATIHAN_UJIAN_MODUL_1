# # SOAL 1
# x = 4
# y = 3
# z = 2
# a = (x+y*z)
# b = (x*y)
# w = ((a/b)**z)
# print("Jawaban soal 1: "+str(w))

# # SOAL 2
# number_1 = int(input('Silahkan masukkan angka berapapun: '))
# calculate = ((number_1)**2)
# print('Kuadrat dari ' + str(number_1) + ' = ' + str(calculate))

# # SOAL 3
# import math
# x = int(input('masukkan hari: '))
# tahun1 = str(math.floor(x / 360))
# bulan1 = str(math.floor((x % 360) / 30))
# minggu1 = str(math.floor((((x % 360) % 30)) / 7))
# hari1 = str(math.floor(((x % 360) % 30) % 7))
# print(tahun1+' tahun '+bulan1+ ' bulan '+minggu1+' minggu '+hari1+' hari ')

# # SOAL 4
# total = int(input('Total umur Andi dan Budi?: '))
# rasio = float(input('Rasio umur Andi dan Budi?: '))

# umur_budi = (total * 10) /(10 + (rasio * 10))
# umur_andi = total - umur_budi
# print('Umur Andi {}'.format(umur_andi + 2))
# print('Umur Budi {}'.format(umur_budi + 2))

# angka1 = int(input('Masukkan angka 1: '))
# angka2 = int(input('Masukan angka 2: '))
# print('Angka anda adalah {} dan {}'.format(angka1,angka2))


# # Soal 5
# text_input = input('Ketik Kata atau Kalimat: ')
# text_input2 = input('Masukkan Huruf yang ingin dicari: ')
# my_count = text_input.count(text_input2)
# print('Jumlah huruf ' + text_input2 + ' pada ' + text_input + ' adalah ' + str(my_count))

# # Soal 6
# JarakMobilA = int(input('Jarak Mobil A: '))
# JarakMobilB = int(input('Jarak Mobil B: '))
# JumlahJarakAdanB = int(input('Jumlah Jarak Mobil A dan B: '))
# t = JumlahJarakAdanB/(JarakMobilA+JarakMobilB) 
# waktu = t*60
# waktu_jam = waktu//60
# waktu_menit = waktu%60
# waktu_jam2 = str(int(9 + waktu_jam))
# waktu_menit2 = ':' + str(int(waktu_menit))
# print('Mobil A dan B akan bertabrakan pada pukul '+ waktu_jam2 + waktu_menit2)

# # SOAL GITHUB 1
# number_input = int(input('Input: '))
# y = (number_input//100)
# x = ((number_input%100)*100)
# print('Output: ')
# print(x+y)

# # SOAL GITHUB 2
# from math import pi
# number_input = float(input('Input radius: '))
# print(pi*(pow(number_input,2)))

# # SOAL GITHUB 3
# x = int(input('Input 1: '))
# y = int(input('Input 2: '))
# calculate_1 = x//10
# calculate_2 = x%10
# calculate_3 = y//10
# calculate_4 = y%10
# print(calculate_1*1000+calculate_2*10+calculate_3*100+calculate_4)

# # SOAL GITHUB 4
# word = input('Input String: ')
# remover = input('Input character to remove: ')
# print(word.replace(remover,''))

# # SOAL GITHUB 5
# word = input('Input: ')
# lis = word.split()
# print(lis)
# print(lis[1]+' '+lis[0])