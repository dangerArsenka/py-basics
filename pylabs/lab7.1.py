#Introduction to programming': Task 7.1
#Tsadzikidze Arsen, FB-24, 29
print ("Introduction to programming: Task 7.1")
print ("Tsadzikidze Arsen, FB-24, 29")
a = float(input('enter a ='))

while True:
    x = float(input('Введіть число x: '))
    if x > 5 or x < -5 or x == 3:
        x = float(input('Введіть число x: '))
    else:
        break
def fact(y):
  if y == 0:
    return 1
  else:
    return y * fact(y-1)

def sqrt (number):
    Epsilon = 0.0001
    while number <= 0:
        if number == 0:
            return 0
        elif number < 0:
            print("Помилка ОДЗ! Кореня з від'ємного числа не існує!")
            break
    b = number
    xn = 1
    while abs(b - xn) >= Epsilon:
        b = xn
        xn = 0.5*(xn+(number/xn))
    b = round(b, 4)
    return(b)
result = sqrt(25-x**2) + (fact(7)*a)/(x-3)
print(result)