# jos kyseessä on lista, joka koostu dictionaryistä, silmukointi

products = [
    {"name": "Kahvinkeitin", "price": 79},
    {"name": "Astianpesukone", "price": 299},
    {"name": "Arkkupakastin", "price": 199},
]

for product in products:
    name = product['name']
    price = product['price']

    print(f"{name}, {price}€")
    