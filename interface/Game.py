import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
from poker.poker_game import TexasHoldemGame
from interface import Bet_Frame_Player
import random
import threading
import time


class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.data_from_toplevel = tk.StringVar()

        self.custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.gender = "Male"
        self.player_chips = 1000
        self.player_name = "You"

        self.background_image = Image.open("image\\background\\background_game_fin_male.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.chips_on_the_table = ttk.Entry(self, style="TEntry", font=self.custom_font, state="readonly")
        self.chips_on_the_table.configure(justify="center")
        self.chips_on_the_table.place(x=485, y=458, height=30, width=130)

        self.name_player_label = tk.Label(self, text="  ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.name_player_label.place(x=495, y=653, width=140)

        self.chips_player_label = tk.Label(self, text=f"{self.player_chips} $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_player_label.place(x=495, y=678, width=140)

        self.chips_player_label_command = tk.Label(self, text="   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_player_label_command.place(x=495, y=725, width=140)

        self.chips_crazy_stu_label = tk.Label(self, text=f"1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_crazy_stu_label.place(x=415, y=202, width=140)

        self.chips_crazy_stu_label_command = tk.Label(self, text=f"   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_crazy_stu_label_command.place(x=415, y=249, width=140)

        self.chips_mike_label = tk.Label(self, text=f"1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_mike_label.place(x=905, y=200, width=140)

        self.chips_mike_label_command = tk.Label(self, text=f"   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_mike_label_command.place(x=905, y=247, width=140)

        self.chips_cool_dog_label = tk.Label(self, text=f"1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_cool_dog_label.place(x=907, y=679, width=140)

        self.chips_cool_dog_label_command = tk.Label(self, text=f"   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_cool_dog_label_command.place(x=907, y=726, width=140)

        self.chips_cathrine_label = tk.Label(self, text=f"1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_cathrine_label.place(x=60, y=623, width=140)

        self.chips_cathrine_label_command = tk.Label(self, text=f"   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_cathrine_label_command.place(x=60, y=670, width=140)

        self.chips_marco_rues_label = tk.Label(self, text=f"1000 $", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_marco_rues_label.place(x=60, y=319, width=140)

        self.chips_marco_rues_label_command = tk.Label(self, text=f"   ", font=("Classic Console Neue", 15), bg='#cbbc3b')
        self.chips_marco_rues_label_command.place(x=60, y=366, width=140)

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        self.style.configure("Custom.TButton", font=self.custom_font)

        self.win_label = tk.Label()

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

        # 45, 128
        # x=907, y=679

        self.big_blind = 10
        self.small_blind = 5

        try:
            with open('save.txt', 'r') as file:
                self.save_dict = eval(file.readline())
                self.player_chips = int(self.save_dict["chips"])
                self.player_name = self.save_dict["name"]
                self.name_player_label.configure(text=self.player_name)
                self.gender = self.save_dict["gender"]
        except:
            pass

        self.update_background_info()

        self.start_new_game = [
            {"name": "Catherine", "start_chips": 1000, "blind": 0, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_cathrine_label, "player": "bot", "card": [self.back_card_2_image_label_female, self.back_card_image_label_female], "player_id": '-', "player_cards": "-", "label_command": self.chips_cathrine_label_command, "label_win": (30, 450), "state_flag": 0},
            {"name": "Marco Reus", "start_chips": 1000, "blind": 1, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_marco_rues_label, "player": "bot", "card": [self.back_card_2_image_label_marco, self.back_card_image_label_marco], "player_id": '-', "player_cards": "-", "label_command": self.chips_marco_rues_label_command, "label_win": (30, 130), "state_flag": 0},
            {"name": "Crazy Stu", "start_chips": 1000, "blind": 2, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_crazy_stu_label, "player": "bot", "card": [self.back_card_2_image_label_bear, self.back_card_image_label_bear], "player_id": '-', "player_cards": "-", "label_command": self.chips_crazy_stu_label_command, "label_win": (370, 75), "state_flag": 0},
            {"name": "Mike", "start_chips": 1000, "blind": 0, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_mike_label, "player": "bot", "card": [self.back_card_2_image_label_mike, self.back_card_image_label_mike], "player_id": '-', "player_cards": "-", "label_command": self.chips_mike_label_command, "label_win": (1030, 30), "state_flag": 0},
            {"name": "Cool dog", "start_chips": 1000, "blind": 0, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_cool_dog_label, "player": "bot", "card": [self.back_card_2_image_label_dog, self.back_card_image_label_dog], "player_id": '-', "player_cards": "-", "label_command": self.chips_cool_dog_label_command, "label_win": (1045, 530), "state_flag": 0},
            {"name": self.player_name, "start_chips": self.player_chips, "blind": 0, "command": None, "active": 0, "bet": 0, "label_chips": self.chips_player_label, "player": "human", "card": [self.back_card_2_image_me_label, self.back_card_image_me_label], "player_id": '-', "player_cards": "-", "label_command": self.chips_player_label_command, "label_win": (630, 550), "state_flag": 0}
        ]

        self.animate_event = threading.Event()
        self.flop_event = threading.Event()
        self.tern_event = threading.Event()
        self.river_event = threading.Event()
        # self.flop_event = threading.Event(
        self.bet_player_event = threading.Event()
        self.update_window()

        self.create_ready_frame()

        self.count = 0

    def save_player_data(self):
        new_save_dict = {"name": self.save_dict["name"], "chips": self.start_new_game[-1]["start_chips"], "gender": self.save_dict["gender"]}
        with open('save.txt', 'w') as file:
            file.write(f"{new_save_dict}")

    def create_ready_frame(self):
        self.image = Image.open("image\\frame\\main_frame_blackjack_start.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.frame = tk.Label(self, image=self.photo, bd=0)
        self.frame.image = self.photo
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.start_blackjack = ttk.Button(self, text="Ready", style="Custom.TButton", command=self.start_main_game)
        self.start_blackjack.place(x=474, y=406, width=151, height=29)

    def create_game_over_frame(self):
        self.image = Image.open("image\\frame\\main_frame_game_over.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.frame_game_over = tk.Label(self, image=self.photo, bd=0)
        self.frame_game_over.image = self.photo
        self.frame_game_over.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.game_over_button = ttk.Button(self, text="New Game", style="Custom.TButton", command=self.game_over)
        self.game_over_button.place(x=474, y=406, width=151, height=29)

    def game_over(self):
        self.frame_game_over.destroy()
        self.game_over_button.destroy()
        self.create_ready_frame()
        self.controller.show_frame("New_game")

    def start_main_game(self):
        self.start_blackjack.destroy()
        self.frame.destroy()
        try:
            with open('save.txt', 'r') as file:
                self.save_dict = eval(file.readline())
                self.start_new_game[-1]["start_chips"] = int(self.save_dict["chips"])
                self.player_name = self.save_dict["name"]
                self.name_player_label.configure(text=self.player_name)
                self.gender = self.save_dict["gender"]
            self.update_window()
            if self.start_new_game[-1]["start_chips"] > 0:
                self.start_blackjack.destroy()
                self.frame.destroy()
                game_thread = threading.Thread(target=self.main_game)
                game_thread.start()
            else:
                self.create_game_over_frame()
        except:
            self.create_game_over_frame()

    def main_game(self):
        self.state_flag = 1
        self.repid()
        self.animate_event.wait()
        self.animate_event.clear()
        self.check_blind()
        self.start_check_active_thread()
        if self.win != True:
            self.flop_event.wait()
            self.flop_event.clear()
            self.state_flag = 2
            self.clear_label_command()
            self.start_flop_card()
            self.check_active()
            if self.win != True:
                self.flop_event.wait()
                self.flop_event.clear()
                self.state_flag = 3
                self.clear_label_command()
                self.start_turn_card()
                self.check_active()
                if self.win != True:
                    self.flop_event.wait()
                    self.flop_event.clear()
                    self.state_flag = 4
                    self.clear_label_command()
                    self.start_river_card()
                    self.check_active()
                    if self.win != True:
                        print("final")
                        self.flop_event.wait()
                        self.flop_event.clear()
                        self.win_opr()
        self.create_ready_frame()

    def start_check_active_thread(self):
        self.active_thread = threading.Thread(target=self.check_active)
        self.active_thread.start()

    def sleep_check_active(self):
        time.sleep(1)
        self.check_active()

    def active_player(self):
        self.thread_player_bet = threading.Thread(target=self.open_bet_frame_player)
        self.thread_player_bet.start()
        self.bet_player_event.wait()
        self.bet_player_event.clear()

    def check_active(self):
        for index, player in enumerate(self.start_new_game):
            if player["active"] == 1:
                if player["start_chips"] > 0:
                    if player["player"] == "human":
                        self.active_player()
                        break
                    else:
                        player["active"] = 0
                        try:
                            for i in range(1, 6):
                                if self.start_new_game[index + i]["command"] != "fold" and self.start_new_game[index + i]["start_chips"] > 0:
                                    self.start_new_game[index + i]["active"] = 1
                                    break
                        except:
                            for i in range(7):
                                if self.start_new_game[i]["command"] != "fold" and self.start_new_game[i]["start_chips"] > 0:
                                    self.start_new_game[i]["active"] = 1
                                    break
                        call = 0
                        for pl in self.start_new_game:
                            if pl["bet"] > call:
                                call = pl["bet"]
                        call_bot = call - player["bet"]
                        if call_bot == 0:
                            call_check = "check"
                        else:
                            call_check = "call"
                        if player["start_chips"] - self.big_blind < 0:
                            rise = call_check
                        else:
                            rise = "rise"
                        action = [rise, "fold",  call_check]
                        var = [0.1, 0.05, 0.85]
                        player["command"] = random.choices(action, var)[0]
                        player["label_command"].configure(text=f"{player['command']}")
                        print(player['name'], player["command"])
                        if player["command"] == "fold":
                            for card in player["card"]:
                                card.place(x=914, y=333)
                            active_player = 0
                            for player in self.start_new_game:
                                if player["command"] != "fold" and player["start_chips"] > 0:
                                    active_player += 1
                            if active_player == 1:
                                self.win_opr()
                            else:
                                self.update_window()
                                self.sleep_check_active()
                        elif player["command"] == "check":
                            player["state_flag"] = self.state_flag
                            flag = False
                            for pl in self.start_new_game:
                                if pl['command'] != 'fold' and pl["bet"] != player["bet"] and pl['start_chips'] > 0:
                                    flag = True
                                    break
                            for pl in self.start_new_game:
                                if pl["state_flag"] != self.state_flag and pl['command'] != "fold" and pl['start_chips'] > 0:
                                    flag = True
                                    break
                            if flag == False:
                                self.update_window()
                                self.flop_event.set()
                                break
                            else:
                                self.sleep_check_active()
                                self.update_window()
                                break
                        elif player["command"] == "call":
                            flag = False
                            player["state_flag"] = self.state_flag
                            if player["start_chips"] - call_bot < 0:
                                player["start_chips"] = 0
                                player["command"] = "fold"
                                player["bet"] = player["bet"] + player["start_chips"]
                                for card in player["card"]:
                                    card.place(x=914, y=333)
                                active_player = 0
                                for player in self.start_new_game:
                                    if player["command"] != "fold" and player["start_chips"] > 0:
                                        active_player += 1
                                if active_player == 1:
                                    self.win_opr()
                                else:
                                    self.update_window()
                                    self.sleep_check_active()
                                    break
                            else:
                                player["start_chips"] = player["start_chips"] - call_bot
                                player["bet"] = player["bet"] + call_bot
                                self.update_window()
                                for pl in self.start_new_game:
                                    if pl['command'] != "false" and pl["bet"] != player["bet"]:
                                        flag = True
                                        break
                                for pl in self.start_new_game:
                                    if pl["state_flag"] != self.state_flag and pl['command'] != "fold" and pl['start_chips'] > 0:
                                        flag = True
                                        break
                                if flag == False:
                                    self.flop_event.set()
                                    break
                                else:
                                    self.sleep_check_active()
                                    break
                        elif player["command"] == "rise":
                            player["state_flag"] = self.state_flag
                            self.rise = True
                            player["start_chips"] = player["start_chips"] - self.big_blind - call_bot
                            player["bet"] = player["bet"] + self.big_blind + call_bot
                            self.update_window()
                            self.sleep_check_active()
                            break
                        self.update_window()
                        break
                else:
                    player["active"] = 0
                    try:
                        for i in range(1, 6):
                            if self.start_new_game[index + i]["command"] != "fold" and self.start_new_game[index + i]["start_chips"] > 0:
                                self.start_new_game[index + i]["active"] = 1
                                break
                    except:
                        for i in range(7):
                            if self.start_new_game[i]["command"] != "fold" and self.start_new_game[i]["start_chips"] > 0:
                                self.start_new_game[i]["active"] = 1
                                break
                    self.sleep_check_active()
                    break

    def check_command(self):
        self.start_new_game[self.player_index]["state_flag"] = self.state_flag
        if self.start_new_game[self.player_index]["command"] == "fold":
            for card in self.start_new_game[self.player_index]["card"]:
                card.place(x=914, y=333)
            active_player = 0
            for player in self.start_new_game:
                if player["command"] != "fold" and player["start_chips"] > 0:
                    active_player += 1
            if active_player == 1:
                self.win_opr()
            else:
                self.start_check_active_thread()
        if self.start_new_game[self.player_index]["command"] == "check":
            flag = False
            for pl in self.start_new_game:
                if pl['command'] != 'fold' and pl["bet"] != self.start_new_game[self.player_index]["bet"] and pl['start_chips'] > 0:
                    flag = True
                    break
            for pl in self.start_new_game:
                if pl["state_flag"] != self.state_flag and pl['command'] != "fold" and pl['start_chips'] > 0:
                    flag = True
                    break
            if flag == False:
                self.update_window()
                self.flop_event.set()
            else:
                self.start_check_active_thread()
                self.update_window()
        if self.start_new_game[self.player_index]["command"] == "call":
            flag = False
            self.start_new_game[self.player_index]["start_chips"] = self.start_new_game[self.player_index]["start_chips"] - self.call_top
            self.start_new_game[self.player_index]["bet"] = self.start_new_game[self.player_index]["bet"] + self.call_top
            if self.start_new_game[self.player_index]["start_chips"] < 0:
                self.start_new_game[self.player_index]["start_chips"] = 0
            for player in self.start_new_game:
                if player['bet'] != self.start_new_game[self.player_index]["bet"] or player['state_flag'] != self.state_flag:
                    if player['command'] != "fold" and player['start_chips'] > 0:
                        flag = True
                        break
            if flag == False:
                self.update_window()
                self.flop_event.set()
            else:
                self.update_window()
                self.start_check_active_thread()
        if self.start_new_game[self.player_index]["command"] == "rise":
            self.clear_label_command()
            self.rise = True
            self.start_new_game[self.player_index]["start_chips"] = self.start_new_game[self.player_index]["start_chips"] - self.big_blind
            self.start_new_game[self.player_index]["bet"] = self.start_new_game[self.player_index]["bet"] + self.big_blind
            if self.start_new_game[self.player_index]["start_chips"] < 0:
                self.start_new_game[self.player_index]["start_chips"] = 0
            self.update_window()
            self.start_check_active_thread()

    def win_opr(self):
        self.win = True
        active_player = []
        for player in self.start_new_game:
            if player["start_chips"] > 0 and player["command"] != "fold":
                active_player.append(player["player_id"])
        player_win, comb = self.game.determine_the_winner_play_bots(active_player)
        self.image_player_card(player_win)
        for player in self.start_new_game:
            if player["start_chips"] > 0 and player["command"] != "fold":
                if player["player_id"] == player_win:
                    player["start_chips"] += self.total_bet
                    x, y = player["label_win"]
                    card_image = Image.open("image\\combination\\win.png")
                    card_photo = ImageTk.PhotoImage(card_image)
                    self.win_label = tk.Label(self, image=card_photo, bd=0)
                    self.win_label.image = card_photo
                    self.win_label.place(x=x, y=y)
                    break
        self.update_window()
        self.save_player_data()

    def text_toplevel(self, data):
        for i in range(len(self.start_new_game)):
            if self.start_new_game[i]["player"] == "human":
                self.player_index = i
                self.start_new_game[i]["command"] = data
                self.start_new_game[i]["active"] = 0
                try:
                    for j in range(1, 6):
                        if self.start_new_game[i + j]["command"] != "fold":
                            self.start_new_game[i + j]["active"] = 1
                            break
                except:
                    for j in range(7):
                        if self.start_new_game[j]["command"] != "fold":
                            self.start_new_game[j]["active"] = 1
                            break
                break
        self.check_command()

    def open_bet_frame_player(self):
        print(1)
        self.bet_player_event.set()
        call = 0
        bet_player = 0
        for player in self.start_new_game:
            if player["bet"] > call:
                call = player["bet"]
            if player["player"] == "human":
                bet_player = player["bet"]
        self.call_top = call - bet_player
        bet_frame_player = Bet_Frame_Player.Main_Frame_Bet(self, self.data_from_toplevel, self.text_toplevel, self.call_top, self.big_blind)
        bet_frame_player.grab_set()

    def update_window(self):
        self.chips_on_the_table.configure(state="normal")
        self.chips_on_the_table.delete(0, tk.END)
        self.total_bet = 0
        for player in self.start_new_game:
            self.total_bet += player["bet"]
            player["label_chips"].config(text=f"{player['start_chips']} $")
        self.chips_on_the_table.insert(0, f"{self.total_bet} $")
        self.chips_on_the_table.configure(state="readonly")

    def check_blind(self):
        for i in range(len(self.start_new_game)):
            if self.start_new_game[i]["blind"] == 1:
                self.start_new_game[i]["bet"] = self.small_blind
                self.start_new_game[i]["label_command"].configure(text="small blind")
                self.start_new_game[i]["start_chips"] = self.start_new_game[i]["start_chips"] - self.small_blind
            if self.start_new_game[i]["blind"] == 2:
                self.start_new_game[i]["label_command"].configure(text="big blind")
                self.start_new_game[i]["bet"] = self.big_blind
                self.start_new_game[i]["start_chips"] = self.start_new_game[i]["start_chips"] - self.big_blind
        for i in range(len(self.start_new_game)):
            if self.start_new_game[i]["blind"] == 1:
                self.start_new_game[i]["blind"] = 0
            if self.start_new_game[i]["blind"] == 2:
                self.start_new_game[i]["blind"] = 1
                try:
                    for j in range(6):
                        if self.start_new_game[i + j + 1]["start_chips"] > 0:
                            self.start_new_game[i + j + 1]["blind"] = 2
                            self.start_new_game[i + j + 1]["active"] = 1
                            break
                except:
                    for j in range(6):
                        if self.start_new_game[j]["start_chips"] > 0:
                            self.start_new_game[j]["active"] = 1
                            self.start_new_game[j]["blind"] = 2
                            break
                break
        self.update_window()

    def check_combination_player(self):
        if self.start_new_game[-1]["command"] != "fold":
            background_image = Image.open(f"image\\combination\\combination_bot\\{self.game.combinations_player_server()}.png")
            background_photo = ImageTk.PhotoImage(background_image)
            self.combination_player_label.configure(image=background_photo)
            self.combination_player_label.image = background_photo
        else:
            card_image = Image.open("image\\combination\\combination_bot\\Start comb.png")
            card_photo = ImageTk.PhotoImage(card_image)
            self.combination_player_label = tk.Label(self, image=card_photo, bd=0)
            self.combination_player_label.image = card_photo
            self.combination_player_label.place(x=377, y=640)

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
            {"label": self.back_card_image_label_dog, "y_step": 1.77, "x_step": -1.34, "id_player": 4},
            {"label": self.back_card_image_me_label, "y_step": 1.77, "x_step": -5.44, "id_player": 5},
            {"label": self.back_card_image_label_female, "y_step": 1.22, "x_step": -7.24, "id_player": 0},
            {"label": self.back_card_image_label_marco, "y_step": -1.83, "x_step": -7.14, "id_player": 1},
            {"label": self.back_card_image_label_bear, "y_step": -3.03, "x_step": -3.54, "id_player": 2},
            {"label": self.back_card_image_label_mike, "y_step": -3.03, "x_step": -1.24, "id_player": 3},
            {"label": self.back_card_2_image_label_dog, "y_step": 1.77, "x_step": -1.04, "id_player": 4},
            {"label": self.back_card_2_image_me_label, "y_step": 1.77, "x_step": -5.14, "id_player": 5},
            {"label": self.back_card_2_image_label_female, "y_step": 1.22, "x_step": -6.94, "id_player": 0},
            {"label": self.back_card_2_image_label_marco, "y_step": -1.83, "x_step": -6.84, "id_player": 1},
            {"label": self.back_card_2_image_label_bear, "y_step": -3.03, "x_step": -3.24, "id_player": 2},
            {"label": self.back_card_2_image_label_mike, "y_step": -3.03, "x_step": -0.94, "id_player": 3}
        ]
        for card in card_info:
            if self.start_new_game[card["id_player"]]["start_chips"] > 0:
                start_y = 333
                start_x = 914
                for i in range(20):
                    time.sleep(0.005)
                    start_y += card["y_step"]*5
                    start_x += card["x_step"]*5
                    card["label"].place(x=start_x, y=start_y)
                self.update()
        self.animate_event.set()

    def update_background_info(self):
        if self.gender == "Male":
            pass
        else:
            background_image = Image.open("image\\background\\background_game_fin_female.png")
            background_photo = ImageTk.PhotoImage(background_image)
            self.background_label.configure(image=background_photo)
            self.background_label.image = background_photo

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
        self.count = 0
        for player in self.start_new_game:
            if player["start_chips"] > 0:
                self.count += 1
        self.game = TexasHoldemGame(num_players=self.count)
        self.giveaway_card_players()
        if self.start_new_game[-1]["start_chips"] > 0:
            self.image_player_card_me()

    def giveaway_card_players(self):
        self.game.giveaway_card()
        players_and_card = self.game.display_players_cards_play_bots()
        pl_id = list(players_and_card.keys())
        for player in self.start_new_game:
            if player["start_chips"] > 0:
                player["player_id"] = pl_id.pop()
                player["player_cards"] = players_and_card[player["player_id"]]

    def image_player_card_me(self):
        card_player = self.start_new_game[-1]["card"]
        for i in range(2):
            player_card = Image.open(f"image\\cards\\card_{self.start_new_game[-1]['player_cards'][i]}.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card_player[i].configure(image=player_card)
            card_player[i].image = player_card

    def image_player_card(self, player_win):
        for player in self.start_new_game:
            if player["player_id"] == player_win:
                card_player = player["card"]
                cards = player["player_cards"]
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
            {"label": self.card_image_flop_1, "y_step": -0.53, "x_step": -5.44},
            {"label": self.card_image_flop_2, "y_step": -0.53, "x_step": -4.49},
            {"label": self.card_image_flop_3, "y_step": -0.53, "x_step": -3.54}
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
            {"label": self.card_image_tern, "y_step": -0.53, "x_step": -2.59},
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
            {"label": self.card_image_river, "y_step": -0.53, "x_step": -1.64}
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

    def clear_label_command(self):
        for player in self.start_new_game:
            if player["label_command"] != "fold":
                player["label_command"].configure(text="   ")

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
        self.win_label.destroy()
        self.rise = False
        self.win = False
        for card in card_info:
            card['label'].place(x=914, y=333)
            player_card = Image.open(f"image\\cards\\card_backs_2.png")
            player_card = player_card.resize((int(player_card.width * 1.7), int(player_card.height * 1.7)))
            player_card = ImageTk.PhotoImage(player_card)
            card['label'].configure(image=player_card)
            card['label'].image = player_card
        for player in self.start_new_game:
            player["state_flag"] = 0
            player["active"] = 0
            player["command"] = "-"
            player["bet"] = 0
            player["label_command"].configure(text="   ")
        self.chips_on_the_table.configure(state="normal")
        self.chips_on_the_table.delete(0, tk.END)
        self.chips_on_the_table.configure(state="readonly")
        self.start_animation_card()
        self.start_game()

# if __name__ == "__main__":
#     app = Game()
#     app.mainloop()
