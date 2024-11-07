"""
list = [1, 2, 3, 4, 5]

#wtf is this?

lists = [1, 2, 3, 4, 5]
if type(lists) is list:
    print ('true')
else:
    print ('this is no int')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
income = float(input('Enter your income: '))

print ('Your name: ', name)
print ('Your age: ', age)
print ('Your income: ', income)
print ()

all_seconds = float (input('Enter number of seconds: '))

hours = all_seconds // 3600
minutes = all_seconds // 60 % 60
seconds = all_seconds % 60

print(hours, minutes, seconds)


future_value = float(input('Enter value: '))

rate = float(input('Enter rate: '))

years = int(input('Enter years: '))

present_value = future_value / (1.0 + rate)**years

print ('Now you must deposit:', present_value)

result = '1' + '2'
print (result, sep='^')
result = 'п' 'р' 'и' 'в' 'е' 'т'
print (result)
print ('one\ntwo\nthree')

temperature = 45
print (f'Now {temperature + 3} degrees')

# importing the module 


from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=vLLmpVG3QJw")
yt = yt.get('mp4', '720p')
yt.download('D:/')
"""

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)
"""
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

n = int(input())
if n <= -3 or n >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')


# put your python code here
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < n2 and n2 < n3:
    print(n2)
elif n2 < n1 and n2 < n1:
    print(n2)
else:
    print(n3)

n = int(input())
if 1 <= n <= 10:
    if n < 4:
        print(n * 'I')


from math import *
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = (x1 - x2) ** 2 - (y1 - y2) ** 2
print(sqrt(p))


a = float(input())
b = float(input())
print((a + b) / 2)
print(sqrt(a * b))
print(2 * a * b / (a + b))
print(sqrt((a ** 2 + b ** 2) / 2))


from math import *

n = radians(float(input()))

print(sin(n) + cos(n) + (tan(n)) ** 2)
"""

# from math import sqrt
# a = float(input())
# b = float(input())
# c = float(input())

# if b ** 2 - 4 * a * c > 0:
#     x1 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     x2 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     print(min(x1, x2), max(x1, x2), sep='\n')
# elif b ** 2 - 4 * a * c == 0:
#     x1 = (-1 * b) / (2 * a)
#     print(x1)
# else:
#     print("Нет корней")

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# n = int(input())
# a, b = 1, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b
# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)
# n = int(input())
# count = 0
# while n >= 25:
#     count += 1
#     n = n - 25
# while n >= 10:
#     count += 1
#     n = n - 10
# while n >= 5:
#     count += 1
#     n = n - 5
# while n >= 1:
#     count += 1
#     n = n - 1
# print(count)
# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)
# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# num = int(input())
# flag = True

# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
#         break
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i):
#         print(j, end="")

#     print(i, end="")

#     for j in range(i - 1, 0, -1):
#         print(j, end="")

#     print()


# s = input()
# for i in range(-1, -len(s)-1, -1):
#     print(s[i])

# s = input()
# count = 0
# for i in range (len(s)-1):
#     if s[i] == s[i+1]:
#         count += 1
# print(count)

# import string

# str = 'pmppmt 12312 3tm tmt  m 123 12asddsa'
# str = str.replace(' ', '')
# print(''.join(sorted(set(str), key=str.index)))


# string = "Good morning, good afternoon!  12"
# print(len(string.split()))

# s = 'i LEARN Python LAnguaGE'
# print(s.swapcase())

# s = 'www.stepik.org'
# print(s.startswith('www'))

# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))

# s = '     I learn Python language               '
# print(s.strip())

# s = 'abcdababa'
# print(s.replace('ab', '123'))

# age = 27
# txt = 'My name is Timur, I am {}'.format(age)
# print(txt)

# first_name = 'Timur'
# last_name = 'Guev'
# age = 27
# profession = 'math teacher'
# affiliation = 'BeeGeek'
# print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')

# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# s = input()
# temp = 0
# if s.count('f') > 1:
#     temp = s.find('f')
#     s = s[temp+1:]
#     print(s.find('f') + temp + 1)
# elif s.count('f') == 1:
#     print(-1)
# else:
#     print(-2)

# s = "127 руб. 25 коп."
# s1 = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         s1 += s[i]

# print(float(s1) / 100)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# print(numbers[1:-1])


# l = [1, 1, 2, 3, 3, 5, 5]
# print(list(set(l)))

# ints_list = [1, 2, 3, 4, 3, 2]
# temp = []
# for x in ints_list:
#     if x not in temp:
#         temp.append(x)
# ints_list = temp
# print(f'{temp}')

# import calendar
# a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
# with open('calendar.html', 'w') as g:
#     print(a.formatyear(2014, width=4), file=g)

# import calendar
# yy = 2023

