import copy
# shallow and deep copy
l1 = [1, 2, 3, 4, 5]
l2 = l1

print(id(l1), id(l2))
l1 = [1, 2, 3, 4, 5, [11, 22, 33, 44]]
l2 = l1[:]  # shallow copy
l3 = l1.copy()  # shallow copy
print(id(l1), id(l2))
print(l1, l2)
l1[2] = 888
l1[5][2] = 999
print(l1, l2, l3)
print(l1, l2, l3)

print("*" * 40)
# l1 = [1, (2, [3, 4, 22], 33), 5, [11, (22, 33), 44]]
l1 = [1, (2, 3, 4), 5, [11, 22, 33, 44]]
for li in l1:
    if isinstance(li, list) or isinstance(li, tuple):
        for li1 in li:
            print(li1, end=" ")
        print()
    else:
        print(li)


# import copy for this example
print("*" * 40)
l1 = [1, 2, 3, 4, 5, [11, 22, 33, 44]]
# l2 = copy.copy(l1) # shallow copy
l2 = copy.deepcopy(l1) # deepcopy
l1[5][2] = 999

print(l1, l2)
