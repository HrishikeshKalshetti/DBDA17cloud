# map function
print("Complex list".center(40, "*"))
products = [("nail", 400), ("face", 200), ("eye", 300), ("cucumber", 50), ("screen", 150)]
print(products)

print("*" * 40)
prices = []
for prod in products:
    prices.append(prod[1])

print(prices)


def get_price_element(prod_par):
    return prod_par[1]


prices_new = map(get_price_element, products)
print(list(prices_new))

prices_new1 = list(map(lambda itm: itm[1], products))
print(prices_new1)

l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = list(map(lambda e: e * 11, l1))
print(l2)