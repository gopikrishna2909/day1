
auction = {}

def compare(bidding_dictionary):
    winner = ""
    bid_value = 0
    for key in bidding_dictionary:
        if bidding_dictionary[key]>bid_value:
            bid_value = bidding_dictionary[key]
            winner = key
    print(f"The winner is {winner} with the bid amount ${bid_value}")


run = True
while run:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    auction[name] = bid
    next_person = input("Are there any other bidders, Type yes or no\n")
    if next_person == "no":
        run = False
        print(auction)
        compare(auction)







