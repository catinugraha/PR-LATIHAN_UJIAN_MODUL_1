# # PR 1
# data_lst = [1,3,3,3,4,4,2,4]
# n = len(data_lst)

# # # FUNCTION MEAN
# def getMean(list1) :
#     mean1 = 0
#     mean1 = sum(data_lst) / n
#     return mean1
# print(getMean(data_lst))

# # # FUNCTION VARIANCE SAMPLE
# def variance(list1):
#     var = 0
#     for number in data_lst:
#         var = var + ((number - getMean(data_lst))**2)
#     var1 = var / (n-1)
#     return var1
# # print(variance(data_lst))

# # # FUNCTION VARIANCE POPULASI
# def varpop(list1):
#     var = 0
#     for number in data_lst:
#         var += ((number - getMean(data_lst))**2)
#     var2 = var / n
#     return var2
# # print(varpop(data_lst))

# # # FUNCTION SKEWNESS
# def skewness(list1):
#     num = 0
#     for number in data_lst:
#         num += ((number - getMean(data_lst))**3)
#     num2 = num / n
#     num3 = num2 / varpop(data_lst)**3
#     return num3
# # print(skewness(data_lst))

# # # FUNCTION EXCESS KURTOSIS
# def excurt(list1):
#     num = 0
#     for number in data_lst:
#         num += ((number - getMean(data_lst))**4)
#     num2 = num / n
#     num3 = (num2 / (varpop(data_lst)**4))-3
#     return num3
# # print('excess kurtosis: '+ str(excurt(data_lst)))

# # # FUNCTION STANDAR DEVIASI
# def stdev(list1):
#     import math
#     stddev = math.sqrt(variance(data_lst))
#     return stddev
# # print(stdev(data_lst))

# # # FUNCTION MEDIAN
# def getMedian(list1) :
#     import math
#     list1.sort()
#     median = 0
#     if (len(list1) % 2 != 0) :
#         median = list1[math.floor(len(list1) / 2)]
#     else :
#         mid1 = list1[(int(len(list1) / 2)) - 1]
#         mid2 = list1[int(len(list1) / 2)]
#         median = (mid1 + mid2) / 2
#     return median
# print(getMedian(data_lst))

# FUNCTION MODE
# def mode(list1):
#     most = max(list(map(list1.count, list1)))
#     return list(set(filter(lambda x: list1.count(x) == most, list1)))
# print(mode(data_lst))

# def statistic_sample(x,y):
#     if y == "mean":
#         return getMean(data_lst)
#     elif y == "variance":
#         return variance(data_lst)
#     elif y == "standar deviasi":
#         return stdev(data_lst)
#     elif y == "median":
#         return getMedian(data_lst)
#     elif y == "skewness":
#         return skewness(data_lst)
#     elif y == "excess kurtosis":
#         return excurt(data_lst)
#     else:
#         print('kata yang anda masukkan salah, silahkan coba lagi')

# inputan = input('input: ')
# inputan = inputan.lower()
# print(statistic_sample(data_lst, inputan))

# # PR 2
# n = int(input('Masukkan ukuran:'))

# num = 1
# number = 0
# for row in range(1, n+1):
#     my_list=[]
#     for col in range(1, row+1):
#         if col == row:
#             my_list.append(num)
#             print(my_list)
#             number += num
#         else:
#             print(num, end=" ") 
#         num += 1

# print('sum of each last part of the triangle is {}'.format(number))