#1. Создайте новую строку 'Path' из строки 'Hello Python!'
#путём конкатенации частей строки и отсутствующего символа. Выведите новую строку на печать

phrase = 'Hello Python!'
first_letter = phrase[6]
other_letters = phrase[-5:-3]
new_phrase = first_letter + 'a' + other_letters
print(new_phrase)

#2. Создайте строку 'zzzzzzz' при помощи умножения и выведите её на экран

one_letter = 'z'
print(one_letter * 7)

#3. Сделайте все буквы строки из предыдущего вопроса заглавными и выведите её на экран

#Первый способ
one_letter = 'z'
print(one_letter.upper() * 7)

#Второй способ
one_letter = 'z'
big_letters = one_letter.upper() * 7
print(big_letters)