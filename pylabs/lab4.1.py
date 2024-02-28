from math import *
#Introduction to programming':Task 4.1
#Tsadzikidze Arsen, FB-24, 29
print("Introduction to programming: Task 4.1")
print("Tsadzikidze Arsen, FB-24, 29")
s = 0.0
n = 2
while (log10(factorial(n))*e**(-n*sqrt(n)) > 0.00001):
    s = log10(factorial(n))*e**(-n*sqrt(n)) + s
    n = n + 1
print(f'{s:.{4}f}')
input(' ')
