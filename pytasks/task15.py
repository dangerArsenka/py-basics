# 1. Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую букву из каждой 
# строки исходного списка. Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

# Первый способ реализации без использования List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
second_letters = []
for word in greetings:
    second_letters.append(word[1])
print(second_letters)

# Второй способ реализации с использованием List Comprehension
second_letters = [word[1] for word in greetings]
print(second_letters)

# 2. Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список 
# содержащий нечетные числа исходного списка. Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

# Первый способ реализации без использования List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = []
for num in digits:
    if num % 2 == 1:
        odd_nums.append(num)
print(odd_nums)

# Второй способ реализации с использованием List Comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = [num for num in digits if num % 2 == 1]
print(odd_nums)