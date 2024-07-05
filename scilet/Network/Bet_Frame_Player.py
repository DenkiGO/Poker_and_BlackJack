import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class Main_Frame_Bet(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Texas holdem")
        self.resizable(False, False)
        self.overrideredirect(True)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")
        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])

        self.background_image = Image.open("/image/background/main_frame_player_2.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.check_and_call_btn = ttk.Button(self, text="Check")
        self.check_and_call_btn.place(x=14, y=52, height=29, width=136)
        self.rise_btn = ttk.Button(self, text="Rise")
        self.rise_btn.place(x=14, y=96, height=29, width=136)
        self.fold_btn = ttk.Button(self, text="Fold")
        self.fold_btn.place(x=14, y=140, height=29, width=136)

        self.style.configure("Custom.TButton", font=custom_font)
        self.check_and_call_btn.configure(style="Custom.TButton")
        self.rise_btn.configure(style="Custom.TButton")
        self.fold_btn.configure(style="Custom.TButton")

        self.configure_window()



    def configure_window(self):
        self.make_draggable()
        self.center_window()

    def make_draggable(self):
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self._drag_data = {'x': event.x_root - self.winfo_rootx(),
                           'y': event.y_root - self.winfo_rooty()}

    def do_move(self, event):
        new_x = event.x_root - self._drag_data['x']
        new_y = event.y_root - self._drag_data['y']
        self.geometry(f"+{new_x}+{new_y}")

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 164  # Ширина вашего окна
        window_height = 184  # Высота вашего окна

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    app = Main_Frame_Bet()
    app.mainloop()
