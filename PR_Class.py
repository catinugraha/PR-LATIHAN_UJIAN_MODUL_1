# # PR CLASS 1
history = []
class bikinMenu:
    def __init__(self, nama, listmakanan, harga): ## BISA MEMASUKKAN PARAMETER LGSG SETELAH INIT WALAUPUN TIDAK ADA DALAM PARAMETER
        self.name = nama
        self.makanan = listmakanan
        self.price = harga
    
    def getmenu(self):
        for makanan in range(len(self.makanan)):
            print("{}. {} harganya adalah {} ".format(makanan+1, self.makanan[makanan], self.price[makanan]))
    
    def menuprice(self):
        user_input = int(input('Mau beli yang mana?: '))
        try:
            print("{} telah membeli {} dengan harga {}".format(self.name, self.makanan[user_input-1],
            self.price[user_input-1]))
            history.append(self.makanan[user_input-1])
        except:
            print('Invalid Input')
        

    def gethistory(self):
        z = ('{} telah membeli'.format(self.name))
        for makanantelahdibeli in range(len(history)):
            z += ' ' + history[makanantelahdibeli]
            if len(history)>2 and (makanantelahdibeli != (len(history)-1)):
                z+= ','
            if (makanantelahdibeli == (len(history)-2)) and (len(history) != 1):
                z+= ' dan'
        print(z)

Paul = bikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])

Paul.getmenu()
Paul.menuprice()
Paul.gethistory()
Paul.getmenu()
Paul.menuprice()
Paul.gethistory()
Paul.getmenu()
Paul.menuprice()
Paul.gethistory()

# # PR CLASS 2
import random
class ramal:
    def __init__(self, uang):
        self.donasi = uang
    
    def getmenu(self):
        a = True
        while a == True:            
            print("App Ramalan Terkini\n")
            print("Pilih ramalan anda:")
            print('1. Ramalan pekerjaan')
            print('2. Ramalan kesehatan')
            print('3. Ramalan percintaan')
            print('4. Keluar')
            user_input = int(input('Masukkan Pilihan: '))
            if user_input == 1:
                if self.donasi < 10000:
                    hasilramalan1 = [['Pekerjaan Sangat Buruk','Pekerjaan Buruk','Pekerjaan biasa saja'],
                    ['Pekerjaan Luar Biasa'],['Pekerjaan Sangat Luar Biasa']]
                    prob = [0.8,0.1,0.1]
                    rnd1 = random.choices(hasilramalan1, prob)
                    rnd2 = random.choices(rnd1[0])
                    hasil = rnd2[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                elif self.donasi == 10000 and self.donasi < 50000:
                    hasilramalan1 = [['Pekerjaan Sangat Buruk'],['Pekerjaan Buruk','Pekerjaan biasa saja',
                    'Pekerjaan Luar Biasa'],['Pekerjaan Sangat Luar Biasa']]
                    prob = [0.1,0.8,0.1]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                else:
                    hasilramalan1 = [['Pekerjaan Sangat Buruk'],['Pekerjaan Buruk'],['Pekerjaan biasa saja',
                    'Pekerjaan Luar Biasa','Pekerjaan Sangat Luar Biasa']]
                    prob = [0.1,0.1,0.8]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
            elif user_input == 2:
                if self.donasi < 10000:
                    hasilramalan1 = [['Kesehatan Sangat Buruk','Kesehatan Buruk','Kesehatan biasa saja'],
                    ['Kesehatan Luar Biasa'],['Kesehatan Sangat Luar Biasa']]
                    prob = [0.8,0.1,0.1]
                    rnd1 = random.choices(hasilramalan1, prob)
                    rnd2 = random.choices(rnd1[0])
                    hasil = rnd2[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                elif self.donasi == 10000 and self.donasi < 50000:
                    hasilramalan1 = [['Kesehatan Sangat Buruk'],['Kesehatan Buruk','Kesehatan biasa saja',
                    'Kesehatan Luar Biasa'],['Kesehatan Sangat Luar Biasa']]
                    prob = [0.1,0.8,0.1]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                else:
                    hasilramalan1 = [['Kesehatan Sangat Buruk'],['Kesehatan Buruk'],['Kesehatan biasa saja',
                    'Kesehatan Luar Biasa','Kesehatan Sangat Luar Biasa']]
                    prob = [0.1,0.1,0.8]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
            elif user_input == 3:
                if self.donasi < 10000:
                    hasilramalan1 = [['Percintaan Sangat Buruk','Percintaan Buruk','Percintaan biasa saja'],
                    ['Percintaan Luar Biasa'],['Percintaan Sangat Luar Biasa']]
                    prob = [0.8,0.1,0.1]
                    rnd1 = random.choices(hasilramalan1, prob)
                    rnd2 = random.choices(rnd1[0])
                    hasil = rnd2[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                elif self.donasi == 10000 and self.donasi < 50000:
                    hasilramalan1 = [['Percintaan Sangat Buruk'],['Percintaan Buruk','Percintaan biasa saja',
                    'Percintaan Luar Biasa'],['Percintaan Sangat Luar Biasa']]
                    prob = [0.1,0.8,0.1]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
                else:
                    hasilramalan1 = [['Percintaan Sangat Buruk'],['Percintaan Buruk'],['Percintaan biasa saja',
                    'Percintaan Luar Biasa','Percintaan Sangat Luar Biasa']]
                    prob = [0.1,0.1,0.8]
                    rnd3 = random.choices(hasilramalan1, prob)
                    rnd4 = random.choices(rnd3[0])
                    hasil = rnd4[0]
                    print('Hasil Ramalan: {}'.format(hasil))
            elif user_input == 4:
                print('Terima kasih telah menggunakan app ramalan.')
                a = False


App = ramal(9999)
App.getmenu()