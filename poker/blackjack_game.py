import random
from poker.poker_game import Card, Deck, Player


class Player_BlackJack(Player):
    def calculate_hand_value(self):
        value = 0
        num_aces = 0
        age_ranks = {
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

        for card in self.hand:
            if card.rank == 'ace':
                num_aces += 1
                value += 11
            elif card.rank in ['jack', 'lady', 'king', 'ten']:
                value += 10
            else:
                value += age_ranks[card.rank]

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value

    def display_hand(self):
        return [str(card) for card in self.hand]


class Dealer(Player_BlackJack):
    def __init__(self):
        super().__init__("Dealer")

    def show_initial_card(self):
        # Показывает только первую карту дилера
        return str(self.hand[0])

    def play(self, deck):
        # Дилер берет карты до тех пор, пока его сумма не достигнет 17 или более
        while self.calculate_hand_value() < 17:
            self.receive_card(deck.deal_card())
        return [str(card) for card in self.hand]


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player_BlackJack("0")
        self.dealer = Dealer()

    def initial_deal(self):
        # Раздаем две карты игроку и дилеру
        self.player.receive_card(self.deck.deal_card())
        self.player.receive_card(self.deck.deal_card())
        self.dealer.receive_card(self.deck.deal_card())

    def player_turn(self):
        while True:
            # Показываем карты игрока и одну карту дилера
            print(self.player.display_hand())
            self.dealer.show_initial_card()

            # Проверяем, не превышен ли лимит 21 очка
            if self.player.calculate_hand_value() > 21:
                print("Bust! Player busted.")
                break

            # Предлагаем игроку выбор: взять еще карту или остановиться
            choice = input("Do you want to hit or stand? ").lower()
            if choice == 'hit':
                self.player.receive_card(self.deck.deal_card())
            elif choice == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

    def dealer_turn(self):
        # Ход дилера
        self.dealer.receive_card(self.deck.deal_card())
        self.dealer.play(self.deck)

    def determine_winner(self):
        player_score = self.player.calculate_hand_value()
        dealer_score = self.dealer.calculate_hand_value()

        if player_score > 21:
            return "Dealer wins!"
        elif dealer_score > 21:
            return "Player wins!"
        elif player_score == dealer_score:
            return "It's a tie!"
        elif player_score > dealer_score:
            return "Player wins!"
        else:
            return "Dealer wins!"

    def play_game(self):
        print("Welcome to Blackjack!")

        # Раздача начальных карт
        self.initial_deal()

        # Ход игрока
        self.player_turn()

        # Ход дилера, если игрок не превысил 21 очко
        if self.player.calculate_hand_value() <= 21:
            self.dealer_turn()

        # Определение победителя
        result = self.determine_winner()
        print(result)

# Пример использования:
if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
