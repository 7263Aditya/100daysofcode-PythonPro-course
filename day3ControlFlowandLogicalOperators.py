#Conditional Statements

# if
# elif
# else
# and
# or
# not
# x = 10
# y = 20
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x and y are equal")

# print(not (x == y))  # True because it's the opposite of    
# "if x equals y" which is false. So, "not (x==y)" will be true.
# Nested Conditionals

# if condition:
#     do this
# else:
#     do that

# Example

# if x == y:
#     print("x and y are equal")
# else:
#     if x < y:
#         print("x is less than y")
#     else:
#         print("x is greater than y")

#Comparison operators

# == equal to
# != not equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# Nested If else statements

#Leap Year Calculator:
# Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year%4==0:
#   # print("Leap year.")
#   if year%100==0:
#     # print("Leap year.")
#     if year%400==0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")


#Multiple if statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")

#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")



# Logical Operators  

# A and B
# C or D
# not E

# a = 12
# print(a>15)
# print(a>10)

# AND Operator
# print(a>10 and a<13)
# print(a>15 and a<13)

# OR Operator
# print(a<10 or a>13)
# print(a>15 or a<13)

# NOT operator
# print(not(a<10))
# print(not(a>15))


#Day 3 project: Treasure Island


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You have to choose Left or Right.")
choice = input().lower()
if choice == 'left':
    print("There is the river in front of you? What do you choose? Swim or wait.")
    choice = input().lower()
    if choice == 'wait':
        print("Which door do you choose? Red, Blue or Yellow.")
        choice = input().lower()
        if choice == 'yellow':
            print("You win!")
        elif choice == 'red':
            print("Burned by fire. Game Over.")
        elif choice == 'blue':
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    elif choice == 'swim':
        print("Attacked by trout. Game Over.")
    else:
        print("Game Over.")
elif choice == 'right':
    print("Fall into a hole. Game Over.")   


else:
    print("Wrong choice.")