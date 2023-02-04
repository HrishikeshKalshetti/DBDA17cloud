my_list = list(range(10, 101, 10))
print(my_list)

my_chars = list("Sachin Tendulkar")
print(my_chars)

# combine two list
my_new_list = my_list + my_chars
print(my_new_list)

print(len(my_list), len(my_chars), len(my_new_list))

print("*" * 40)
print("my_list", my_list)
print("my_list[:]", my_list[:])  # copy shallowcopy
print("my_list[::1]", my_list[::1])
print("my_list[::2]", my_list[::2])
print("my_list[::3]", my_list[::3])
print("my_list[::-1]", my_list[::-1])
print("my_list[::-2]", my_list[::-2])
print("my_list[1:5]", my_list[1:5])
print("my_list[1:6:2]", my_list[1:6:2])
print("my_list[1:6:2][::-1]", my_list[1:6:2][::-1])
