# # SOAL 1
# z=''
# for item in range (5,0,-1):
#     for item1 in range(item):
#         z += ' * '
#     z += '\n'
# print(z)

# # SOAL 2 (PIRAMID SAMPING)
# z = ''
# for i in range(5, 0, -1):
#     if (i > 1):
#         for j in range (0, i):
#             z += ' * '
#         z += '\n'
#     elif i == 1:
#         for k in range (0, 5):
#             for l in range (0 , k+1):
#                 z += ' * '
#             z += '\n'        
# print (z)

# # SOAL 3
# num = int(input("Please input number: "))
# for i in range(0, num, +2):
#     if i <= num:
#        print(" "*(num-1-i)+"* "*(i+1))

# # SOAL 4
# num = int(input("Please input number:"))
# for i in range(0, num, +2):
#     if i <= num:
#        print(" "*(i+1)+"* "*(num-i))

# # SOAL 5
# num = int(input('input number of row(odd): '))
# for i in range(0, num, +2):
#        print(" "*(num-1-i)+"* "*(i+1))
# for i in range(0, num, +2):
#     if i <= num:
#        print(" "*(i)+"* "*(num-i))

# # SOAL 6
# num = int(input('masukkan jumlah bintang: '))
# calculate = num*2-1

# for item in range(0,calculate):
#     if item < num:
#         bintang = " * "*(calculate - item - (num - 1))+ "   "*item
#     else:
#         bintang = " * "*(item - (num - 2))+"   "*(2*num - item - 2)
#     bintang = bintang + bintang[-4::-1]
#     print(bintang)