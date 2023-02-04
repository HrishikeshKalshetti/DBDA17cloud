# conditions
score = 134
print("1.if".center(40, "*"))
if (score > 99):
    print("It is a century")
    print("It is hundreth century")
else:
    print("Try again for century")

print("Happy to now the score")

score = 34
print("2.if".center(40, "*"))

if score > 199:
    print("Its a double")
elif score > 99:
    print("It is a century")
    print("It is hundredth century")
else:
    print("Try again for century")

print("Happy to now the score")

print("3.if".center(40, "*"))
age = 18
if age > 12 and age < 50:
    print("Eligible")
else:
    print("Not Eligible")

print("4.if".center(40, "*"))
age = 18
if 12 < age < 50:  # operator chaining
    print("Eligible")
else:
    print("Not Eligible")