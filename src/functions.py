"""
def fun():
    print("Hello")

x = fun()
print(x)


def add(a, b=5):
    return a + b

print(add(3))
print(add(3, 2))


x = 10

def test():
    x = 20
    print(x)

test()
print(x)


def outer():
    def inner():
        return "Inside"
    return inner()

print(outer())


def func(lst=[]):
    lst.append(1)
    print(lst)

func()
func()


def calc(a, b):
    print(a + b)
    return a * b

x = calc(2, 3)
print(x)


def rec(n):
    if n == 0:
        return 0
    print(n)
    rec(n-1)

rec(3)


def change(x):
    x = x + 5
    return x

a = 10
change(a)
print(a)
"""