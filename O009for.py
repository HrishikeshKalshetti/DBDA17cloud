# loop -> iterations

print(" 1.for ".center(50, "*"))
for num in range(5):
    print(num, end=" ")
print()

print(" 2.for ".center(50, "*"))
for num in range(10, 51, 5):
    print(num, end=" ")
print()

print(" 3.for ".center(50, "*"))
for num in range(10, 51, 5):
    if num == 25:
        break
    print(num, end=" ")
print()

print(" 4.for ".center(50, "*"))
for num in range(10, 51, 5):
    if num == 25:
        continue
    print(num, end=" ")
print()

print(" 5.for ".center(50, "*"))
for num in range(10, 51, 5):
    if num == 25:
        break
    print(num, end=" ")
else:
    print("Succefull looping")
print()

print(" 6.for ".center(50, "*"))
for num in range(10, 51, 5):
    if num == 25:
        continue
    print(num, end=" ")
else:
    print("Succefull looping")
print()

print(" 7.for ".center(50, "*"))
for num in range(10, 51, 5):
    print(num, end=" ")
else:
    print("\nSuccefull looping")
print()

print(" 8.for ".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for player in players:
    print(player, end="->")
print()

for player in players:
    if player == "rahul":
        break
    print(player, end="~~>>")
print()

print(" 9.for ".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for player in players:
    print(player, end="->")
else:
    print("\nshowed All Players")
print()

print(" 10.1for with enumerate".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for player in enumerate(players):
    print(player)

print(" 10.2for with enumerate".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for player in enumerate(players, start=10):
    print(player)

print(" 10.3for with enumerate".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for player in enumerate(players, start=10):
    print(player[0], player[1])

print(" 10.4for with enumerate".center(50, "*"))
players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]
for index, name in enumerate(players, start=10):
    print(index, name)

print(" 11.1 for tuple".center(50, "*"))
t1 = (1, 2, 3, 4, 5, 6)
for t in t1:
    print(t)

print(" 11.2 for tuple".center(50, "*"))
t1 = (101, 201, 301, 401, 501, 601)
for t in enumerate(t1):
    print(t)

print(" 11.3 for tuple".center(50, "*"))
t1 = (101, 201, 301, 401, 501, 601)
for t in enumerate(t1):
    print("index=", t[0], "value=", t[1])

print(" 11.4 for tuple".center(50, "*"))
t1 = (101, 201, 301, 401, 501, 601)
for ind, val in enumerate(t1):
    print("index=", ind, "value=", val)

print(" 12.1 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for itm in d:
    print(itm)

print(" 12.2 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for itm in d.keys():
    print(itm)

print(" 12.3 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for itm in d.values():
    print(itm)

print(" 12.4 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for itm in d.items():
    print(itm)

print(" 12.5 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for itm in d.items():
    print(itm[0], itm[1])

print(" 12.6 for dictionary".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for k, v in d.items():
    print(k, v)

print(" 12.6 for dictionary enumerate".center(50, "*"))
d = {"key1": "val1", "key2": "val2", "key3": "val3", "key4": "val4"}
for i, itm in enumerate(d.items()):
    k, v = itm
    print(i, k, v)

print(" 13.1 for string".center(50, "*"))
st = "sachin tendulkar"
for char in st:
    print(char, end=" ")
print()

print(" 13.2 for string".center(50, "*"))
st = "sachin tendulkar"
for char in enumerate(st):
    print(char, end=" ")
print()

print(" 13.3 for string".center(50, "*"))
st = "sachin tendulkar"
for i, c in enumerate(st):
    print(i, c)
print()
