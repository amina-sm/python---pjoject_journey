print("Welcome to auction")
bids={}
bidding_finished= False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid=bid_amount
            winner= bidder
            print(f" The winner  is {winner} with a bid of ${highest_bid}")
            
while not  bidding_finished:
    name= input("What is your name? \n")
    bid_price=int(input("What is your bid price?\n $"))
    bids[name]=bid_price
    additional_user= input("Is there other users who want to bid? (yes/no  :)")
    if additional_user.lower =="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif additional_user=="yes":
        continue    
    

# # Print the final dictionary of bids
#     print("Auction Results:")
# for name, price in bids.items():
#     print(f"{name} bid ${price}")