
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без
# повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их
# пересечение)

import random


n = int(input('введите количество элементов первого множества '))
m = int(input('введите количество элементов второго множества '))
n_min = int(input('введите мин элемент первого множества'))
n_max = int(input('введите макс элемент первого множества'))
m_min = int(input('введите мин элемент второго множества'))
m_max = int(input('введите макс элемент второго множества'))
array_n = [random.randint(n_min, n_max) for i in range(n)]
array_m = [random.randint(m_min, m_max)  for i in range(m)]
print(array_n)
print(array_m)
print(*set(array_n).intersection(array_m))




