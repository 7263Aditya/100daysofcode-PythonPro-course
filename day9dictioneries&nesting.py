#dictionary
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades={}
 
 
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student]= "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log.

# def add_new_country(country_name, times_visited, cities_visited):
#     new_country= {}
#     new_country["country"] = country_name
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)


# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")


# Day 9 challenge
from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = True


def finder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid of the amount {highest_bid}")


while bidding_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidder? Type 'yes' or 'no'.")
  if should_continue == "no":
    bidding_finished = False
    finder(bids)
  elif should_continue == "yes":
    clear()
