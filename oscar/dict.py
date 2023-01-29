# declaring a dictionary
# each key should be unique
content = {
    "name": "oscarlincoln",
    "email":"oscarlincoln520@gmail.com",
    "age": 23,
    "is_verified": True
}
# accessing items in the dictionary
# we can also use the get method to access items in the dictionary and also supply a value
print(content["name"])
print(content.get("email"))
print(content.get("number", "0783438083"))