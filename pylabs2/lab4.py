#Introduction to programming: Task 3
#Tsadzikidze Arsen, FB-24, 26
print('Introduction to programming: Task 3')
print('Tsadzikidze Arsen, FB-24, 26')
#Використовуючи стек, написати перевірку правильності розстановки дужок ({, (, [ ), у
#деякому рядку. Наприклад “ab(cd{ef}gh[j])”

def is_balanced(string):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return False
    return not stack

# Приклад використання:
string = "ab(cd{ef}gh[j])"
if is_balanced(string):
    print(f"Рядок {string} містить правильні дужки")
else:
    print(f"Рядок {string} містить неправильні дужки")