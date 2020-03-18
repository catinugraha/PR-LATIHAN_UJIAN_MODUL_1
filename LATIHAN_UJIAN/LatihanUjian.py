# LATIHAN UJIAN 1
# Princ = int(input("Principal: "))
# Intr = float(input("Interest: "))
# Tax = float(input("Tax: "))
# Desird = int(input("Desired: ")) 

# def calculate_years(principal, interest, tax, desired):
#     countyears = 0
#     while principal < desired:
#         calculate1 = principal * interest
#         calculate2 = calculate1 * tax
#         principal += (calculate1-calculate2)
#         countyears += 1
#     print('Mr. Scoorege has to wait for {} years before get {}'.format(countyears,Desird))

# calculate_years(Princ,Intr,Tax,Desird)

# # LATIHAN UJIAN 2
# string1 = input('Masukkan angka: ')
# def expandedForm(num):
    # list1 = list(filter(lambda num: len(num)<100,string1))
#     lth = len(list1)
#     jadi = []
#     for number in list1:
#         hitung = int(number)*pow(10,lth-1)
#         lth -= 1
#         if hitung != 0:
#             jadi.append(str(hitung)) # WITH JOIN
#             # jadi.append(hitung) # WITHOUT JOIN
#     #         jadi.append('+')
#     # # if (jadi[len(jadi)-1] == '+'):
#     # #     jadi[len(jadi)-1] = ''
#     # # for x in jadi:
#     # #     print(x, end=" ")
    # print(' + '.join(jadi))
# expandedForm(string1)

# # LATIAN 3
# def tower_builder(floor, size):
#     width,height = size
#     z = ''
#     for row in range(floor):
#         for tinggi in range(height):
#             for spasi in range(0,floor-row):
#                 z+='  '
#             for l in range(width +(4*row)):
#                 z+='*'
#             z += '\n'
#     print(z)
# tower_builder(6,(2,2))