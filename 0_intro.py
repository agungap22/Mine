############################################## HELLO WORLD #################################################
# (print('hello wordl')

# #fungsi print adalah mencetak sesuatu

# nama = 'Agung'
# umur = 22
# pekerjaan = 'Mahasiswa'
# print(nama)
# print (umur)
# print (pekerjaan)

# print (type(nama))
# # Kalau bingung terlalu banyak kurung bisa menggunakan 
# # dtype_nama = type(nama)
# #print(dtype_nama)
# print (type(umur))
# nama = input ('What is your name : ') 
# print ( 'My name is ' + nama + ' umur saya ' + str(29)) # Jika menggunakan "+" jangan lupa menggunakan spasi dan hanya variabel yang sama
# print ('My name is', nama, 'Umur saya', 29)



############################################## Penjumlahan matematika #################################################

# print(4 // 2)# Pembagian 2 => int
# print(4 // 3) # Pembagian float
# print(5 % 2) # Modulo
# print(2 ** 3) # Pangkat/power atau print(pow(8,2))



############################################## Mengganti Data types  #################################################
# x = '10'
# print(type(x))
# y = int(x)
# print(y)

# z='25.5'
# print(float(z))

# a = 23
# a_str = str(a)
# print(a_str)
# print(type(a_str))

# b = 1.5
# b_str = str(b)
# print(b_str)
# print(type(b_str))

############################################## Quiz  #################################################
#***Buat program untuk menginput umur, nama, dan umur 5 tahun kedepan***#

# nama = input('Nama : ')
# umur = input('Umur : ') # Meskipun menggunakan input, datatyoes yang kita terima selalu dalam bentuk string
# print('Halo nama saya ', nama, 'Umur saya 5 tahun kedepan adalah ', int(umur)+5)

# #OR

# print('Halo nama saya' + nama + ', umur saya 5 tahun ke depan adalah ' + str(int(umur)+5))

#***Update data ***#
# usiaAndi = 30
# usiaAndi = usiaAndi + 5 
# #or
# usiaAndi += 5
# usiaAndi /= 2
# usiaAndi *= 3

# print(usiaAndi)

############################################## Import Library  #################################################
#Cara pertama
# import math
# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(2, 2))
# print(math.sqrt(64))

# print(round(4.7)); #dibulatkan keatas
# print(round(4.4)); #dibulatkan kebawah
# print(math.floor(4.7)); # Dibulatkan kebawah
# print(math.ceil(4.4)); #dibulatkan keatas

#Cara kedua 
# from math import pi, pow, fabs, sqrt 
# print(pi)
# print(fabs(-4.7))
# print(pow(2, 2))
# print(sqrt(64))

############################################## Strings  #################################################
x = 'Hallo Dunia Lain'
print(x)
print(type(x))
print(len(x))
print(x.index('a'))
print(x.split())
print(x.lower())
print(x.upper())
print(x.capitalize())
print('halllo dunia lain. Apa kabnar?'.capitalize())
print(x.replace('Dunia', 'apa'))

## Indexing and Slicing
print(x[0])
print(x[4])


# Homework 
x = 4
y = 3
z = 2
print(True+True)
print(True+False)