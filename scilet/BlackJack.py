import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, font
import threading
import time
from poker.blackjack_game import Blackjack
from interface import Bet_Frame_BlackJack


class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom Window")
        self.geometry("1100x800")

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.data_from_toplevel = tk.StringVar()

        self.custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.background_image = Image.open("../image/background/background_blackjack.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        image = Image.open("../image/frame/frame_action_blackjack.png")
        photo = ImageTk.PhotoImage(image)
        self.frame_action_player = tk.Label(self, image=photo, bd=0)
        self.frame_action_player.image = photo
        self.frame_action_player.place(x=70, y=555)


        self.name_you_label = tk.Label(self, text="Dealer", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.name_you_label.place(x=475, y=162, width=140)

        self.chips_on_the_table = ttk.Entry(self, style="TEntry", font=self.custom_font, state="readonly")
        self.chips_on_the_table.configure(justify="center")
        self.chips_on_the_table.place(x=485, y=400, height=30, width=130)

        self.score_player = ttk.Entry(self, style="TEntry", font=self.custom_font, justify="center")
        self.score_player.insert(0, "Score: 0")
        self.score_player.place(x=100, y=602, height=30, width=289)
        self.score_player.configure(state="readonly")

        self.hit_button = ttk.Button(self, text="Hit", style="Custom.TButton", command=self.hit_card_player)
        self.hit_button.place(x=103, y=680, height=30, width=137)

        self.stand_button = ttk.Button(self, text="Stand", style="Custom.TButton", command=self.stand)
        self.stand_button.place(x=249, y=680, height=30, width=137)

        self.double_button = ttk.Button(self, text="Double", style="Custom.TButton", command=self.double)
        self.double_button.place(x=103, y=641, height=30, width=283)

        self.chips_player_label = tk.Label(self, text="1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_player_label.place(x=475, y=690, width=140)
        self.chips_player = 1000

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        self.style.configure("Custom.TButton", font=self.custom_font)

        self.style.configure("TEntry",
                 background="green",
                 foreground="black",
                 fieldbackground="#a9aaa7")

        self.dop_card_player = 0
        self.bet_player = 0
        self.dop_card_dealer = 0
        self.game = Blackjack()

        self.back_card_image_me_label = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_2_image_me_label = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_3_image_me_label = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_4_image_me_label = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_5_image_me_label = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_image_label_your = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_2_image_label_your = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_3_image_label_your = self.create_card("../image/cards/card_backs_1.png")
        self.back_card_4_image_label_your = self.create_card("../image/cards/card_backs_1.png")

        self.upper_back_card_image_label = self.create_card("../image/cards/card_backs_1.png")
        self.upper_back_card_image_label.place(x=945, y=340)

        image = Image.open("../image/frame/main_frame_blackjack_start.png")
        photo = ImageTk.PhotoImage(image)
        self.frame = tk.Label(self, image=photo, bd=0)
        self.frame.image = photo
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.start_blackjack = ttk.Button(self, text="Ready", style="Custom.TButton", command=self.man_thread_play)
        self.start_blackjack.place(x=474, y=406, width=151, height=29)

        self.command_event = threading.Event()
        self.command_2_event = threading.Event()

    def man_thread_play(self):
        self.play_blackjk_thread = threading.Thread(target=self.play_blackjack_main)
        self.play_blackjk_thread.start()

    def play_blackjack_main(self):
        while True:
            self.restart()
            self.open_bet_frame_player()
            self.command_event.wait()
            self.command_event.clear()
            self.start_start_animation_card()
            self.play_blackjack()
            self.show_frame_action()
            self.command_2_event.wait()
            self.command_2_event.clear()
            self.hide_frame_action()
            if self.hand_value > 21:
                pass
            else:
                self.play_dealer()
            self.image_winner()
            time.sleep(3)

    def text_toplevel(self, data):
        self.bet_player = data
        self.chips_player = self.chips_player - data
        self.chips_on_the_table.configure(state="normal")
        self.chips_on_the_table.delete(0, tk.END)
        self.chips_on_the_table.insert(0, f"{data} $")
        self.chips_on_the_table.configure(state="readonly")
        self.chips_player_label.configure(text=f"{self.chips_player} $")
        self.command_event.set()
        print("Data from Toplevel:", data)

    def open_bet_frame_player(self):
        bet_frame_player = Bet_Frame_BlackJack.Main_Frame_Bet(self, self.data_from_toplevel, self.text_toplevel, self.chips_player)
        bet_frame_player.grab_set()

    def image_winner(self):
        winner = self.game.determine_winner()
        if winner == "Dealer wins!":
            player_card = Image.open(f"../image/background/win blackjack/background_blackjack_dealer_win.png")
            player_card = ImageTk.PhotoImage(player_card)
            self.background_label.configure(image=player_card)
            self.background_label.image = player_card
            self.chips_on_the_table.configure(state="normal")
            self.chips_on_the_table.delete(0, tk.END)
            self.chips_on_the_table.insert(0, f"0 $")
            self.chips_on_the_table.configure(state="readonly")
        elif winner == "Player wins!":
            self.chips_player = self.bet_player*2 + self.chips_player
            self.chips_on_the_table.configure(state="normal")
            self.chips_on_the_table.delete(0, tk.END)
            self.chips_on_the_table.insert(0, f"{self.bet_player*2} $")
            self.chips_on_the_table.configure(state="readonly")
            player_card = Image.open(f"../image/background/win blackjack/background_blackjack_player_win.png")
            player_card = ImageTk.PhotoImage(player_card)
            self.background_label.configure(image=player_card)
            self.background_label.image = player_card
        else:
            self.chips_player = self.bet_player + self.chips_player

    def restart(self):
        card_info = [
            {"label": self.back_card_image_me_label, "y_step": 1.84, "x_step": -3.26},
            {"label": self.back_card_image_label_your, "y_step": -3.23, "x_step": -3.26},
            {"label": self.back_card_2_image_me_label, "y_step": 1.84, "x_step": -2.96},
            {"label": self.back_card_3_image_me_label, "y_step": 1.84, "x_step": -2.96},
            {"label": self.back_card_4_image_me_label, "y_step": 1.84, "x_step": -2.96},
            {"label": self.back_card_5_image_me_label, "y_step": 1.84, "x_step": -2.96},
            {"label": self.back_card_2_image_label_your, "y_step": -3.23, "x_step": -2.96},
            {"label": self.back_card_3_image_label_your, "y_step": -3.23, "x_step": -2.96},
            {"label": self.back_card_4_image_label_your, "y_step": -3.23, "x_step": -2.96}
        ]
        player_card = Image.open(f"../image/cards/card_backs_1.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.back_card_2_image_label_your.configure(image=player_card)
        self.back_card_2_image_label_your.image = player_card
        player_card = Image.open(f"../image/background/background_blackjack.png")
        player_card = ImageTk.PhotoImage(player_card)
        self.background_label.configure(image=player_card)
        self.background_label.image = player_card
        self.chips_on_the_table.configure(state="normal")
        self.chips_on_the_table.delete(0, tk.END)
        self.chips_on_the_table.configure(state="readonly")
        self.score_player.configure(state="norm")
        self.score_player.delete(0, tk.END)
        self.score_player.insert(0, f"Your: 0 | Dealer: 0 ")
        self.score_player.configure(state="readonly")
        self.bet_player = 0
        for card in card_info:
            card["label"].place(x=945, y=340)
        self.chips_player_label.configure(text=f"{self.chips_player} $")

    def double(self):
        if (self.chips_player - self.bet_player) >= 0:
            self.chips_player = self.chips_player - self.bet_player
            self.bet_player = self.bet_player*2
        self.dop_card_player += 1
        self.game.player.receive_card(self.game.deck.deal_card())
        self.start_animation_card()
        self.calculate_hand()
        self.command_2_event.set()

    def stand(self):
        self.command_2_event.set()

    def hide_frame_action(self):
        items = [self.hit_button, self.stand_button, self.double_button]
        for item in items:
            item.config(state="disabled")

    def show_frame_action(self):
        items = [
            {"item": self.hit_button, "x": 103, "y": 680, "height": 30, "width": 137},
            {"item": self.stand_button, "x": 249, "y": 680, "height": 30, "width": 137},
            {"item": self.double_button, "x": 103, "y": 641, "height": 30, "width": 283},
        ]
        for item in items:
            item["item"].config(state="normal")

    def start_animation_card(self):
        self.animate_card_thread = threading.Thread(target=self.animate_card_rise)
        self.animate_card_thread.start()

    def start_start_animation_card(self):
        self.start_animate_card_thread = threading.Thread(target=self.start_animate_card_rise)
        self.start_animate_card_thread.start()

    def start_animate_card_rise(self):
        card_info = [
            {"label": self.back_card_image_me_label, "y_step": 1.84, "x_step": -3.26},
            {"label": self.back_card_image_label_your, "y_step": -3.23, "x_step": -3.26},
            {"label": self.back_card_2_image_me_label, "y_step": 1.84, "x_step": -2.96},
            {"label": self.back_card_2_image_label_your, "y_step": -3.23, "x_step": -2.96}
        ]
        for card in card_info:
            start_y = 340
            start_x = 945
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"] * 5
                start_x += card["x_step"] * 5
                card["label"].place(x=start_x, y=start_y)
            self.update()

    def animate_card_rise(self):
        print(self.dop_card_player)
        if self.dop_card_player == 1:
            card = self.game.player.display_hand()[-1]
            player_card = Image.open(f"../image/cards/card_{card}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_3_image_me_label.configure(image=player_card)
            self.back_card_3_image_me_label.image = player_card
            card_info = [
                {"label": self.back_card_3_image_me_label, "y_step": 1.84, "x_step": -2.66},
            ]
        elif self.dop_card_player == 2:
            card = self.game.player.display_hand()[-1]
            player_card = Image.open(f"../image/cards/card_{card}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_4_image_me_label.configure(image=player_card)
            self.back_card_4_image_me_label.image = player_card
            card_info = [
                {"label": self.back_card_4_image_me_label, "y_step": 1.84, "x_step": -2.36}
            ]
        elif self.dop_card_player == 3:
            card = self.game.player.display_hand()[-1]
            player_card = Image.open(f"../image/cards/card_{card}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_5_image_me_label.configure(image=player_card)
            self.back_card_5_image_me_label.image = player_card
            card_info = [
                {"label": self.back_card_5_image_me_label, "y_step": 1.84, "x_step": -2.06}
            ]
        elif self.dop_card_dealer == 1:
            player_card = Image.open(f"../image/cards/card_{self.hand_dealer[2]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_3_image_label_your.configure(image=player_card)
            self.back_card_3_image_label_your.image = player_card
            card_info = [
                {"label": self.back_card_3_image_label_your, "y_step": -3.23, "x_step": -2.66}
            ]
        elif self.dop_card_dealer == 2:
            player_card = Image.open(f"../image/cards/card_{self.hand_dealer[2]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_3_image_label_your.configure(image=player_card)
            self.back_card_3_image_label_your.image = player_card
            player_card = Image.open(f"../image/cards/card_{self.hand_dealer[3]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            self.back_card_4_image_label_your.configure(image=player_card)
            self.back_card_4_image_label_your.image = player_card
            card_info = [
                {"label": self.back_card_3_image_label_your, "y_step": -3.23, "x_step": -2.66},
                {"label": self.back_card_4_image_label_your, "y_step": -3.23, "x_step": -2.36}
            ]
        try:
            if self.dop_card_dealer != 0 or self.dop_card_player != 0:
                for card in card_info:
                    start_y = 340
                    start_x = 945
                    for i in range(20):
                        time.sleep(0.005)
                        start_y += card["y_step"] * 5
                        start_x += card["x_step"] * 5
                        card["label"].place(x=start_x, y=start_y)
                    self.update()
        except:
            pass

    def create_card(self, image_path):
        card_image = Image.open(image_path)
        card_image = card_image.resize((int(card_image.width * 1.7), int(card_image.height * 1.7)))
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self, image=card_photo, bd=0)
        card_label.image = card_photo
        return card_label

    def play_blackjack(self):
        self.dop_card_player = 0
        self.game = Blackjack()
        self.game.initial_deal()
        self.image_card_player()
        self.calculate_hand()

    def image_card_player(self):
        player_card_im = self.game.player.display_hand()
        dealer_card_im = self.game.dealer.show_initial_card()
        # print(dealer_card_im)
        card_info = [
            {"label": self.back_card_image_me_label, "image": player_card_im[0]},
            {"label": self.back_card_image_label_your, "image": dealer_card_im},
            {"label": self.back_card_2_image_me_label, "image": player_card_im[1]},
        ]
        for card in card_info:
            player_card = Image.open(f"../image/cards/card_{card['image']}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card['label'].configure(image=player_card)
            card['label'].image = player_card

    def hit_card_player(self):
        self.dop_card_player += 1
        self.game.player.receive_card(self.game.deck.deal_card())
        self.start_animation_card()
        if self.game.player.calculate_hand_value() > 21:
            self.command_2_event.set()
        self.calculate_hand()

    def play_dealer(self):
        self.dop_card_player = 0
        self.game.dealer_turn()
        self.hand_dealer = self.game.dealer.display_hand()
        player_card = Image.open(f"../image/cards/card_{self.hand_dealer[1]}.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.back_card_2_image_label_your.configure(image=player_card)
        self.back_card_2_image_label_your.image = player_card
        self.dop_card_dealer = len(self.hand_dealer) - 2
        self.start_animation_card()
        self.calculate_hand()

    def calculate_hand(self):
        self.hand_value = self.game.player.calculate_hand_value()
        self.hand_value_dealer = self.game.dealer.calculate_hand_value()
        self.score_player.configure(state="norm")
        self.score_player.delete(0, tk.END)
        self.score_player.insert(0, f"Your: {self.hand_value} | Dealer: {self.hand_value_dealer}")
        self.score_player.configure(state="readonly")


if __name__ == "__main__":
    app = CustomWindow()
    app.mainloop()
