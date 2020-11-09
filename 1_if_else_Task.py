#Latihan menghitung berat badan ideal
# M = int(input ('Masukkan berat badan anda (kg) : '))

# T = int (input('Masukkan tinggi badan anda (cm) : '))/100
# IMT = (M/(T**2))
# print(IMT)
# if IMT < 18.5 :
#     print('Berat badan kurang')
# elif IMT >= 18.5 and IMT <= 24.9 :
#     print('Berat badan ideal')
# elif IMT >= 25.0 and IMT <= 29.9:
#     print('Berat badan berlebih')
# elif IMT >= 300.0 and IMT <= 39.9 :
#     print('Berat badan sangat berlebih')
# else :
#     print("Obesitas")


#Latihan Lagi

# 1. Anda adalah penjual pisang. Yang mana pisang anda berharga 3000.
# Buatlah sebuah program if-else yg memiliki kondisi, jika seseorang berbelanja di Anda lebih dari 100,000
# maka akan diberikan diskon 10%. Kalau lebih dari 50,000 namun kurang dari 100,000 maka akan diberi diskon 5%.
# Kalau kurang dari 50,000 maka tidak diberi diskon sama sekali.

# contoh:
# in: berapa pisang yg ingin anda beli? 30
# out: total belanja Anda adalah IDR 85,500

# pembeli = int (input('Berapa pisang yang ingin anda beli : '))
# b = (pembeli * 3000)
# print(b)
# if b > 100000 :
#     h = int(b-(b * 0.1 )) 
#     print (f" Total belanja anda adalah IDR {h}")
# elif b > 50000 and b < 100000:
#     h = int(b-(b * 0.05 ))
#     print (f" Total belanja anda adalah IDR {h}")
# else :
#     print (f" Total belanja anda adalah IDR {b}")

# 2. Anda adalah seorang pemilik perusahaan dan Anda berniat untuk memberi bonus kepada pegawai Anda.
# Buatlah program if-else yg memiliki kondisi, jika Year of Service seorang pegawai lebih dari 10 tahun,
# maka gajinya akan diberi bonus sebesar 10%.

# contoh:
# in: berapa gaji anda? 10000000
# in: year of service? 15
# out: Selamat Anda mendapat bonus! Total gaji anda IDR 11000000

# gaji = int (input ('Berapa gaji anda : '))
# tahun = int (input ('Year of servive : '))
# if tahun > 10 :
#     bonus = ((gaji*0.1)+gaji)
#     print(f'Selamat anda mendapat bonus! Total gaji anda sebesar IDR {bonus}')
# else :
#     print (f"Gaji anda sebesar IDR {gaji}")


#3. Ambil 3 input umur dari 3 user lalu tentukan siapa yang lebih tua.

# contoh:
# in: umur user_1 = 50
# in: umur user_2 = 40
# in: umur user_3 = 25

# out: user 1 adalah yang paling tua

# contoh lain:
# in: umur user_1 = 40
# in: umur user_2 = 40
# in: umur user_3 = 40

# out: tidak ada yang lebih tua

# a = int (input(' Umur User 1 = '))
# b = int (input(' Umur User 2 = '))
# c = int (input(' Umur User 3 = '))

# if a > b and a > c :
#     print (" User 1 adalah yang paling tua ")
# elif b > a and b > c :
#     print (" User 2 adalah yang paling tua ")
# elif c > a and c > b :
#     print (" User 3 adalah yang paling tua ")
# else :
#     print (" Tidak ada yang lebih tua ")

#4. Buatlah program sederhana untuk menentukanapakah seorang siswa boleh mengikuti ujian
#   atau tidak berdasarkan presentase absennya. Minimal absensi adalah 75%.

# contoh : 
# in : total kelas yang diadakan : 100
# in : total attendances : 50

#  out : Total kehadiran anda 50%. Maaf anda tidak diperbolehkan mengikuti ujian.
import math
total = int (input ("Total kelas yang diadakan : "))
hadir = int(input ("Total attendances : "))

pr = (total/hadir)
persen = round(100/pr,2)
if persen >= 0.75 :
    print ( f"Totan kehadiran anda adalah {(persen)}%. Silahkan mengikuti ujian")
else :
    print (f"Total kehadiran anda adalah {(persen)}%. Maaf anda tidak diperbolehkan mengikuti ujian")