from Notes05 import products, persons, list1

'''
#list2 = map(lambda x: x * 2, list1)
list2 = [x * 2 for x in list1]
print(list2)
'''

def up_price(product):
    product['price'] = round(product['price'] * 1.05, 2)
    return product


new_products = map(up_price, products)

for product in new_products:
    print(product)