
#try except
# num1 = None
# num2 = None
# while num1 == None or num2 == None or num2 == 0:
#     try:    
#         num1 = int(input("Enter number : "))
#         num2 = int(input("Enter number : "))
#         print(f"Res = {num1/num2*num3}")
   
#     except ValueError:
#         #pass
#         print("Value Error!!! You need to enter number")
#     except ZeroDivisionError:
#         print("Go study Math!!! You can't Division by zero")
#     except NameError:
#         print("Don't use not defined value")
#     except Exception:
#         print("Error")
    
    
# print("Continue...... End!!!!!")
# try:
#     age = int(input("Enter age : "))#-5  125 15 300
#     if age < 0 :
#         raise Exception("Age error Age < 0!") 
#     if age >= 135:
#         raise Exception("Age error Age > 135!")  
#     print("Test")   
# except ValueError:
#     print("Value Error!!! You need to enter number")
# except Exception as ex:
#     print(ex, type(ex).__name__)
# else :
#     print("Good!!!")
# finally:
#     print("Finnaly close file!")
try:
    colors = ['red','green','brown','cyan']
    index = int(input("Enter position color : "))
    print(colors[index])
except ValueError:
    print("Value Error!!! You need to enter number")
except IndexError:
    print("Index was out of range")
except Exception:
    print("Error")