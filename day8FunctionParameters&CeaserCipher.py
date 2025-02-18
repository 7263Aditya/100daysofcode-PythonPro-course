# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.


# # def greet(name):
# #   print(f"Hello,{name}")
# #   print(f"How do you do {name}?")
# #   print("Isn't the weather nice today?")

# # greet("Aditya")

# # Positional Arguments
# # def greet_with(name,location):
# #   print(f"Hello {name}")
# #   print(f"What is it like in {location}")

# # greet_with("John","London")

# def greet_with(name,location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}")


# greet_with("Aditya", "Pune")

# # Keyword Arguments

# def greet_personalized(name, location):
#     print(f"Hello {name}")
#     print(f" What is it like in {location}")

# greet_personalized(location= "Pune", name = "Aditya")


# Write your code below this line 👇
# import math
# def paint_calc(height,width,cover):
#   num_of_cans = (test_h*test_w)/coverage
#   print(f"You'll need {math.ceil(num_of_cans)} cans of paint.")



# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# prime number checker
# Write your code below this line 👇
# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0 :
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")


# # Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input()) # Check this number
# prime_checker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
  
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_end = True
while should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
  if restart == "no":
    should_end = False
    print("Bye User👋")