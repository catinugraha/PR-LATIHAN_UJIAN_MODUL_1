# # SOLVE IT #1
# lst = []
# n = int(input('Berapa kata yang ingin Anda masukkan?: '))
# for i in range(n):
#     kata = input('Masukkan kata:')
#     lst.append(kata)
# print(lst)
# o = input('search: ')
# res = list(filter(lambda x: o in x.lower(), lst))
# print(res)

# 7 SEGMENT
dictx = {
    '0': (' __ ', '|  |', '|__|'),
    '1': ('    ', '   |', '   |'),
    '2': (' __ ', ' __|', '|__ '),
    '3': (' __ ', ' __|', ' __|'),
    '4': ('    ', '|__|', '   |'),
    '5': (' __ ', '|__ ', ' __|'),
    '6': (' __ ', '|__ ', '|__|'),
    '7': (' __ ', '   |', '   |'),
    '8': (' __ ', '|__|', '|__|'),
    '9': (' __ ', '|__|', ' __|'),
}

n = input('masukkan angka: ')
splitter = n.split()

def seven_segment():
    digits = [dictx[digit] for digit in splitter]
    for i in range(3):
        print("  ".join(segment[i] for segment in digits))
seven_segment()