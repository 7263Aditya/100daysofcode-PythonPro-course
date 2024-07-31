# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month == 2 and is_leap(year):
#     return 29
#   else:
#     return month_days(month - 1)

  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)



# #or printing output directly
# # print(format_name((input("What is your first name? "),input("What is your last name?"))

# #Already used functions with outputs/
# formatted_name= "kjasnduf"
# length = len(formatted_name)


# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of time"""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name?"),input("What is your last name?")))

#This is comment
# a = """
# This is 
# Multiline comment
# """

# print(a)


#or printing output directly
# print(format_name((input("What is your first name? "),input("What is your last name?"))

# #Already used functions with outputs/
# formatted_name= "kjasnduf"
# length = len(formatted_name)


# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of time"""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name?"),input("What is your last name?")))

#This is comment
# a = """
# This is 
# Multiline comment
# """

# print(a)

#Calculator

#Calculator


#Add
def add(n1,n2):
  return n1+n2

#subtract
def subtract(n1,n2):
  return n1-n2

# multiply
def multiply(n1,n2):
  return n1*n2

#divide
def divide(n1,n2):
  return n1/n2

#dictionary
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = float(input("What is the first number?\n"))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue: 
    operation_symbol = input("Pick an operation\n")
    num2 = float(input("What is the second number?\n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with answer {answer}:\n") == "y":
      num1 = answer
    else:
      should_continue = False
    
    operation_symbol = input("Pick another operatiom:")
    num3 = int(input("What is the next number?"))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(answer, num3)
    
    print(f"{answer} {operation_symbol} {num3} = {second_answer}")

calculator()
 