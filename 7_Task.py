# # z = lambda a: 'genap' if a%2==0 else 'ganjil'
# # print(z(4))
# # print(z(3))

# name_list = 'Andi Budi Caca'.split()
# # print(name_list)

# def function(a):
#     return len(a)

# len_list = list(map(function,name_list))
# print(len_list)


# list_1 = 'coklat mellon nongka'. split()
# List_2 = [ 10000, 5000, 20000]
# couple_list = list(map(lambda a,b: a+str(b),list_1,List_2))
# print(couple_list)

# h =range(11)
# def kurang_lima (x):
#     if x < 5 :
#         return True
#     else :
#         return False

# j = list(filter(kurang_lima,h))

# print(j)
# print(list(h))

# k=[1,2,3,4,5]
# l=[1,2,3,6,7,8]
# m = list(filter(lambda a: a not in l, k))
# print(m)

# i=[2,4,6,8]
# o = list(map(lambda a:for c in i[]: c*i ))

worl_list =['merdeka', 'sohib','kari ayam','mobil','pesawat','loker','kamar','saya','motor','pertamax']
x = str(input("What do u want to search : "))
m=filter(lambda a: x in a,worl_list)

print(list(m))
