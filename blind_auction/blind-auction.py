import os
from art import logo
print(logo)

def finding_winner():
    highest_bidder=0
    winner = ""
    for bidder in bidding_info:
        bidding_guess = bidding_info[bidder]
        if bidding_guess > highest_bidder:
            highest_bidder=bidding_guess
            winner = bidder
    print(f'The winner is "{name}" with a bidding amount of ${highest_bidder}.')

bidding_info = {}
new_bid = True
while new_bid:
    name = input("What is your name? ")
    bid = int(input("How much you want to bid? $"))
    bidding_info[name] = bid
    # print(bidding_info)
    result = input("Is there any bidder? yes or no. ")
    os.system('cls||clear')
    if result=="no":
        finding_winner()
        new_bid=False
    