import json
def fillItem():
     id = int(input("Enter id : "))
     name = input("Enter name : ")
     company = input("Enter the company of the item: ")
     company2 = company.title()
     price = float(input("Enter the price of the item: "))
     type = input("Input the type of an item: ")
     return {"id": id,"name": name, "company": company2, "price": price, "type": type}

def createListItems(count):
     items = []
     for i in range(count):
         items.append(fillItem())
     return items

def writeItems(items):
     with open("products.json", 'w') as file:
         file.write(json.dumps(items))

def readItems():
     with open("products.json", 'r') as file:
         return json.loads(file.read())

def PrintAllItems():
     items = readItems()
     print("List:")
     for i in range(len(items)):
         for key, value in items[i].items():
             print(f"{key} : {value}")

def Deleteitem(idd2):
    items = readItems()
    for i in range(len(items)):    
        if i > len(items) - 1:
            break
        i2 = i - 1
        if items[i2]["id"] == idd2:
           items.pop(i2)
           print("Product details was deleted successfully!")
        elif items[i2]["id"] == idd2 and i != 1:
           items.pop(i2)
           print("Product details was deleted successfully!")
    writeItems(items)

def edititem(new_details, idd22):
    items = readItems()
    for i in range(len(items)):    
        if i > len(items) - 1:
            break
        i2 = i - 1
        if items[i2]["id"] == idd22 and i != 1:
           items[i2].update(new_details)
           print("Product details was updated successfully!")
        elif items[i2]["id"] == idd22:
           items[i2].update(new_details)
           print("Product details was updated successfully!")
    writeItems(items)

def search_items(field, value):
    items = readItems()
    for i in range(len(items)):
        if items[i][field].lower() == value.lower():
            for key, value in items[i].items():
                print(f"{key}: {value}")

def sort_items(field):
    items = readItems()
    field2 = field.lower()
    sorted_products = sorted(items,key = lambda x:x[field2])
    for data in sorted_products:
           print(f"ID: {data['id']}, {field2}: {data[field2]}")

def filter_items(product_type, min_price, max_price):
    items = readItems()
    for details in items:
        if details['type'].lower() == product_type.lower() and min_price <= details['price'] <= max_price:
            for key, value in details.items():
                print(f"{key}: {value}")

while True:
     choice = int(input('''
                        1 - Fill Database with products
                        2 - Print All Items
                        3 - Add an Item
                        4 - Delete an Item
                        5 - Edit an Item
                        6 - Sort Items
                        7 - Search specific Item
                        8 - Range of prices
                        0 - Exit
                        Enter your choice : '''))
     if choice == 0:
         print("Executing exiting process...")
         break
     if choice == 1:
         countItems = int(input("Enter count of items : "))
         items = createListItems(countItems)
         writeItems(items)   
     if choice == 2:      
         PrintAllItems()
     if choice == 3:
         items = readItems()
         items.append(fillItem())
         writeItems(items)
     if choice == 4:
         idd = int(input('Enter the id: '))
         items = Deleteitem(idd)
     if choice == 5:
            idd2 = int(input('Enter the id: '))
            new_details = {
                "id": int(input("Enter the ID you want to change to: ")),
                "name": input("Enter new product name (leave empty to keep unchanged): "),
                "company": input("Enter new company name: "),
                "price": float(input("Enter new product price (leave 0 to keep unchanged): ")),
                "type": input("Enter new product type (leave empty to keep unchanged): ")
            }
            edititem(new_details, idd2)
     if choice == 6:
            field = input("Enter field to sort by (name/price): ")
            sort_items(field)
     if choice == 7:
         search = input("Search by (name/company): ")
         value = input(f"Enter value for {search} search: ")
         search_items(search, value)
     if choice == 8:
            producttype = input("Enter product type to filter: ")
            minprice = float(input("Enter minimum price of the item: "))
            maxprice = float(input("Enter maximum price of the item: "))
            filter_items(producttype, minprice, maxprice)
         

         
             
