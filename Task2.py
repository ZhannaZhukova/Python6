#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

num = int(input('Введите число: '))
result = lambda n: ((n == 1) and 1) or n * factorial(n - 1)
lst = [result(i) for i in range(1, num + 1)]
print(lst)