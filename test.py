# Рекурсивна функція - повертає суму чисел у вхідному наборі
def CalcSumNumbers(A):
    if A == []:
        # якщо набір пустий, повернути 0
        return 0
    else:
        # Обчислити суму - додати перший елемент набору
        summ = CalcSumNumbers(A[1:]) # рекурсивний виклик цієї ж функції

        # Додати до загальної суми перший елемент
        summ = summ + A[0]

        return summ

# Демонстрація використання функції CalcSumNumbers()
# 1. Створити набір чисел
L = [ 2, 3, 8, 11, 4, 6 ]
print()
# 2. Викликати функцію
summ = CalcSumNumbers(L)

# 3. Роздрукувати суму
print("summ = ", summ)