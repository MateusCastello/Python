from art import logo
bids = {}

def add_bidder(bids):
    person = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bids[person] = bid

is_finished = False

print(logo)

while not is_finished:
    add_bidder(bids)
    finished = input("Is there another bidder? Y or N? ").lower()
    if finished != "y":
        is_finished = True

print(bids)

