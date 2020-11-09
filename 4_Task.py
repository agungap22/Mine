# x = input('Masukkan hari : ').lower()
# day = {
#     'senin' : 'Monday',
#     'selasa' :'Tuesday',
#     'rabu' : 'Wednesday',
#     'kamis' : 'Thrusday',
#     'jumat' : 'Friday',
#     'sabtu' : 'Saturday',
#     'mingu' : 'Sunday',
# }
# ind= list(day.keys())
# eng= list(day.values())
# if x in ind:
#     print('Bahasa inggris',x.capitalize(),'Adalah',day[x].capitalize)
# else: 
#     print("Hari tidak ditemukan")

x = input ( 'Masukkan hari (INA/ENG) : ' ).lower()
day = {
    'senin' : 'monday',
    'selasa' :'tuesday',
    'rabu' : 'wednesday',
    'kamis' : 'thrusday',
    'jumat' : 'friday',
    'sabtu' : 'saturday',
    'mingu' : 'sunday',
}
ind =list(day.keys())
eng= list(day.values())
if x in eng :
    print("Bahasa Indonesia dari ",x.capitalize(), ' adalah ',ind[eng.index(x)].capitalize())
elif x in ind :
    print ("Bahasa Inggris dari ", x.capitalize(),"adalah", day[x].capitalize())
else : 
    print (" Not found ")
