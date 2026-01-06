
# print(min( 12, -5, 7 )) 
# print(len("hello, world"))
# x = -17.89
# print(abs(x))
# print(round(x))
# nums = [4, 7, 10, 2, 6]
# print(max(nums))
# print(min(nums))
# print(len(nums))
# print(sum(nums))
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# number=(5, 10, 2)
# len = len(number)
# print(sum(number))
# sum = sum(number)
# znach=sum/len
# print(znach)
# print(max(number))
# print(min(number))

# def greet(leaning):
# #     print("i`m learning python")
# def say_hi():
#     print("Привет!")
# say_hi()    

# def greeting():
#     print("privet")
# greeting()    

# def greetingname(name):
#     print("hello" , name )
# greetingname("shaxzoda")    

# def square (x):
#     return x * x
# print(square(9))

# def plus (x, y):
#     return x + y 
# print(plus(5, 8))

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius + 9/5) + 32
#     return fahrenheit
# # print(celsius_to_fahrenheit(10))

# # def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# # Test conversions
# c1 = 0
# f1 = celsius_to_fahrenheit(c1)
# print(f"{c1}°C = {f1}°F")

# c2 = 100
# f2 = celsius_to_fahrenheit(c2)
# print(f"{c2}°C = {f2}°F")

# f3 = 32
# c3 = fahrenheit_to_celsius(f3)
# print(f"{f3}°F = {c3}°C")

# f4 = 212
# c4 = fahrenheit_to_celsius(f4)
# print(f"{f4}°F = {c4}°C")

# def hours_to_minutes(hours):
#     minutes = 60 * hours
#     return minutes 

# def minutes_to_hours(minutes):
#     hours = minutes * 1/60
#     return hours 

# # h1 = 1
# # m1 = (hours_to_minutes(h1))
# # # print(f"{h1} hours = {m1} minutes")

# def area_of_rectangular(width, height):
#     area = width * height
#     return area

# def perimeter_of_rectangular (width, height):
#     perimeter = 2 * (width + height)
#     return perimeter

# w=float(input("enter width:"))
# h=float(input("enter height:"))

# area = area_of_rectangular(w,h)
# perimeter = perimeter_of_rectangular(w,h)
# print(f"rectangle {w}*{h}: ")
# print("Area:",  area )
# print("perimeter:" , perimeter)







































# quiz_scores = [88, 90, 54, 89, 100]
# print("there is" , quiz_scores)
# first_st_score = quiz_scores[0]
# last_st_score = quiz_scores[-1]
# difference = quiz_scores[-1]-quiz_scores[0]
# print("the first student get" , first_st_score)
# print("the last student score:" , last_st_score)
# print("difference between them", difference)



# used_money=[100, 80, 55, 67, 86]
# total_expences = 0.0
# for expence in used_money:
#     total_expences += expence 
# print("total monthly expensces: $", total_expences)     


# things = [12, 56, 78, 90, 34]
# print("initial numbers", things)
# # things.append(55)
# # print(things)
# things.insert(1, 22)
# print(things)
# things.remove(12)
# print(things)
# things.pop()
# print(things)
# things[1] = 13
# print(things)



# names = ['alex', 'feliz', 'anna' , 'timur', 'mary', 'irina']
# # last = names[2:]
# # print(last)
# last = names[:3]
# print(last)
# last=names[1::2]
# print(last)

# filter_high_scores=[88, 91, 75, 99, 82]
# last=filter_high_scores[1::2]
# print(last)

# filter_high_scores=[10, 25, 50, 75]
# lasr=filter_high_scores[2:]
# print(lasr)



# Write a program that checks if a student is eligible for the dean’s list.

# # Requirements:

# # Ask for: student name, GPA (0.0-4.0), total credit hours
# # Dean’s list requirements:
# # GPA >= 3.5 AND credit hours >= 12
# # Display:
# # Student information
# # Whether they made the dean’s list (True/False)
# # How many more GPA points needed (if GPA < 3.5)
# # How many more credits needed (if credits < 12)


item1=input('enter you first item:')
item1_price=int(input('enter the price:'))
item1_quantity=int(input('enter the quantity'))
all1= item1_price*item1_quantity

item2=input('enter you second item:')
item2_price=int(input('enter the price:'))
item2_quantity=int(input('enter the quantity'))
all2= item2_price*item2_quantity

item3=input('enter you third item:')
item3_price=int(input('enter the price:'))
item3_quantity=int(input('enter the quantity'))
all3=item3_price*item3_quantity

subtotal=all1+all2+all3
total_items=item1_quantity+item2_quantity+item3_quantity

name=input('enter your name:')
is_member=input('are you member? (yes/no)').lower()                          
is_member = (is_member == "yes")
total_previour_purchase=input('enter your total previous purchase:')

member_discount=is_member*0.1*subtotal
if total_items>5:
    bulk_discount=0.05*subtotal
if total_previour_purchase >= 1000000:
    loyalty_discount=0.03*subtotal


# Specific Requirements:

# Collect: Item name, price, and quantity for 3 electronics items
# Get customer information: Name, is_member (yes/no), total_previous_purchases (in sum)
# Discount Rules: Calculate eligibility and amounts for each discount type:

# Member discount: 10% off subtotal (eligible if customer is a member)
# Bulk discount: 5% off (eligible if total items > 5)
# Loyalty discount: 3% off (eligible if total_previous_purchases >= 1000000)
# All discounts stack - apply them sequentially using boolean arithmetic
# Other Calculations:

# Tax rate: 12% applied to subtotal after all discounts
# Shipping: 25000 sum (but 0 if subtotal > 500000)
# Calculate using: shipping = (subtotal <= 500000) * 25000
# Output must show:

# Customer name and membership status
# Itemized list of all 3 purchases (item, quantity, price, total)
# Subtotal before discounts
# Each discount type with:
# Eligibility status (True/False)
# Discount amount (will be 0 if not eligible)
# Total discounts applied
# Subtotal after discounts
# Tax amount
# Shipping cost with free shipping status (True/False)
# Final total
# Total amount saved



