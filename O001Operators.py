a = 11
b = 3
# arithmetic operators
print("a=", a, "b=", b)
print("add + ", a + b)
print("diff -", a - b)
print("prod * ", a * b)
print("div /", a / b)
print("floor div //", a // b)
print("exp **", a ** b)
print("mod %", a % b)

'''
    comparison operator
    ==
    !=
    <>
    >
    <
    >=
    <=
'''

"""
    Assignment operators
    
    =
    augmentor
    +=
    -=
    *=
    /=
    //=
    **=
    %=

"""

'''
    Bitwise operator
    &  and
    |  or
    ^  xor
    << left shift
    >> right shift
    ~
'''
print("*"*60)
x = 5 #0b101
y = 7 #0b111
print("x", x, bin(x))
print("y", y, bin(y))
print("x&y", x & y)
print("x|y", x | y)
print("x^y", x ^ y)

print(~0)
print(~5)

'''
Logical operators

and
or
not
'''

'''
membership operators

in
not in
'''

st = "india is great"

if "in1" not in st:
    print("Apple")
else:
    print("Orange")

'''
Identity operators
is
is not
'''

a = 10
b = 20  # b=a
print(id(a), id(b))

if a is b:
    print("same")
else:
    print("not same")

if a is not b:
    print("apple")
else:
    print("orange")


'''
operator precedence order
1) **
2) ~+- unary
3)*/%//
4) +- binary
5) >> << 
6) &
7) ^|
8) <= < > >=
9) <> == !=
10) =,%=,/=,//=,-=,+=,*=,**=
11) is,is not
12) in , not in
13) not, or,and

'''
