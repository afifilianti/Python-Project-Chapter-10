#1

data = open('bilangan.txt', 'r')
ganjil = 0
genap = 0
for i in data:
    if int(i) % 2 == 0:
        genap += 1
    else:
        ganjil += 1
data.close()
hasil = {'genap' : genap, 'ganjil' : ganjil}
print('Banyaknya bilangan genap :', hasil.get('genap'))
print('Banyaknya bilangan ganjil :', hasil.get('ganjil'))
