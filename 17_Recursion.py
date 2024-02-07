# def ShowUser(userName):
#     print(userName)
    
# ShowUser("Helen")

# def modifyUser(userName):
#     newName1 = userName.lower()
#     newName2 = userName.upper()
#     return newName1,newName2

# myNewName = modifyUser("HeLeN")
# print(myNewName)
# nameLower, nameUpper= myNewName
# print(f"Name lower = {nameLower}, nameUpper = {nameUpper}")
# nameLower, nameUpper= modifyUser("OlekSandr")
# print(f"Name lower = {nameLower}, nameUpper = {nameUpper}")
    
# def checkLog(userLog):
#     if userLog == 'admin':
#         return userLog.upper()
#     elif userLog == 'user':
#         return userLog.lower()
#     else:
#         return "Wrong login!!!"
           
# print(checkLog("admin"))
# print(checkLog("user"))
# print(checkLog("students"))

# def functAVG(*args):
#     summa = 0
#     count = 0
#     for num in args:
#         summa+= num
#         count +=1
#     return summa/count

# numbers = [5,7,8,9,36,45,2,14,100,45,78]#list
# res = functAVG(*numbers)
#line = list(map(int, input("Enter numbers : ").split(" "))) 
#list_2 = input("Enter numbers : ").split(" ")
#print(list_2)
#res = functAVG(*line)
# print(f"Average = {res}")
    
# users = [
#     ['user1','1111'],
#     ['user2','2222'],
#     ['user3','3333']
# ]
# def printInfo(*clients):
#     for i in range(len(clients)):
#         if i == 0:
#             print(f"Login : {clients[i]}", end= " ")
#         elif i == 1:
#             print(f"Password : {clients[i]}")

# for user in users:
#     printInfo(*user)

# def ShowUser(userName):
#    print(userName)
   
# print(type(ShowUser))
# print(id(ShowUser))
# print(ShowUser)
# greeting = ShowUser
# print(greeting)
# ShowUser("Olga")
# greeting("Petro")

    
# customers = ["AdminJane","adminBob","STUDENTbob","studentAlice","Kate"]
# def sayHello(customer):
#     if customer.find("admin") != -1:
#         print(f"Hello dear , {customer} !!!")
#     elif customer.find("student") != -1:
#         print(f"Hello dear , {customer} !!!")
#     else:
#         print(f"Hello , {customer} !!!")
        

# def greetingCustomer(customers,greetFunc ):
#     for c in customers:
#         greetFunc(c.lower())
  
# greetingCustomer(customers,sayHello)    

def Hello(5,1):
    5*5*5*5*5**5*5*1
    return 5*Hello(5, step-1)
    print("Hello , user")
    Hello()  
    
#Hello()
#5! = for 1.....5 = 1*2*3*4*5
#5! = 5* 4!
#4! = 4* 3!
#3!=  3* 2!
#2! = 2 * 1!
#1! = 1
#0! = 1
#5 * 4 * 3 * 2 * 1
#3* 
def fact(n):
    print(n)
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(3))

word = "madam"
print(word)
print(word[0])
print(word[-1])
print(word[0:5:2])
print(word[0:2])
def isStrPalindrom(myStr):
    if len(myStr) == 0:
        return True    
    if myStr[0] == myStr[-1]:
        return isStrPalindrom(myStr[1:-1])
    else:
        return False
    
if isStrPalindrom(word.lower()) == True:
    print("Word is palindrome")
else:
    print("Word is not palindrome")