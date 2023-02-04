# add and remove items from the list

l1 = list(range(10, 101, 10))
print(l1)
print(" Append ".center(40, "*"))
l1.append(110)
print(l1)

print(" Insert(pos,value)) ".center(40, "*"))
l1.insert(0, 5)
l1.insert(3, 55)
print(l1)

print(" pop(ind) ".center(40, "*"))
l1.pop()
print(l1)
l1.pop(2)
print(l1)

print(" remove(val) ".center(40, "*"))
print(l1)
l1.remove(90)  # exception if trying remove which does not exist
print(l1)

print(" del[range] ".center(40, "*"))
print(l1)
del l1[2]
print(l1)
del l1[2:5]
print(l1)

print(" clear ".center(40, "*"))
l1.clear()
print(l1)
