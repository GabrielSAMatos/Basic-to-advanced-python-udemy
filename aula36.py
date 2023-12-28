from pprint import pprint

def p(v):
    pprint(v, indent=10) 


products = [
    {'name': 'p1','price':20,},
    {'name': 'p2','price':10,},
    {'name': 'p3','price':30,},
    {'name': 'p4','price':30,},
]


new_products = [ 
    {**product, 'price': product['price']*1.10}
    if product['price'] > 20 else {**product}
    for product in products
    if product['price'] > 10
]

p(new_products)

list_ = [
    (' ')
    for x in range(3)
    for y in range(3)
]

#print(list_)
