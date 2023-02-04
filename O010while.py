# while

a = 10
while (a > 1):
    print(a, end=" ")
    a -= 1
else:
    print("done")
print()

x = 55
y = 15

while (x != y):
    if (x > y):
        x -= y
    if (y > x):
        y -= x

print(f"The HCF is {x}")

players = ["sachin", "Sewag", "rahul", "vvs", "yuvraj", "dhoni", "anil", "irfan"]

index = 0
length = len(players)
while (True):
    print(players[index])
    index += 1
    if (index >= length):
        break
