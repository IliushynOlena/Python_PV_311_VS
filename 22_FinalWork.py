# user
#id : 1
#name : "Yura"
#id : 2
#name : "Ivanka"

# import json
# def fillItem():
#     id = int(input("Enter id : "))
#     name = input("Enter name : ")
#     return {"id":id,"name": name}

# def createListUsers(count):#3
#     users = []
#     for i in range(count):
#         users.append(fillItem())
#     return users

# def writeUser(users):
#     with open("users.json", 'w') as file:
#         file.write(json.dumps(users))

# def readUsers():
#     with open("users.json", 'r') as file:
#         return json.loads(file.read())

# def PrintAllUser():
#     users = readUsers()
#     print(users)
#     for i in range(len(users)):
#         #print(users[i])
#         for key in  users[i].keys():
#             print(f"Id : {key:<10} . Name : {users[i][key]}")


# while True:
#     choice = int(input('''
#                        1 - Fill Database
#                        2 - Add User
#                        3 - Delete User
#                        4 - Print User
#                        5 - Sort Users
#                        0 - exit
#                        Enter your choice : '''))
#     if choice == 1:
#         countUser = int(input("Enter count of users : "))
#         users = createListUsers(countUser)
#         writeUser(users)
#     if choice == 0:
#         break
#     if choice == 2:
#         users = readUsers()
#         users.append(fillItem())
#         writeUser(users)
#     if choice == 4:
#         PrintAllUser()


list1 = [
    {"id":1,"name": "Olena", "age":12},
    {"id":2,"name": "Tom", "age":12},
    {"id":3,"name": "Bob", "age":12},
    {"id":3,"name": "Jack", "age":12},
    {"id":3,"name": "Lia", "age":12},
    {"id":4,"name": "Ivanka", "age":12}
]
print(list1)
for i in range(len(list1)):
        #print(users[i])
    for key in  list1[i].keys():
        print(f"Id : {key:<10} . Name : {list1[i][key]}")

# list1.pop(1)

# def printUser(data):
#     for i in range(len(data)):
#         print(data[i])

# printUser(list1)
# print("Sort by id")
# list1.sort(key = lambda x:x['id'])
# printUser(list1)
# print("Sort by name")
# list1.sort(key = lambda x:x['name'])
# printUser(list1)
# print("Sort by name with soted_list")
# soted_list = sorted(list1, key = lambda x:x['name'])
# printUser(soted_list)
# print("Filter list by id = 3")
# filters_list = list(filter(lambda x:x['id']== 3, list1))
# print(filters_list)



