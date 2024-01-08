#*********
# ******* 
#  *****  
#   ***
#    *
# print(" "*0, "*"*9, " "*0, sep="")
# print(" "*1, "*"*7, " "*1, sep="")
# print(" "*2, "*"*5, " "*2, sep="")
# print("red","green","blue", sep="")
# space = 0
# star = 15
# while star > 0:
#     print(" "*space, "*"*star, " "*space, sep="")
#     star-=2
#     space+=1
    
# i = 1
# star = 1
# space = 8
# flag = True
# while i < 10:
#     i+=1
#     if i == 5:
#         flag = False
#     if flag :
#         print("*"*star, " "*space, "*"*star, sep="")
#         star+=1
#         space-=2
#     else:
#         print("*"*star, " "*space, "*"*star, sep="")
#         star-=1
#         space+=2
n = 8
for i in range(1,n-1):
    for j in range(1,n-1):
        # if i == j :
        #     print("#", end=" ")
        # else:
        #     print(" ", end=" ")
        if i+j == n-1:
            print("$", end=" ")   
        else:
            print("*", end=" ")         
        #print("*", end=" ")
    print()
    
for i in range(1,n-1):
    for j in range(1,n-1):
        if i+j >= n-1:
            print("$", end=" ")   
        else:
            print(" ", end=" ")         
        #print("*", end=" ")
    print()
print()
print() 
for i in range(1,n-1):
    for j in range(1,n-1):
        if i <= j :
            print("#", end=" ")
        else:
            print(" ", end=" ")
      
        #print("*", end=" ")
    print()
    

# for i in range(1,7):
#     for j in range(1,7):
#         print("*", end=" ")
#     print()

# 1 * 1 = 1   2 * 1 = 2
# 1 * 2 = 2   2 * 2 = 4
# 1 * 3 = 3   2 * 3 = 6
# 1 * 4 = 4   2 * 4 = 8
# 1 * 5 = 5   2 * 5 = 10

# for i in range(1,11):
#     for j in range(1,11):
#         print(f" {i} * {j} = {i*j}")
#     print()
# x = 1
# while x < 10:
#     print(x, end=" ")
#     x+=1
# print()
# print("Continue.....")
# x = 0
# while True:
#     print(x, end=" ")
#     x+=1
#     # if x >= 10:
#     #     break
#     if not (x < 10):
#         break
 
# floor = 1
# energy = 70
# print(f"I am on the {floor} floor")
# while floor != 5:#while floor < 6
#     step = 0
#     if floor == 3:
#         print(f"I am on the {floor} floor. I will take an elevator!!!")
#         break
#     while step != 20:#while step < 21
#         step+=1
#         energy-=1
#         if energy == 0:
#             print("I'm tired, I will rest a little")
#             energy+=70
#     floor+=1
#     print(f"Now I'm on the {floor} floor")
# print('I have got to the right floor')
 