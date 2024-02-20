# import requests

# url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"

# result = requests.get(url).json()
# #print(type(result.content))
# print(result[1]['buy'])
# print(result[1]['sale'])
# print(type(result))
# product = {'name':'cucumber', 'price':4.5}
# sale_doll = float( result[1]['sale'])
# print(type(sale_doll))
# print(type(product['price']))
# price = product['price']
# res = price*sale_doll
# print(res)
#url = "https://upload.wikimedia.org/wikipedia/commons/5/5e/Flag_of_Ukraine.jpg"
# img = requests.get(url)
# with open("./img/flag.jpg",'wb') as file :
#     file.write(img.content)
# url = "https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&q=yellow+flowers&image_type=photo"

# res = requests.get(url).json()["hits"]

# counter = 1
# for img in res : 
#     with open(f"./img/{counter}.jpg",'wb') as file :
#         pict = requests.get(img['webformatURL'])
#         file.write(pict.content)
#     counter+=1
    
# Завдання:::Створити магазин з товарами і  створити програму конвертер валюти, 
# спілкування з користувачем, реалізувати через меню   https://api.privatbank.ua/
# Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, що складаються не менше, ніж із семи літер.
url = r"./write.txt"
url2 = r"./my2.txt"

def filter_leater_word(url, url2):
    with open(url, 'r') as file:
        with open(url2, 'w') as f_out:
            for line in file:
                words = line.split()
                filtered_words = [word for word in words if len(word) >= 7]
                if filtered_words:
                    f_out.write(" ".join(filtered_words) + "\n")


print()
filter_leater_word(url, url2)
