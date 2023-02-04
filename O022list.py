# list find,sort,sorted,index,count,reverse,reversed
l1 = list(range(10, 101, 10))
print(l1)
l1.insert(8, 50)
print(l1)
print("find".center(40, "*"))
print(l1.index(40))
print(l1.index(50))
print(l1.index(50, 5))

if 45 in l1:
    print(l1.index(45))

print("count".center(40, "*"))
print(l1.count(40))
print(l1.count(50))

print("sort".center(40, "*"))
l1 = [4, 1, 3, 5, 2]
print(l1)
l1.sort(reverse=True)
print(l1)

print("sorted".center(40, "*"))
l1 = [4, 1, 3, 5, 2]
print(l1)
l2 = sorted(l1, reverse=True)
print(l1)
print(l2)

print("reverse".center(40, "*"))
l1 = [4, 1, 3, 5, 2]
print(l1)
l1.reverse()
print(l1)

print("reversed".center(40, "*"))
l1 = [4, 1, 3, 5, 2]
print(l1)
l2 = reversed(l1)
print(l1)
print(list(l2))

print("Complex list".center(40, "*"))
products = [("nail", 400), ("face", 200), ("eye", 300), ("cucumber", 50), ("screen", 150)]
print(products)
products.sort()
print(products)


def sort_item(prod):
    return prod[1]


products.sort(key=sort_item)
print(products)

products.sort(key=sort_item, reverse=True)
print(products)

products.sort(key=lambda x: x[0], reverse=True)
print(products)
products.sort(key=lambda x: x[1])
print(products)
