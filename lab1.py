import random

arr = []
size = int(input("Введіть кількість елементів списку: "))
i = 0
sumArr = 0

while i < size:
    arr.append(random.randint(0, 10))
    i += 1

for x in arr:
    sumArr += x

print(arr)
print("Сума елементів списку = " + str(sumArr))
print("Середнє значення елементів масиву = " + str(sumArr/size))