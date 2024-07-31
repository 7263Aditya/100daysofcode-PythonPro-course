# Day 2 project: Tip Calculator


#Day 2 Lesson: Datatypes and string manipulation

# print("Hello"[4])
# print("123"+"345")

# #integer

# print(123 + 345)

123_456_789

#float
3.14159

#boolean
True
False

#string
"Hello"
'World'

#string concatenation
"Hello" + "World"

#string multiplication
"Hello" * 10

#string indexing
"Hello"[0]

#string slicing
"Hello"[0:5] #0, 1, 2, 3, 4, 5
"Hello"[:5] #0, 1, 2, 3, 4, 5
"Hello"[5:] #5, 6, 7, 8, 9, 10

#capitalization
"hello".upper()
"HELLO WORLD".lower()

#checking if a character is inside a string
"Hello" in "Hello World"
"H" not in "Hello World"

#finding the position of a substring
"Hello".find("o")
"Hello".rfind("o")
"Hello".index("l")
"Hello".rindex("l")

#counting occurrences of a substring
"Hello".count("o")
"Hello".count("l", 1)

#Type Error, TypeChecking and TypeConversion
# num_char = len(input("what is your name? "))
# print(type(num_char))
# print("your name has " + str(num_char) +" characters")

# a = str(123)
# print(type(a))

# print(70 + float("100.3"))
# print(str(70) + str(100))

# #Exercise

# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# # Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# # The last line of your program should print the result.
# #Solution:
# # try checking the type of the two_digit number first

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# # Add the two integers together
# two_digit_number = first_digit + second_digit

# print(two_digit_number)
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# print(int(two_digit_number[0])+int(two_digit_number[1]))



#Mathematical operations in python
# print(3+5) # Addition
# print(7-4) # subtraction
# print(3*2) # multiplication
# print(6/3) # dividation
# print(2**3) # Square

# Order of priority
# PEMDAS
# Parentheses -> Exponents -> Multiplications and Divisions -> Additions and Subtractions

# print(3 * (3 + 3) / 3 - 3)


#BMI Calculator
# 1st input: enter height in meters e.g: 1.65
# height = float(input())
# # 2nd input: enter weight in kilograms e.g: 72
# weight = float(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# print("Your BMI is " + str(weight/(height)**2))
# print(round(int(weight)/(float(height))**2))


#Number manipulation and fstrings in python
# print(round(2.6666666666, 2))
# print(4/2)


#fstrings
# score = 0
# height= 1.8
# isWinning= True
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#LifeinWeeks
# age = input()
# years = 90 - int(age)

# print(f"You have {(90-int(age))* 52} weeks left.")


#Day 2 project: Tip Calculator


print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_for_split = int(input("How many people to split the bill?"))
print("Each person should pay: $" + str(round((bill * (1 + tip / 100)) / people_for_split, 2)))
