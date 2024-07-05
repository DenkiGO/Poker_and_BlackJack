import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import socket
import pickle
import threading
import _thread
import time


class PokerClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Game")

        self.background_image = Image.open("C:\\Users\\griba\\Cursach\\image\\background\\background_fin_network.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.back_card_image_me_label = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.back_card_2_image_me_label = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.back_card_image_label_your = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.back_card_2_image_label_your = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")

        self.card_image_flop_1 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.card_image_flop_2 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.card_image_flop_3 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.card_image_tern = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.card_image_river = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")

        self.top_card_deck = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_1.png")
        self.top_card_deck.place(x=945, y=340)

        # self.new_game = ttk.Button(self.root, text="New game", command=self.new_game())
        # self.new_game.place(x=307, y=402, height=27, width=100)

        connect = threading.Thread(target=self.connect_to_server)
        connect.start()

    def create_card(self, image_path):
        card_image = Image.open(image_path)
        card_image = card_image.resize((int(card_image.width * 1.7), int(card_image.height * 1.7)))
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self.root, image=card_photo, bd=0)
        card_label.image = card_photo
        return card_label

    def start_animation_card(self):
        self.animate_card_thread = threading.Thread(target=self.animate_card_rise)
        self.animate_card_thread.start()
        self.image_player_card()

    def start_flop_card(self):
        self.animate_flop_thread = threading.Thread(target=self.giveaway_flop)
        self.animate_flop_thread.start()
        # self.check_combination_player()

    def start_turn_card(self):
        self.animate_turn_thread = threading.Thread(target=self.giveaway_turn)
        self.animate_turn_thread.start()
        # self.check_combination_player()

    def start_river_card(self):
        self.animate_river_thread = threading.Thread(target=self.giveaway_river)
        self.animate_river_thread.start()
        # self.check_combination_player()

    def image_player_card(self):
        card_player = [self.back_card_image_me_label, self.back_card_2_image_me_label]
        for i in range(2):
            player_card = Image.open(f"C:\\Users\\griba\\Cursach\\image\\cards\\card_{self.dict['client'][i]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card_player[i].configure(image=player_card)
            card_player[i].image = player_card

    def animate_card_rise(self):
        card_info = [
            {"label": self.back_card_image_me_label, "y_step": 1.84, "x_step": -5.9},
            {"label": self.back_card_image_label_your, "y_step": -3.23, "x_step": -3.26},
            {"label": self.back_card_2_image_me_label, "y_step": 1.84, "x_step": -5.6},
            {"label": self.back_card_2_image_label_your, "y_step": -3.23, "x_step": -2.96}
        ]
        for card in card_info:
            start_y = 340
            start_x = 945
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.root.update()

    def giveaway_flop(self):
        # self.card_image_flop_1.place(x=310, y=260)
        # self.card_image_flop_2.place(x=405, y=260)
        # self.card_image_flop_3.place(x=500, y=260)
        card_flop = [self.card_image_flop_1, self.card_image_flop_2, self.card_image_flop_3]
        for i in range(3):
            player_card = Image.open(f"C:\\Users\\griba\\Cursach\\image\\cards\\card_{self.dict['flop'][i]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card_flop[i].configure(image=player_card)
            card_flop[i].image = player_card
        card_info = [
            {"label": self.card_image_flop_1, "y_step": -0.8, "x_step": -6.35},
            {"label": self.card_image_flop_2, "y_step": -0.8, "x_step": -5.40},
            {"label": self.card_image_flop_3, "y_step": -0.8, "x_step": -4.45}
        ]
        for card in card_info:
            start_y = 340
            start_x = 945
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.root.update()

    def giveaway_turn(self):
        # self.card_image_tern.place(x=595, y=260)
        # cards_turn_table = self.game.display_turn_cards_table()['turn']
        player_card = Image.open(f"C:\\Users\\griba\\Cursach\\image\\cards\\card_{self.dict['turn'][0]}.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.card_image_tern.configure(image=player_card)
        self.card_image_tern.image = player_card
        card_info = [
            {"label": self.card_image_tern, "y_step": -0.8, "x_step": -3.5},
        ]
        for card in card_info:
            start_y = 340
            start_x = 945
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.root.update()

    def giveaway_river(self):
        # self.card_image_river.place(x=690, y=260)
        # cards_turn_table = self.game.display_turn_cards_table()['turn']
        player_card = Image.open(f"C:\\Users\\griba\\Cursach\\image\\cards\\card_{self.dict['river'][0]}.png")
        player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
        player_card = ImageTk.PhotoImage(player_card)
        self.card_image_river.configure(image=player_card)
        self.card_image_river.image = player_card
        card_info = [
            {"label": self.card_image_river, "y_step": -0.8, "x_step": -2.55},
        ]
        for card in card_info:
            start_y = 340
            start_x = 945
            for i in range(20):
                time.sleep(0.005)
                start_y += card["y_step"]*5
                start_x += card["x_step"]*5
                card["label"].place(x=start_x, y=start_y)
            self.root.update()

    def restart(self):
        card_info = [
            {"label": self.back_card_image_me_label, "y_step": 1.77, "x_step": -5.44},
            {"label": self.back_card_2_image_me_label, "y_step": 1.77, "x_step": -5.14},
            {"label": self.back_card_image_label_your, "y_step": 1.77, "x_step": -5.44},
            {"label": self.back_card_2_image_label_your, "y_step": 1.77, "x_step": -5.14},
            {"label": self.card_image_flop_1, "y_step": -0.73, "x_step": -5.44},
            {"label": self.card_image_flop_2, "y_step": -0.73, "x_step": -4.49},
            {"label": self.card_image_flop_3, "y_step": -0.73, "x_step": -3.54},
            {"label": self.card_image_river, "y_step": -0.73, "x_step": -1.64},
            {"label": self.card_image_tern, "y_step": -0.73, "x_step": -2.59}
        ]
        for card in card_info:
            card['label'].place(x=945, y=340)
        self.start_animation_card()

    def receive_data(self, client_socket):
        while True:
            resp = client_socket.recv(4096)
            if not len(resp):
                break
            else:
                self.dict = pickle.loads(resp)
                if self.dict['command'] == 'flop':
                    self.start_flop_card()
                elif self.dict['command'] == 'turn':
                    self.start_turn_card()
                elif self.dict['command'] == 'river':
                    self.start_river_card()
                elif self.dict['command'] == 'new_game':
                    self.restart()
                # Добавьте код для обработки полученных данных, если необходимо

    def connect_to_server(self):
        HOST = ("localhost", 10000)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(HOST)
        print("Connected to", HOST)
        resp = client.recv(4096)
        self.dict = pickle.loads(resp)
        self.start_animation_card()
        threading.Thread(target=self.receive_data, args=(client,), daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = PokerClient(root)
    root.geometry("1100x800")
    root.mainloop()
