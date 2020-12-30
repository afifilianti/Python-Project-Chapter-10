#5

data = open('angka.txt', 'r')
for i in data:
    j = i.split('|')
    hasil = int(j[0]) + int(j[1])
    print(hasil)
data.close()
