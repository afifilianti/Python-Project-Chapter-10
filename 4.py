#4

def cariNIM(nim):
    file = open(source, 'r')
    dataMhs = file.read()
    data = dataMhs.replace(' | ', ' ')
    data = data.replace('\n', ' ')
    data = data.split(' ')
    data.remove('')
    try:
        j = data.index(nim)
        if nim in data:
            print('Data Mahasiswa')
            print('Nim    : ', data[j])
            print('Nama   : ', data[j + 1])
            print('Alamat : ', data[j + 3])
    except ValueError:
        print('Data mahasiswa tidak ditemukan')

source = 'Data Mahasiswa.txt'
ulang = 'y'
while ulang == 'y':
    nim = input('Masukkan NIM yang akan Anda cari : ')
    data = cariNIM(nim)
    ulang  = input('\nUlangi input lagi?(y/n) : ')
    ulang = ulang.lower
