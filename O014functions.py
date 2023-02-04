def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


for n in range(11):
    print(fib(n), end=" ")
print()


def fact(num):
    if num < 2:
        return 1
    return num * fact(num - 1)


print(fact(5))
print(fact(6))


def print_all(*args, **kwargs):
    print("Args = ", end=" ")
    for arg in args:
        print(arg, end=" ")
    print()
    for k, v in kwargs.items():
        print(k, v)


print_all(11, 22, 33, 44, 55, name="sachin", age=45, rating=9.4)

print('*' * 40)


def test_fun(par):
    par = "tendulkar"


name = "sachin"
print(name)
test_fun(name)  # string's are immutable and does not change
print(name)


def test_fun1(par):
    par[0] = "Mr.tendulkar"


names = ["rahul", "sewag", "mahi"]
print(names)
test_fun1(names)
print(names)
