# # PR 18 DESEMBER 2019 # #
datapengguna = {}
classchoose = {}
currentuser = []
History = []

def menu():
    print('''Welcome to the Purwadhika Class Registration, Please choose your selection:
1. Register
2. Login
3. Class Registration
4. History
5. Logout
6. Exit''')

successlogin = False
a = True
while a == True:
    if len(currentuser) == 1:
        print('\nYou login as {}'.format(currentuser[0]))
    menu()
    user_input = input('Choose: ')
    try:
        if int(user_input) == 1:
            username = input('Masukkan username baru: ')
            password = input('Masukkan password baru: ')
            if username not in datapengguna[username]:
                datapengguna[username] = password
                classchoose[username] = []
            elif username in datapengguna[username]:
                print('User name already exist.\n')

        if int(user_input) == 2 and successlogin == False:
            usernameterdaftar = input('username: ')
            passwordsterdaftar = input('password: ')
            if usernameterdaftar in datapengguna and passwordsterdaftar in datapengguna.values():
                currentuser.append(username)
                successlogin = True
            else:
                print('username or password is wrong or username does not exist.\n')
        elif int(user_input) == 2 and successlogin == True:
            print('Please log out first, before login again.')

        if int(user_input) == 3 and successlogin == False:
            print("Not logged in yet or haven't register.")
        elif int(user_input) == 3 and successlogin == True:
            print('Please choose your class:')
            print('1. Data Science Class\n2. Web and Mobile Class\n3. Digital Marketing Class\n4. UI/UX Class')
            pilihankelas = input('Choose your class: ')
            if int(pilihankelas) == 1:
                if 'Data Science Class' not in classchoose[currentuser[0]]:
                    classchoose[currentuser[0]] = 'Data Science Class'
                    print('Class Successfully Registered')
                    History.append('Data Science Class')
                else:
                    print('Class has been registered.')
            if int(pilihankelas) == 2:
                if 'Web and Mobile Class' not in classchoose[currentuser[0]]:
                    classchoose[currentuser[0]] = 'Web and Mobile Class'
                    print('Class Successfully Registered')
                    History.append('Web and Mobile Class')
                else:
                    print('Class has been registered.')
            if int(pilihankelas) == 3:
                if 'Digital Marketing Class' not in classchoose[currentuser[0]]:
                    classchoose[currentuser[0]] = 'Digital Marketing Class'
                    print('Class Successfully Registered')
                    History.append('Digital Marketing Class')
                else:
                    print('Class has been registered.')
            if int(pilihankelas) == 4:
                if 'UI/UX Class' not in classchoose[currentuser[0]]:
                    classchoose[currentuser[0]] = 'UI/UX Class'
                    print('Class Successfully Registered')
                    History.append('UI/UX Class')
                else:
                    print('Class has been registered.')
            elif int(pilihankelas) < 1 or int(pilihankelas) > 4:
                print("Saat ini hanya tersedia 4 kelas, silahkan pilih kelas yang tersedia.\n")

        if int(user_input) == 4 and successlogin == False:
            print("Not logged in yet or haven't register.\n")
        elif int(user_input) == 4 and classchoose[currentuser[0]] == []:
            print('Anda belum daftar kelas manapun.\n')
        elif int(user_input) == 4:
            printhist = 'Class taken by {} is'.format(currentuser[0])
            for i in range(len(History)):
                printhist += ' '+ History[i]
                if len(History)> 2 and (i != len(History)-1):
                    printhist += ','
                if i == (len(History)-2) and (len(History) != 1):
                    printhist += ' and'
            print(printhist)

        if int(user_input) == 5 and len(currentuser) == 0:
            print('You have not login yet, Please login first.\n')
        elif int(user_input) == 5 and successlogin == False:
            print("Not logged in yet or haven't register.\n")
        elif int(user_input) == 5:
            currentuser.pop(0)
            successlogin = False
            print("\n\nYou have been logged out.")

        elif int(user_input) == 6:
            a = False
            print('Terima kasih.')

        elif int(user_input) < 0 and int(user_input) > 6:
            print('Masukkan angka sesuai pilihan angka yang tersedia.')
    except:
        print('invalid input!')






# def find_outlier(integers):
#     outlier = []
#     non_outlier = []
#     angka_ganjil = 0
#     angka_genap = 0
#     for numbers in integers:
#         if numbers % 2 == 0:
#             angka_genap += 1
#         if numbers % 2 > 0:
#             angka_ganjil += 1
#         if angka_genap > angka_ganjil:
#             if numbers % 2 == 0:
#                 non_outlier.append(numbers)
#             if numbers % 2 > 0:
#                 outlier.append(numbers)
#         if angka_ganjil > angka_genap:
#             if numbers % 2 == 0:
#                 outlier.append(numbers)
#             if numbers % 2 > 0:
#                 non_outlier.append(numbers)

#     for i in outlier:
#         if angka_ganjil == angka_genap:
#             print("Tidak ada outlier")
#             break
#         else:
#             print("angka outlier dalam list {}".format(i))

# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
# find_outlier([161, 3, 1719, 19, 11, 13, -20])
# find_outlier([2, 4, 0, 100, 19, 11, 13, 17])