"""
x = 10
y = 20
if x > y:
    print("A")
elif x == 10:
    if y < 15:
        print("B")
    else:
        print("C")
else:
    print("D")

o/p: C 


x = 5
y = 10
if x < y:
    print("A")
if x == 5:
    print("B")
else:
    print("C")

o/p: A
     B


a = 7
b = 7
if a > b:
    print("X")
elif a == b:
    print("Y")
else:
    print("Z")

o/p : Y


num = 12
if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Only divisible by 2")
else:
    print("Odd")

o/p: Divisible by 2 and 3


x = 0
if x:
    print("True")
else:
    print("False")

o/p: False


a = -5
if a > 0:
    print("Positive")
elif a:
    print("Non-zero")
else:
    print("Zero")

o/p: Non-Zero


x = 15
if x > 10:
    print("A")
    if x < 20:
        print("B")
elif x == 15:
    print("C")
else:
    print("D")

o/p: A 
     B 


x = 8
if x % 2 == 0:
    print("Even")
if x % 4 == 0:
    print("Divisible by 4")
else:
    print("Not divisible by 4")

o/p: Even 
     Divisible by 4


a = 10
b = 5
if a > b:
    if b > 2:
        if a - b == 5:
            print("Yes")
        else:
            print("No")
    else:
        print("Maybe")
else:
    print("Never")

o/p: Yes
"""