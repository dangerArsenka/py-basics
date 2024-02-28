#Introduction to programming': Task 7.1
#Tsadzikidze Arsen, FB-24, 29
print ("Introduction to programming: Task 7.1")
print ("Tsadzikidze Arsen, FB-24, 29")
l = []
def convert(b):
    if (b == 0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b // 2)
a = int(input("Введіть число: "))
convert(a)
l.reverse()
print("Двійкова система числення:")
for i in l:
    print(i)