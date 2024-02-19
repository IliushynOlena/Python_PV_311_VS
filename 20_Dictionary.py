# list1= ['Olena','Ilushyn',20,"Rivne",2566985554,258,]
# list1= ['Olena','Ilushyb',"20",2566985554,258,"Rivne"]
# list1= ['Olena','Ilushynb',20,2566985554,258,"Rivne"]
# list1= ['Olena','Ilushynb',20,2566985554,258,"Rivne"]
# list1= ['Olena','Ilushynb',20,2566985554,258,"Rivne"]
# #key  - str or numbers
# #value

# student = {
#     'name':'Olena',
#     'lastname':'Iliushyn',
#     'rating':11.8, 
#     'group':'PV311',
#     'birthday':'01.01.2001'
#     }
# print(student['name'])
# print(student['lastname'])
# print(student['rating'])
# print(student)
# print(list1)

# for key in  student.keys():
#     print(f"Key : {key:<10} . Value : {student[key]}")
    
    
# for value in student.values():
#     print('\t',value)
    
# for key, value in student.items():
#     print(f"Key : {key:<10} . Value : {value}")
    
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student)
# del student['rating']
# print(student)
# student.popitem()
# print(student)
# student.pop('lastname')
# print(student)
# student['email']= 'lena@gmil.com'
# print(student)

# students = [{'name':'Olena','lastname':'Iliushyn', 'rating':11.8, 'group':'PV311', 'birthday':'01.01.2001' },
#             {'name':'Bob','lastname':'Tomson', 'rating':12.0, 'group':'PV311', 'birthday':'01.01.2005' },
#             {'name':'Tom','lastname':'Gamilton', 'rating':4.7, 'group':'PV311', 'birthday':'01.01.2007' },
#             {'name':'Anton','lastname':'Sudorchuk', 'rating':6.7, 'group':'PV311', 
#              'birthday':'01.01.2002','marks':[10,12,11,12,11] }
#             ]
# print(students[1]['name'])
# print(students[3]['marks'][0])
# print(students[3]['marks'])
# for mark in students[3]['marks']:
#     print(mark,end= " ")
# #print("hello","good","bad", sep= " + ")
save_student = {
    'name':'Olena',
    'lastname':'Iliushyn',
    'rating':11.8, 
    'group':'PV311',
    'birthday':'01.01.2001'
    }
import json    
print(type(save_student)) 
print(save_student)

byte_list = json.dumps(save_student)  
print(type(byte_list)) 
print(byte_list)
with open("students.txt",'w') as file:
    file.write(str(byte_list))

new_student = json.loads(byte_list)
print(type(new_student)) 
print(new_student)
print(new_student['name'])

with open("students.txt",'r') as file:
    info = file.read()
    print(info)
    info = json.loads(info)
    print(info['name'])

