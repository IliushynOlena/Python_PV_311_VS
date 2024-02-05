# a = 5
# b = 7
# def showMessage():    
#     #print(b)
#     print("Hello, Olena")
    
# def welcomeUser(name):    
#     #print(b)
#     print(f"Hello, {name}")   
    
# #print(b)
# print(showMessage)
# showMessage()
# showMessage()
# showMessage()

# userName = input("Enter user name : ")

# welcomeUser(userName)
# welcomeUser('Lilia')
# welcomeUser('Oleg')

# def summa(a,b):
#     #print(a+b)
#     #some code    
#     return a+b
# def sub(a,b):  
#     return a-b
# def multy(a,b):  
#     return a*b
# def div(a,b):  
#     if b == 0:
#         return#return = break    
#     return a/b


# def calculator(a,b,op):
#     if op == '+':
#         return summa(a,b)
#     if op == '-':
#         return sub(a,b)
#     if op == '*':
#         return multy(a,b)
#     if op == '/':
#         return div(a,b)
    
# def getOperation(line):
#     if line.find('+') != -1:
#         return '+'
#     if line.find('-') != -1:
#         return '-'
#     if line.find('*') != -1:
#         return '*'
#     if line.find('/') != -1:
#         return '/'
    
# example = input("Enter example (2+2) ---> ")
# op = getOperation(example)

# number_1 = float(example.split(op)[0]) 
# number_2 = float(example.split(op)[1])

 
# res = calculator(number_1,number_2,op)    
# print (f'Result :  {res}')
    
# print (f'Summa in main program {summa(3,8)}')
# res = summa(1,1)
# print (f'Summa in main program {res}')
# summa(2,2)
# summa(4,9)
import random
def fillList(list, count = 30, min = 1, max = 50):
    # list = [random.randint(min,max+1) for i in range(count)]  
    # return list
    return [random.randint(min,max+1) for i in range(count)]  
    
numbers= []
print(numbers)
numbers = fillList(numbers,30,20,1000)
print(numbers)

# #print("\033[31m",line_1)
print("\033[31m\033[47m\033[1m{}\033[0m".format(numbers), end=" ")
print("\033[32m\033[46m\033[2m{}\033[0m".format(numbers),end=" ")
print("\033[33m\033[45m\033[3m{}\033[0m".format(numbers),end=" ")
print("\033[34m\033[44m\033[4m{}\033[0m".format(numbers),end=" ")

for i in range(10):
    print('*',end=' ')
    
    
number = 123456
a1 = number//100000
print(a1)
a2 =number//10000%10
print(a2)
a3 = number//1000%10
print(a3)
# a4 = 
# print(a4)
# a5 = 
# print(a5)
# a6 = 
# print(a6)

    

    
