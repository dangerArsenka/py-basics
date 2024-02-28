from math import *
#Introduction to programming':Task 3
#Tsadzikidze Arsen, FB-24, 29
print('Introduction to programming:Task2')
print('Tsadzikidze Arsen, 29')
a = float (input('enter a = '))
b = float (input('enter b = '))
#calculation = ((a-2)/(2*a+b))+(sin(3*a)/cos(b))

if a == -b/2 or isclose(cos(b),0):
    print("Error:Division by zero" )

else:
    y = ((a-2)/(2*a+b))+(sin(3*a)/cos(b))
    print('y = ', y)
    
                              


