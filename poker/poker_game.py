import random
from collections import Counter


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}_{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♥', '♦', '♠', '♣']
        ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'lady', 'king', 'ace']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)


class ComputerPlayer(Player):
    def __init__(self, name_player):
        super().__init__(name_player)


class TexasHoldemTable:
    def __init__(self):
        self.community_cards = []
        self.table_card = {}

    def deal_flop(self, deck):
        self.table_card['flop'] = []
        for _ in range(3):
            card = deck.deal_card()
            if card:
                self.community_cards.append(card)
                self.table_card['flop'].append(str(card))
        return self.table_card


    def deal_turn(self, deck):
        self.table_card['turn'] = []
        card = deck.deal_card()
        if card:
            self.community_cards.append(card)
            self.table_card['turn'].append(str(card))
        return self.table_card

    def deal_river(self, deck):
        self.table_card['river'] = []
        card = deck.deal_card()
        if card:
            self.community_cards.append(card)
            self.table_card['river'].append(str(card))
        return self.table_card

    def display_community_cards(self):
        print("Карты на столе:")
        for card in self.community_cards:
            print(card)


class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def is_straight(self):
        values = [card.rank for card in self.cards]
        # Преобразуем достоинства карт в числа для сравнения
        value_to_number = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'lady': 12, 'king': 13, 'ace': 14}
        numeric_values = [value_to_number[value] for value in values]

        sorted_values = sorted(numeric_values)
        for i in range(1, len(sorted_values)):
            if sorted_values[i] - sorted_values[i - 1] != 1:
                return False

        return True

    def is_flush(self):
        suits = {card.suit for card in self.cards}
        return len(suits) == 1

    def is_pair(self):
        counts = Counter(card.rank for card in self.cards)
        return 2 in counts.values()

    def is_two_pair(self):
        counts = Counter(card.rank for card in self.cards)
        return list(counts.values()).count(2) == 2

    def is_three_of_a_kind(self):
        counts = Counter(card.rank for card in self.cards)
        return 3 in counts.values()

    def is_four_of_a_kind(self):
        counts = Counter(card.rank for card in self.cards)
        return 4 in counts.values()

    def is_full_house(self):
        counts = Counter(card.rank for card in self.cards)
        return 2 in counts.values() and 3 in counts.values()

    def evaluate(self):
        if self.is_straight() and self.is_flush():
            return "Straight Flush"
        if self.is_four_of_a_kind():
            return "Four of a Kind"
        if self.is_full_house():
            return "Full House"
        if self.is_flush():
            return "Flush"
        if self.is_straight():
            return "Straight"
        if self.is_three_of_a_kind():
            return "Three of a Kind"
        if self.is_two_pair():
            return "Two Pair"
        if self.is_pair():
            return "Pair"
        return "High Card"

    def compare(self, other_hand):
        self_rank = self.evaluate()
        other_rank = other_hand.evaluate()

        if self_rank == other_rank:
            self_values = sorted([card.rank for card in self.cards], reverse=True)
            other_values = sorted([card.rank for card in other_hand.cards], reverse=True)

            for i in range(5):
                if self_values[i] > other_values[i]:
                    return "Победа"
                elif self_values[i] < other_values[i]:
                    return "Поражение"

            return "Ничья"

        ranks = [
            "High Card", "Pair", "Two Pair", "Three of a Kind", "Straight",
            "Flush", "Full House", "Four of a Kind", "Straight Flush"
        ]

        return "Победа" if ranks.index(self_rank) > ranks.index(other_rank) else "Поражение"


class TexasHoldemGame:
    def __init__(self, num_players, num_comp = 0):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(f"{i}") for i in range(num_players)]
        self.computer_players = [ComputerPlayer(f"comp {i}") for i in range(num_comp)]
        self.table = TexasHoldemTable()
        self.active_players = []  # Список активных игроков в текущем раунде

    def deal_initial_cards(self, num_cards):
        for _ in range(num_cards):
            for player in self.players:
                card = self.deck.deal_card()
                if card:
                    player.receive_card(card)
            for comp_player in self.computer_players:
                card = self.deck.deal_card()
                if card:
                    comp_player.receive_card(card)

    def display_players_cards(self):
        pl_cards = {}
        for player in self.players:
            pl_cards[f'{player.name}'] = []
            for card in player.hand:
                pl_cards[f'{player.name}'].append(str(card))
        return pl_cards

    def display_players_cards_play_bots(self):
        pl_cards = {}
        for player in self.players:
            pl_cards[player] = []
            for card in player.hand:
                pl_cards[player].append(str(card))
        return pl_cards

    def computers_cards(self, name):
        pass

    def display_flop_cards_table(self):
        return self.table.deal_flop(self.deck)

    def display_turn_cards_table(self):
        return self.table.deal_turn(self.deck)

    def display_river_cards_table(self):
        return self.table.deal_river(self.deck)

    def play(self):
        self.active_players = self.players

        best_hand = None
        winner = None

        for player in self.active_players:
            player_hand = PokerHand(player.hand + self.table.community_cards)
            if best_hand is None or player_hand.compare(best_hand) == "Победа":
                best_hand = player_hand
                winner = player

        # self.table.display_community_cards()

        print(f"Победитель: {winner.name} с комбинацией {best_hand.evaluate()}")

    def determine_the_winner_play_bots(self, list_player):
        self.active_players = list_player

        # Определение победителя
        best_hand = None
        winner = None

        for player in self.active_players:
            player_hand = PokerHand(player.hand + self.table.community_cards)
            if best_hand is None or player_hand.compare(best_hand) == "Победа":
                best_hand = player_hand
                winner = player
        return (winner, best_hand.evaluate())

    def determine_the_winner(self):
        self.active_players = self.players

        # Определение победителя
        best_hand = None
        winner = None

        for player in self.active_players:
            player_hand = PokerHand(player.hand + self.table.community_cards)
            if best_hand is None or player_hand.compare(best_hand) == "Победа":
                best_hand = player_hand
                winner = player
        return (winner.name, best_hand.evaluate())

    def combinations_player_server(self):
        return PokerHand(self.players[0].hand + self.table.community_cards).evaluate()

    def combinations_player_client(self):
        return PokerHand(self.players[1].hand + self.table.community_cards).evaluate()

    def giveaway_card(self):
        num_initial_cards = 2
        self.deal_initial_cards(num_initial_cards)


if __name__ == "__main__":
    num_players = 7
    game = TexasHoldemGame(num_players)
    game.giveaway_card()
    game.display_flop_cards_table()
    game.display_turn_cards_table()
    game.display_river_cards_table()
    # print(list(game.display_players_cards_play_bots().keys()))
    print(list(game.display_players_cards_play_bots().keys())[0])
    print(game.determine_the_winner_play_bots(list(game.display_players_cards_play_bots().keys())[0]))
