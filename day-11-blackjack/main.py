from Hand import Hand


def hit_or_stand() -> str:
    while True:
        answer = input("Do you want to draw another card? (y/n): ").lower()
        if answer == "y":
            return "hit"
        elif answer == "n":
            return "stand"


# def play_round(player_hand: object, dealer_hand: object) -> None:


def hit(player_hand: object) -> bool:
    player_hand.draw_card()

    print("Player's hand are: ")
    player_hand.display_hand()

    if player_hand.get_total() > 21:
        print(f"Player's total is: {player_hand.get_total()}\n")
        print("Player lost!")
        return False

    print("\n")
    return True


def stand(player_hand: object, dealer_hand: object) -> bool:

    player_total = player_hand.get_total()

    print("Player's final hand is: ")
    player_hand.display_hand()
    print(f"Player's total is: {player_total}\n")

    dealer_total = dealer_hand.get_total()

    while dealer_total < 17:
        dealer_hand.draw_card()
        dealer_total = dealer_hand.get_total()

    print("Dealer's final hand is: ")
    dealer_hand.display_hand()
    print(f"Dealer's total is: {dealer_total}\n")

    if dealer_total > 21 or player_total > dealer_total:
        print("Player won!")
    elif player_total == dealer_total:
        print("It's a tie!")
    else:
        print("Player lost!")

    return False


playing = True

player_hand = Hand()
dealer_hand = Hand()

print("Player's hand are: ")
player_hand.display_hand()

print("Dealer's first card is: ")
dealer_hand.display_hand(1)

while playing:
    action = hit_or_stand()

    if action == "hit":
        playing = hit(player_hand)

    elif action == "stand":
        playing = stand(player_hand, dealer_hand)
