
# sum = 0
# for i in range(12):
#     #print(i, end=" ")
#     mark = int(input(f"Enter {i + 1} mark : "))
#     sum += mark
# print(f"Average mark : {sum/12}")

# name = "Bob"
# print(name)
# name = "Ivan"

# category = ["Drama", "Comedy","Horror","Fantasy"]
# marks = [12,7,8,9,6,12,11,10,5,3,1]
# courses = list(("Math","Database", "Algorithms"))

# print(category)
# print(marks)
# print(courses)
# print(category[0])
# print(marks[10])
# print(marks[len(marks)-1])
# print(courses[1])

# studentScores = []
# students = list()
# print(studentScores)
# print(students)

# myCourses = ["Database", 2435, 7009, 3.14, "Networks"]
# print(myCourses)

# mylist = [1,2,3,4.5,[45,"Summer", "Red"]]
# print(mylist)
# print(mylist[len(mylist)-1])
# print(mylist[len(mylist)-1][1])

# customers = ['Bob', "Anna","Joe","Bob","Nick"]
# print(customers)

# mySymbols = list("asdfghjk")
# print(mySymbols)

# list1 = [i for i in range(6)]
# print(list1)

# list2 = [i*i for i in range(6)]
# print(list2)
# import random
# number = [random.randint(10,50) for i in range(10)]
# print(number)
# marks = [random.randint(1,12) for i in range(20)]
# print(marks)


# list3 = [i+'*' for i in "example"]  
# print(list3)  

# line = [s for s in 'language']
# print(line)
# print(''.join(line))
# print('_'.join(line))

# line = [s for s in 'language'[0:5]]
# print(line)

# line = "red green blue yellow white black purple orange braun tomato potato cucumber"
# words = line.split(' ')
# print(words)

# list4 = [i*5 for i in "abcde"]
# print(list4)

# list5 = [i*i for i in range(1,11) if i%2==0]
# print(list5)

# customers = ['Bob', "Anna","Joe","Bob","Nick"]
# list6 = [i for i in customers if i!="Bob" and i!= "Joe" ]
# print(list6)

# mylist = ['user',12,2000,3.14,False,True]
# print(mylist[1])
# print(mylist[-1])
# print(mylist[5])
# print(mylist[len(mylist)-1])
# print(mylist[-2])
# print(mylist[1:3])
# print(mylist[-4:-2])
# print(mylist[1:-1])
# print(mylist[:-1])
# print(mylist[3:])
# print(mylist[: : 2])
# print(mylist[: : -1])


# category = ["Drama", "Comedy","Horror","Fantasy"]
# print(category)
# category[0] = "History"
# print(category)
# print(len(category))
# print(max(category))
# print(min(category))
# #print(sum(category))
# print(sorted(category))
# for item in category:
#     print(item, end=" ")
# print()
# for i in range(len(category)):
#     print(category[i])
    
    
colors = ['red','green','blue','yellow','red','red']
for item in colors:
    print(item, end=" ")
print()  
 
colors.append("orange")
print(colors)
color = ['white','red','broun']
colors.extend(color)
print(colors)

colors.insert(2,"black")
print(colors)

colors.remove('red')
print(colors)

colors.pop(0)
print(colors)

colors.pop()
print(colors)

print(f"Index 'red' = {colors.index('red')}")
#print(f"Index 'red' = {colors.index('red',0,3)}")

print(f"Count 'red' = {colors.count('red')}")
print(colors)
colors.reverse()
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

print('red' in colors)
print('purple' in colors)

if 'red' in colors :
    print("'Red' is in list")
else:
    print("Not found")
    
for i in range(len(colors)):
    if colors[i] == 'red':
        print(i)
        break



colors.clear()
print(colors)
