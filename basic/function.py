# def test():
#     pass

#
# def test():
#     return "Hello python"
#
#
# print(test())

#
# def addsub(x, y):
#     add = x + y
#     sub = x - y
#     return [add, sub]
#
#
# data = addsub(5, 7)
# print(data[0])
# print(data[1])


# def introduction():
#     """
#     this is introduction function
#
#     """
#     return "hi"


# print(introduction.__doc__)
# print(introduction.__name__)


# def introduction(name, age=0):
#     print(name)
#     print(age)
#
#
# introduction('ram')

# * array argument
# ** keyword argument

# def test(x, *data, **abc):
#     print(data)
#     print(abc)
#
#
# test(1, 2, 4, 5, 6, 7, 8, 9, name='ram')
#
# print()

# x = 10
#
#
# def test():
#     global x
#     x = x + 20
#     print(x)
#
#
# test()


# def takeValue():
#     p = int(input("Enter p: "))
#     t = int(input("Enter t: "))
#     r = int(input("Enter r: "))
#     return [p, t, r]
#
#
# def calculate():
#     data = takeValue()
#     x = data[0]
#     y = data[1]
#     z = data[2]
#     return x * y * z / 100
#
#
# def result():
#     print(calculate())
#
#
# result()

#
# def my_rep(data, times):
#     x = 0
#     while x < times:
#         print(data)
#         x += 1
#
#
# dt = input("Enter any data: ")
# tm = int(input("Number of times: "))
# my_rep(dt, tm)


# def pr(data):
#     print(data)
#
#
# pr("Hello")


# def dell():

# def names(*name, **nm):
#     print(name)
#     print(nm)
#
# names('ram', 'shyam', 'hari', name='sita', age=20,)

# x = 10
#
#
# def data():
#     global x
#     print(x)
#     y = x + x + 5
#     print(y)
#
#
# data()

# def test():

# def test():
#     def data():
#         def get():
#             return "hello man"
#
#         return get
#
#     return data
#
#
# a = test()
# dt = a()
# mt = dt()
#
# print(mt)
#
# def get_name():
#     num_of_student = int(input("Enter number of student:"))
#     students = []
#     x = 0
#     while x < num_of_student:
#         name = str(input("Enter name:"))
#         students.append(name)
#         x += 1
#
#     return students
#
#
# def display():
#     for name in get_name():
#         print(name)
#
#
# display()

# def display():/)


# def total_number(*number):
#     size_of_array = len(number)
#     x = 0
#     sum = 0
#     evn_total = 0
#     odd_total = 0
#     while x < size_of_array:
#         if number[x] % 2 == 0:
#             evn_total += number[x]
#         else:
#             odd_total += number[x]
#         sum += number[x]
#         x += 1
#
#     print(f"Total number: {sum}")
#     print(f"Total Even: {evn_total}")
#     print(f"Total Odd : {odd_total}")
# total_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#
# def take_mask():
#     number_of_student = int(input("Enter number of students: "))
#     x = 1
#     students = []
#     while x <= number_of_student:
#         print(f"======Student {x}")
#         st_mks = []
#         for mask in range(0, 5):
#             ms = int(input("Enter mask: "))
#             st_mks.append(ms)
#
#         students.append(st_mks)
#         x += 1
#
#     return students
#
#
# def display():
#     result = []
#     for student in take_mask():
#         total = 0
#         for st in student:
#             total += st
#
#         result.append(total)
#
#     for rs in result:
#         print(f"Result: {rs}")
#
#
# display()

#
# def my_function():
#     print("Hello")
#
#
# a = my_function
# a()

# def function(any_function):
#     def inner_function(x, y):
#         if x == 0:
#             return "Enter any number"
#         return any_function(x, y)
#
#     return inner_function
#
#
# @function
# def test(x, y):
#     return x + y


# print(test(10, 20))

from functools import wraps


def get_doc(function):
    def inn_fun():
        print(function.__doc__)

    return inn_fun

def zero_check(function):
    def inn_fun():
        print(function.__doc__)

    return inn_fun


@get_doc
@zero_check
def insert():
    """
    insert methods
    """
    return "insert"


def update():
    x=110
    x+=10
    """
        update methods
        """

    return "update"


def select():
    """
        select methods
        """
    return "select"


def delete():
    """
        delete methods
        """
    return "delete"



insert()