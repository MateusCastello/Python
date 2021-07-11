import os
from art import logo
bids = {}

def add_bidder(bids):
    person = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bids[person] = bid


def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0

    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is:{winner}, with a bid of: $ {highest_bid}")


is_finished = False

print(logo, "\nWelcome to the silent auction program!")

while not is_finished:
    add_bidder(bids)
    finished = input("Is there another bidder? Y or N? ").lower()
    if finished != "y":
        is_finished = True
    os.system('clear')

find_highest_bidder(bids)

