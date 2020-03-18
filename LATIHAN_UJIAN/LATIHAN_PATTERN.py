
####### SOAL 1 (FULL PIRAMIDA)
 
# def pattern(n):
#       k = 2 * n - 2
#       for i in range(0,n):
#            for j in range(0,k):
#                print(end=" ")
#            k = k - 1
#            for j in range(0, i+1):
#                 print("#", end=" ")
#            print("") 
# pattern(5)



####### SOAL 2 (PIRAMIDA TERBALIK)
# def pattern(n):
#       k = 2*n -2
#       for i in range(n,-1,-1):
#            for j in range(k,0,-1):
#                 print(end=" ")
#            k = k +1
#            for j in range(0, i+1):
#                 print("*", end=" ")
#            print("")
# pattern(8)



######### SOAL 3 (PIRAMIDA ROTATE 90' KE KANAN)
# def pattern(n):
#       for i in range(0, n):
#            for j in range(0, i + 1):
#                 print("* ", end="")
#            print("")
#       for i in range(n, -1 , -1):
#           for j in range(0, i + 1):
#                print("* ", end="")
#           print("")
# pattern(5)



######### SOAL 4 (PIRAMIDA ROTATE 90' KE KIRI)
# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0, n-1):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 2
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("")
#     k = -1
#     for i in range(n-1,-1,-1):
#         for j in range(k,-1,-1):
#             print(end=" ")
#         k = k + 2
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("")

# pattern(5)



######## SOAL 5 (HOURGLASS)
# def pattern(n):
#     k = n - 2
#     for i in range(n,-1,-1):
#         for j in range(k,0,-1):
#             print(end=" ")
#         k = k +1
#         for j in range(0, i+1):
#             print("*", end=" ")
#         print("")
#     k = 2*n -2
#     for i in range(0,n+1):
#         for j in range(0,k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i+1):
#             print("*", end=" ")
#         print("") 
      
# pattern(5)



########## SOAL 6 (HALF PYRAMID SISI KANAN)
# def pattern(n):
#      for i in range(0,n):
#          for j in range(0, i+1):
#               print("* " , end="")
#          print("")
# pattern(5)



######### SOAL 7 (HALF PYRAMID SISI KIRI)
# def pattern(n):
#      k = 2 * n - 2
#      for i in range(0, n):
#           for j in range(0, k):
#                print(end=" ")
#           k = k - 2
#           for j in range(0, i + 1):
#               print("* ", end="")
#           print("")
# pattern(5)



######## SOAL 8 (Downward Half-Pyramid Pattern Program)

# def pattern(n):
#       for i in range(n, -1, -1):
#            for j in range(0, i + 1):
#                print("* ", end="")
#            print("")
# pattern(5)



######## SOAL 9 (DIAMOND PATTERN)
# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0 , k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0 , i + 1 ):
#             print("* ", end="")
#         print("")
#     k = n - 2
#     for i in range(n , -1, -1):
#         for j in range(k , 0 , -1): 
#             print(end=" ")
#         k = k + 1
#         for j in range(0 , i + 1):
#             print("* ", end="")
#         print("")
# pattern(5)


# SOAL 10 (DIAMOND STAR PROGRAM)
# for i in range(5):
#     for j in range(5):
#         if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


######## SOAL 11 (SIMPLE NUMBERS PROGRAM)

# def pattern(n):
#     x = 0
#     for row in range(0,n):
#         x += 1
#         for col in range (0, row+1):
#             print(x, end=" ")
#         print("")
# pattern(5)



########## SOAL 12 (PASCAL TRIANGLE)

#### RATA KIRI
# def pascal(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(function(i, j)," ", end="")
#         print()
 
# def function(n, k):
#     res = 1
#     if (k > n - k):
#         k = n - k
#     for i in range(0, k):
#         res = res * (n - i)
#         res = res // (i + 1) 
#     return res
# pascal(7)



#### PIRAMID
# def pascal(n):
#     for row in range(0, n):
#         for col in range(row,n-1):
#             print(end=' ')
#         for col in range(0, row + 1):
#             print(function(row, col), end=' ')
#         print()
 
# def function(n, k):
#     res = 1
#     if (k == n - k):
#         k = n - k
#     for i in range(0, k):
#         res = res * (n - i)
#         res = res // (i + 1)
 
#     return res
 
# pascal(4)




######### SOAL 13 (HALF PYRAMID NUMBER PATTERN, DOWN FIRST)

# def pattern(n):
#     for row in range(1,n+1):
#         for col in range(1,row+1):
#             print(col, end= " ")
#         print("")
# pattern(5)



######### SOAL 14 (DIAMON PATTERN WITH NUMBERS)

# def pattern(n):
#     k = 2 * n - 2
#     x = 0
#     for i in range(0, n):
#         x += 1
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print(x, end=" ")
#         print("\r")
#     k = n - 2
#     x = n + 2
#     for i in range(n, -1, -1):
#         x -= 1
#         for j in range(k, 0, -1):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i + 1):
#             print(x, end=" ")
#         print("\r")

# pattern(5)



########## Descending Order Pattern Program

# def pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
 
#         print("\r")
 
# pattern(5)



############ Binary Numbers Pattern Program

# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print('10', end="")
 
#         print("\r")
 
# pattern(5)



########### Right Alphabetical TRIANGLE

# def pattern(n):
#     x = 65
#     for i in range(0, n):
#         ch = chr(x)
#         x += 1
#         for j in range(0, i + 1):
#             print(ch, end=" ")
#         print("\r")
 
# pattern(5)



############## Character Pattern Program

# def pattern(n):
#     k = 2 * n - 2
#     x = 65
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             ch = chr(x)
#             print(ch, end=" ")
#             x += 1
#         print("\r")
 
 
# pattern(7)


############ K Shape Character Program

# for i in range(7):
#     for j in range(7):
#         if j == 0 or i - j == 3 or i + j == 3:
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()




########### Triangle Character Pattern Program

# def pattern(n):
#     k = 2 * n - 2
#     x = 65
#     for i in range(0, n):
#         ch = chr(x)
#         x += 1
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print(ch, end=" ")
#         print("\r")



########### Diamond Shaped Character Pattern Program

# def pattern(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         x = 65
#         for j in range(0, i + 1):
#             ch = chr(x)
#             print(ch, end=" ")
#             x += 1
#         print("\r")
#     k = n - 2
#     x = 65
#     for i in range(n, -1, -1):
#         for j in range(k, 0, -1):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i + 1):
#             ch = chr(x)
#             print(ch, end=" ")
#             x += 1
#         print("\r")
  
# pattern(5)



