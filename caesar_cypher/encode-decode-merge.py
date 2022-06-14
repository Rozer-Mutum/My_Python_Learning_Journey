from unittest import result
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_start=True
while new_start:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar_cypher(start_text, shift_number, cypher_direction):
        if shift_number>26:
            shift_number%=26
        end_text = ""
        if cypher_direction=="decode":
            shift_number*= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_number
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text+=char
        print(f"The {cypher_direction}d letter is {end_text}")
        

    caesar_cypher(start_text=text, shift_number=shift, cypher_direction=direction)
    result = input('Do you want to continue? "yes" or "no"\n')
    if result=="no":
        new_start=False
        print("Goodbye")
