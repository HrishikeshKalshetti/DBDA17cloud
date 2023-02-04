# string methods
# center
print("Center".center(50, "*"))
print("The Indian Premier League (IPL), also known as TATA IPL ")
print("The Indian Premier League (IPL), also known as TATA IPL ".center(100))
print("The Indian Premier League (IPL), also known as TATA IPL ".center(100, '*'))

# find
print("find".center(50, "*"))
info = "The Indian Premier League (IPL), also known as TATA IPL for sponsorship reasons"

print(info.find("TATA"))
print(info.find("Tata"))
print(info.lower().find("Tata".lower()))
print(info.find("IPL"))
print(info.find("IPL", 28))
print(info.find("IPL", 28, 55))
print(info.find("IPL", 28, 53))

# join
print("find".center(50, "*"))
val1 = ["sachin", "saurav", "rahul", "anil", "sunil"]

print(val1)
print("".join(val1))
print(" ".join(val1))
print("+".join(val1))
sep = '/'
print(sep.join(val1))

# split
print("split".center(50, "*"))
st = "India is great"
print(st)
val2 = st.split()
print(val2)

st = "India+is+great"
print(st)
val2 = st.split("+")
print(val2)

# reverse
print("reverse & reversed".center(50, "*"))
val1 = ["sachin", "saurav", "rahul", "anil", "sunil"]
print(val1)
val1.reverse()
print(val1)
val1 = ["sachin", "saurav", "rahul", "anil", "sunil"]
print(val1)
val2 = reversed(val1)  # reversed api
print(val1)
print(list(val2))

# problem
print("problem".center(50, "*"))
st = "India is Great"
st1 = " ".join(reversed(st.split()))
print(st)
print(st1)
