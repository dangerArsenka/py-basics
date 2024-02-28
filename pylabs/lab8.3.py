#Сортування "вибором"
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

def get_index_of_smallest(l1, i):
    index_of_smallest = i
    for j in range(i + 1, len(l1)):
        if l1[j] < l1[index_of_smallest]:
            index_of_smallest = j
    return index_of_smallest
def selection_sort(l1):
    for i in range(len(l1)):
        index_of_smallest = get_index_of_smallest(l1, i)
        l1[i], l1[index_of_smallest] = l1[index_of_smallest], l1[i]
selection_sort(l1)

def get_index_of_smallest(l2, i):
    index_of_smallest = i
    for j in range(i + 1, len(l2)):
        if l2[j] > l2[index_of_smallest]:
            index_of_smallest = j
    return index_of_smallest
def selection_sort(l2):
    for i in range(len(l2)):
        index_of_smallest = get_index_of_smallest(l2, i)
        l2[i], l2[index_of_smallest] = l2[index_of_smallest], l2[i]
selection_sort(l2)
print(l1)
print(l2)
        

