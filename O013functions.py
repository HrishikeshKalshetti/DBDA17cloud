from collections import namedtuple


def get_results(x, y):
    add = x + y
    diff = x - y
    prod = x * y
    div = x / y
    fdiv = x // y
    result = namedtuple("Result", "sum sub mul,div floor")
    current_result = result(add, diff, prod, div, fdiv)
    return current_result


print(get_results(10, 4))

calc = get_results(10, 4)

print(calc)
print(type(calc))

print(calc.sum, calc.sub, calc.mul)
