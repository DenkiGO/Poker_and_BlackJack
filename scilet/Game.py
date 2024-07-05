import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from poker.poker_game import TexasHoldemGame
import threading
import time


class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.background_image = Image.open("image\\background\\background_game_fin_male.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.new_game = ttk.Button(self, text="New game", command=self.repid)
        self.new_game.place(x=307, y=402, height=27, width=100)

        self.flop = ttk.Button(self, text="flop", command=self.start_flop_card)
        self.flop.place(x=427, y=402, height=27, width=50)

        self.turn = ttk.Button(self, text="turn", command=self.start_turn_card)
        self.turn.place(x=497, y=402, height=27, width=50)

        self.river = ttk.Button(self, text="river", command=self.start_river_card)
        self.river.place(x=567, y=402, height=27, width=50)

        self.name_player_label = tk.Label(self, text="  ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.name_player_label.place(x=495, y=653, width=140)

        self.back_card_image_me_label = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_me_label = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_image_label_dog = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_dog = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_image_label_female = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_female = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_image_label_marco = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_marco = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_image_label_bear = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_bear = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_image_label_mike = self.create_card("image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_mike = self.create_card("image\\cards\\card_backs_2.png")

        self.card_image_flop_1 = self.create_card("image\\cards\\card_backs_2.png")
        self.card_image_flop_2 = self.create_card("image\\cards\\card_backs_2.png")
        self.card_image_flop_3 = self.create_card("image\\cards\\card_backs_2.png")
        self.card_image_tern = self.create_card("image\\cards\\card_backs_2.png")
        self.card_image_river = self.create_card("image\\cards\\card_backs_2.png")

        self.top_card_deck = self.create_card("image\\cards\\card_backs_2.png")
        self.top_card_deck.place(x=914, y=333)

        card_image = Image.open("image\\combination\\combination_bot\\Start comb.png")
        card_photo = ImageTk.PhotoImage(card_image)
        self.combination_player_label = tk.Label(self, image=card_photo, bd=0)
        self.combination_player_label.image = card_photo
        self.combination_player_label.place(x=377, y=640)

    def check_combination_player(self):
        background_image = Image.open(f"image\\combination\\combination_bot\\{self.game.combinations_player_server()}.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.combination_player_label.configure(image=background_photo)
        self.combination_player_label.image = background_photo

    def create_card(self, image_path):
        card_image = Image.open(image_path)
        card_image = card_image.resize((int(card_image.width * 1.7), int(card_image.height * 1.7)))
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self, image=card_photo, bd=0)
        card_label.image = card_photo
        return card_label

    def start_animation_card(self):
        self.animate_card_thread = threading.Thread(target=self.animate_card_rise)
        self.animate_card_thread.start()

    def animate_card_rise(self):
        card_info = [
            {"label": self.back_card_image_label_dog, "y_step": 1.77, "x_step": -1.34},
            {"label": self.back_card_image_me_label, "y_step": 1.77, "x_step": -5.44},
            {"label": self.back_card_image_label_female, "y_step": 1.22, "x_step": -7.24},
            {"label": self.back_card_image_label_marco, "y_step": -1.83, "x_step": -7.14},
            {"label": self.back_card_image_label_bear, "y_step": -3.03, "x_step": -3.54},
            {"label": self.back_card_image_label_mike, "y_step": -3.03, "x_step": -1.24},
            {"label": self.back_card_2_image_label_dog, "y_step": 1.77, "x_step": -1.04},
            {"label": self.back_card_2_image_me_label, "y_step": 1.77, "x_step": -5.14},
            {"label": self.back_card_2_image_label_female, "y_step": 1.22, "x_step": -6.94},
            {"label": self.back_card_2_image_label_marco, "y_step": -1.83, "x_step": -6.84},
            {"label": self.back_card_2_image_label_bear, "y_step": -3.03, "x_step": -3.24},
            {"label": self.back_card_2_image_label_mike, "y_step": -3.03, "x_step": -0.94}
        ]
        for card in card_info:
            start_y = 333
            start_x = 914
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.update()

    def update_player_info(self, player_name, gender):
        self.player_name = player_name
        self.name_player_label.config(text=f'{player_name}')
        self.gender = gender
        if gender == "Male":
            pass
        else:
            background_image = Image.open("image\\background\\background_game_fin_female.png")
            background_photo = ImageTk.PhotoImage(background_image)
            self.background_label.configure(image=background_photo)
            self.background_label.image = background_photo
        self.start_animation_card()
        self.start_game()

    def start_flop_card(self):
        self.animate_flop_thread = threading.Thread(target=self.giveaway_flop)
        self.animate_flop_thread.start()
        self.check_combination_player()

    def start_turn_card(self):
        self.animate_turn_thread = threading.Thread(target=self.giveaway_turn)
        self.animate_turn_thread.start()
        self.check_combination_player()

    def start_river_card(self):
        self.animate_river_thread = threading.Thread(target=self.giveaway_river)
        self.animate_river_thread.start()
        self.check_combination_player()

    def start_game(self):
        self.game = TexasHoldemGame(num_players=1)
        self.image_player_card()

    def image_player_card(self):
        card_player = [self.back_card_image_me_label, self.back_card_2_image_me_label]
        self.game.giveaway_card()
        for player, cards in self.game.display_players_cards().items():
            for i in range(2):
                player_card = Image.open(f"image\\cards\\card_{cards[i]}.png")
                player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
                player_card = ImageTk.PhotoImage(player_card)
                card_player[i].configure(image=player_card)
                card_player[i].image = player_card

    def giveaway_flop(self):
        card_flop = [self.card_image_flop_1, self.card_image_flop_2, self.card_image_flop_3]
        cards_flop_table = self.game.display_flop_cards_table()['flop']
        for i in range(3):
            player_card = Image.open(f"image\\cards\\card_{cards_flop_table[i]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card_flop[i].configure(image=player_card)
            card_flop[i].image = player_card
        card_info = [
            {"label": self.card_image_flop_1, "y_step": -0.73, "x_step": -5.44},
            {"label": self.card_image_flop_2, "y_step": -0.73, "x_step": -4.49},
            {"label": self.card_image_flop_3, "y_step": -0.73, "x_step": -3.54}
        ]
        for card in card_info:
            start_y = 333
            start_x = 914
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.update()

    def giveaway_turn(self):
        # self.card_image_tern.place(x=655, y=260)
        cards_turn_table = self.game.display_turn_cards_table()['turn']
        player_card = Image.open(f"image\\cards\\card_{cards_turn_table[0]}.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.card_image_tern.configure(image=player_card)
        self.card_image_tern.image = player_card
        card_info = [
            {"label": self.card_image_tern, "y_step": -0.73, "x_step": -2.59},
        ]
        for card in card_info:
            start_y = 333
            start_x = 914
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.update()

    def giveaway_river(self):
        # self.card_image_river.place(x=750, y=260)
        cards_river_table = self.game.display_river_cards_table()['river']
        player_card = Image.open(f"image\\cards\\card_{cards_river_table[0]}.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.card_image_river.configure(image=player_card)
        self.card_image_river.image = player_card
        card_info = [
            {"label": self.card_image_river, "y_step": -0.73, "x_step": -1.64}
        ]
        for card in card_info:
            start_y = 333
            start_x = 914
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.update()


    def repid(self):
        background_image = Image.open(f"image\\combination\\combination_bot\\Start comb.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.combination_player_label.configure(image=background_photo)
        self.combination_player_label.image = background_photo

        self.combination_player_label.config(text='   ')
        card_info = [
            {"label": self.back_card_image_label_dog, "y_step": 1.77, "x_step": -1.34},
            {"label": self.back_card_2_image_label_dog, "y_step": 1.77, "x_step": -1.04},
            {"label": self.back_card_image_me_label, "y_step": 1.77, "x_step": -5.44},
            {"label": self.back_card_2_image_me_label, "y_step": 1.77, "x_step": -5.14},
            {"label": self.back_card_image_label_female, "y_step": 1.22, "x_step": -7.24},
            {"label": self.back_card_2_image_label_female, "y_step": 1.22, "x_step": -6.94},
            {"label": self.back_card_image_label_marco, "y_step": -1.83, "x_step": -7.14},
            {"label": self.back_card_2_image_label_marco, "y_step": -1.83, "x_step": -6.84},
            {"label": self.back_card_image_label_bear, "y_step": -3.03, "x_step": -3.54},
            {"label": self.back_card_2_image_label_bear, "y_step": -3.03, "x_step": -3.24},
            {"label": self.back_card_image_label_mike, "y_step": -3.03, "x_step": -1.24},
            {"label": self.back_card_2_image_label_mike, "y_step": -3.03, "x_step": -0.94},
            {"label": self.card_image_flop_1, "y_step": -0.73, "x_step": -5.44},
            {"label": self.card_image_flop_2, "y_step": -0.73, "x_step": -4.49},
            {"label": self.card_image_flop_3, "y_step": -0.73, "x_step": -3.54},
            {"label": self.card_image_river, "y_step": -0.73, "x_step": -1.64},
            {"label": self.card_image_tern, "y_step": -0.73, "x_step": -2.59}
        ]
        for card in card_info:
            card['label'].place(x=914, y=333)
        self.start_animation_card()
        self.start_game()