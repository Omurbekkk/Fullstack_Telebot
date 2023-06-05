# import json
# import requests
# from bs4 import BeautifulSoup as BS


# main_url = 'https://www.ts.kg/selection/top_2022_anime'

# # response = requests.get(main_url)
# # soup = BS(response.text, 'lxml')

# def get_soup(url:str) -> BS:
#     response = requests.get(url)
#     soup = BS(response.text, 'lxml')
#     return soup

# def get_product_info(product:BS) -> dict:
#     title = product.find('div', {'class':'selection-show-text'}).find('h4').text
# # print(title)

#     # image = product.find('div', {'class':'row selection-show'}).find('img').get('src')
#     image = product.find('img').get('src')
# # print(image)
#     return {'title':title, 'image':main_url+image}

# def get_all_products_from_page(url:str) -> list:
#     res = []
#     soup = get_soup(url)
#     box = soup.find('div', {'class':'container'})
#     print(box)
#     products = box.find_all('div', {'class':'row selection-show'})
#     # print(len(products))
#     for product in products:
#         product_info = get_product_info(product)
#         res.append(product_info)
#     return res

# print(get_all_products_from_page(main_url))