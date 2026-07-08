"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
print(response.json()["name"])





import requests

response = requests.get("https://jsonplaceholder.typicode.com/abc")

print(response.status_code)
print(response.ok)





import requests

data = {
    "title": "Python",
    "body": "API Practice",
    "userId": 5
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json()["title"])





import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/3")

todo = response.json()

print(type(todo))
print(todo["completed"])




import requests

try:
    response = requests.get(
        "https://wrong-url.com",
        timeout=2
    )
    print(response.status_code)
except requests.exceptions.RequestException:
    print("Request Failed")





import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

posts = response.json()

print(type(posts))
print(len(posts))
print(posts[0]["id"])




import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

print(users[0]["name"])
print(users[-1]["id"])
print(len(users))
"""