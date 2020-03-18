# # SOAL 1
data_list = [40, 100, 1, 5, 25, 10]
new_list = []

while data_list:
    min  = data_list[0] 
    for index in data_list: 
        if index < min:
            min = index
    new_list.append(min)
    data_list.remove(min)

print (new_list)


# # SOAL 2
data_list = [40, 100, 1, 5, 25, 10]

print('Data list:' + str(data_list))
def max_num_list(data_list):
	max = data_list[0]
	for i in data_list:
		if i > max:
			max = i
	return max
print('Angka tertinggi dalam list = '+ str(max_num_list(data_list)))

def min_num_list(data_list):
	min = data_list[0]
	for i in data_list:
		if i < min:
			min = i
	return min
print('Angka terendah dalam list = '+str(min_num_list(data_list)))


# # SOAL 3
lst = []
import sys
def menu0(lst):
    print(" ")
    print('1. Isi Array/List')
    print('2. Lihat Array/List')
    print('3. Sort Array/List Ascending')
    print('4. Sort Array/List Descending')
    print('5. Nilai tertinggi dan terendah')
    print('6. Jumlah Ganjil dan Genap')
    print('7. Keluar')
    print(" ")
    menu_input = int(input('Pilih yang mana?: '))
    
    if menu_input == 1:
        n = int(input('berapa angka yang ingin anda masukkan?: '))
        for i in range(0, n):
            ele = int(input('Masukkan angka: '))
            lst.append(ele)
        print('List data Anda: ', lst)
        menu0(lst)
    if menu_input == 2:
        print('List data Anda: ',lst[:])
        menu0(lst)
    if menu_input == 3:
        if lst > [0]:       
            lst.sort()
            print('Urutan data Anda dari yang terkecil adalah: ',lst[:])
            menu0(lst)
        else:
            print('List data Anda kosong! Silahkan masukkan data terlebih dahulu (input angka 1)')
            menu0(lst)    
    if menu_input == 4:
        if lst > [0]:
            lst.sort(reverse=True)
            print('Urutan data Anda dari yang terbesar adalah: ',lst[:])
            menu0(lst)
        else:
            print('List data Anda kosong! Silahkan masukkan data terlebih dahulu (input angka 1)')
            menu0(lst)
    if menu_input == 5:
        if lst > [0]:
            print('List data Anda: ' + str(lst))
            def max_num_list(lst):
                max = lst[0]
                for i in lst:
                    if i > max:
                        max = i
                return max
            print('Angka tertinggi dalam list = '+ str(max_num_list(lst)))
            def min_num_list(lst):
                min = lst[0]
                for i in lst:
                    if i < min:
                        min = i
                return min
            print('Angka terendah dalam list = '+str(min_num_list(lst)))
            menu0(lst)
        else:
            print('List data Anda kosong! Silahkan masukkan data terlebih dahulu (input angka 1)')
            menu0(lst)
    if menu_input == 6:
        if lst > [0]:
            even_count, odd_count = 0, 0
            even_count2, odd_count2 = [], []
            for num in lst:
                if num % 2 == 0:
                    even_count = even_count + 1
                    even_count2.append(num)
                else:
                    odd_count = odd_count + 1
                    odd_count2.append(num)
            print('Jumlah bilangan Genap dalam data Anda:', even_count, even_count2)
            print('Jumlah bilangan Ganjil dalam data Anda:', odd_count, odd_count2)
            menu0(lst)
        else:
            print('List data Anda kosong! Silahkan masukkan data terlebih dahulu (input angka 1)')
            menu0(lst)
    if menu_input == 7:
        sys.exit('---Terima kasih telah menggunakan App ini---')
        menu0(lst)
    else:
        print('Menu tidak ada dalam pilihan, silahkan masukkan angka yg tertera dalam list')
        menu0(lst)     
menu0(lst)