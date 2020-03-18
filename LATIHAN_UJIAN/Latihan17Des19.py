# # NOMOR 1
# def nbYear(p0, percent, aug, p):
#     countyears = 0
#     while p0 < p:
#         calculate = (p0 * percent/100) + aug
#         p0 += calculate
#         countyears += 1
#     print(countyears)

# nbYear (1000, 2, 50, 1200)
# nbYear (1500, 5, 100, 5000)
# nbYear (1500000, 2.5, 10000, 2000000)


# # NOMOR 2
# def tickets(peopleinline):
#     changes = []
#     for j in peopleinline:
#         if j == 25:
#             changes.append(j)
#             results = True
#         if j == 50:
#             for k in range(len(changes)):
#                 if changes[k] == 25:
#                     changes.pop(k)
#                     changes.append(j)
#                     results = True
#                     break
#                 else:
#                     results = False
#                     break
#         if j == 100:
#             for k in range(len(changes)):
#                 if(k!=len(changes)-1) and (changes[k]+changes[k+1]==75):
#                     results = True
#                     changes.append(k)
#                     changes.pop(k)
#                     changes.pop(k+1)
#                     break
#                 else:
#                     results = False
#                     break

#     if (results == True):
#         print("'YES'")
#     else:
#         print("'NO'")

# tickets([25, 25, 50, 25, 25, 100, 50, 100])


# # NOMOR 3
# user_input = int(input('how many row do you want?: '))
# def rowSumOddNumbers(n):
#     num = 1
#     hasiljumlah = []
#     for row in range(0, n):
#         for col in range(0, row + 1):
#             print('{}'.format(num), end=' ')
#             if  row == n-1:
#                 hasiljumlah.append(num)
#             num += 2
#         print()
#     hasil = sum(hasiljumlah)
#     print('\njumlah line terakhir = '+str(hasil))

# rowSumOddNumbers(user_input)