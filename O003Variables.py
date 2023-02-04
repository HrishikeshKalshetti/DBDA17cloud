# variable (name to a memory location)

# type inference
player_count = 11
rating = 8.5
has_won_wc = True
team_name = "India"

print(player_count, type(player_count))
print(rating, type(rating))
print(has_won_wc, type(has_won_wc))
print(team_name, type(team_name))

print("*" * 40)
a, b, c = 1, True, "Sachin"
print(a, type(a))
print(b, type(b))
print(c, type(c))
b = "saurav"
print(b, type(b))

print("*" * 40)
a = b = c = 100
print(a, type(a))
print(b, type(b))
print(c, type(c))

'''
naming rules for variables
1. Case Senitive
2. must not be python keywords
...
'''

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
