import json
from pprint import pprint


def load_prod_data():
    with open('products/list_product.json', 'r') as f:
        result = json.load(f)
    return result


def save_prod_data(new_data):
    with open('products/list_product.json', 'r') as f:
        result = json.load(f)
    # return result
    result.append(new_data)

    with open('products/list_product.json', 'w') as f:
        json.dump(result, f)

#
# dd = {
#     'id': 3,
#     'name': "dd",
#     "description": "ff",
#     'img_name': "df.jpg",
#     'price': '22'
# }
# save_prod_data(dd)
#
# with open('list_product.json', 'r') as f:
#     result = json.load(f)
# pprint(result)
