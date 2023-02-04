# 1. simple function
print("1.simple function".center(50, "*"))


def greet():
    print("Deebawali TN")
    print("Deepavali Kar")
    print("Diwali Rest")


greet()

# 2. function with parameter
print("2.function with parameter".center(50, "*"))


def greet(name, age, gender):
    print(f"welcome {name} you are {age} and a {gender}")


greet("sachin", 45, "Male")
greet("Usha", 65, "Female")

# 3. function with default parameter
print("3.default parameter".center(50, "*"))


def fun(fname, lname, city="bengaluru"):
    print("Name={} Mr.{} city={}".format(fname, lname, city))


fun("rahul", "dravid")
fun("sachin", "tendulkar", "Mumbai")
fun("KL", "rahul")

# 4. function with return value(return types are implicitly deduced)
print("4.return value".center(50, "*"))


def prod(x, y):
    return x * y


print("10*3=", prod(10, 3))

# 5.1 variable number of arguments
print("5.1 variable arguments".center(50, "*"))


def get_all(*nums):  # args
    print(nums)
    for n in nums:
        print(n, end=" ")
    print()


get_all(1, 2, 3, 4, 5, 6)

# 5.2 variable number of arguments
print("5.2 variable arguments".center(50, "*"))


def get_all_arguments(**nums):  # kwargs
    print(nums)
    print("nums['four']", nums["four"])
    print('nums["fi"]', nums["fi"])


get_all_arguments(one=1, two=2, three=3, four=4, fi=5, sics=6)
