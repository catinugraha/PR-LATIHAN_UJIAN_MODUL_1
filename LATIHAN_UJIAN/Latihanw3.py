# lst = []
# user_input1 = int(input('Berapa angka yang ingin anda masukkan?: '))
# for number in range(0, user_input1):
#     user_input2 = int(input('Masukkan angka: '))
#     lst.append(user_input2)

# def sum_list(lst):
#     sum_number = 0
#     for number in lst:
#         sum_number += number
#     return sum_number

# print(('Jumlah keseluruhan dari list anda adalah {}').format(sum_list(lst)))


for row in range(7):
    z=''
    for column in range(5):
        if (column == 0 and row != 0) or (column == 4 and row != 0) or (row == 0 and (column != 0 or column != 4)):
            z += "*"
        else:
            z += ' '
    print(z)