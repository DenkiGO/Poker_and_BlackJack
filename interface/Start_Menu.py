import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        background_image = Image.open("image\\background\\background.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label = tk.Label(self, image=background_photo, font=controller.title_font)
        self.background_label.place(relwidth=1, relheight=1)
        self.background_label.image = background_photo

        frame_image = Image.open("image\\frame\\frame_menu.png")
        frame_photo = ImageTk.PhotoImage(frame_image)
        frame_label = tk.Label(self, image=frame_photo, bd=0, font=controller.title_font)
        frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_label.image = frame_photo

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])

        self.cont = ttk.Button(self, text="Continue", command=lambda: controller.show_frame("Game_Mods"))
        self.cont.place(x=407, y=363, height=27, width=287)

        self.new_game = ttk.Button(self, text="New game", command=lambda: controller.show_frame("New_game"))
        self.new_game.place(x=407, y=402, height=27, width=287)

        self.exit = ttk.Button(self, text="Exit", command=self.exit)
        self.exit.place(x=407, y=441, height=27, width=287)

        self.style.configure("Custom.TButton", font=custom_font)
        self.cont.configure(style="Custom.TButton")
        self.new_game.configure(style="Custom.TButton")
        self.exit.configure(style="Custom.TButton")

        self.check_cont_file()

    def check_cont_file(self):
        with open('save.txt', 'r') as file:
            line = file.readline()
            if len(line) == 0:
                self.cont.configure(state="disabled")

    def button_click(self):
        print("Кнопка была нажата!")

    def exit(self):
        self.controller.destroy()