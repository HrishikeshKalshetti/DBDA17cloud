player_name = "sachin"
player_last_name = "tendulkar"
player_description = '''Sachin Tendulkar was 
the most complete batter 
of his time, the most prolific 
run-maker of all time, 
and arguably the biggest cricket icon the game has ever'''

print(player_name)
print(player_last_name)
print(player_description)

print("len".center(40, '*'))
print(len(player_name))

print("charector extract".center(40, '*'))
print(player_name)
print(player_name[0])
print(player_name[3])
print(player_name[-1])
print(player_name[-3])

print("slice".center(40, '*'))
print(player_name)
print(player_name[0:])
print(player_name[:3])
print(player_name[:])
print(player_name[2:5])
print(player_name[1:5:2])
print(player_name[::-1])
print(player_name[::-2])

print("other".center(40, '*'))
player_name = "   sachin   "
print("Initial ", player_name)
print("upper   ", player_name.upper())
print("lower   ", player_name.lower())
print("title   ", player_name.title())
print("strip   ", player_name.strip() + "cdac")
print("lstrip  ", player_name.lstrip() + "cdac")
print("rstrip  ", player_name.rstrip() + "cdac")
player_name = "sachin tendulkar"
print(player_name)
print(player_name.replace("tend", "tiger"))

print("end" in player_name)
print("1" + "2")
print("11" + "22")

a = "12"
b = "sachin"

print(a, "isnumeric", a.isnumeric())
# print(b,"isnumeric",b.isnumeric())
print(a, "isdigit", a.isdigit())
# print(b,"isdigit",b.isdigit())
print(a, "isdecimal", a.isdecimal())
# print(b,"isdecimal",b.isdecimal())
print("42 isdigit,isnumeric & isdecimal".center(40, '*'))
print("42".isdecimal())
print("42".isdigit())
print("42".isnumeric())

print("00b2 isdigit,isnumeric & isdecimal".center(40, '*'))
print("\u00b2".isdecimal())
print("\u00b2".isdigit())
print("\u00b2".isnumeric())

# isdecimal -> decimal numbers only
# isdigit  -> decimal + superscript ,subscript
# isnumeric -> isdigit + roman numerals,currency numerals

# subscript
print(u'H\u2082SO\u2084')  # H₂SO₄

# superscript
print("x\u00b2 + y\u00b2 = 2")  # x² + y² = 2