#Introduction to programming':Task 1
#Tsadzikidze Arsen, FB-24, 26
#Напишіть програму, яка вводить з клавіатури два непусті неспадаючі списки цілих
#чисел, і друкує ті і тільки ті елементи, які входять тільки в один зі списків (симетрична
#різниця множин)
print('Introduction to programming:Task 1')
print('Tsadzikidze Arsen, 26')

length = int(input('Введіть кількість елементів списку: '))
l = []
for i in range(length):
    el = int(input((f"Введіть {i+1} елемент списку: ")))
    l.append(el)
l.sort()
print('Ваш список:', l)

length = int(input('Введіть кількість елементів списку: '))
l1 = []
for i in range(length):
    el = int(input((f"Введіть {i+1} елемент списку: ")))
    l1.append(el)
l1.sort()
print('Ваш список:', l1)


def sorting_elements(l):
  for i in l:
    if not (i in l1):
        print(i, end=' ')

sorting_elements(l)