# # display the calendar
# print(calendar.calendar(yy))

# n = int(input())
# list1 = []
# list2 = []
# count = 0
# for i in range(n):
#     list1.append(input())
# k = int(input())
# for i in range(k):
#     list2.append(input())

# for i in range(n):
#     count = 0
#     for j in range(k):
#         if list2[j].lower() in list1[i].lower():
#             count += 1
#     if count == k:
#         print(list1[i])


# for a in range(1, 100):
#     for c in range(1, a):
#         for d in range(1, c):
#             for b in range(1, d):
#                 if a ** 3 + b ** 3 == c ** 3 + d ** 3:
#                     print(a, b, c, d)


# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# s = input().split()
# s.sort(key=int)
# print(*s, sep=' ')
# s.sort(key=int, reverse=True)
# print(*s, sep=' ')

# chars = [c for c in 'abcdefg']
# print(chars)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i[1:] for i in keywords]

# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i for i in keywords if len(i) > 4]

# print(new_keywords)

# palindromes = [int(i) for i in range(100, 1000) if str(i) == str(i) [::-1]]

# print(palindromes)

# [print(s) for s in input().split()]

# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)

# n = 5
# m = 7
# draw_box(n, m)
# print(n, m)

# def merge(list1, list2):
#     return sorted(list1 + list2)

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merge(n):
#     total = []
#     for i in range(n):
#         num = [int(q) for q in input().split()]
#         total += num
#     return sorted(total)
# # вызываем функцию
# print(*quick_merge(int(input())))

# def is_prime(cur_num):
#     if cur_num == 1:
#         return False
#     for i in range(2, int(cur_num ** 0.5 + 1)):
#         if cur_num % i == 0:
#             return False
#     else:
#         return True

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))

# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num ** 0.5 + 1)):
#         if num % i == 0:
#             return False
#     else:
#         return True

# def get_next_prime(num):
#     if is_prime(num + 1) == False:
#         num+=1
#     return num

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))

# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     if password.isupper() or password.islower() or password.isalpha() or password.isdigit():
#         return False

#     return True

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))

# def is_one_away(word1, word2):
#     result = False

#     if len(word1) == len(word2):
#         result = True
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] == word2[i]:
#             count += 1
#     if len(word1) - count == 1:
#         result = True
#     else:
#         result = False
#     return result

# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))

# def is_palindrome(text):
#     result = False
#     for i in text:
#         if i in '.,!?- ':
#             text = text.replace(i, '')
#     if text.lower() == text[::-1].lower():
#         result = True
#     return result
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_palindrome(txt))

# # объявление функции
# def is_prime(cur_num):
#     if cur_num == 1:
#         return False
#     for i in range(2, int(cur_num ** 0.5 + 1)):
#         if cur_num % i == 0:
#             return False
#     else:
#         return True

# def is_valid_password(password):
#     result = 0
#     password = password.split(':')
#     if password[0] == password[0][::-1] and int(password[2]) % 2 == 0 and len(password) == 3:
#         result += 2
#     if is_prime(int(password[1])):
#         result += 1
#     if result == 3:
#         return True
#     else:
#         return False
# # считываем данные
# psw = input()

# # вызываем функцию
# print(is_valid_password(psw))

# import math
# # объявление функции
# def solve(a, b, c):
#     if b ** 2 - 4 * a * c > 0:
#         x1 = (-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#         x2 = (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#         return x1, x2
#     elif b ** 2 - 4 * a * c == 0:
#         x1 = (-1 * b) / (2 * a)
#         return x1, x1

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# # объявление функции
# def number_to_words(num):
#     se = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     sd = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num < 10:
#         return se[num%10]
#     elif 9 < num < 20:
#         return se[num]
#     else:
#         return sd[num//10] + ' ' + se[num%10]
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))

# объявление функции
# def is_magic(date):
#     date = date.split('.')
#     if int(date[0]) * int(date[1]) == int(date[2][2:]):
#         return True
#     else:
#         return False
# # считываем данные
# date = input()

# # вызываем функцию
# print(is_magic(date))


# n, s = 4, 'Hawnj pk swhg xabkna ukq nqj.'
# for i in s:
#     if i.isalpha():
#         c = ('a', 'A')[i.isupper()]
#         print(chr(ord(c) + (ord(i) + n - ord(c)) % 26), end='')
#     else:
#         print(i, end='')

# # задача Иосифа Флавия(?)
# n = int(input())
# k = int(input())

# res = 0
# for i in range(1, n + 1):
#     res = (res + k) % i
# print(res + 1)

# s = input()
# print(s[::-1])

# word = input() + ' запретил букву '
# alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# for i in alpha:
#     if i in word:
#         word = word.replace(i, '').lstrip()
#         word = word.replace('  ', ' ').lstrip()
#         print(word + i)
#         if len(word) < 1:
#             break


