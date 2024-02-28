from math import *
#Introduction to programming': Task 5
#Tsadzikidze Arsen, FB-24, 29
print ("Introduction to programming': Task 5")
print ("Tsadzikidze Arsen, FB-24, 29")
c = float (input('enter c = '))
d = float (input('enter d = '))

y = (sin (c*c)*c) + cos (c)
max = y 
c = c + 0.001
while c<=d:
  y = (sin (c*c)*c) + cos (c)
  if y>max:
    max = y
  c = c + 0.001
print ('max значення: ', max)
  



  


