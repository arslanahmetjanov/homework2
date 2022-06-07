#1 Выведите все символы из строки «Программисты — не волшебники, способные вернуть удалённые в прошлом году фотографии, взломать за 5 секунд любой сайт и
# починить микроволновку. Но именно эти люди создают то пространство, где и появляются мемы про них», значения индексов которых делятся на 10.
s = "Программисты — не волшебники, способные вернуть удалённые в прошлом году фотографии, взломать за 5 секунд любой сайт и починить микроволновку." 
+ " Но именно эти люди создают то пространство, где и появляются мемы про них"
for i in range(len(s)):
    if i % 10 == 0:
        print(s[i])
        

#2 Напишите скрипт по проверки условия: если число больше 20 и меньше 40 - вывести “YES”, иначе “NO”.
i = input("Вводи число: ")
if i.isdigit() != True:
    print("Ну, попросил же :(")
    while i.isdigit() != True:
        i = input("Не балуйся! Вводи число:")
        
i = int(i)

if i > 20 and i < 40:
    print("YES")
else:
    print("NO")

#3 Выведите числа из диапазона от 1 до 10 двумя способами, используя циклы for и while.
for i in range(1,11):
    print(i)
    
j = 1
while j != 11:
    print(j)
    j += 1

#4 Посчитайте количество вхождений элемента со значением «3» тремя способами в сле­дующем списке: [3 0 1 3 0 4 3 3 4 5 6 6 1 3], 
# используя цикл for, while и метод count.
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
c = 0
for i in lst:
    if i == 3:
        c += 1
print("1 -", c)

c = 0
j = 0
while len(lst) > 0:
    if j < len(lst):
        if lst[j] == 3:
            c += 1
        j += 1
    else:
        break
print("2 -",c)

c = lst.count(3)
print("3 -",c)

#5 Напишите программу, выводящую среднее из десяти значений.
def average_count(some_structure):
    if (type(some_structure) == list or type(some_structure) == set or type(some_structure) == tuple):
        rslt = sum(some_structure) / len(some_structure)
        return rslt
    elif (type(some_structure) == dict):
        counter_sum = 0
        for i in some_structure:
            counter_sum += some_structure[i]
        rslt = counter_sum / len(some_structure)
        return rslt
    else:
        return("Ошибка в типах данных параметров. Параметр может быть списком, множеством, кортежом или словарем")


#6 Выведите числа из диапазона от -20 до 20 с шагом 3 двумя способами, используя цикл for и while.
for i in range (-20, 21, 3):
    print(i)


j = -20
while j <= 20:
    print(j)
    j += 3

#7 Напишите программу, которая считывает целое число (месяц), после чего выводит сезон к которому этот месяц относится.
i = int(input("Введи номер месяца: "))

if i >= 3 and i <= 5:
    print("весна")
elif i >= 6 and i <= 8:
    print("лето")
elif i >= 9 and i <= 11:
    print("осень")
elif i > 0 and (i <= 2 or i <= 12):
    print("зима")
else:
    print("В году 12 месяцев :)")

#8 Напишите функцию, вычисляющую максимальное из трех чисел. Два вызова функции.
def max(a, b, c):
    if (type(a) == int and type(b) == int and type(c) == int):
        if (a >= b and a >= c):
            return a
        elif (b >= a and b >= c):
            return b
        elif (c >= a and c >= b):
            return c
    else:
        return "Ошибка в типах данных параметров. Параметры - цифры в виде (1, 2, 3)"
        
print(max(1, 2, 3))

print(max([1,2,3], "a", 1))

#9 Напишите функцию, которая возвращает инвертированную строку, передаваемую ей на вход.
s = input("Введите строку: ")
f = lambda x: x[::-1]
print(f(s))

#10 Напишите функцию для вычисления факториала задаваемого числа. Два вызова функции.
def factorial_count(n):
    if (type(n) == int and n > 0):
        if n == 1:
            return 1
        return factorial_count(n - 1) * n
    else:
        return "Ошибка в типе данных параметра. Параметр - число"

print(factorial_count(5))
print(factorial_count("1"))

#11 Напишите функцию, удаляющую повторяющиеся элементы в списке. Три вызова функции.
def unique_list(l):
    if (type(l) == list):
        t = [] 
        t = list(set(l))
    else:
        return "Ошибка в типе данных параметра. Параметр - список"

l= [1, 2, 3, 4, 3, 2, 1, 2, 6, 6, 0, 1, 2]

print(unique_list(l))
print(unique_list('123'))
print(set(l))

#12 Напишите функцию, которая проверяет, является ли строка палин­дромом (читается одинаково как слева направо, так и наоборот). 
# Два вызова функции (с палиндромом и нет).
def check_palindrom(s1): 
    if (type(s1) == str):
        f = lambda s: s[::-1]
        s2 = f(s1)
        if s1 == s2:
            return True
        else:
            return False
    else:
        return "Ошибка в типе данных параметра. Параметр - список"
        
print(check_palindrom("оно"))
print(check_palindrom("она"))

#13 Декорируйте функцию из 8 задания таким образом, чтобы возвращаемое ей значение возводилось в квадрат.
def squaring_decorator(function):
    def wrapper(a, b, c):
        func = function(a, b, c)
        make_squaring = func ** 2
        return make_squaring
    return wrapper

@squaring_decorator
def max_count(a, b, c):
    if (type(a) == int and type(b) == int and type(c) == int):
        if (a >= b and a >= c):
            return a
        elif (b >= a and b >= c):
            return b
        elif (c >= a and c >= b):
            return c
    else:
        return "Ошибка в типах данных параметров. Параметры - цифры в виде (1, 2, 3)"


#14 Декорируйте функцию из 9 задания таким образом, чтобы возвращалась строка в верхнем регистре.
def uppercase_decorator(function):
    def wrapper(some_str):
        func = function(some_str)
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
    
@uppercase_decorator
def custom_invert_str(some_str):
    if (type(some_str) == str):
        return some_str[::-1]
    else:
        return "Ошибка в типе данных параметра. Параметр - строка"

