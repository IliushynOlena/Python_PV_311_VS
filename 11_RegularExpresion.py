import re
import random


str_1 = '123'
str_2 = '234'
str_3 = "Lorem 21 ipsum red"
str_4 = "Lorem 2.1 ipsum red 3.14"

# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('1',str_1))
# print('\t',str_2,'--->', re.search('1',str_2))
# print('\t',str_3,'--->', re.search('1',str_3))

# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('12',str_1))
# print('\t',str_2,'--->', re.search('12',str_2))
# print('\t',str_3,'--->', re.search('12',str_3))
# print('\t',str_3,'--->', re.search('red',str_3))

# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[12]',str_1))
# print('\t',str_2,'--->', re.search('[12]',str_2))
# print('\t',str_3,'--->', re.search('[12]',str_3))
# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[1-9]',str_1))
# print('\t',str_2,'--->', re.search('[1-5]',str_2))
# print('\t',str_3,'--->', re.search('[a-zA-Z]',str_3))

# match = re.search('[1-9]',str_1)
# if match:
#     print("Find numbers")
# else:
#     print("numbers not found")
    
# match = re.search('[a-zA-Z]',str_3)
# if match:
#     print("Find letters")
# else:
#     print("letters not found")
    
# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[1-9]{5}',str_1))
# print('\t',str_2,'--->', re.search('[1-5]{3}',str_2))
# print('\t',str_3,'--->', re.search('[a-zA-Z]{5}',str_3))

# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[1-9]+',str_1))
# print('\t',str_2,'--->', re.search('[1-5]+',str_2))
# print('\t',str_3,'--->', re.search('[a-zA-Z]+',str_3))

# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[1-9]*',str_1))
# print('\t',str_2,'--->', re.search('[1-5]*',str_2))
# print('\t',str_3,'--->', re.search('[a-zA-Z]*',str_3))
# print("================= re.search()======================")
# print('\t',str_1,'--->', re.search('[1-9]{3}\W',str_1))
# print('\t',str_2,'--->', re.search('[1-5]{3}\d',str_2))
# print('\t',str_3,'--->', re.search('[a-zA-Z]{3}$',str_3))

# print('\t',str_3,'--->', re.search('^\w+',str_3).group())

# print('\t',str_3,'--->', re.search('^[Lorem]',str_3).group(0))


print('\t',str_3,'--->', re.findall(r'\w+',str_3))
first_word =  re.findall(r'\w+',str_3)[0]
print(first_word)
print('\t',str_3,'--->', re.findall(r'\w+',str_3)[0])
print('\t',str_3,'--->', re.findall(r'\w+',str_3)[1])
print('\t',str_3,'--->', re.findall(r'\w+',str_3)[2])
print('\t',str_3,'--->', re.findall(r'\w+',str_3)[3])

match = re.findall(r'\w+',str_3)

for item in match:
    print(item)

print('\t',str_3,'--->', re.sub(r'\w+','yellow',str_3))
print('\t',str_3,'--->', re.sub(r'\d+','yellow',str_3))

print('\t',str_4,'--->', re.findall(r'\d+\.\d+|\d+\,\d+',str_4))




