# i = 1 
# while i<= 10 : 
#     x = i * 2
#     print(x)
# i=1

# b =("12345")
# while i <= 10 :
#     x = input("Masukkan Password : ")
#     if x == b : 
#          print ("Password Correct")
#          break    
#     else: 
#             print ("Password incorrect")
#     i+=1

# i = 1
# x = input('Masukkan Huruf yang ingin di replace : 

# while i <= 10 :
    
# nilai = ("Masukkan Nilai  : ")
# i=nilai
# while i == 0 :
#     x = (i*(i-1) 
#     i-=1
#     print x  



# vokal = ['a', 'i', 'u', 'e', 'o']
# kalimat = input('Masukkan kalimat: ')
# kalimat2 = ''
# for i in kalimat:
#     if i in vokal:
#         huruf = 'o'
#     else: huruf = i
#     kalimat2 += huruf
# print(kalimat2)



# def factorial(n):
#     result = 1

#     if n < 0 :
#         return 'Must be positive int'
#     else:
#         i = 1
#         while i <= n:
#             result *= i
#             i += 1
#     return result

# n = int(input('Masukkan n : '))
# print(factorial(n))


# def factorial() :
      

#     if fac <= 0 :
#         print("Must be positive digit")
#     else:
#         i=0
#         while i <= fac:
#             h=h*i
#         i-=1

         

# fac = int(input("Masukkan nilai factorial : "))
# print(factorial)

n = input ("Sambarang")
def factorial(n): # n = 5
    if n == 0: # 5 == 0 False
        return 1
    elif n == 1: # 5 == 1 False
        return 1
    elif n < 0: # 5 < 0 False
        return 'must be positive digit'
    else:
        result = 1 # 5 // 20 // 60 // 120
        i = n # 5 // 4 // 3 // 2 // 1
        while i != 1: # 5 != 1 True // 4 != 1 True // 3 != 1 True // 2 != 1 True // i != 1 False
            result *= i # 1*5=5 // 5*4=20 // 20*3=60 // 60*2=120
            i -= 1 #5-1=4 // 4-1=3 // 3-1=2 // 2-1=1
        return result