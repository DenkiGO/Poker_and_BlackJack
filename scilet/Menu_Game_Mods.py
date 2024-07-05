import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class Game_Mods(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom Window")
        self.geometry("1100x800")

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        background_image = Image.open("../image/background/background.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self, image=background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        self.background_label.image = background_photo

        frame_image = Image.open("../image/frame/frame_game_mods.png")
        frame_photo = ImageTk.PhotoImage(frame_image)
        frame_label = tk.Label(self, image=frame_photo, bd=0)
        frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_label.image = frame_photo

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])

        self.blackjack_button = ttk.Button(self, text="BlackJack")
        self.blackjack_button.place(x=407, y=343, height=28, width=287)

        self.texasholdem_button = ttk.Button(self, text="Texas Holdem")
        self.texasholdem_button.place(x=407, y=382, height=28, width=287)

        self.slotmachine_button = ttk.Button(self, text="Slot Machine")
        self.slotmachine_button.place(x=407, y=421, height=28, width=287)

        self.roulette_button = ttk.Button(self, text="Roulette")
        self.roulette_button.place(x=407, y=460, height=28, width=287)

        self.style.configure("Custom.TButton", font=custom_font)
        self.blackjack_button.configure(style="Custom.TButton")
        self.texasholdem_button.configure(style="Custom.TButton")
        self.slotmachine_button.configure(style="Custom.TButton")
        self.roulette_button.configure(style="Custom.TButton")


if __name__ == "__main__":
    app = Game_Mods()
    app.mainloop()
