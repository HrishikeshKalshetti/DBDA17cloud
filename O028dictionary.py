# form dictionary from keys provided

score = {}.fromkeys(["computers", "maths", "physics"])
print(score)

score = {}.fromkeys(["computers", "maths", "physics"], 35)
score["maths"] = 65
print(score)

print(list(sorted(score.keys())))

t1 = ("one", "two", "three")
print(t1)
d1 = dict.fromkeys(t1, 100)
print(d1)

one={"sachin":15000}
two={"sunil":10000}
three={"saurav":8000}

combine={**one,**two,**three}
print(combine)
