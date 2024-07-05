import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class New_game_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        background_image = Image.open("image\\background\\background.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self, image=background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        self.background_label.image = background_photo

        frame_image = Image.open("image\\frame\\frame_new_game_start_fin.png")
        frame_photo = ImageTk.PhotoImage(frame_image)
        frame_label = tk.Label(self, image=frame_photo, bd=0)
        frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_label.image = frame_photo

        self.welcome_label = tk.Label(self, text="Hello, player!", font=("Classic Console Neue", 15), bg='#a9aaa7')
        self.welcome_label.place(x=385, y=249)

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.OK_new_game = ttk.Button(self, text="OK", command=lambda: controller.show_frame("Game_Mods"))
        self.OK_new_game.place(x=407, y=542, height=27, width=287)

        self.style.configure("Custom.TButton", font=custom_font)
        self.OK_new_game.configure(style="Custom.TButton")

    def update_player_info(self, player_name, gender):
        self.player_name = player_name
        self.gender = gender
        self.welcome_label.config(text=f"Hello, {player_name}!")