import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, font
import threading
import time
from random import shuffle

class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom Window")
        self.geometry("1100x800")

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.background_image = Image.open("C:\\Users\\griba\\Cursach\\image\\background\\bg_slot.png")
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.images = [
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\apple.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\berry.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\cherry.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\fruit cocktail.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\lemon.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\peach.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\watermelon.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\melon.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\slots\\pear.png"))
        ]

        self.images_bg_help = [
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_1.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_2.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_3.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_4.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_5.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_6.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_7.png")),
            ImageTk.PhotoImage(Image.open("C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_8.png"))
        ]

        self.stop_event = threading.Event()

        self.create_column_spin_area()
        self.button_slot_machine()

    def create_column_spin_area(self):
        self.rightmost_slot_labels = [
            tk.Label(self, image=self.images[0], bd=0),
            tk.Label(self, image=self.images[1], bd=0),
            tk.Label(self, image=self.images[2], bd=0)
        ]

        for i, label in enumerate(self.rightmost_slot_labels):
            label.image = self.images[i]
            label.place(x=262, y=147 + i * 118)

        self.right_slot_labels = [
            tk.Label(self, image=self.images[0], bd=0),
            tk.Label(self, image=self.images[1], bd=0),
            tk.Label(self, image=self.images[2], bd=0)
        ]

        for i, label in enumerate(self.right_slot_labels):
            label.image = self.images[i]
            label.place(x=382, y=147 + i * 118)

        self.middle_slot_labels = [
            tk.Label(self, image=self.images[0], bd=0),
            tk.Label(self, image=self.images[1], bd=0),
            tk.Label(self, image=self.images[2], bd=0)
        ]

        for i, label in enumerate(self.middle_slot_labels):
            label.image = self.images[i]
            label.place(x=502, y=147 + i * 118)

        self.left_slot_labels = [
            tk.Label(self, image=self.images[0], bd=0),
            tk.Label(self, image=self.images[1], bd=0),
            tk.Label(self, image=self.images[2], bd=0)
        ]

        for i, label in enumerate(self.left_slot_labels):
            label.image = self.images[i]
            label.place(x=624, y=147 + i * 118)

        self.leftmost_slot_labels = [
            tk.Label(self, image=self.images[0], bd=0),
            tk.Label(self, image=self.images[1], bd=0),
            tk.Label(self, image=self.images[2], bd=0)
        ]

        for i, label in enumerate(self.leftmost_slot_labels):
            label.image = self.images[i]
            label.place(x=745, y=147 + i * 118)

    def button_slot_machine(self):
        self.image_normal_help_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\help off.png")
        self.image_pressed_help_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\help active.png")

        self.help_button = tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#a79c85", command=self.help_btn_on)
        self.help_button.config(image=self.image_normal_help_button, relief="sunken", background="#a79c85")
        self.help_button.place(x=100, y=670)

        self.help_button.bind("<Leave>", self.on_help_button_leave)
        self.help_button.bind("<Button-1>", self.on_help_button_enter)


        self.image_normal_bet_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\bet off.png")
        self.image_pressed_bet_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\bet active.png")

        self.bet_button = tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#a79c85")
        self.bet_button.config(image=self.image_normal_bet_button, relief="sunken", background="#a79c85")
        self.bet_button.place(x=550, y=670)

        self.bet_button.bind("<Leave>", self.on_bet_button_leave)
        self.bet_button.bind("<Button-1>", self.on_bet_button_enter)


        self.image_normal_auto_spin_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\auto spin off.png")
        self.image_pressed_auto_spin_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\auto spin active.png")

        self.auto_spin_button = tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#a79c85", command=self.auto_spin_on)
        self.auto_spin_button.config(image=self.image_normal_auto_spin_button, relief="sunken", background="#a79c85")
        self.auto_spin_button.place(x=200, y=670)

        self.auto_spin_button.bind("<Leave>", self.on_auto_spin_button_leave)
        self.auto_spin_button.bind("<Button-1>", self.on_auto_spin_button_enter)


        self.image_normal_spin_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\spin off.png")
        self.image_pressed_spin_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\spin active.png")

        self.spin_button = tk.Button(self, text="Невидимая кнопка", command=self.start_spinning, bd=0, highlightthickness=0,  activebackground="#a79c85")
        self.spin_button.config(image=self.image_normal_spin_button, relief="sunken", background="#a79c85")
        self.spin_button.place(x=300, y=670)

        # Привязка функций к событиям мыши
        self.spin_button.bind("<Leave>", self.on_spin_button_leave)
        self.spin_button.bind("<Button-1>", self.on_spin_button_enter)

    def auto_spin_on(self):
        self.help_button.config(command=self.auto_spin_off)
        self.stop_event.clear()
        self.image_normal_auto_spin_on_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\auto spin on.png")
        self.image_pressed_auto_spin_on_button = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\auto spin active on.png")
        self.auto_spin_button.bind("<Leave>", self.on_auto_spin_on_button_leave)
        self.auto_spin_button.bind("<Button-1>", self.on_auto_spin_on_button_enter)
        self.auto_spin_button.config(image=self.image_normal_auto_spin_on_button, command=self.auto_spin_off)
        self.auto_spin_thread = threading.Thread(target=self.auto_spin_run)
        self.auto_spin_thread.start()

    def auto_spin_run(self):
        while not self.stop_event.is_set():
            self.start_spinning()
            time.sleep(3)
        print("STOP")

    def auto_spin_off(self):
        self.help_button.config(command=self.help_btn_on)
        self.stop_event.set()
        self.auto_spin_button.bind("<Leave>", self.on_auto_spin_button_leave)
        self.auto_spin_button.bind("<Button-1>", self.on_auto_spin_button_enter)
        self.auto_spin_button.config(image=self.image_normal_auto_spin_button, command=self.auto_spin_on)

    def on_auto_spin_on_button_enter(self, event):
        self.auto_spin_button.config(image=self.image_pressed_auto_spin_on_button)

    def on_auto_spin_on_button_leave(self, event):
        self.auto_spin_button.config(image=self.image_normal_auto_spin_on_button)

    def help_btn_on(self):
        self.spin_button.config(command=self.exit_help)
        columns = [self.rightmost_slot_labels, self.right_slot_labels, self.middle_slot_labels, self.left_slot_labels, self.leftmost_slot_labels]
        for colum in columns:
            for i, label in enumerate(colum):
                label.destroy()

        self.image_help = 0

        self.image_2 = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\help btn right.png")
        self.help_btn_right= tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#020177", command=self.help_right)
        self.help_btn_right.config(image=self.image_2, relief="sunken", background="#020177")
        self.help_btn_right.place(x=703, y=511)

        self.image_1 = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\help btn exit.png")
        self.help_btn_exit= tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#020177", command=self.exit_help)
        self.help_btn_exit.config(image=self.image_1, relief="sunken", background="#020177")
        self.help_btn_exit.place(x=480, y=511)

        self.image = ImageTk.PhotoImage(file="C:\\Users\\griba\\Cursach\\image\\button slot machine\\help btn left.png")
        self.help_btn_left = tk.Button(self, text="Невидимая кнопка", bd=0, highlightthickness=0,  activebackground="#020177", command=self.help_left)
        self.help_btn_left.config(image=self.image, relief="sunken", background="#020177")
        self.help_btn_left.place(x=227, y=511)

        background_image = Image.open(f"C:\\Users\\griba\\Cursach\\image\\background\\help slot machine\\bg_slot_help_1.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label.configure(image=background_photo)
        self.background_label.image = background_photo

    def exit_help(self):
        self.spin_button.config(command=self.start_spinning)
        self.help_btn_right.destroy()
        self.help_btn_exit.destroy()
        self.help_btn_left.destroy()

        background_image = Image.open(f"C:\\Users\\griba\\Cursach\\image\\background\\bg_slot.png")
        background_photo = ImageTk.PhotoImage(background_image)
        self.background_label.configure(image=background_photo)
        self.background_label.image = background_photo

        self.spin_button.place()

        self.create_column_spin_area()

    def help_right(self):
        if self.image_help + 1 == 8:
            self.image_help = 1
        else:
            self.image_help = self.image_help + 1
        self.background_label.configure(image=self.images_bg_help[self.image_help])
        self.background_label.image = self.images_bg_help[self.image_help]

    def help_left(self):
        if self.image_help - 1 == -1:
            self.image_help = 7
        else:
            self.image_help = self.image_help - 1
        self.background_label.configure(image=self.images_bg_help[self.image_help])
        self.background_label.image = self.images_bg_help[self.image_help]

    def on_help_button_enter(self, event):
        self.help_button.config(image=self.image_pressed_help_button)

    def on_help_button_leave(self, event):
        self.help_button.config(image=self.image_normal_help_button)

    def on_bet_button_enter(self, event):
        self.bet_button.config(image=self.image_pressed_bet_button)

    def on_bet_button_leave(self, event):
        self.bet_button.config(image=self.image_normal_bet_button)

    def on_auto_spin_button_enter(self, event):
        self.auto_spin_button.config(image=self.image_pressed_auto_spin_button)

    def on_auto_spin_button_leave(self, event):
        self.auto_spin_button.config(image=self.image_normal_auto_spin_button)

    def on_spin_button_enter(self, event):
        self.spin_button.config(image=self.image_pressed_spin_button)

    def on_spin_button_leave(self, event):
        self.spin_button.config(image=self.image_normal_spin_button)

    def start_spinning(self):
        shuffle(self.images)
        threading.Thread(target=self.animate_spin).start()
        threading.Thread(target=self.right_animate_spin).start()
        threading.Thread(target=self.middle_animate_spin).start()
        threading.Thread(target=self.left_animate_spin).start()
        threading.Thread(target=self.leftmost_animate_spin).start()
        self.animate_spin()


    def animate_spin(self, spins=0):
        image = self.images
        shuffle(image)
        if spins < 20:
            self.rightmost_rotate_images()
            self.after(30, lambda: self.animate_spin(spins + 1))

    def right_animate_spin(self, spins_right=0):
        image = self.images
        shuffle(image)
        if spins_right < 30:
            self.right_rotate_images()
            self.after(30, lambda: self.right_animate_spin(spins_right + 1))

    def middle_animate_spin(self, spins_right=0):
        image = self.images
        shuffle(image)
        if spins_right < 40:
            self.middle_rotate_images()
            self.after(30, lambda: self.middle_animate_spin(spins_right + 1))

    def left_animate_spin(self, spins_right=0):
        image = self.images
        shuffle(image)
        if spins_right < 50:
            self.left_rotate_images()
            self.after(30, lambda: self.left_animate_spin(spins_right + 1))

    def leftmost_animate_spin(self, spins_right=0):
        image = self.images
        shuffle(image)
        if spins_right < 60:
            self.leftmost_rotate_images()
            self.after(30, lambda: self.leftmost_animate_spin(spins_right + 1))

    def rightmost_rotate_images(self):
        last_image = self.images[-1]
        self.images = [last_image] + self.images[:-1]

        for i, label in enumerate(self.rightmost_slot_labels):
            label.config(image=self.images[i])
            label.image = self.images[i]

    def right_rotate_images(self):
        last_image = self.images[-1]
        self.images = [last_image] + self.images[:-1]

        for i, label in enumerate(self.right_slot_labels):
            label.config(image=self.images[i])
            label.image = self.images[i]

    def middle_rotate_images(self):
        last_image = self.images[-1]
        self.images = [last_image] + self.images[:-1]

        for i, label in enumerate(self.middle_slot_labels):
            label.config(image=self.images[i])
            label.image = self.images[i]

    def left_rotate_images(self):
        last_image = self.images[-1]
        self.images = [last_image] + self.images[:-1]

        for i, label in enumerate(self.left_slot_labels):
            label.config(image=self.images[i])
            label.image = self.images[i]

    def leftmost_rotate_images(self):
        last_image = self.images[-1]
        self.images = [last_image] + self.images[:-1]

        for i, label in enumerate(self.leftmost_slot_labels):
            label.config(image=self.images[i])
            label.image = self.images[i]



if __name__ == "__main__":
    app = CustomWindow()
    app.mainloop()
