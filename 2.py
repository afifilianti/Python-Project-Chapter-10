#2

def mahasiswa(data, nim, nama, alamat):
    file = open(data, 'a')
    file.write('{} | {} | {} \n'.format(nim, nama, alamat))
    file.close()
def dataMhs(data):
    buka = open(data, 'r')
    for i in buka:
        print(i)
    buka.close()

data = 'Data Mahasiswa.txt'
ulang = 'y'
while ulang == 'y':
    nim    = input('Masukkan NIM            : ')
    nama   = input('Masukkan Nama Mhs       : ')
    alamat = input('Masukkan Alamat         : ')
    mahasiswa(data, nim, nama, alamat)
    ulang  = input('\nUlangi input lagi?(y/n) : ')
if ulang != 'y':
    print('\nData Mahasiswa')
    dataMhs(data)
