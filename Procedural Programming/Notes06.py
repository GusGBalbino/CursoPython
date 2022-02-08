from Notes05 import products, persons, list1

'''
#Mapeamento
#list2 = map(lambda x: x * 2, list1) - Multiplicando elementos da lista
list2 = [x * 2 for x in list1] - List comprehensions
print(list2)
'''
#----------------------------------------------------------------------------------------------------------#

'''
def up_price(product):
    product['price'] = round(product['price'] * 1.05, 2)
    return product


new_products = map(up_price, products)

for product in new_products:
    print(product)
'''
#----------------------------------------------------------------------------------------------------------#

#Filter
#listnew1 = filter(lambda p: p['price'] > 50, products)
# listnew2 = [x for x in list1 if x > 5] - List comprehensions
def filtra(persons):
    if persons['Age'] >= 21:
        return True
    else:
        return False

listnew3 = filter(filtra, persons)

for person in listnew3:
    print(person)