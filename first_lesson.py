
# 1. \n
# 2. \t - 4..8
# 2. \" 
# 2. \\ 
 
# print('\tHello\n\t\tword ')
# print('\t\t\tword ')

# print("I love \"Python\"")
# print("I love \\Python\\")
# print("I love 'Python'")
# print('''
#       I love 'Python' 
#            I love 'Python'
#                  I love 'Python'      
#       ''')



# line_1 = "Hyper"#string
# line_2 = "Text"#string
# line_3 = "Markup"#string
# line_4 = "Language"#string

# message = line_1+ " " + line_2+" " + line_3+" " + line_4#string
# print("="*30)
# print(message*3)
# print("======================================")
# #print("\033[31m",line_1)
# print("\033[31m\033[47m\033[1m{}\033[0m".format(line_1), end=" ")
# print("\033[32m\033[46m\033[2m{}\033[0m".format(line_2),end=" ")
# print("\033[33m\033[45m\033[3m{}\033[0m".format(line_3),end=" ")
# print("\033[34m\033[44m\033[4m{}\033[0m".format(line_4),end=" ")

# print(978//100)
# print(978%100)
''' 
import math
print(math.ceil(2.5)) # ceil(2.5) ≈ 3
print(math.floor(2.5)) # floor(2.5) ≈ 2
print(math.pow(2, 4)) # pow(2, 4) = 2*2*2*2 = 16.0
print(math.sqrt(16)) # sqrt(16) = 4*4 = 4.0
'''
# calculate
import math
price_1 = 270
price_2 = 200
gramm = int(input("Enter weight (gramm): "))
kg = gramm / 1000
print("Your weight: {} kg".format(kg))
if (kg<0.5):
     total = kg * price_1
else:
     total = kg * price_2
total = math.ceil(total)
print("Your total: {} coin".format(total))
# import random
# print(random.random()) # 0.4956579385740163
# print(random.randint(0, 1)) # 0
# print(random.randint(1, 100)) # 66
# print(random.randint(10, 20)) # 16

'''
a = 7
b = 8
c = 5

a = 7
b = 8
c = 5
print(a , b, c)
print("Numbers : a = {}".format(a))
print("Numbers : a = {}. b = {}. c = {}".format(a,b,c))
print(f"Numbers : a = {a}, b = {b}, c = {c}")
value = "load"
match value:
      case "load":
           print("A")
      case "save":
           print("C")
      case _:
           print("X")
           
'''




