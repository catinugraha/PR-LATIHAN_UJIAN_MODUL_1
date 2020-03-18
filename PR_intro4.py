# # PR 3 DESEMBER 2019
# kata = input('silahkan ketik sebuah kalimat: ')
# def jumlah_kata(kata):
#     my_string = kata.lower().split()
#     my_dict = {}
#     for item in my_string:
#         if item in my_dict:
#             my_dict[item] += 1
#         else:
#             my_dict[item] = 1
#     print(my_dict)
#     for key, val in my_dict.items():
#         print("Jumlah kata '{}' ada sebanyak {}".format (key.title(), val))

# jumlah_kata(kata)

# # PR BONUS 3 DESEMBER 2019
import sys
import random
my_list = []
n = int(input('Masukkan ukuran:'))

def list_angka(my_list):
    num = 1
    for row in range(n):
        my_list=[]
        for col in range(n):
            my_list.append(num)
            print(num,end=" ")
            num += 1
        print()

# # Function to rotate the matrix
def rotateright(my_list):
    for c in range(3):
        list_kanan = []
        for i in range(len(my_list)):
            list_temp = []
            for j in range((my_list(n)-1),-1,-1):
                list_temp.append(my_list[j][i])
            list_kanan.append(list_temp)
        my_list = list_kanan
    
def menu(my_list):
    print('Pilih'+'\n'+'1. Angka Urut'+'\n'+'2. Angka Random')
    pilihan = int(input('Masukkan pilihan: '))
    if pilihan == 1:
        list_angka(my_list)
    pilihan_kika = input('Putar ke arah? ')
    if pilihan_kika == 'kanan':
        pilih3 = int(input('berapa kali?: '))
        if pilih3 >= 1:
            rotateright(my_list)
    if pilihan_kika == 'kiri':
        pilih3 = int(input('berapa kali?: '))
        if pilih3 >= 1:
            print('Kondisi belum dibuat')
    pilih4 = input('apakah anda ingin melanjutkan?(Y / N): ')
    if pilih4 == "Y":
        menu(my_list)
    if pilih4 == "N":
        sys.exit
menu(my_list)