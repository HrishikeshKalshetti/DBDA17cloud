'''
l1 = [1, 2, 3, 4, 5,6,7,8]
print(l1)
l2 = list(map(lambda e: e * 11, l1))
print(l2)
'''

# list comprehension
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [num * 11 for num in l1]  # map
print(l1)
print(l2)

products = [("nail", 400), ("face", 200), ("eye", 300), ("cucumber", 50), ("screen", 150)]
print(products)

prices = [prod[1] for prod in products]  # map
print(prices)

# filter
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [num * 10 for num in l1 if num < 6]  # filter
print(l1)
print(l2)

products = [("nail", 400), ("face", 200), ("eye", 300), ("cucumber", 50), ("screen", 150)]
print(products)

products_purchased = [prod for prod in products if prod[1] < 300]  # filter
print(products_purchased)

st = "The quick brown fox jumps over the lazy dog"
words = st.split()
print(st)
print(words)
word_length = [len(word) for word in words]
print(word_length)

my_words = [wrd for wrd in words if len(wrd) == 5]
print(my_words)
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
combine = [(w, l) for w in l1 for l in l2]
print(combine)
