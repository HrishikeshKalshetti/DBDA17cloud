l1 = ['a', 'b', 'c', 'd', 'e', 'f']

print(l1)
print("*" * 50)

for l in l1:
    print(l, end=" ")
print()
print("*" * 50)

for l in enumerate(l1):
    print(l)

print("*" * 50)

for l in enumerate(l1):
    print(l[0], l[1])

print("*" * 50)

for k, v in enumerate(l1):
    print(k, v)

print("*" * 50)

my_list = [[1, 2, 3], [11, 22, 33], [111, 222, 33]]

my_list[2][1]=999
for index, lst in enumerate(my_list):
    print(f"list {index + 1} : ")
    for ind1, val in enumerate(lst):
        print(f"my_list[{index}][{ind1}]={val}", end=" ")
    print()
