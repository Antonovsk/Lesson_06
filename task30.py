a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = []


for i in range(n):  
    an = a1 + i * d  
    progression.append(an)

print("Арифметическая прогрессия:", progression)