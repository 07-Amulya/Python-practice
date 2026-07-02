"""
marks = {"Math": 90, "Science": 80}
marks["Science"] += 10
print(marks)



employee = {"id": 101}
employee["name"] = "Amulya"
print(employee)



car = {"brand": "BMW", "year": 2020}
x = car.pop("year")
print(x)
print(car)



user = {"name": "John"}
print(user.get("age", 25))


profile = {"city": "Chennai"}
profile.update({"city": "Delhi", "age": 22})
print(profile)



data = {"a": 1, "b": 2}
for i in data:
    print(i, data[i])


student = {
    "name": "Raj",
    "marks": {"math": 95}
}
print(student["marks"]["math"])

"""