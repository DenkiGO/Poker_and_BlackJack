import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk


class Main_Frame_Bet(tk.Toplevel):
    def __init__(self, parent, shared_data, callback, call=0, blind=0):
        tk.Toplevel.__init__(self, parent)

        self.shared_data = shared_data
        self.callback = callback
        self.call_st = call
        self.blind = blind

        self.title("Texas holdem")
        self.resizable(False, False)
        self.overrideredirect(True)

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")
        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])

        self.background_image = Image.open("C:\\Users\\griba\\Cursach\\image\\background\\main_frame_player_2.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.check_and_call_btn = ttk.Button(self, text="Check")
        self.check_and_call_btn.place(x=14, y=52, height=29, width=136)
        self.rise_btn = ttk.Button(self, text=f"Rise {self.blind+self.call_st}$", command=self.rise)
        self.rise_btn.place(x=14, y=96, height=29, width=136)
        self.fold_btn = ttk.Button(self, text="Fold", command=self.fold)
        self.fold_btn.place(x=14, y=140, height=29, width=136)

        self.style.configure("Custom.TButton", font=custom_font)
        self.check_and_call_btn.configure(style="Custom.TButton")
        self.rise_btn.configure(style="Custom.TButton")
        self.fold_btn.configure(style="Custom.TButton")

        self.check_and_call()

        self.configure_window()

        self.lift()

    def check_and_call(self):
        if self.call_st == 0:
            self.check_and_call_btn.configure(text="Check", command=self.check)
        else:
            self.check_and_call_btn.configure(text=f"Call {self.call_st}$", command=self.call)

    def rise(self):
        data = "rise"
        self.shared_data.set(data)
        self.callback(data)
        self.destroy()

    def call(self):
        data = "call"
        self.shared_data.set(data)
        self.callback(data)
        self.destroy()

    def check(self):
        data = "check"
        self.shared_data.set(data)
        self.callback(data)
        self.destroy()

    def fold(self):
        data = "fold"
        self.shared_data.set(data)
        self.callback(data)
        self.destroy()


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

        window_width = 164
        window_height = 184

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main_Frame_Bet(root, shared_data=None, callback=None, call=0, blind=0)
    app.mainloop()
