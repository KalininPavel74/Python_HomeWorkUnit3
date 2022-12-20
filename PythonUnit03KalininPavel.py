# Калинин Павел 19.12.2022 
# Знакомство с языком Python (семинары) 
# Урок 3. 
# Домашняя работа

import random

taskName = '''Задание  №1.
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.           
           '''
"""
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    N = int(input('Введите кол-во эл. списка - натуральное число: '))
    #N = random.randint(1,6)
    list1 = list(map(lambda n: random.randint(0,10), range(N)))
    print("Задан список:")
    print(list1)
    sum = 0
    for i,v in enumerate(list1):
        if i%2:
            sum+=v
    #--------------
    print('Ответ:')
    print(sum)
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------

taskName = '''Задание  №2.
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
           '''
"""
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    N = int(input('Введите кол-во эл. списка - натуральное число: '))
    #N = random.randint(2,6)
    list1 = list(map(lambda n: random.randint(0,10), range(N)))
    print("Задан список:")
    print(list1)
    half = len(list1)//2
    list2 = [list1[i]*list1[-(i+1)] for i in range(half)]
    #--------------
    print('Ответ:')
    print(list2)
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------

taskName = '''Задание  №3.
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.
           '''
"""
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    N = int(input('Введите кол-во эл. списка - натуральное число: '))
    #N = random.randint(1,6)
    list1 = list(map(lambda n: round(10 * random.random(), 2), range(N if N else 1)))
    print("Задан список:")
    print(list1)
    list2 = list(map(lambda n: n-int(n), list1))
    #--------------
    print('Ответ:')
    print(round(max(list2)-min(list2),2))
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------

taskName = '''Задание  №4.
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
           '''
"""
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    a10 = int(input('Введите целое десятичное число: '))
    #--------------
    print('Ответ:')
    print(bin(a10).replace('0b',''))
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------

taskName = '''Задание  №5.
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
           '''
"""
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
def fibonacci_bidirectional_generator(qty_elem, negative=False):
    if qty_elem >= 1:
        yield 0
        if qty_elem >= 2:
            yield 1
            if qty_elem >= 3:
                n1, n2 = (0, 1)
                i = 2
                while i < qty_elem:
                    n3 = n1 + n2 * (-1 if negative else 1)
                    yield n3
                    n1,n2 = n2,n3
                    i += 1

isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    N = int(input('Введите кол-во эл. Фибоначи положительной части - натуральное число: '))
    list_positive = [i for i in fibonacci_bidirectional_generator(N)]
    list_negative = [i for i in fibonacci_bidirectional_generator(N, negative = True)]
    list_negative.reverse()
    #--------------
    print('Ответ:')
    print(list_negative+list_positive[1:])
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------
