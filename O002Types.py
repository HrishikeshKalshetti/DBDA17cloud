# Types in python

'''
1) numbers
    integers
    float
    long
    Boolean
    Complex
2) collections
    sequence
        immutable
            string
            unicode
            tuple
        mutable
            list
    mappings
        dictionary
3) callables
    functions
    class
    method
        bound
        unbound
4) other
    module
    instance
    file
    None
5) internals
    type
    Code
    Frame
    Traceback
'''

a = 1
b = -1
c = 1.0
d = -1.0
e = +2e3
f = -2e3
g = 3.141j  # complex
h = -3.14j

print("a=", a, "type(a)", type(a))
print("b=", b, "type(b)", type(b))
print("c=", c, "type(c)", type(c))
print("d=", d, "type(d)", type(d))
print("e=", e, "type(e)", type(e))
print("f=", f, "type(f)", type(f))
print("g=", g, "type(g)", type(g))
print("h=", h, "type(h)", type(h))

print("*" * 40)
a = 10
print("a=", a, "type(a)", type(a))
a = float(a)
print("a=", a, "type(a)", type(a))
a = int(a)
print("a=", a, "type(a)", type(a))
a = bool(a)
print("a=", a, "type(a)", type(a))
a = complex(a)
print("a=", a, "type(a)", type(a))


print("*"*40)
print(0b101)
print(0o15)
print(0xe)

a=100
print(bin(a))
print(oct(a))
print(hex(a))
