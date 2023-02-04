# filter
l1 = [11, 22, 33, 44, 55, 66, 77, 88]
print(l1)

filtered = filter(lambda x: x % 2 == 0, l1)

print(list(filtered))

products = [("nail", 400), ("face", 200), ("eye", 300), ("cucumber", 50), ("screen", 150)]
print(products)
filter_products = list(filter(lambda prd: prd[1] < 300, products))
print(filter_products)
