# 1. Используйте цикл for для вычисления суммы всех чётных чисел 
# в диапазоне от 10 до 30 (включая крайние значения). 
# Выведите результат на печать

sum = 0
for number in range(10,31):
    if number % 2 == 0:
        sum = sum + number
print(sum)

# Вторая реализация
even_numbers_sum = 0
for number in range(10, 31):
    if number % 2 == 0:
        even_numbers_sum += number

print(even_numbers_sum)

# 2. Получите от пользователя число на вводе 
# и используйте цикл for для вывода на экран текста 'Hello!' столько же раз

num = int(input('Введите число: '))
for i in range(num):
    print('Hello!')