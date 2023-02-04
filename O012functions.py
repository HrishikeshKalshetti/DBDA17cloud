def multiply_all(*args):
    res = 1
    for n in args:
        res *= n
    return res


print(multiply_all(1, 2, 3, 4, 5, 6))

print("*" * 40)


def get_config(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} -> {v}")


get_config(ip="127.0.0.1", port="80", uri="callbackservice")
print("*" * 40)


def get_results(x, y):
    """
        This function does arithmetic operations
        :param x: first number
        :param y: second number
        :return: tuple of add,sub,mul,div and floor div
    """
    add = x + y
    diff = x - y
    prod = x * y
    div = x / y
    fdiv = x // y
    return add, diff, prod, div, fdiv


print("get_results(10,3)=", get_results(10, 3))
print("*" * 40)
print(get_results.__doc__)
print("*" * 40)
print(help(get_results))
print("*" * 40)


def samplefun():
    # this is a test fun
    print("Sample")


print(samplefun.__doc__)
print("*" * 40)
print(help(samplefun))
print("*" * 40)
