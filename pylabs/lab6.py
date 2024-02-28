#Introduction to programming': Task 6
#Tsadzikidze Arsen, FB-24, 26
print ("Introduction to programming': Task 6")
print ("Tsadzikidze Arsen, FB-24, 26")
length = int(input('Введіть кількість елементів списку: '))
res=[]
for i in range(length):
    el = (input((f"Введіть {i+1} елемент списку: ")))
    res.append(el)
print('Ваш список1:', res)

length = int(input('Введіть кількість елементів списку: '))
res2=[]
for i in range(length):
    el = (input((f"Введіть {i+1} елемент списку: ")))
    res2.append(el)
print('Ваш список2:', res2)

for item in res2:
    if item in res:
        res.remove(item)
c = res
print(c)

