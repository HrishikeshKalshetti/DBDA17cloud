# list unpacking
my_list = list(range(10, 31, 10))
print(my_list)

x, y, z = my_list
print("x,y,z=", x, y, z)

print("*" * 50)
my_list = list(range(10, 101, 10))
print(my_list)

x, y, *z = my_list
print("x,y,z=", x, y, z)

*x, y, z = my_list
print("x,y,z=", x, y, z)

x, *y, z = my_list
print("x,y,z=", x, y, z)

l1 = [11, 22, 33, 44, 55]
l2 = ['a', 'b', 'c', 'd', 'e']
# unpacking
l3 = [*l1, *l2]
print(l1, l2, l3)
l1[2] = 999
print(l1, l2, l3)
