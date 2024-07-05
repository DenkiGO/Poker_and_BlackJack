import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, font
import socket
import pickle
import threading
import time
from interface import Bet_Frame_Player


class PokerClient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.data_from_toplevel = tk.StringVar()

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.background_image = Image.open("image\\background\\background_fin_network_client.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        card_image = Image.open("image\\combination\\combination_networ\\me\\Start comb.png")
        card_photo = ImageTk.PhotoImage(card_image)
        self.combination_player_label_me = tk.Label(self, image=card_photo, bd=0)
        self.combination_player_label_me.image = card_photo
        self.combination_player_label_me.place(x=356, y=658)

        card_image = Image.open("image\\combination\\combination_networ\\your\\Start comb.png")
        card_photo = ImageTk.PhotoImage(card_image)
        self.combination_player_label_you = tk.Label(self, image=card_photo, bd=0)
        self.combination_player_label_you.image = card_photo
        self.combination_player_label_you.place(x=645, y=150)

        card_image = Image.open("image\\combination\\do\\me\\Start.png")
        card_photo = ImageTk.PhotoImage(card_image)
        self.action_player_label_me = tk.Label(self, image=card_photo, bd=0)
        self.action_player_label_me.image = card_photo
        self.action_player_label_me.place(x=356, y=680)

        card_image = Image.open("image\\combination\\do\\your\\Start.png")
        card_photo = ImageTk.PhotoImage(card_image)
        self.action_player_label_you = tk.Label(self, image=card_photo, bd=0)
        self.action_player_label_you.image = card_photo
        self.action_player_label_you.place(x=645, y=173)

        self.back_card_image_me_label = self.create_card("image\\cards\\card_backs_1.png")
        self.back_card_2_image_me_label = self.create_card("image\\cards\\card_backs_1.png")
        self.back_card_image_label_your = self.create_card("image\\cards\\card_backs_1.png")
        self.back_card_2_image_label_your = self.create_card("image\\cards\\card_backs_1.png")

        self.card_image_flop_1 = self.create_card("image\\cards\\card_backs_1.png")
        self.card_image_flop_2 = self.create_card("image\\cards\\card_backs_1.png")
        self.card_image_flop_3 = self.create_card("image\\cards\\card_backs_1.png")
        self.card_image_tern = self.create_card("image\\cards\\card_backs_1.png")
        self.card_image_river = self.create_card("image\\cards\\card_backs_1.png")

        self.top_card_deck = self.create_card("image\\cards\\card_backs_1.png")
        self.top_card_deck.place(x=945, y=340)

        self.name_player_new_game = ttk.Entry(self, style="TEntry", font=custom_font, state="readonly")
        self.name_player_new_game.configure(justify="center")
        self.name_player_new_game.place(x=485, y=458, height=30, width=130)

        self.style.configure("TEntry",
                 background="green",
                 foreground="black",
                 fieldbackground="#a9aaa7")

        self.chips_your_label = tk.Label(self, text="1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_your_label.place(x=475, y=182, width=140)

        self.chips_player_label = tk.Label(self, text="1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_player_label.place(x=475, y=690, width=140)

        self.name_player_label = tk.Label(self, text="  ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.name_player_label.place(x=475, y=670, width=140)

        self.name_you_label = tk.Label(self, text="  ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.name_you_label.place(x=475, y=162, width=140)


    def update_player_info(self, player_name, ipv4_server):
        self.player_name = player_name
        self.ipv4 = ipv4_server
        connect = threading.Thread(target=self.connect_to_server)
        connect.start()

    def update_window(self):
        self.chips_your_label.configure(text=f'{self.player_you["chips"]} $')
        self.chips_player_label.configure(text=f'{self.player_me["chips"]} $')
        self.name_player_new_game.configure(state="normal")
        self.name_player_new_game.delete(0, tk.END)
        self.name_player_new_game.insert(0, f"{self.player_me['bet'] + self.player_you['bet']} $")
        self.name_player_new_game.configure(state="readonly")
        if self.player_you['command'] != "-":
            comb_image = Image.open(f"image\\combination\\do\\your\\{self.player_you['command']}.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.action_player_label_you.configure(image=comb_image)
            self.action_player_label_you.image = comb_image

    def blind(self):
        if self.player_me['blind'] == 0:
            comb_image = Image.open(f"image\\combination\\do\\me\\High Blind.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.action_player_label_me.configure(image=comb_image)
            self.action_player_label_me.image = comb_image
            comb_image = Image.open(f"image\\combination\\do\\your\\Small Blind.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.action_player_label_you.configure(image=comb_image)
            self.action_player_label_you.image = comb_image
        else:
            comb_image = Image.open(f"image\\combination\\do\\me\\Small Blind.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.action_player_label_me.configure(image=comb_image)
            self.action_player_label_me.image = comb_image
            comb_image = Image.open(f"image\\combination\\do\\your\\High Blind.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.action_player_label_you.configure(image=comb_image)
            self.action_player_label_you.image = comb_image
        self.update_window()

    def check_command(self):
        if self.player_me['command'] == "fold":
            self.dict["winner"] = ("0", " ")
        elif self.player_me['command'] == "call":
            call = self.player_you["bet"] - self.player_me["bet"]
            self.player_me["chips"] = self.player_me["chips"] - call
            self.player_me['bet'] = self.player_me['bet'] + call
        elif self.player_me['command'] == "check":
            pass
        elif self.player_me['command'] == "rise":
            self.player_me["chips"] = self.player_me["chips"] - (self.high_blind + (self.player_you['bet'] - self.player_me['bet']))
            self.player_me['bet'] = self.player_me['bet'] + self.high_blind + (self.player_you['bet'] - self.player_me['bet'])
        comb_image = Image.open(f"image\\combination\\do\\me\\{self.player_me['command']}.png")
        comb_image = ImageTk.PhotoImage(comb_image)
        self.action_player_label_me.configure(image=comb_image)
        self.action_player_label_me.image = comb_image
        self.send_server()
        self.update_window()

    def text_toplevel(self, data):
        self.player_me['command'] = data
        self.player_you['active'] = 1
        self.player_me['active'] = 0
        self.check_command()
        print("Data from Toplevel:", data)


    def open_bet_frame_player(self):
        call = self.player_you["bet"] - self.player_me["bet"]
        bet_frame_player = Bet_Frame_Player.Main_Frame_Bet(self, self.data_from_toplevel, self.text_toplevel, call, self.high_blind)
        bet_frame_player.grab_set()


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
        self.image_player_card()

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

    def image_player_card(self):
        card_player = [self.back_card_image_me_label, self.back_card_2_image_me_label]
        for i in range(2):
            player_card = Image.open(f"image\\cards\\card_{self.dict['client'][i]}.png")
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
            self.update()

    def giveaway_flop(self):
        card_flop = [self.card_image_flop_1, self.card_image_flop_2, self.card_image_flop_3]
        for i in range(3):
            player_card = Image.open(f"image\\cards\\card_{self.dict['flop'][i]}.png")
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
            self.update()

    def giveaway_turn(self):
        player_card = Image.open(f"image\\cards\\card_{self.dict['turn'][0]}.png")
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
            self.update()

    def giveaway_river(self):
        player_card = Image.open(f"image\\cards\\card_{self.dict['river'][0]}.png")
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
            self.update()

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
            player_card = Image.open(f"image\\cards\\card_backs_1.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card['label'].configure(image=player_card)
            card['label'].image = player_card
        comb_image = Image.open(f"image\\combination\\do\\me\\Start.png")
        comb_image = ImageTk.PhotoImage(comb_image)
        self.action_player_label_me.configure(image=comb_image)
        self.action_player_label_me.image = comb_image
        self.name_player_new_game.configure(state="normal")
        self.name_player_new_game.delete(0, tk.END)
        self.name_player_new_game.configure(state="readonly")
        comb_image = Image.open(f"image\\combination\\combination_networ\\your\\Start comb.png")
        comb_image = ImageTk.PhotoImage(comb_image)
        self.combination_player_label_you.configure(image=comb_image)
        self.combination_player_label_you.image = comb_image
        player_card = Image.open(f"image\\background\\background_fin_network_client.png")
        player_card = ImageTk.PhotoImage(player_card)
        self.background_label.configure(image=player_card)
        self.background_label.image = player_card
        self.check_combination_player()
        self.start_animation_card()

    def check_combination_player(self):
        comb_image = Image.open(f"image\\combination\\combination_networ\\me\\{self.dict['combination-client']}.png")
        comb_image = ImageTk.PhotoImage(comb_image)
        self.combination_player_label_me.configure(image=comb_image)
        self.combination_player_label_me.image = comb_image

    def send_server(self):
        resp = pickle.dumps({"client": self.player_me, "server": self.player_you})
        self.client.send(resp)

    def receive_data(self, client_socket):
        while True:
            resp = client_socket.recv(4096)
            if not len(resp):
                break
            else:
                self.info = pickle.loads(resp)
                self.dict = self.info['dict']
                self.player_you = self.info['player_me']
                self.player_me = self.info['player_you']
                self.high_blind = self.info['high_blind']
                self.update_window()
                self.dict_command()
                if self.player_me['active'] == 1:
                    self.open_bet_frame_player()

    def dict_command(self):
        if self.dict['command'] == 'flop':
            self.start_flop_card()
        elif self.dict['command'] == 'turn':
            self.start_turn_card()
        elif self.dict['command'] == 'river':
            self.start_river_card()
        elif self.dict['command'] == 'new_game':
            self.restart()
            self.blind()
        elif self.dict['command'] == 'winner':
            self.win_players()
        else:
            pass

    def win_players(self):
        player, combination = self.dict['winner']
        if player == '0':
            print('Сервер вин')
            card_player = [self.back_card_image_label_your, self.back_card_2_image_label_your]
            for i in range(2):
                player_card = Image.open(f"image\\cards\\card_{self.dict['server'][i]}.png")
                player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
                player_card = ImageTk.PhotoImage(player_card)
                card_player[i].configure(image=player_card)
                card_player[i].image = player_card
            comb_image = Image.open(f"image\\combination\\combination_networ\\your\\{self.dict['combination-server']}.png")
            comb_image = ImageTk.PhotoImage(comb_image)
            self.combination_player_label_you.configure(image=comb_image)
            self.combination_player_label_you.image = comb_image
        elif player == '1':
            print('Клиент вин')
        player_card = Image.open(f"image\\background\\win network\\background_fin_network_client_win_{player}.png")
        player_card = ImageTk.PhotoImage(player_card)
        self.background_label.configure(image=player_card)
        self.background_label.image = player_card

    def set_name(self):
        self.name_player_label.config(text=f"{self.player_me['name']}")
        self.name_you_label.config(text=f"{self.player_you['name']}")

    def connect_to_server(self):
        HOST = (self.ipv4, 10000)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(HOST)
        print("Connected to", HOST)
        resp = self.client.recv(4096)
        self.info = pickle.loads(resp)
        self.dict = self.info["dict"]
        self.player_you = self.info['player_me']
        self.player_me = self.info['player_you']
        self.player_me["name"] = self.player_name
        self.high_blind = self.info['high_blind']
        self.set_name()
        self.send_server()
        self.blind()
        self.start_animation_card()
        threading.Thread(target=self.receive_data, args=(self.client,), daemon=True).start()


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = PokerClient(root)
#     root.geometry("1100x800")
#     root.mainloop()
