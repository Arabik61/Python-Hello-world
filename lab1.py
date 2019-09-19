import random

list = []
size = int(input("Введіть кількість елементів списку: "))
i = 0
sum = 0

while i < size:
    list.append(random.randint(0,10))
    i += 1

for x in list:
    sum += x

print(list)
print("Сума елементів списку = " + str(sum))
print("Середнє значення елементів масиву = " + str(sum/size))
