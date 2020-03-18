# # # PR POWERPOINT 2 # # #

# # SOLVE IT! 1
# angka = int(input('Masukkan angka: '))
# if(angka%2 == 0):
#     print('Angka '+str(angka)+' tergolong bilangan GENAP!')
# elif(angka%2 > 0):
#     print('Angka '+str(angka)+' tergolong bilangan GANJIL!')

# # SOLVE IT! 2
# massa = float(input('Masukkan Massa(kg): '))
# tinggi_cm = float(input('Masukkan Tinggi(cm): '))
# tinggi_m = tinggi_cm/100
# IMT = massa/tinggi_m**2
# IMT1 = round(IMT, 1)

# if IMT1 < 18.5:
#     hasil = 'Berat badan kurang.'
# elif IMT1 >= 18.5 or IMT1 <= 24.9:
#     hasil = 'Berat badan ideal'
# elif IMT1 == 25.0 or IMT1 <= 29.9:
#     hasil = ('Berat badan berlebih')
# elif IMT1 == 30.0 or IMT1 <= 39.9:
#     hasil = 'Berat badan sangat berlebih'
# else:
#     hasil = 'Obesitas'    

# print('massa {} kg & tinggi {} m'.format(massa,tinggi_m))
# print('IMT = {}, {}'.format(IMT1, hasil) )

# # SOLVE IT! TAMBAHAN
# nama = str(input('Masukkan nama anda: '))
# umur = int(input('Masukkan umur anda: '))
# if(len(nama)>10 and umur%2 == 0):
#      print('Pekerjaan Lancar!')
# elif(len(nama)>10 and umur%2 > 0):
#     print('Kesehatan Baik!')
# elif(len(nama) <= 10 and umur%2 == 0):
#     print('Keuangan Lancar!')
# else:
#     print('Jodoh sudah dekat!')