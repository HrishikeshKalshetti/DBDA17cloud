# scope
def fun():
    x, y, z = 1, 2, 3  # local variable
    print("fun x,y,z=", x, y, z)


fun()


def fun1(name):  # local variables(parameters)
    print("fun1 name=", name)


fun1("sachin")

msg = "India is great"  # global variable


def fun3():
    print("fun3 msg=", msg)


fun3()

print("main module msg=", msg)


def fun4():
    msg = "India wins world cup"  # local variable
    print("fun4 msg=", msg)


fun4()

print("main module msg=", msg)


def fun5():
    global msg
    msg = "India wins world cup"  # local variable
    print("fun5 msg=", msg)


fun5()

print("main module msg=", msg)

print("*" * 50)

my_name = "global"


def outerfun():
    my_name = "local"
    print("outer start", my_name)

    def innerfun():
        # global my_name
        nonlocal my_name
        my_name = "inner name"
        print("inner fun", my_name)

    innerfun()
    print("outer finished", my_name)


outerfun()
print("main", my_name)
