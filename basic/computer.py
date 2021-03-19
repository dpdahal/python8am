dell = 20000
mac = 50000
toshiva = 30000
total = 0
delPrice = 0
bag = 0
plastic = 0
gift_box = 0
tax_amount = 0

print("====================Computer Bazar======")
print("1. Dell (Rs:20000) 2. Mac(Rs:50000) 3. Toshiva (Rs:30000)")
ch = int(input("Enter any option: "))

if ch == 1:
    qt = int(input("Enter quantity: "))
    total = qt * dell

if ch == 2:
    qt = int(input("Enter quantity: "))
    total = qt * mac

if ch == 3:
    qt = int(input("Enter quantity: "))
    total = qt * toshiva

print("========1. Home (1000) 2. Pickup (free)")
delOpt = int(input("Enter option: "))
if delOpt == 1:
    delPrice = 1000

print("======1. Bab(1000) 2.Plastic (500) 3. Gift Box (5000) 4. none")
wriOpt = int(input("Enter option: "))

if wriOpt == 1:
    bag = 1000

if wriOpt == 2:
    plastic = 500

if wriOpt == 3:
    gift_box = 5000

print("=============1. Kathmandu (13%) 2. Lalitpur(Free) 3. Bhaktapur(Free)")
loc_option = int(input("Enter option: "))

if loc_option == 1:
    tax_amount = total * 13 / 100

gt = total + tax_amount + plastic + bag + gift_box + delPrice

print("============Result===========")
print(f"Total: {total}")
print(f"Tax: {tax_amount}")
print(f"GT: {gt}")


#
# print("=========1. Kalanki 2. Bask park")
#
# location = int(input("Enter location: "))
# students = 0
# old = 0
# client = 0
# fee = 0
# dis_total = 0
# if location == 1:
#     print("1.Student 2.Old 3. Client")
#     opt = int(input("Enter option: "))
#     if opt == 1:
#         dis_total = free = ''
#     if opt == 2:
#         dis_total = free = ''
