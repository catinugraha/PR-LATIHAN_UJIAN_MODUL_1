# # LATIHAN 1
# def timeConverter(seconds):
#     import math
#     if seconds <= 359999: 
#         jam = math.floor(seconds / 3600)
        
#         menit = math.floor((seconds % 3600) / 60)
#         detik = int(seconds - 3600*jam - 60*menit)
#         print(f"{jam:02d}:{menit:02d}:{detik:02d}")
#     else:
#         print("invalid input")

# timeConverter(3600)
# timeConverter(7201)    
# timeConverter(359999)

# # LATIHAN 2
# def spinwords(string):
#     lst = string.split()
#     kataterbalik = []
#     for kata in lst:
#         if len(kata) >= 5:
#             terbalik = "".join(reversed(kata))
#             kataterbalik.append(terbalik)
#         else:
#             kataterbalik.append(kata)
#     for item in kataterbalik:
#         print(item, end=" ")
#     print()

# spinwords('Hey fellow warriors')
# spinwords('This is a test')
# spinwords('This is another test')

# # LATIAN 3
# def moveZeros(list1):
#     # CARA 1
#     for repeat in range(len(list1)):
#         for isilist in range(len(list1)):
#             if str(list1[isilist]) == '0' and str(list1[isilist]) != 'False' :
#                 list1.append(list1[isilist])
#                 list1.pop(isilist)
#     print(list1)
#     # CARA 2
#     list1.sort(key=lambda item: item is 0)
#     print(list1)

# moveZeros([False,1,0,1,2,0,1,3,"a"])
# moveZeros([0,0,0,'Test',0,3,"a", True])
# moveZeros([True, True, False, 'a', 'b', 1, 1, 1])

# # LATIAN 4
class PaginationHelper:
    def __init__(self, list1, page):
        self.list = list1
        self.halaman = page
        self.isi = []

    def page_count(self):
        import math
        jumlah_halaman = 0
        hitungdepan = 0
        for isihalaman in range(math.ceil(len(self.list)/self.halaman)):
            self.isi.append(self.list[hitungdepan:self.halaman])
            hitungdepan += self.halaman
            self.halaman += self.halaman
            jumlah_halaman += 1
        print(jumlah_halaman)
    
    def item_count(self):
        counter = len(self.list)
        print(counter)
    
    def page_item_count(self,angka):
        if angka <= len(self.isi)-1:
            isiitemhalaman1 = len(self.isi[angka])
            print(isiitemhalaman1)
        elif angka < 0 or angka > len(self.isi)-1 :
            print('-1 (invalid input)')
    
    def page_index(self,angka):
        if angka > -1 and angka <= (len(self.list) -1):
            for idx in range(len(self.isi)):
                for idx2 in range(len(self.isi[idx])):
                    if self.isi[idx][idx2] == self.list[angka]:
                        print(idx)
        else:
            print('-1 (invalid input)')
    
helper = PaginationHelper(['a','b','c','d','e','f'],4)

helper.page_count()
helper.item_count()
helper.page_item_count(0)
helper.page_item_count(1)
helper.page_item_count(2)
helper.page_index(5) # should return 1 (zero based index)
helper.page_index(2) # should return 0
helper.page_index(20) # should return -1
helper.page_index(-10) # should return -1 because negative indexes are invalid