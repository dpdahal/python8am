# Data types: Integer, String
# INT - Integer
# x = 10.34
# print(dir(x))
# print(type(x))

# x = 10
# y = 30
#
# print(x + y)

# name = "ram"
# print(name)
# print(type(name))

# fName = "ram"
# lName = "abc"
# age = 20
# print(f"name {fName} age {age}")
# print("name {} age {}".format(fName, age))
# print('Name', fName, 'age', age)
# Format string


# print(fName + " " + lName)

# a = "40"
# print(type(a))
#
# x = int(input("Enter any number: "))
# y = int(input("Enter any number: "))
# x = int(x)
# print(type(x))
# print(x + y)
# print(type(x))

# x = True
# y = False
# z = None

# p = 10
# t = 10
# r = 10
# result = p * t * r / 100
#
# print(result)

# [] - list, starting: 0

# data = ["ram", 1234, "x", "sita", "hari", "gita"]
# data[1] = "rita"
# print(data[1])
# print(type(data))

# print(dir(data))
#
# users = [
#     ["Ram", "sita", "gita"],
#     ["Laxmi", "binita", "Kabita"],
#     ["Madan", "Hari", "pradip", [["Sophia"]]]
# ]
#
# print(users[2][1])

# data = (
#     ("ram", 'sita''hari'),
#     ("A", "B", "C")
# )


# print(data[1][2])
# print(type(data))
# print(dir(data))


# data = {"Ram", 'Sita', 'Gita', 'Ram'}
#
# print(data)

# user = {"name": "sophia", "age": 20, "address": "ktm"}
#
# print(user['name'])

users = [
    {"name": "sophia", "age": 20, "address": "ktm"},
    {"name": "gita", "age": 24, "address": "ltp"},
    {"name": "gita", "age": 24, "address": [
        {"loc": "bkt"}
    ]}
]

print(users[2]['address'][0]['loc'])

# print(users[1]['address'])
