import pprint
import copy
from data import products

new_products = [
    {**p, 'price': round(p['price']*1.1, 2)}
    for p in copy.deepcopy(products)
]

products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda item:item['name'], reverse=True
)

products_sorted_by_price = sorted(
    copy.deepcopy(products),
    key=lambda item:item['price']
)

pprint.pp(products)
print()
pprint.pp(new_products)
print()
pprint.pp(products_sorted_by_name)
print()
pprint.pp(products_sorted_by_price)