# list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
# print(list1[0][1] + list1[1][2] + list1[2][2])

# list1 = [[1] * 3] * 3
# list1[0][1] = 5
# print(list1[1][1])

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

# maximum = my_list[0][0]
# minimum = my_list[0][0]

# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)

# print(maximum + minimum)

# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]

# maximum = -1
# minimum = 100

# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]

# print(minimum + maximum)
# import math


# def count_intersecting_cells(R):
#     intersecting_cells = 0
#     for x in range(0, int(R) + 1):
#         for y in range(0, int(R) + 1):
#             if math.sqrt(x**2 + y**2) <= R:
#                 intersecting_cells += 1
#         return intersecting_cells * 4


# R_values = [0.5, 1, 1.5, 2, 3]
# for R in R_values:
#     print(f"Для R = {R} количество пересекаемых ячеек: {count_intersecting_cells(R)}")

# import math


# def count_intersected_cells(R):
#     count = 0
#     for x in range(0, math.ceil(R)):
#         for y in range(0, math.ceil(R)):
#             if not (
#                 math.sqrt((x + 1) ** 2 + (y + 1) ** 2) <= R
#                 or math.sqrt(x**2 + y**2) >= R
#             ):
#                 count += 1
#     return count * 4


# # Примеры использования
# print(count_intersected_cells(0.5))  # Ожидаемый результат: 4
# print(count_intersected_cells(1))  # Ожидаемый результат: 4
# print(count_intersected_cells(1.5))  # Ожидаемый результат: 12
# print(count_intersected_cells(2))  # Ожидаемый результат: 12
# print(count_intersected_cells(3))  # Ожидаемый результат: 20
# print(count_intersected_cells(4))  # Ожидаемый результат: 28


# from math import radians
# import numpy as np  # installed with matplotlib
# import matplotlib.pyplot as plt


# def main():
#     x = np.arange(0, radians(400), radians(12))
#     plt.plot(x, np.cos(x), np.sin(x), "b")
#     plt.show()

# main()

############ КУРС ОТ ЯНДЕКС ОБРАЗОВАНИЯ (ОСНОВЫ PYTHON) ############

# name = input()
# price = int(input())
# weight = int(input())
# amount = int(input())
# print("Чек")
# print(name, "-", str(weight) + "кг -", str(price) + "руб/кг")
# print("Итого:", str(price * weight) + "руб")
# print("Внесено:", str(amount) + "руб")
# print("Сдача:", str(amount - price * weight) + "руб")

# N = int(input())
# string = input()
# print(f'Я больше никогда не буду писать "{string}"!\n' * N)

# name_child = input()
# number = int(input())
# print(f"Группа №{number // 100}.")
# print(str(number % 10) + ".", name_child + ".")
# print("Шкафчик:", str(number) + ".")
# print("Кроватка:", str(number // 10 % 10) + ".")

# number = int(input())
# print(
#     str(number // 100 % 10)
#     + str(number // 1000)
#     + str(number % 10)
#     + str(number // 10 % 10)
# )

# num1 = int(input())
# num2 = int(input())
# num_one = (num1 % 10 + num2 % 10) % 10
# num_two = (num1 // 10 % 10 + num2 // 10 % 10) % 10
# num_three = (num1 // 100 + num2 // 100) % 10
# print(str(num_three) + str(num_two) + str(num_one))

# num_child = int(input())
# candies = int(input())
# print(candies // num_child)
# print(candies % num_child)


# hours = int(input())
# minutes = int(input())
# lag = int(input())

# hours = (hours + (minutes + lag) // 60) % 24

# print(f"{hours:02d}:{(minutes + lag) % 60:02d}")

# warehouse = int(input())
# store = int(input())
# speed = int(input())
# print(f"{(store - warehouse) / speed:.2f}")

# summ = int(input())
# binary_sum = input()
# print(summ + int(binary_sum, 2))

# binary_sum = input()
# summ = int(input())
# print(summ - int(binary_sum, 2))

# name = input()
# price = int(input())
# weight = int(input())
# cash = int(input())

# price_string = str(weight) + "кг * " + str(price) + "руб/кг"
# sum_string = str(price * weight) + "руб"
# cash_string = str(cash) + "руб"
# change_string = str(cash - price * weight) + "руб"

# print("================Чек================")
# print(f"Товар: {name:>28}")
# print(f"Цена: {price_string:>29}")
# print(f"Итого: {sum_string:>28}")
# print(f"Внесено: {cash_string:>26}")
# print(f"Сдача: {change_string:>28}")
# print("===================================")

print(f"{123:0>9}")
print(f"{123:0<9}")
print(f"{123:0^9}")
print(f"{3:02d}")
