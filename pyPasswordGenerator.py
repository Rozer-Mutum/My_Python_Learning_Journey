import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPasswordGenerator!")
number_of_letters = input("How many letters would you like in your password?\n")
number_of_numbers = input("How many numbers would you like?\n")
number_of_symbols = input("How many symbols would you like?\n")

#generate a random letter first here
generate_letter = random.choice(letters)
#just gping to the loop fir n-1 times and add with the first generated letter
for n in range(1, int(number_of_letters)):
    random_letters = random.choice(letters)
    generate_letter += random_letters 

generate_number = random.choice(numbers)
for n in range(1, int(number_of_numbers)):
    random_numbers = random.choice(numbers)
    generate_number += random_numbers 

generate_symbol = random.choice(symbols)
for n in range(1, int(number_of_symbols)):
    random_symbols = random.choice(symbols)
    generate_symbol += random_symbols 

#combining all the generated strings, numbers and symbols and make a string
combining_password = str(generate_letter) + str(generate_number) + str(generate_symbol)
#shuffle the combined password string
password = ''.join(random.sample(combining_password, len(combining_password)))
print(f"Here is your password: {password}")