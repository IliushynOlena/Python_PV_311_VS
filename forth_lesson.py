#Ctrl + K + C - comment
#Ctrl + K + U - uncomment
#Ctrl + / - comment /uncomment 
# a = 5
# b = 7
'''
c = 10

print(a,b,c)
print("Number a = {}".format(a))
print("Number b = {}".format(b))
print("Number c = {}".format(c))
print("Number a = {}. b = {}. c = {}".format(a,b,c))
print("Number a = {}. b = {}. c = {}".format(c,b,a))
print(f"Numbers : a = {a} . b = {b}. c = {c}")
'''
print(5)
a = 10
if a > 5:
    print("True")
else :
    print("False")
    
# a = 10
# b = "New Year"
# print(a+b)

#=   ==
#a == 8#False
#b == 22
#print(a+b)
'''
import math
print(math.ceil(2.5))
print(math.floor(2.5))
print(math.pow(2,3))
print(math.sqrt(16))

import random
print(random.random())#0.0....1.0
print(random.randint(0,1))#0....1
print(random.randint(0,1000))#0....1000
print(random.randint(20,50))#20....50

price_1 = 270
price_2 = 200
gramm = float(input("Enter weight of candies (gramms)"))
kg = gramm/1000
print(f"Your buy {kg} kg candies  ")
if kg > 0.5:
    total = kg*price_2
else :
    total = kg *price_1
total = math.ceil(total)
print(f"Your total price : {total}")

month = int(input("Enter number of month :"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Incorrect number of month")

month = int(input("Enter number of month :"))#key 
match month:#2
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _:
        print("Error")
        

a = 123//100    #1
b = 123 //10%10 #2
c = 123%10      #3
'''      
#Так, роки 100, 200, 300, 500, 600, 700, 900, 1000, 1100, 1300, 1400, 1500 , 
# 1700, 1800 , 1900 
year = 2000

if year % 400 == 0 or (year %100 != 0 and year %4 == 0):
    print(f"Month is leap {year}")
else :
    print(f"Month is not leap {year}")

