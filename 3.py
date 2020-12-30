#3

file = open('Data Mahasiswa.txt', 'r')
data = {}
j = 1
for i in file:
    pisah = i.split()
    data[j] = {'nim' : pisah[0], 'nama' : pisah[2], 'alamat' : pisah[4]}
    j += 1
file.close()
print(data)
