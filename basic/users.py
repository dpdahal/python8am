# import os
# from getpass import getpass
#
# if not os.path.exists('database.txt'):
#     fh = open('database.txt', 'w')
#     fh.close()
#
#
# def register():
#     username = input("Enter username: ")
#     if username in open('database.txt', 'r').read():
#         print("Username already exists")
#         exit()
#     password = getpass("Enter password: ")
#     c_password = getpass("Enter confirm password: ")
#     if password != c_password:
#         print("Password not match")
#         exit()
#
#     handle = open('database.txt', 'a')
#     handle.write(username)
#     handle.write(" ")
#     handle.write(password)
#     handle.write("\n")
#     handle.close()
#     print("User was successfully inserted")
#     exit()
#
#
# def login():
#     username = input("Enter username: ")
#     password = getpass("Enter password: ")
#     get_record = open('database.txt', 'r').readlines()
#     users = []
#     for user in get_record:
#         users.append(user.split())
#
#     total_users = len(users)
#     increment = 0
#     login_success = False
#     while increment < total_users:
#         uname = users[increment][0]
#         pas = users[increment][1]
#         if username == uname and password == pas:
#             login_success = True
#
#         increment += 1
#
#     if login_success == True:
#         print(f"Welcome {username}")
#     else:
#         print("Username & password not match")
#
#
# question = input("Do you have an account y/n: ")
#
# if question == 'y':
#     login()
# else:
#     register()


import csv

with open('data.csv', 'w', newline='') as files:
    header = ['s.n', 'name', 'age', 'address']
    fs = csv.DictWriter(files, fieldnames=header)
    fs.writeheader()
    fs.writerow({'s.n': 1, 'name': 'ram', 'age': 20, 'address': 'ktm'})
    fs.writerow({'s.n': 2, 'name': 'sita', 'age': 22, 'address': 'ktm'})

# print(dir(csv))
# with open('data.csv', 'r') as file:
#     get_data = csv.reader(file)
#     for user in get_data:
#         print(user)
