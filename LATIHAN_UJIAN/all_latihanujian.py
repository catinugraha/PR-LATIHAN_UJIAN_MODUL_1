# # LATIHAN UJIAN 11 DES 2019 # #
# # -- TIME CONVERTER -- # #
# def timeconverter(seconds):
#     import math
#     if seconds > 0 and seconds <= 35999:
#         jam =  math.floor(seconds / 3600)
#         menit = math.floor((seconds%3600)/60)
#         detik = math.floor((seconds%3600)%60)
#         print(f'{jam:02d} : {menit:02d} : {detik:02d}')
#     else:
#         print('max. input 35999')

# timeconverter(3600)
# timeconverter(7201)
# timeconverter(35999)
# timeconverter(36000)

# # -- SPIN WORDS -- # #
# def spinWords(string):
#     lst_kata = string.split()
#     result = []
#     for kata in lst_kata:
#         if len(kata) >= 5:
#             revs_kata = "".join(reversed(kata))
#             result.append(revs_kata)
#         else:
#             result.append(kata)
    
#     for kata_baru in result:
#         print(kata_baru, end=" ")
#     print()

# spinWords('Hey fellow warriors')
# spinWords('This is a test')
# spinWords('This is another test')

# # -- MoveZeros -- # #
# def MoveZeros(list1):
#     for idx in range (len(list1)):
#         if str(list1[idx]) == '0' and str(list1[idx]) != False:
#             list1.append(list1[idx])
#             list1.pop(idx)
#     print(list1)

# MoveZeros([False,1,0,1,2,0,1,3,"a"])



# # LATIHAN UJIAN 13 DESEMBER 2019 # #
# # -- BACKWARDS PRIME -- # #
# def primechecker(num):
#     x = True
#     for i in range(2, num):
#         if num % i == 0:
#             x = False
#             break
#     return x

# def backwardPrimes(start, stop):
#     result = []
#     if start <= 11:
#         start = 12
#     for number in range(start,stop+1):
#         balik = int(str(number)[::-1])
#         if number == balik:
#             continue
#         if primechecker(number) and primechecker(balik):
#             result.append(number)
#     print(result)

# backwardPrimes(2,100)
# backwardPrimes(9900,10000)
# backwardPrimes(501,599)


# # -- HIGHEST X SEQUENCE -- # #
# def get_highest_xnum(num, sequence):
#     newnum = str(num)
#     lst = []
#     for number in range(len(newnum)):
#         angkabaru = newnum[number:sequence+number]
#         lst.append(angkabaru)
    
#     print(max(lst))

# get_highest_xnum(1794103177, 3)
# get_highest_xnum(1794103177, 4)
# get_highest_xnum(87173114, 5)


# # -- MOVE 1ST LETTER AND +AY TO THE END OF THE WORD -- # #
# def ay_word(text):
#     kata = text.split()
#     simpan = []
#     for i in kata:
#         z=''
#         perhuruf = list(filter(lambda num: len(num)<100,i))
#         idx = 0
#         for j in range(len(perhuruf)):
#             if perhuruf[idx].isalpha():
#                 perhuruf.append(perhuruf[idx])
#                 perhuruf.pop(idx)
#                 break
#             idx += 1
            
#         for alph in perhuruf:
#             z += alph
#         if z.isalpha():
#             z += 'ay'
#         simpan.append(z)
#     for x in simpan:
#         print(x, end=" ")
#     print()

# ay_word('Pig Latin is Cool')
# ay_word('Hello world !')
# ay_word('! Stop the war')



# # LATIHAN UJIAN 17 DES '19 # #
# # -- POPULATION GROWTH -- # #
# def nbYear(p0,percent,aug,p):    
#     year_count = 0
#     while p0 < p:
#         p0 = p0 + p0*(percent/100) + aug
#         year_count += 1
#     print('It will need {} entire years'.format(year_count))

# nbYear(1500, 5, 100, 5000)
# nbYear(1500000, 2.5, 10000, 2000000)

# # -- VASYA CLERK -- # #
# def tickets(peopleinLine):
#     lst = []
#     changes = {25:0, 50:0, 100:0}
#     for i in peopleinLine:
#         if i == 25:
#             changes[25] += 1
#             lst.append(i)
#         elif i == 50 and changes[25] > 0:
#             changes[50] += 1
#             changes[25] -= 1
#             lst.append(i)
#         elif i == 50 and changes[25] == 0:
#             print('NO')
#             break
#         elif i == 100 and changes[50] >= 1 and changes[25] >= 1:
#             changes[100] += 1
#             changes[50] -= 1
#             changes[25] -= 1
#             lst.append(i)
#         elif i == 100 and changes[25] >= 3:
#             changes[100] += 1
#             changes[25] -= 3
#             lst.append(i)
#         else:
#             print('NO')
#             break
    
#     if len(lst) == len(peopleinLine):
#         print('YES')

# tickets([25, 25, 50])
# tickets([25, 100])
# tickets([25, 25, 50, 50, 100])
# tickets([25, 25, 50, 50, 25, 50, 25, 100])


# # -- rowOddNumbers Triangle -- # #
# def rowsumoddnumbers(n):
#     k = 2 * n - 2
#     num = 1
#     lastlst = []
#     for row in range(0,n):
#         for col1 in range(0,k):
#             print(end="  ")
#         k = k - 1
#         for col2 in range(0, row+1):
#             print(str(num).ljust(4),end="")
#             if row == n-1:
#                 lastlst.append(num)
#             num += 2
#         print()
#     hasil = sum(lastlst)
#     print('jumlah angka dari row terakhir adalah {}'.format(hasil))

# rowsumoddnumbers(4)

# # LATIHAN UJIAN # #
# # -- YEAR OF INVESTMENT -- # # 
# def calculate_years(principal,interest,tax,desired):
#     count_years = 0
#     while principal < desired:
#         calculate1 = principal*(interest)
#         calculate2 = calculate1*tax
#         principal += (calculate1-calculate2)
#         count_years += 1
#     print('Thus Mr. Scoorage has to wait for {} years for the initial principal for the amount for desired sum'.format(count_years))

# calculate_years(1000.00, 0.05, 0.18, 1100.00)
# calculate_years(1200.00, 0.17, 0.05, 2000.00)
# calculate_years(1500.00, 0.07, 0.6, 5000.00)