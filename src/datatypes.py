'''
x = 10
y = 10.0
print(type(x + y))

x = 10
y = 10.0
print(type(x + y))

x = "100"
y = 50
print(int(x) + y)

x = "25"
y = 5
print(x - y)

x = 5
y = 2
print(x / y)
print(x // y)
print(type(x // y))

x = 3 + 4j
print(type(x))
print(x.real)
print(x.imag)

a = 10
b = a
a = 20
print(a, b)

a = 257
b = 257
print(a is b)

a = 10
b = 10
print(a is b)

x = None
print(type(x))
print(x == 0)

x = "5"
print(x * 3)

x = float("10")
y = int(5.9)
print(x, y)

x = bool("")
y = bool("Hello")
print(x, y)

x = int(True)
y = int(False)
print(x + y)

x = int("10.5")
print(x)

x = str(100)
y = str(200)
print(x + y)

x = 10
print(id(x))
x = x + 1
print(id(x))

x = complex(5)
print(x)
print(type(x))

x = 5
y = "5"
print(str(x) == y)
'''

x = bool(0)
y = bool(-1)
z = bool(1)
print(x, y, z)