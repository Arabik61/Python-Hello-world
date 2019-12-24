import random


def calculate():
    suma = sum(arr)
    return {'sum': suma, 'avg': suma / len(arr)}


if __name__ == '__main__':
    arr = [random.randint(0, 10) for i in range(int(input("Введіть кількість елементів списку: ")))]
    print(arr)
    print(calculate())
