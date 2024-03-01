# #Introduction to programming':Task 2
# #Tsadzikidze Arsen, FB-24, 26
# #2. Визначте, скільки разів зустрічається в деякому тексті кожне слово.
print('Introduction to programming:Task 2')
print('Tsadzikidze Arsen, 26')


text = input('Введіть текст і ви отримаєте слово, що зустрічається найчастіше:')
textl = text.lower()  # Перевів текст в нижній регістр, щоб програма коректно шукала однакові слова
words = textl.split()  # Розділив текст, щоб занести його до словника
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print('Словник який відображає скільки разів слово зустрілось:', word_count)





