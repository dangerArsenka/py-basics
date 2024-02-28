#1.Выведите на печать вторую букву l из строки 'Hello Python!'.Присвойте строку переменной, затем выведите на печать букву

greeting = 'Hello Python!'
print(greeting[3])

#2.Выведите на печать вторую букву l из строки 'Hello Python!'. Сделайте это без присваивания строки переменной, в одной строке кода.
# Если не знаете, как это сделать, попробуйте погуглить

print('Hello Python!'[3])

#3. Выведите на печать 'He' из строки 'Hello Python!' минимум двумя способами

#First variant
greeting = 'Hello Python'
print(greeting[0:2])

#Second variant
print('Hello Python' [0:2])

#Other variants
greeting = 'Hello Python!'
print(greeting[:2])
print(greeting[-13:-11])
print(greeting[0:2:1])
print(greeting[:2:1])
print(greeting[-13:-11:1])

#4. Создайте новую строку 'Path' из строки 'Hello Python!' путём конкатенации части строки и отсутствующего символа.
# Выведите новую строку на печать

greeting = 'Hello Python!'
new_word = greeting[6] + 'a' + greeting[8] + greeting[9]
print(new_word)