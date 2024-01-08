import time
start_time = time.time()
# Your code here
time.sleep(5)
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Time elapsed: {elapsed_time} seconds')

# import time
 
# named_tuple = time.localtime() # отримуємо struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# time_string = time.strftime("%H:%M:%S", named_tuple)
 
# print(time_string)

# i = 1
# star = 1
# space = 8
# while i < 10:
#     i+=1
#     print("*"*star," "*space, sep="")
#     star +=1
#     space-=2


# for i in range(7):
#     for j in range(7):
#         if i>= j:
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()
# print()
# for i in range(7):
#     for j in range(7):
#         if i <= j:
#             print('* ',end='')
#         else:
#             print('  ',end='')
#     print()