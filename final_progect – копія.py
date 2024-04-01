
 
import requests
import json
def getCours():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    result = requests.get(url).json()
    return result[1]['sale']
 
def fillItem():
    users = readUsers()
    while True:
        try:
            id = int(input("Enter Id: "))
            if any(id == user['id'] for user in users):
                print("This Id is already in use.")
                continue
            else:
                name = input("Enter name(computer/Laptop/PC mouse/other) :")
                price = float(input("Enter price by dollar:"))
                number = int(input("Enter number(How much do you have?) :"))
                brand = input("Enter brand :")
                coursNow = getCours()
                priceHRN =price* float (coursNow)
                return {'id': id, 'name': name,'price':priceHRN,'priceDol':price,'number':number,'brand':brand}

                break  
        except ValueError:
            print("Please enter a valid integer for Id.")   
        
                
       



    
    
 
 
def createListUsers(count):
    #users = []
    users = readUsers()
    for i in range(count):
        users.append(fillItem())
        writeUsers(users)
    return users
def writeUsers(users):
    with open("users.json", 'w') as file:
        file.write(json.dumps(users))
def readUsers():
    with open("users.json") as file:
        return json.loads(file.read())
def PrintAllUser():
    users = readUsers()
    print('='*100)
    for i in range(len(users)):
        for key, value  in  users[i].items():
            print(f'{key}: {value:<10} ', end='')
        print()
        print('='*100)
       
def deleteUser():
    users = readUsers()
    a = int(input("Enter number kogo ydalit"))
    users.pop(a-1)
    writeUsers(users)
    PrintAllUser()
    while True:
        choise = int(input('''
        Enter choise
                    1 - delete
                    2 - exit
        '''))
        if choise == 1:
            a = int(input("Enter number kogo ydalit"))
            users.pop(a-1)
            writeUsers(users)
            PrintAllUser()
        elif choise == 2:
            break
        else:
            print("sorry you made a mistake")

def sortUsers():
    users = readUsers()
    def printUsers(data):
        for i in range(len(data)):
            print(data[i])
    writeUsers(users)
    PrintAllUser()
    while True:
        choice1 = int(input('''
    1 - Sort by id
    2 - Sort by name
    3 - Sort by price
    4 - Sort by number
    5 - Sort by brand
    0 - exit
    Enter your choice: '''))
        if choice1 == 1:
            print("Sort by id")
            users.sort(key = lambda x:x['id'])
            writeUsers(users)
            PrintAllUser()
        elif choice1 == 2:
            print("Sort by name")
            users.sort(key = lambda x:x['name'])
            writeUsers(users)
            PrintAllUser()
        elif choice1 == 3:
            print("Sort by price")
            users.sort(key = lambda x:x['price'])
            writeUsers(users)
            PrintAllUser()
        elif choice1 == 4:
            print("Sort by number")
            users.sort(key = lambda x:x['number'])
            writeUsers(users)
            PrintAllUser()
        elif choice1 == 5:
            print("Sort by brand")
            users.sort(key = lambda x:x['brand'])
            writeUsers(users)
            PrintAllUser()
        elif choice1 == 0:
            break
        else:
            print("sorry you made a mistake")
def searchALLLL():
    users = readUsers()
    x = input('Enter which you want search(computer/Laptop/PC mouse/other)')
    a = input("Enter brand which you want search")
    b = float(input("Enter price  and I search machinery for your balance(dol)"))
    c = int(input("Enter kol-vo and i search "))
    for i in range(len(users)):
        if users[i]['brand'] == a and users[i]['priceDol'] <= b and users[i]['number'] >= c and users[i]['name'] == x:
            print('='*100)
            for key, value  in  users[i].items():
                print(f'{key}: {value:<10} ', end='')
            print()
            print('='*100)
        else:
            print("We haven't this goods")
while True:
    choice = int(input('''
                  <==========================>
                   | 1 - Fiil database      |
                   | 2 - add product        |
                   | 3 - delete product     |
                   | 4 - print product      |
                   | 5 - sort product       |
                   | 6 - search product     |
                   | 0 - exit               |
                   | Enter your choice: '''))
    if choice == 0:
        break
    elif choice == 1:
        countUser = int(input("Enter count of product :"))
        users = createListUsers(countUser)
        writeUsers(users)
    elif choice == 2:
        users = readUsers()
        users.append(fillItem())
        writeUsers(users)
    elif choice == 3:
        deleteUser()
    elif choice == 4:
        PrintAllUser()
    elif choice == 5:
        sortUsers()
    elif choice == 6:
        searchALLLL()
    else:
        print("sorry you made a mistake")
