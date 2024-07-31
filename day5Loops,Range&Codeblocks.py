#for loop

#for item in list_of_items:
  #Do something to each item


# Program to find the average height of the students

# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇

# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")

# number_of_students= 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")

# average_height = round(total_height/number_of_students)
# print(f"average height = {average_height}")


# Highest score in the list

# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# highest_score = student_scores[0]
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print(f"The highest score in the class is: {highest_score}")


# For loop using Range() function

# for number in range(1,101, 3):
#     print(number)

# for calculating numbers from the 1 to 100
# total = 0
# for number in range(1,101):
#     total += number
# print(total)

# for calculating even number by given range
# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇
# total = 0
# for number in range(2, target+1, 2):
#   total += number 
# print(total)
# target = int(input())
# alternative_sum = 0
# for number in range(1, target+1):
#     if number % 2 == 0:
#         alternative_sum += number
# print(alternative_sum)


#Fizzbuzz number printing
# Write your code here 👇
# target = int(input())
# for number in range(1, target+1):
#   if number % 3 == 0  and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
  


# Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)


# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")