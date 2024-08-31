# ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.
# ответ
# я знаю не сколько методов, в datetime например есть матод strptime, strftime, date, days, now, time, years timedelta и другие в randome их тоже много например randint, choice, choices, randome, sample

# ### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.

# ответ
# я знаю методы with, open, close, read, write, readline, readlines и другие
# 
# ### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.
# ответ 
# Github это платформа для работы с версиями вашей программы внем есть все версии вашей програми с которомы вы можете работать изменять и можете работать совместно с другимм разработчиками можно назвать основой приложенение стволом дерева а вещи которые разработчки добовляют ветвями

# у гит хаба есть множество команд например git init для создания паки гита в вашем проекте и связывает его с гитом, git add добовляет выбранный  файл в ваш гит папку, git commit -m  для создания коментарий про этот файл git brench для создания новой ветви вашей программы git remote add origin  для связывании вашего проекта с вашим репостом git push для отправки ваших фалов в ваш репостр
# 
# ### 1 Question
# Write a Python program to insert an ient at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]
# # input
#     Enter an element: Sorbon
#     Index: 3
# # output
#     [1, 1, 2, "Sorbon", 3, 4, 4, 5, 1]

# a = input("Enter an element: ")
# b = int(input("Index: "))
# lict = [1, 2, 3, 4, 5, 6]
# lict.insert(b, a)
# print(lict)

# ### 2 Question
# Write program to print 2 days before, today, 2 days after / Напишите программу для печати позавчера, сегодня, послезавтра. / Барномаи нависед, то пареррӯз, имрӯз, фардои дигарро чоп кунад 

# from datetime import datetime, timedelta
# now1 = datetime.now()
# dt = now1 - timedelta(days=2)
# ht = now1 + timedelta(days=2)
# print("Позавчера:", dt.date())
# print("Сегодня:", now1.date())
# print("Послезавтра:", ht.date())

# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.
# from datetime import datetime, timedelta
# now1 = datetime.now()
# dt = now1 - timedelta(days=5)
# print(dt.strftime('%Y.%m.%d'))


# ### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 

# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10

# def sum_of_vowels(santence):
#     dict = {
#         "A": 4,
#         "E": 3,
#         "I": 1,
#         "O": 0,
#         "U": 0
#     }
#     cnt = 0
#     for i in santence.upper():
#         if i in dict:
#             cnt += dict[i]
#     return cnt
# print(sum_of_vowels(input()))

# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# # input
#     3
# # otput
#     Tajikistan

# n = int(input())
# with open("filee1.txt", 'r') as file:
#     lin = file.readlines()
#     print(lin[n - 1].strip())


# ### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 
# n = input()
# with open("filee2.txt", 'r') as file:
#     lin = file.readlines()
# for i in range(1, len(lin)):
#     if i % 2 != 0:
#         lin[i-1] = n  
# with open("filee2.txt", 'w') as file:
#     for line in lin: 
#         file.write(line+"\n")
    

# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5
# import random
# lict = ['qwertyuiopasdfghjkl;\'zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+*=-']
# n = int(input("Enter the desired password length: "))
# d = ""
# for i in range(n): 
#     s = random.choice(lict[0])
#     d += s
# print(f"Generated password: {d}")

# ### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# n = int(input())
# dicti={}
# for i in range (1,n+1):
#     dicti.update({i:i*i})
# print(dicti)


# ### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical. Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.

# Input       
# char_appears("She sells sea shells by the seashore.", "s")

# Output
# [1, 2, 1, 2, 0, 0, 2]
# a = input()
# sim = input()
# lict = a.split()
# cnt = 0
# lst = []
# for i in lict:
#     cnt = 0
#     for j in str(i).lower():
#         if j == sim:
#             cnt+=1
#     lst.append(cnt)
# print(lst)

# ### 10 Task
# Given a list of elements of any data types. Create a Python program to separate elements by their types and save them into a new dictionary.
# The keys of a dictionary must be of a data type, and its element must be data belonging to that type.
# Дан список элементов любых типов данных. Создайте программу Python для разделения элементов по их типам и сохранения их в новый словарь.
# Ключи словаря должны иметь тип данных, а его элементом должны быть данные, принадлежащие этому типу.
# # input
#     1 hello True 12 Muhammad
# # output
#     {"int": [1,12], "str": ["hello", "Muhammad"], "bool": [True]}

# n = input()
# dicti = {}
# lict = n.split()
# for i in lict:
#     if i.isdigit() or (i[0] == '-' and i[1:].isdigit()): 
#         key = int(i)

#         if 'int' not in dicti:
#             dicti['int'] = []
#         dicti['int'].append(key)
#     elif i.lower() == 'true' or i.lower() == 'false': 
#         key = i.lower() == 'true'
#         if 'bool' not in dicti:
#             dicti['bool'] = []
#         dicti['bool'].append(key)
#     elif str(i) == i: 
#         if 'str' not in dicti:
#             dicti['str'] = []
#         dicti['str'].append(i)
# print(dicti)