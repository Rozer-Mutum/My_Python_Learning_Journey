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

# Day3
# conditional statements, logical operators, code blocks and scope
# syntax if-else statement
if condition:
   do this
else:
   do this

# Write a program that works out whether if a given number is an odd or even number.

#% gives the remainder of the division
number = int(input("Which number do you want to check? "))
if (number%2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

height = float(input("Enter your height in m:  "))
weight = float(input("Enter your weight in kg:  "))
#using round to get to one decimal in output
bmi = round((weight)/(height)**2, 1)
if (bmi<18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
elif (bmi<25):
    print(f"Your BMI is {bmi}, you are in normal weight.")
elif (bmi<30):
    print(f"Your BMI is {bmi}, you are overweight.")
elif (bmi<35):
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#Write a program that works out whether if a given year is a leap year.
on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

print("Checking for a leap year")
year = int(input("Enter the year you want to check "))
if (year%4==0):
    if(year%100==0):
        if (year%400==0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

#rollercoaster ride cost calculator
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if (height >= 120):
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if (age < 12):
    bill = 5
    print("Child tickets are $5.")
  elif (age <= 18):
    bill = 7
    print("Youth tickets are $7.")
  elif (age>=35 and age>=45):
    print("Your ticket is free. Please enjoy the ride!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if (wants_photo == "Y" or "y" or "Yes" or "yes"):
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

#Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

#Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $28.

print("Welcome to the Python Pizza Delivery!!!")
pizza_size = input("What size of pizza you want? | S M L | ")
add_pepparoni = input("Do you like to add pepparoni? | Y or N | ")
extra_cheese = input("Do you like to add extra cheese? | Y or N | ")
bill=0
if (pizza_size=="S"):
    bill+=15
elif (pizza_size=="M"):
    bill+=20
elif (pizza_size=="L"):
    bill+=25
else:
    print(f"Not valid\nPlease provide in capital S or M or L")
if (add_pepparoni=="Y"):
    if (pizza_size=="S"):
        bill+=2
    elif (pizza_size=="M"or"L"):
        bill+=3
if (extra_cheese=="Y"):
    bill+=1
print(f"Total bill is ${bill}")


#You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
#combining the strings
combine_name = name1+name2
#convert to lowercase letter
combine_name_lowecase = combine_name.lower()
#counting occurence of word in the combined strings
t = combine_name_lowecase.count("t")
r = combine_name_lowecase.count("r")
u = combine_name_lowecase.count("u")
e = combine_name_lowecase.count("e")
#convert to string
total1 = str(t+r+u+e)
l = combine_name_lowecase.count("l")
o = combine_name_lowecase.count("o")
v = combine_name_lowecase.count("v")
e = combine_name_lowecase.count("e")
total2 = str(l+o+v+e)
#combining the number in the form of string and convert to integer to use in if statement
love_score = int(total1+total2)
if (love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (40<=love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}, try your luck.")

# treasure_hunt
see treasure_hunt.py
\ backslash to escape

#ascii_art
https://ascii.co.uk/art
Ctrl+F and search the desire ascii