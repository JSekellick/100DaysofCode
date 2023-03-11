# the clear() will not work without import Replit

from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids_dict = {}
bidding_done = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = highest_bid
    print(f"The weiner is {winner} with a bid of ${highest_bid}, congratulations!")
            

while bidding_done == False:
    name = input("What is yoru name?: ")
    bid = int(input("What is your bid?: $"))
    bids_dict[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if others == 'no':
        bidding_done = True
        highest_bidder(bids_dict)
    elif others == "yes":
        clear()