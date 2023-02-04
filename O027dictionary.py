'''
dictionary -> unordered collection -> key-value
'''

d1 = {}
d2 = dict()
print("*" * 40)
print(d1, d2)

players = {"sachin": "Batsman", "kapil": "Captain", "kirmani": "keeper", "Azhar": "Fielder"}
print("*" * 40)
print(players)
print(type(players))
print("*" * 40)
my_info = {"name": "saurav", 1: "ganguly", "age": 56}
print(my_info)

print("*" * 40)
for k, v in my_info.items():
    print(k, v)

print("*" * 40)

d3 = dict({1: "one", 2: "two", 3: "three"})
print(d3)
d4 = dict([(1, "one"), (2, "two"), (3, "three")])
print(d4)
d5 = dict(x="one", y="two", z="three")
print(d5)

# access elements
print(d5["x"])
print(d5["z"])

# change the value
d5["y"] = "why"
print(d5)

# add item
d5["a"] = "aye"
print(d5)

print("*" * 40)
my_sqrs = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(my_sqrs)
my_sqrs.pop(3)
print(my_sqrs)
my_sqrs.popitem()
print(my_sqrs)
my_sqrs.popitem()
print(my_sqrs)
my_sqrs.popitem()
print(my_sqrs)

print("*" * 40)
my_sqrs = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(my_sqrs)
del my_sqrs[2]
print(my_sqrs)

my_sqrs.clear()
print(my_sqrs)

del my_sqrs
# print(my_sqrs) # throws error


print("*" * 40)

vehicle = {
    "manufacturer": "Hyundai",
    "model": "i20",
    "year": 2021,
    # "color":"grey"
}

print(vehicle)
xx = vehicle.setdefault("color", "black")
print(vehicle)
print(xx)

phone = {"sachin": "1234", "saurav": "4567", "rahul": "789"}

print("saurav phone number is {saurav}".format_map(phone))
print("saurav={saurav} sachin={sachin} rahul={rahul}".format_map(phone))
