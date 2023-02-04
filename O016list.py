# sequence Data structure
# lists and tuple

# list
# mutable

players = []
runs = list()

print(players, runs)
print(type(players), type(runs))
print("*" * 50)

players = ["sachin", "sewag", "vvs", "rahul", "yuvraj"]

print("players", players)
print("len()", len(players))

# access list item
print("[2]", players[2])
print("[1]", players[1])
print("[-1]", players[-1])
print("[-2]", players[-2])

# update list item
print("players", players)
players[1] = "viru"
print("players", players)

# append an item

players.append("virat")
print("players", players)

# delete an item
del players[2]
print("players", players)