import random

CARDS = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


class Hand:

    def __init__(self) -> None:
        self.hand = random.choices(list(CARDS.keys()), k=2)

    def draw_card(self) -> None:
        return self.hand.append(random.choice(list(CARDS.keys())))

    def display_hand(self, number: int = None) -> None:
        def upper_char(char):
            return f"|{char:<{7}}|"

        def lower_char(char):
            return f"|{char:{7}}|"

        head = " ------- "
        side = "|       |"
        top = ""
        upper = ""
        middle = ""
        lower = ""

        for char in self.hand[:number]:
            top += head + " "
            upper += upper_char(char) + " "
            middle += side + " "
            lower += lower_char(char) + " "

        print(top)
        print(upper)
        print(middle)
        print(middle)
        print(middle)
        print(lower)
        print(top)

    def get_total(self) -> int:
        total = 0

        for card in self.hand:
            total += CARDS[card]

        if total <= 21:
            return total
        else:
            try:
                self.hand.index("A")
                total -= 10
            except ValueError:
                pass

            return total
