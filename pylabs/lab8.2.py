#Сортування "вставкою"
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

def insert(l1, i):
    value = l1[i]
    j=i
    while j != 0 and l1[j - 1] > value:
        l1[j] = l1[j-1]
        j -= 1
    l1[j] = value
def insertion_sort(l1):
    for i in range(len(l1)):
        insert(l1, i)
insertion_sort(l1)
print(l1)

def insert(l2, i):
    value = l2[i]
    j=i
    while j != 0 and l2[j - 1] < value:
        l2[j] = l2[j-1]
        j -= 1
    l2[j] = value
def insertion_sort(l2):
    for i in range(len(l2)):
        insert(l2, i)
insertion_sort(l2)
print(l2)