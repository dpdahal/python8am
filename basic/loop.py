# for, while, nested loop

# data = [
#     ['ram', 'sita', 'gita', 'hari'],
#     ['hari', 'admin', 'gopal', 'ramesh'],
#     ['madan', 'sophia', 'kabita', 'dinesh']
#
# ]
#
# for user in data:
#     for usr in user:
#         if usr=='admin' or usr=='kabita':
#             print(usr)


# x = 0
#
# while x < 10:
#     print(x)
#     x += 1

# num = int(input("Enter any number: "))
# x = 1
# even_total = 0
# odd_total = 0
# while x <= num:
#     if x % 2 == 0:
#         print(x)
#         even_total += x
#     else:
#         odd_total += x
#     x += 1
#
# print(f"Total Even: {even_total}")
# print(f"Total Odd: {odd_total}")


# num = int(input("Enter number of name: "))
# x = 1
# users = []
# while x <= num:
#     name = input('Enter name: ')
#     users.append(name)
#     x += 1
#
# print("================")
# for user in users:
#     print(user.upper())


num = int(input("Enter number of students: "))
x = 1
students = []
while x <= num:
    print(f"======Student {x}======")
    store_maks = []
    for i in range(0, 5):
        mask = int(input("Enter maks: "))
        store_maks.append(mask)

    students.append(store_maks)
    x += 1

result = []
total = 0

for ms in students:
    total_mask = 0
    for a in ms:
        total_mask += int(a)

    result.append(total_mask)

for res in result:
    print(f"Result: {res}")
