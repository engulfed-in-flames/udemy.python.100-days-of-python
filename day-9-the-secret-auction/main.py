import art


def get_bidder():
    while True:
        name = input("What is your name?: ")
        try:
            bid = int(input("What's your bid?: $"))
            return name, bid
        except ValueError:
            print("The bid is invalid. Please enter a valid value.\n")


def should_continue():
    def clear_console():
        print("\033[H\033[2J", end="")

    while True:
        answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        if answer == "yes":
            clear_console()
            return True
        elif answer == "no":
            clear_console()
            return False


def find_winner(bidders):
    winner = None
    # highest_bid = 0

    winner = max(bidders, key=lambda x: bidders[x])

    # for name, bid in bidders.items():
    #   if bid > highest_bid:
    #     winner = name

    return winner, bidders[winner]


print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}
bidding = True

while bidding:
    name, bid = get_bidder()
    bidders[name] = bid

    bidding = should_continue()

name, bid = find_winner(bidders)
print(f"The winner is {name} with a bid of ${bid}")
