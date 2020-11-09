# data_diri = open('daftar_nama.csv','r')
# x = data_diri.read().split('\n')
# print(x)

# header_list=x[0]
# print('header list',header_list)
# header_element = header_list.split(',')
# print('header element',header_element)

# value_list=x[1:]
# print('value list' ,value_list)
# data=[]
# for i in value_list :
#     a = i.split(',')
#     header_value = dict(zip(header_element, a))
#     data.append(header_value)

# print(data)

json = open ('daftar_nama.json','r')
print(json.read())

import json

with open('daftar_nama.json', mode='r') as daftar:
    output = json.load(daftar)

print(output)

for i in range(len(output)):
    print(output[i])

output.append({'Nama':'dede','usia' : 24, 'kota':'bekasi'})
print(output)
with open('daftar_nama_update.json','w') as update :
    json.dump(output,update)

import csv
list_data=[]
with open ('daftar_nama.csv','r') as nama :
    read = csv.DictReader(nama)
    for data in read:
        list_data.append(dict(data))
print(list_data)
list_data.append({'Nama':'dede','usia' : 24, 'kota':'bekasi'})
print(list_data)

with open('daftar_nama.csv','r') as update :
    columns = list_data[2].keys()
    write = csv.DictWriter(update, fieldnames=columns)
    write.writeheader()
    write.writerows(list_data)

print(columns)