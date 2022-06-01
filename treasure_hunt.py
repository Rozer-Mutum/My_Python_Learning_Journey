print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are in an vocanic island, you can see the boiling lava and there was a road separated into two ways")
first_choice = input("Choose your path. L or R? | ")
if (first_choice=="L"):
    print("You had found a small cave in the mountain.\nSuddenly the ground started shaking\n*****************Y")
    second_choice = input("Do you want to still continue moving ahead? Y or N | ")
    if (second_choice=="Y"):
        print("You ran and jumped with faith and able to reach the gateways\nThere are there doors - White, Red and Black")
        third_choice = input("Select the door you want to open. | W or R or B | ")
        if (third_choice=="W"):
            print("You fell into a trap. You lose.")
        elif (third_choice=="R"):
            print("You saw a box and opened it. Hurray you found the treasure. You win.")
        else:
            print("You see a box but unable to open. You were crushed by the wall. You lose.")
    else:
        print("You had been crushed by the rocks. You died.")
else:
    print("You slipped through the terrain and felt down. You died.")