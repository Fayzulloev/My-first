

#age = 26
#name = 'Swaroop'
#print('Возраст {0} -- {1} лет'.format(name, age))
#print('Почему {0} даваляется с этим Python?' .format(name))

#a = '{0:_^110}'.format('hello')
#print(a)

#s = '''Это многострочная строка. это третая строчка'''
#print(s)

#i = 1; print(i)

#a = 2; a = a * 3
#print(a)

#a = 5
#b = 2
#c = a * b
#print('Площадь равна', c)
#print('Периметр равен', 2*(a+b))

""" number = 23 
running = True

while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
        break
else:
    print('Цикл while закончен.')
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.') """


""" for i in list(range(1,10,2)):
    print(i)
else:
    print('Цико for закончен')

 """
""" 
while True:
    s = input('Введите что-нибудь : ') 
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')
 """
""" 
while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины') # Разные другие действия здесь...
 """
""" 
def sayHello():
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции
sayHello() # вызов функции 
sayHello() # ещё один вызов функции
 """

""" 
def printMax(a, b): 
    if a > b:
        print(a, 'максимально') 
    elif a == b:
        print(a, 'равно', b) 
    else:
        print(b, 'максимально')

printMax(3, 4) # прямая передача значений

x = 5 
y = 7

printMax(x, y) # передача переменных в качестве аргументов
 """
""" 
x = 50

def func(x):
    print('x равен', x)
    x=2
    print('Замена локального x на', x)

func(x)
print('x по-прежнему', x)
 """
""" 
x = 50

def func():
    global x
    print('x равно', x)
    x=2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)
 """

""" 
def func_outer(): 
    x=2
    print('x равно', x)

    def func_inner(): 
        nonlocal x
        x=5 

    func_inner()
    print('Локальное x сменилось на', x)
func_outer()
 """
""" 
def say(message, times = 1):
    print(message * times)

say('Привет')
say('Мир ', 5)
 """
""" 
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
 """
""" 
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #проход по всем элементам кортежа
    for single_item in numbers: print('single_item', single_item)
        #проход по всем элементам словаря
    for first_part, second_part in phonebook.items(): print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
 """
""" 
def total(initial=5, *numbers, extra_number): 
    count = initial
    for number in numbers: 
        count += number
    count += extra_number
    print(count)

total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)

# Вызовет ошибку, поскольку мы не указали значение # аргумента по умолчанию для 'extra_number'.
 """

""" 
#!/usr/bin/python
# Filename: func_return.py
def maximum(x, y): 
    if x > y:
        return x 
    elif x == y:
        return 'Числа равны.' 
    else:
        return y 
print(maximum(2, 3))
 """
""" 
def printMax(x, y):
#Выводит максимальное из двух чисел.

#Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно 
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)
 """

""" import sys
print('Аргументы командной строки:') 

for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
 """
""" 
import os; print(os.getcwd()) """
""" 
from math import *

n = int(input("Введите диапазон:- ")) 
p = [2, 3]
count = 2
a=5
while (count < n):
    b=0
    for i in range(2,a):
        if ( i <= sqrt(a)): 
            if (a % i == 0):
                print(a,"непростое")
                b=1 
            else:
                pass
    if (b != 1): 
        print(a,"простое") 
        p = p + [a]
    count = count + 1
    a = a + 2 
print(p)
 """
""" 
if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
 """
""" 
def sayhi():
    print('Привет! Это говорит мой модуль.')

__version__ = '0.1'
sayhi()
# Конец модуля mymodule.py  
 """
 """
import mymodule
mymodule.sayhi()
print ('Версия', mymodule.__version__)
"""














