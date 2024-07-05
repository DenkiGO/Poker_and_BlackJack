import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class Main_Frame_Bet(tk.Toplevel):
    def __init__(self, parent, shared_data, callback, total_balance):
        tk.Toplevel.__init__(self, parent)

        self.shared_data = shared_data
        self.callback = callback
        self.balance_player = total_balance

        self.title("Texas holdem")
        self.resizable(False, False)
        self.overrideredirect(True)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")
        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])

        self.background_image = Image.open("image\\frame\\main_frame_blackjack.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.header_frame = ttk.Frame(self, cursor="fleur", style="Transparent.TFrame")
        self.header_frame.place(x=57, y=7, height=27, width=224)

        self.style.configure("Transparent.TFrame", background="#00009e")

        self.bet_blackjack = ttk.Button(self, text="0 $", command=self.show_bet_value)
        self.bet_blackjack.place(x=12, y=111, height=29, width=262)

        self.style.configure("Custom.TButton", font=custom_font)
        self.bet_blackjack.configure(style="Custom.TButton")

        self.style.configure("TScale", troughcolor="#8c8c8c", sliderthickness=25, background="#acacac")
        self.style.map('TScale', background=[('active', '#acacac'), ('!active', '#acacac'), ('hover', '#acacac')])
        self.scale = ttk.Scale(
            self,
            from_=0,
            to=self.balance_player,
            orient=tk.HORIZONTAL,
            length=262,
            style="TScale",
            command=self.update_bet_value
        )
        self.scale.place(x=12, y=56)

        self.style.configure("Custom.TButton", font=custom_font)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 288
        window_height = 155

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.configure_window()

        self.lift()

    def configure_window(self):
        self.make_draggable()

    def make_draggable(self):
        self.header_frame.bind("<ButtonPress-1>", self.start_move)
        self.header_frame.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self._drag_data = {'x': event.x_root - self.winfo_rootx(),
                           'y': event.y_root - self.winfo_rooty()}

    def do_move(self, event):
        new_x = event.x_root - self._drag_data['x']
        new_y = event.y_root - self._drag_data['y']
        self.geometry(f"+{new_x}+{new_y}")

    def update_bet_value(self, value):
        self.bet_blackjack.configure(text=f"{float(value):.0f} $")

    def show_bet_value(self):
        self.shared_data.set(int(f"{float(self.scale.get()):.0f}"))
        self.callback(int(f"{float(self.scale.get()):.0f}"))
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main_Frame_Bet(root, total_balance=None)
    app.mainloop()
