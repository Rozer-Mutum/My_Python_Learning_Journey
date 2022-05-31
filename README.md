# DAY_1
# trying out print function
print("DAY 1 - Python Print Function")
print("The function is declared like this:")
print("print('what want to print')")

#passing \n to print in new line
print("This is the first line \nThis is the second line")

#adding two strings using + sign
print("Hello" + " " + "Tom")
print("Hello" + " Tom")

# input() will get user input
# here taking input and printing
print("Hello " + input("Type name"))

# debugging practice 
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# taking user input
# calculate length of a string
print(len(input("Type any string ")))

#using variable, printing length of a stirng 
name = input("Type any string ")
length = len(name)
print(length)

# variable exercise
# 🚨 Don't change the code below 👇
from calendar import c

a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
# ouput should be interchange of input

# band name generator exercise
print("Welcome to the Band name generator")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet name?\n")
print("Your band name could be " +city_name,pet_name)

#DAY_2
#Data types, numbers, operation, type conversion , f-strings

#Data_types
#String
print("Hello"[0])
#this give output "H"
print("123" + "456")
#Output = "123456"

#Integer
print(123 + 456)
#Output = 579

#Float
3.14

#boolean
true false

# use this command to know the data type
print(type(variable_name))

PEMDASLR
parenthesis ()
exponential **
multiplicatio * | division /
addition +
subtraction -
# Note: Calculation goes from left to right in * and /
example1 : 2*2+6/3 = 4+6/3 =4+2 =6
example2 : 2/2+6*3 = 1+6*3 =1+2 =3


# how to write power
2**3
# Output = 8

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# taking input from user
number = input("Enter two digit numbers: ")
# taking the first digit and second digit (subscript) from string and convert to integer 
first_digit = int(number[0])
second_digit = int(number[1])
# adding the two integers
adding_each_digit = first_digit + second_digit
print(adding_each_digit)

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
height = input("Enter your height in m:  ")
weight = input("Enter your weight in kg:  ")
bmi = int(weight)/float(height)**2
print(int(bmi))

# using f-string to pass all the data types in {}
score = 1
height = 1.6
isWinning = True
print(f"Your score is {score}, your height is {height}, your winning is {isWinning}")
# output = Your score is 1, your height is 1.6, your winning is True

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
current_age = input("What is your current age? ")
expected_lifespan = input("Expected lifespan ")
# calculating the remaining years
remaining_year = int(expected_lifespan)-int(current_age)
# 1 year = 365 days = 52 weeks = 12 months
days = remaining_year*365
weeks = remaining_year*52
months = remaining_year*12
print(f"You have {days} days, {weeks} weeks, and {months} months upto {expected_lifespan} years")
# input1 = 56, input2 = 90
# output = You have 12410 days, 1768 weeks, and 408 months upto 90 years

# exercise
print("Welcome to the tip calculator")
# taking user input string and convert to float
total_bill = float(input("What was the total bill? $"))
# here in integer for number of total_people
total_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage of tip you would like to give? 10, 12 or 15? "))
# calculating only the tip amount 
tip_amount = float((tip_percent*total_bill)/100)
# total amount divided by no of person and and rounding to two decimal
# total_with_tip = round((total_bill + tip_amount)/total_people, 2) | this does not give 0 at the second decimal
total_with_tip = "{:.2f}".format((total_bill + tip_amount)/total_people) #convert into string
print("Each person should pay: $" +str(total_with_tip))

#                                                              Day3
#                                 conditional statements, logical operators, code blocks and scope
# syntax if-else statement
if condition:
   do this
else:
   do this
