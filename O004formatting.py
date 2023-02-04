from string import Template
import math

# formatting string

# Illustration 1 c-style printf formatting
print("C style".center(40, '*'))
print("This is %s and %s's debut at %i " % ("sachin", "Tendulkar", 13))
fmt_str = "Hello %s you are getting %i and %f"
values = ("Saurav", 3000, 3.1415)
print(fmt_str % values)
fmt_str = "Hello %s you are getting %i and %.2f"
print(fmt_str % values)

# Illustration 2 unix shells style formatting (from string import Template)
print("unix style".center(40, '*'))
tml_str = Template("Hello $person you are getting $salary and $bonus")
print(tml_str.substitute(person="Saurav", salary=3000, bonus=3.145))

# Illustration 3 string formatting
print("string format".center(40, '*'))

print("Hello {} you are getting {} and {}".format("saurav", 3000, 3.1415))
print("Hello {0} you are getting {1} and {2}".format("Saurav", 3000, 3.1415))
print("You are getting {1} Mr.{0} and Bonus {2}".format("Saurav", 3000, 3.1415))
print("You are getting {salary} Mr.{name} and Bonus {bonus}".format(name="Saurav", salary=3000, bonus=3.1415))
print("You are getting {salary} Mr.{name} and Bonus {bonus:.2f}".format(name="Saurav", salary=3000, bonus=3.1415))

# Illustration 4 interpolation python 3.6 and above
print("Interpolation".center(40, '*'))
a, b, c = 11, 22.22, 33
print(f"a={a},b={b} and c={c}")

# Examples
print("Examples".center(40, '*'))

print("{name} {} {age} {}".format(100, 200, 300, 400, name="vvs", age=45))
print("{name} {} {age} {}".format(500, 700, name="vvs", age=45))

fname = ["sachin", "Tendulkar"]
print("Mr.{name[1]} welcome".format(name=fname))
# dunder a __a__
tmpl = "The {mod.__name__} module comprises {mod.pi} for pi"
tmpl = tmpl.format(mod=math)
print(tmpl)

# exercise on conversion
print("exercise".center(40, '*'))
# what is (s r and a) ?
print("{pi!s} {pi!r} {pi!a}".format(pi="A"))

print("The age is {age}".format(age=42))
print("The age is {age:10} level".format(age=42))
print("The age is {age:010} level".format(age=42))
print("The age is {age:<10} level".format(age=42))
print("The age is {age:f}".format(age=42))
print("The age is {age:.2f}".format(age=42))
print("The age is {age:b}".format(age=42))
print("one googol={}".format(10**100))
print("one googol={:,}".format(10**100))


print("{:b}".format(5))
print("{:#b}".format(5))
print("{:o}".format(5))
print("{:#o}".format(5))
print("{:x}".format(5))
print("{:#x}".format(5))

print("{:g}".format(5))
print("{:#g}".format(5))
