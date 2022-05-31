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