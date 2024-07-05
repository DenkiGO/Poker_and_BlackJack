import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class New_game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.controller = controller

        background_image = Image.open("image\\background\\background.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self, image=background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        self.background_label.image = background_photo

        frame_image = Image.open("image\\frame\\frame_new_game_fin.png")
        frame_photo = ImageTk.PhotoImage(frame_image)
        frame_label = tk.Label(self, image=frame_photo, bd=0)
        frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_label.image = frame_photo

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        self.style.map('TRadiobutton', background=[('!active', '#a9aaa7'), ('pressed', '#a9aaa7'), ('active', '#a9aaa7')])
        self.OK_new_game = ttk.Button(self, text="OK", command=self.get_player_info)
        self.OK_new_game.place(x=406, y=496, height=30, width=137)

        self.cancel_new_game = ttk.Button(self, text="Cancel", command=lambda: controller.show_frame("Menu"))
        self.cancel_new_game.place(x=558, y=496, height=30, width=137)

        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")

        self.female_radio = ttk.Radiobutton(self, text="Female", variable=self.gender_var, value="Female",
                                            style="Custom.TRadiobutton")
        self.female_radio.place(x=400, y=405, height=30, width=137)

        self.male_radio = ttk.Radiobutton(self, text="Male", variable=self.gender_var, value="Male",
                                          style="Custom.TRadiobutton")
        self.male_radio.place(x=565, y=405, height=30, width=137)

        self.name_player_new_game = ttk.Entry(self, style="TEntry", font=custom_font)
        self.name_player_new_game.insert(0, "You")
        self.name_player_new_game.configure(justify="center")
        self.name_player_new_game.place(x=400, y=445, height=30, width=300)

        self.style.configure("TEntry",
                 background="green",
                 foreground="black",
                 fieldbackground="#a9aaa7")

        self.style.configure("Custom.TButton", font=custom_font)
        self.style.configure("Custom.TRadiobutton", background="#a9aaa7", font=custom_font)

        self.OK_new_game.configure(style="Custom.TButton")
        self.cancel_new_game.configure(style="Custom.TButton")

    def get_player_info(self):
        save_dict = {"name": self.name_player_new_game.get(), "chips": 1000, "gender": self.gender_var.get()}
        with open('save.txt', 'w') as file:
            file.write(f"{save_dict}")
        player_name = self.name_player_new_game.get()
        gender = self.gender_var.get()
        self.controller.frames["New_game_frame"].update_player_info(player_name, gender)
        self.controller.show_frame("New_game_frame")
