import os, sys, math
from datetime import datetime, timedelta
from collections import Counter, defaultdict

PI = 3.14159


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Average:", self.average())
        print("Grade:", self.grade())


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(limit):
    a, b = 0, 1
    result = []
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    return result


def even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


def square_numbers(nums):
    return list(map(lambda x: x * x, nums))


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")


def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)


def calculate_circle(radius):
    area = PI * radius**2
    circumference = 2 * PI * radius
    return area, circumference


def word_count(sentence):
    words = sentence.lower().split()
    return Counter(words)


def create_dictionary(keys, values):
    return dict(zip(keys, values))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = square_numbers(numbers)
evens = even_numbers(numbers)

student1 = Student("Amulya", 22, [89, 92, 95, 87, 91])

student1.display()

print(factorial(5))

print(fibonacci(50))

print(evens)

print(squares)

print(divide(10, 2))

print(divide(10, 0))

area, circumference = calculate_circle(5)

print(area, circumference)

sentence = "python is easy python is powerful and python is fun"

print(word_count(sentence))

keys = ["id", "name", "city", "salary"]
values = [101, "John", "Bangalore", 50000]

employee = create_dictionary(keys, values)

print(employee)

for i in range(5):
    print(i)

for num in numbers:
    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten = [item for row in matrix for item in row]

print(flatten)

data = {"apple": 10, "banana": 5, "orange": 12}

for key, value in data.items():
    print(key, value)

today = datetime.now()

future = today + timedelta(days=7)

print(today)

print(future)

count = defaultdict(int)

for char in "mississippi":
    count[char] += 1

print(count)

try:
    x = int("100")
    y = int("abc")
except ValueError as e:
    print(e)
finally:
    print("Finished")


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting Function")
        result = func(*args, **kwargs)
        print("Ending Function")
        return result

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Amulya")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


r = Rectangle(10, 5)

print(r.area)

generator = (i * i for i in range(10))

for value in generator:
    print(value)

unique = {1, 2, 2, 3, 4, 5, 5, 6}

print(unique)

tuple_data = (10, 20, 30)

a, b, c = tuple_data

print(a, b, c)

print(os.getcwd())

print(sys.version)

print(math.sqrt(144))

print("Program Completed")
