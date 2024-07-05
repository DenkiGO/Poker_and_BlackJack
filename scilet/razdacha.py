import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
import threading


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Texas holdem")
        self.geometry("1100x800")
        self.resizable(False, False)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.background_image = Image.open("C:\\Users\\griba\\Cursach\\image\\background\\background_game_fin_male.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")
        self.style.configure("Custom.TButton", font=custom_font)

        self.back_card_image_me_label = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_me_label = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_image_label_dog = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_dog = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_image_label_female = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_female = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_image_label_marco = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_marco = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_image_label_bear = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_bear = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_image_label_mike = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.back_card_2_image_label_mike = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")

        self.card_image_flop_1 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.card_image_flop_2 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.card_image_flop_3 = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.card_image_tern = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.card_image_river = self.create_card("C:\\Users\\griba\\Cursach\\image\\cards\\card_backs_2.png")
        self.card_image_flop_1.place(x=370, y=260)
        self.card_image_flop_2.place(x=465, y=260)
        self.card_image_flop_3.place(x=560, y=260)
        self.card_image_tern.place(x=655, y=260)
        self.card_image_river.place(x=750, y=260)

        # self.new_game = ttk.Button(self, text="New game", command=self.repid)
        # self.new_game.place(x=407, y=402, height=27, width=287)

        self.animate_card_thread = threading.Thread(target=self.animate_card_rise)
        self.animate_card_thread.start()

    def repid(self):
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
            {"label": self.back_card_2_image_label_mike, "y_step": -3.03, "x_step": -0.94}
        ]
        for card in card_info:
            card['label'].place(x=914, y=333)
        self.animate_card_thread = threading.Thread(target=self.animate_card_rise)
        self.animate_card_thread.start()

    def create_card(self, image_path):
        card_image = Image.open(image_path)
        card_image = card_image.resize((int(card_image.width * 1.7), int(card_image.height * 1.7)))
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(self, image=card_photo, bd=0)
        card_label.image = card_photo
        return card_label

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
            for i in range(100):
                start_y += card["y_step"]
                start_x += card["x_step"]
                card["label"].place(x=start_x, y=start_y)
            self.update()


if __name__ == "__main__":
    app = Game()
    app.mainloop()
