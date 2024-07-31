# import random

# random_int = random.randint(1, 100)
# print(random_int)
# print(my_module.pi)
# random_float = random.random()* 5
# print(random_float)

# score = random.randint(1, 100)
# print(f"Your score is {score}")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# print(dirty_dozen)


# Lists
# List = ["Fruit1","Fruit2"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# names = ["shubham","aditya","rohit","prateek","pravin","rajesh","sandeep","saurabh","sakshi","shreyas"]
# # The code above converts the input into an array separating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random
# print(f"{names[random.randint(0,(len(names)) - 1)]} is going to buy the meal today!")


#dirty dozen

# dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

# fruits = ["Straweberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
# vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)

#Rock Paper Scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose")
else:
    print(game_images[user_choice])
    Computer_choice = random.randint(0,2)
    
    print("Computer chose:")
    print(game_images[Computer_choice])
    
    
    if user_choice == 0 and Computer_choice == 2:
      print("You win")
    elif Computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif Computer_choice > user_choice:
      print("You lose")
    elif user_choice > Computer_choice:
      print("You win")
    elif Computer_choice == user_choice:
      print("It's a draw")