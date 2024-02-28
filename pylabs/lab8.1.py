#Сортування "бульбашкою" (Bubble sorting algorithm)
length = int(input('Введіть кількість елементів списку: '))
l=[]
for i in range(length):
    el = int(input((f"Введіть {i+1} елемент списку: ")))
    l.append(el)
print('Ваш список:', l)

l1 = []
l2 = []
def dividing_elements(l):
    for i in range(len(l)): 
        if l[i] % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
dividing_elements(l)

end = len(l1) - 1

while end != 0:
    for i in range(end):
        if l1[i] > l1[i + 1]:
            l1[i], l1[i + 1] = l1[i + 1], l1[i]
    end = end - 1

end = len(l2) - 1

while end != 0:
    for i in range(end):
        if l2[i] < l2[i + 1]:
            l2[i], l2[i + 1] = l2[i + 1], l2[i]
    end = end - 1
print(l1)
print(l2)



