# Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, що складаються не менше, ніж із семи літер.
url = r"./write.txt"
url2 = r"./my2.txt"

def filter_leater_word(url, url2):
    with open(url, 'r') as file:
        with open(url2, 'w') as f_out:
            for line in file:
                words = line.split()
                filtered_words = [word for word in words if len(word) >= 7]
                if filtered_words:
                    f_out.write(" ".join(filtered_words) + "\n")


print()
filter_leater_word(url, url2)



# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має збігатися з порядком рядків у заданому файлі. 

# url = r"G:\Python\file_homework\my.txt"
# url2 = r"G:\Python\file_homework\my2.txt"

# def copy_file(url, url2):
#     with open(url, 'r') as source:
#         with open(url2, 'w') as test:
#             for line in source:
#                 test.write(line)
                
# copy_file(url, url2)


# Завдання 3
# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має бути зворотним до порядку рядків у заданому файлі.

# url = r"G:\Python\file_homework\my.txt"
# url2 = r"G:\Python\file_homework\my2.txt"



# def reverse(url, url2):
#     with open(url, 'r') as test:
#         lines = test.readlines()

#     
# 
#     with open(url, 'w') as dest:
#         for line in reversed(lines):
#             dest.write(line)
            
# reverse(url,url2)

# Завдання 4
# Маємо текстовий файл. Додайте до нього рядок із дванадцяти зірочок (************), помістивши його після останнього з рядків, 
# в яких немає коми. Якщо таких рядків немає, додайте новий після всіх рядків файлу. Результат запишіть до іншого файлу.

# url = r"G:\Python\file_homework\my.txt"
# url2 = r"G:\Python\file_homework\my2.txt"


# def sumbol(url, url2):
#     with open(url, 'r') as sumbol_index:
#         lines = sumbol_index.readlines()
#     index_sumbol = None
#     for i, line in enumerate(lines):
#         if ',' not in line:
#             index_sumbol = i

#     with open(url2, 'w') as sumbol_in:
#         for i, line in enumerate(lines):
#             sumbol_in.write(line)
#             if i == index_sumbol:
#                 sumbol_in.write("************\n")
#         if index_sumbol is None:
#             sumbol_in.write("************\n")
            
# sumbol(url, url2)

# Маємо текстовий файл. Перепишіть до іншого файлу всі його рядки замінюючи в них символ * на символ &, і навпаки. 
# url = r"G:\Python\file_homework\my.txt"
# url2 = r"G:\Python\file_homework\my2.txt"

# def replace(url, url2):
#     with open(url, 'r') as r_in_file:
#         with open(url2, 'w') as f_out:
#             for line in r_in_file:
#                 new_line = line.replace('*', '&').replace('&', '*')
#                 f_out.write(new_line)
                
# replace(url,url2)



# Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку. 

# url2 = r"G:\Python\file_homework\my2.txt"

# def test(list, url2):
#     with open(url2, 'w') as f:
#         for element in list:
#             f.write(str(element) + '\n')


# list = ['one', 'twy', 'three', 'four', 'five']

# test(list, url2)


# Маємо текстовий файл. Підрахуйте кількість символів у ньому. 

# url = r"G:\Python\file_homework\my.txt"


# def count_leater(url):
#     with open(url, 'r') as file:
#         content = file.read()
#         sumbol_count = len(content)
#     return sumbol_count

# res = count_leater(url)
# print("Count sumbol in file:", res)


# Маємо текстовий файл. Підрахуйте кількість рядків у ньому.

# url = r"G:\Python\file_homework\my.txt"


# def count_line(url):
#     with open(url, 'r') as file:
#         lines = file.readlines()
#         line_count = len(lines)
#     return line_count

# res = count_line(url)
# print("Count line in file:", res)