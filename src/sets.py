"""
customers = {"A101", "A102", "A103"}
new_customers = {"A102", "A104"}
customers.update(new_customers)
print(customers)



day1 = {"Ram", "Sita", "Arun"}
day2 = {"Sita", "Kiran", "Ram"}
print(day1 & day2)



stock = {"pen", "pencil", "eraser"}
sold = {"pen", "eraser"}
print(stock - sold)



items = {"apple", "banana", "grapes"}
items.remove("banana")
items.add("orange")
print(items)



permissions = {"read", "write"}
if "delete" in permissions:
    print("Allowed")
else:
    print("Denied")



marks = [90, 80, 90, 70, 80]
unique_marks = set(marks)
print(len(unique_marks))


colors = {"red", "blue", "green"}
x = colors.pop()
print(x)
print(colors)
"""