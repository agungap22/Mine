# nomor 1
# dicthari = {
#     'senin': 'Monday',
#     'selasa': 'Tuesday',
#     'rabu': 'Wednesday',
#     'kamis': 'Thursday',
#     'jumat': 'Friday',
#     'sabtu': 'Saturday',
#     'minggu': 'Sunday'
#     }
# hari = input('Masukkan hari: ').lower()
# print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari]}')



# nomor 2
# dicthari = {
#     'senin': 'monday',
#     'selasa': 'tuesday',
#     'rabu': 'wednesday',
#     'kamis': 'thursday',
#     'jumat': 'friday',
#     'sabtu': 'saturday',
#     'minggu': 'sunday'
#     }
# hari = input('Masukkan hari (ENG/INA): ').lower()
# ina = list(dicthari.keys()) # [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
# eng = list(dicthari.values()) # [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
# if hari in ina:
#     print(f'Bahasa Inggris dari {hari.capitalize()} adalah {dicthari[hari].capitalize()}')
# elif hari in eng:
# #                                                                 ina[4].capitalize()
#     print(f'Bahasa Indonesia dari {hari.capitalize()} adalah {ina[eng.index(hari)].capitalize()}')
# else: print(f'Kata yang Anda masukkan bukan nama hari.')

# print(dicthari.items())

# mobil = ['Toyota', 'Honda', 'Mercedes','Toyota']
# print('Index dari mobil Toyota:', mobil[mobil.index('Toyota')][3])
# print(mobil.count('Toyota'))
# z = {1,2,3,1,2,3,4,4,4,4,4}
# print(type(z))
# z2 = {}
# print(type(z2))
# print(z)
# z_list = list(z)
# print(z_list)

def lanjut(n) :
    duit = 0 
    for i in range(len(n)):
        if int (n[i]) == 25 : 
                duit += int (n[i])
        elif  int (n[i]) > 25 :
                hasil = duit - int (n[i])
                if hasil < 0 :
                    print("NO")
                    break
                else : 
                    duit += hasil
                    continue

            # elif n[i] > 25 :
                # duit = n[i] - 25    
        else : 
            print ("NO")
            break
    print(duit)

z = ['25','25','50']
x = ['25','100']
y = ['25','25','50','50','100']
v = ['25','100']
print(lanjut(v))