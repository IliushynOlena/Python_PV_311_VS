print("Zavdania_1")
def increase_between_max_min(list):
  max_value = list[0]
  min_value = list[0]
  max_index = 0
  min_index = 0
  for i, value in enumerate(list):
    if value > max_value:
      max_value = value
      max_index = i
    elif value < min_value:
      min_value = value
      min_index = i

  for i in range(min_index + 1, max_index):
    list[i] *= 2

  return list

list = [1, 5, 3, 7, 2, 4, 6]
print(f"Список до оновлення: {list}")
updated_list = increase_between_max_min(list)
print(f"Список після оновлення: {updated_list}")




print("Zavdania_2")
def swap_elements_pairwise(list):
    for i in range(0, len(list)-1, 2):
        list[i], list[i+1] = list[i+1], list[i]

my_list = [1, 2, 3, 4, 5, 6]
print("Original list:", my_list)

swap_elements_pairwise(my_list)
print("List after swapping elements pairwise:", my_list)






# print("Zavdania_3")
# def find_duplicates(list):
#     duplicates = set()
#     unique_elements = set()

#     for element in list:
#         if element in unique_elements:
#             duplicates.add(element)
#         else:
#             unique_elements.add(element)

#     return list(duplicates)

# my_list = [1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 8]
# duplicates = find_duplicates(my_list)
# print("Original list:", my_list)
# print("Duplicate values in the list:", duplicates)




print("Zavdania_4")
def calculate_sums(matrix):
    rows_sum = [sum(row) for row in matrix]

    columns_sum = [sum(column) for column in zip(*matrix)]

    total_sum = sum(sum(row) for row in matrix)

    return rows_sum, columns_sum, total_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows_sum, columns_sum, total_sum = calculate_sums(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("\nSum of elements in each row:", rows_sum)
print("Sum of elements in each column:", columns_sum)
print("Total sum of all elements in the matrix:", total_sum)