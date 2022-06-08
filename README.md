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

#input() will get user input
#here taking input and printing
print("Hello " + input("Type name"))

#debugging practice 
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#taking user input
#calculate length of a string
print(len(input("Type any string ")))

#using variable, printing length of a stirng 
name = input("Type any string ")
length = len(name)
print(length)

#variable exercise
#🚨 Don't change the code below 👇
from calendar import c

a = input("a: ")
b = input("b: ")
#🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

#🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
#ouput should be interchange of input

#band name generator exercise
print("Welcome to the Band name generator")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet name?\n")
print("Your band name could be " +city_name,pet_name)

# DAY_2
# Data types, numbers, operation, type conversion , f-strings

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
#Note: Calculation goes from left to right in * and /
example1 : 2*2+6/3 = 4+6/3 =4+2 =6
example2 : 2/2+6*3 = 1+6*3 =1+2 =3


#how to write power
2**3
#Output = 8

#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#taking input from user
number = input("Enter two digit numbers: ")
#taking the first digit and second digit (subscript) from string and convert to integer 
first_digit = int(number[0])
second_digit = int(number[1])
#adding the two integers
adding_each_digit = first_digit + second_digit
print(adding_each_digit)

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
height = input("Enter your height in m:  ")
weight = input("Enter your weight in kg:  ")
bmi = int(weight)/float(height)**2
print(int(bmi))

#using f-string to pass all the data types in {}
score = 1
height = 1.6
isWinning = True
print(f"Your score is {score}, your height is {height}, your winning is {isWinning}")
#output = Your score is 1, your height is 1.6, your winning is True

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.
current_age = input("What is your current age? ")
expected_lifespan = input("Expected lifespan ")
#calculating the remaining years
remaining_year = int(expected_lifespan)-int(current_age)
#1 year = 365 days = 52 weeks = 12 months
days = remaining_year*365
weeks = remaining_year*52
months = remaining_year*12
print(f"You have {days} days, {weeks} weeks, and {months} months upto {expected_lifespan} years")
#input1 = 56, input2 = 90
#output = You have 12410 days, 1768 weeks, and 408 months upto 90 years

# exercise
print("Welcome to the tip calculator")
#taking user input string and convert to float
total_bill = float(input("What was the total bill? $"))
#here in integer for number of total_people
total_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage of tip you would like to give? 10, 12 or 15? "))
#calculating only the tip amount 
tip_amount = float((tip_percent*total_bill)/100)
#total amount divided by no of person and and rounding to two decimal
#total_with_tip = round((total_bill + tip_amount)/total_people, 2) | this does not give 0 at the second decimal
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

# Day 4
#randomisation and python lists

# Random Module
https://en.wikipedia.org/wiki/Mersenne_Twister

#pythonask
https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#modules are already written function where one can called and use it.
#Random Number generation
import random
#generate any number between 1 and 10
random_number = random.randint(1,10)
print(f"{random_number}")

#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#e.g. 1 means Heads 0 means Tails
import random
#generating 0 and 1 randomly
random_number = random.randint(0, 1)
#checking condition
if (random_number==0):
  print("Tails")
else:
  print("Heads")
#To check output whether 0 or 1
#print(f"{random_number}")

# python lists/datastructure
Way of organising and storing data

#python.docs datastructure
https://docs.python.org/3/tutorial/datastructures.html

#sample fruit lists
fruit_lists = ["lemon", "orange", "apple"]
print(fruit_lists)
print(fruit_lists[1])

#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.

import random
from unicodedata import name
names_string = input("Give the names separated by , with a space.\n")
#separating the input by ", " and making into a list
names = names_string.split(", ")
#counting the number of person
number_of_person = len(names)
#generating random integer from 0 to one less than the number of person
random_number = random.randint(0, number_of_person-1)
#assigning the random number to the list to get random names from the list
person_paying_the_bill = names[random_number]
print(f"{person_paying_the_bill} is going to buy the meal today!")

import random
names_string = input("Give the names separated by , with a space.\n")
#separating the input by ", " and making into a list
names = names_string.split(", ")
#randomly pick names from the list
random_name = random.choice(names)
#print(names)
print(f"{random_name} is going to buy the meal today!")

#You are going to write a program which will mark a spot with an X.
#column 2, row 3 would be entered as:
#output
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
#nested list to easy replace inside list
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
#Taking user input to mark X
changing_place = input("Enter the column and row you want to replace with X.\n")  #23
#getting the column 
column = int(changing_place[0])  #2
row = int(changing_place[1])  #3
#from nested list, particular row is obtained
selected_row = map[row-1]  #map[3-1]               #map[row-1][column-1] = "X"
#replacing the X to the desire column in that row  #
selected_row[column-1] = "X"  #2-1                 #
print(f"{row1}\n{row2}\n{row3}")

# rock paper scissors game
rock_paper_scissors.py

# Day 5
# for loops, range and code blocks

#You are going to write a program that calculates the average student height from a List of heights.
#Average height rounded to the nearest whole number
#Important You should not use the sum() or len() functions in your answer.

#average height calculator
print("Welcome to the average height calculator program!")
heights_collect = input("Please enter the heights in metre separated by comma without spaces.\n")
#making a list of input heights by separating with referece to comma
height_lists = heights_collect.split(",")
#Taking how many number of person from the list
number_of_person = len(height_lists)
height_add = 0
#for loop in range
for n in range (0, len(height_lists)):
    height_add += int(height_lists[n])
#average = (Total height)/(number of person)
average = height_add/number_of_person
print(round(average))

#You are going to write a program that calculates the average student height from a List of heights.
print("Welcome to finding highest number in list using for loop program!")
numbers = input("Please enter the numbers separated by comma without spaces.\n").split(",")
highest_number = 0
for number in numbers:
    if (int(number) > int(highest_number)):
        highest_number = number
print(f"The highest number is {highest_number}")

#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
print("Adding all the even numbers from 1 to 100")
total = 0
for number in range(2, 101, 2):
    total+=number
print(f"The total of the even numbers is {total}")

#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#divisible by 3 = fizz
#divisible by 5 = buzz
#both divisible by 3 and 5 = fizzbuzz

print("Let's play FIZZBUZZ")
for number in range(1, 101):
    if (number%3==0 and number%5==0):
        print("Fizzbuzz")
    elif (number%3==0):
        print("Fizz")
    elif (number%5==0):
        print("Buzz")
    else:
        print(number)

#*******************
#TIPS
#how to shuffle a string
#*******************
from random import shuffle
name = "game"
l = list(name)
shuffle(l)
name = ''.join(l)
print(name)
#*******************
#another approach
#*******************
import random
name = "game"
print(''.join(random.sample(name, len(name))))
#******************

#Password Generator Project
pyPasswordGenerator.py file

# Day 6
# Functions, Code blocks and While groups

#Function
https://docs.python.org/3/library/functions.html

#syntax
def function_name():
    print("Hello")
    print("Everyone")
function_name()

#simple game
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#space vs tab
https://peps.python.org/pep-0008/
4 spaces should be given for indentation

#while loop
#syntax
while something_is_true:
    #Do this

#hurdle4
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while right_is_clear()!=True:
        if front_is_clear():
                move()
    turn_right()
    if front_is_clear()==True:
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if front_is_clear()==True:
        move()
    elif wall_in_front()==True:
        jump()

# Day 7
# Hangman Project
Check the hangman folder