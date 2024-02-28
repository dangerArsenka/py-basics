#Introduction to programming':Task 4.2
#Tsadzikidze Arsen, FB-24, 29
print("Introduction to programming: Task 4.2")
print("Tsadzikidze Arsen, FB-24, 29")
n = int(input('enter number'))
if n >= 0:
  n = n
else:
  n = -n  

f = 1
while n >= 10:
  n = n / 10
  f = f + 1
 
print(f)
