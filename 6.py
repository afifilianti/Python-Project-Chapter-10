#6

def sandiCaesar(data, key):
    hasil = ''
    file = open(data, 'r')
    for i in file.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) + key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) + key - 65) % 26 + 65)
    file.close()
    fileEnkripsi = open(data + '.encrypt', 'w')
    fileEnkripsi.write(hasil)
    fileEnkripsi.close()
    print('File enkripsi : {}.encrypt'.format(data))

data = input('Nama file yang ingin di enkripsi : ')
key = int(input('Input Keyword : '))
sandiCaesar(data, key)
