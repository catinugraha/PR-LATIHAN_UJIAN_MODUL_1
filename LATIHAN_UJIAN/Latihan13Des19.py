# # BACKWARDS PRIME (NOMOR 1)
def backwardsprime(start,stop):
    result=[]
    if start <= 11:
        start = 12
    for item in range(start,stop+1):
        balik = int(str(item)[::-1])
        if item == balik:
            continue
        if primechecker(item) and primechecker(balik):
            result.append(item)
    return result
def primechecker(k):
    x=True    
    for i in range(2,k):
        if k % i == 0:
            x = False
            break
    return x
print(backwardsprime(9900,10000))



# NO. 2 (HIGHEST NUMBER X SEQUENCE)
# def get_highest_xnum(num, sequence):
#     hitungdepan = 0
#     num = str(num)
#     newlist = []
#     if len(num) <= 10:
#         for angka3 in range(len(num) - 2):
#             newlist.append(int(num[hitungdepan:sequence]))
#             hitungdepan += 1
#             sequence += 1
#     else:
#         print('max. numbers is 10 digits')
    
#     idx = 1
#     angka2 = 0
#     for angka in newlist:
#         if angka > newlist[idx] and angka > angka2:
#             angka2 = angka
#             idx += 1
#     print(angka2)

# get_highest_xnum(1794103177, 3)
# get_highest_xnum(1794103177, 4)
# get_highest_xnum(87173114, 5)


# # NO. 3 AY WORD
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