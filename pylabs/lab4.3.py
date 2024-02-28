from math import *
#Introduction to programming':Task 4.3
#Tsadzikidze Arsen, FB-24, 29
print("Introduction to programming: Task 4.3")
print("Tsadzikidze Arsen, FB-24, 29")
while True:
    a = float(input("Введіть число щоб отримати його корінь:"))
    try:
        def sqrt(xn,a):
            xn = 1
            e = 1e-4
            #return (1/2)*(xn+a/xn)
            if a == 0:
                return 0
            else:
                while abs(sqrt(xn, a)-xn) > e:
                    sqrt = sqrt(xn, a)
                    n = sqrt
        break 
    except:
        continue
print (sqrt(xn,a))

         


#def x(n, a):
    #return (1/2)*(n+a/n)
#sqrt = 1
#n = 1
#e = 1e-4
#if a < 0 :
    #print('Неможливо це зробити')

#elif a == 0:
   #print (0)

#else :
    #while abs(x(n, a)-n) > e:
        #sqrt = x(n, a)
        #n = sqrt
    #print(round(sqrt, 4))