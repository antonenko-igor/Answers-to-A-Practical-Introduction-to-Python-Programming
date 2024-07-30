from random import *

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        names = ["Jack", "Queen", "King", "Ace"]
        if self.value <= 10:
            return f"{self.value} {self.suit}"
        else:
            return f"{names[self.value - 11]} {self.suit}"

class Poker_Deck():
    def __init__(self):
        self.cards = []
        for s in ["♣", "♦", "♥", "♠"]:
            for v in range(2,15):
                self.cards.append(Card(v, s))

class Poker_Hand:
    def __init__(self, cards):
        self.cards = cards
        self.deals = sample(self.cards, 5)
        self.suits = [self.deals[i].suit for i in range(len(self.deals))]
        self.values = [self.deals[i].value for i in range(len(self.deals))]
        self.cards = [self.deals[i].__str__() for i in range(len(self.deals))]
        self.values.sort()
        self.cards_count = {i:self.values.count(i) for i in self.values}
        self.value_count = list(self.cards_count.values())
        self.value_count.sort()

    def has_royal_flush(self):
        return self.values == [10,11,12,13,14] and self.has_flush()

    def has_straight_flush(self):
        return self.has_straight() and self.has_flush()

    def has_four_of_a_kind(self):
        return self.value_count == [1, 4]

    def has_full_house(self):
        return self.value_count == [2,3]

    def has_flush(self):
        return self.suits.count(self.suits[0]) == 5

    def has_straight(self):
        return self.values == [self.values[0] + i for i in range(5)]

    def has_three_of_a_kind(self):
        return self.value_count == [1,1,3]

    def has_two_pair(self):
        return self.value_count == [1,2,2]

    def has_pair(self):
        return self.value_count == [1,1,1,2]

    def best(self):
        if self.has_royal_flush():
            return "royal flush"
        elif self.has_straight_flush():
            return "straight flush"
        elif self.has_four_of_a_kind():
            return "four of a kind"
        elif self.has_full_house():
            return "full house"
        elif self.has_flush():
            return "flush"
        elif self.has_straight():
            return "straight"
        elif self.has_three_of_a_kind():
            return "three of a kind"
        elif self.has_two_pair():
            return " two pair"
        elif self.has_pair():
            return "pair"
        else:
            return "high cards"
print("To continue, press - ENTER, to end, press - 0 ")
enter = "1"
while enter != "0":
    deck = Poker_Deck()
    hand = Poker_Hand(deck.cards)
    print(" | ".join(hand.cards) + "|")
    print(hand.best())    
    enter = input()