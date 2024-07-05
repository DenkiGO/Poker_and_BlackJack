import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, font


class Client_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.style = ttk.Style(self)
        self.style.theme_use('alt')

        self.background_image = Image.open("image\\background\\background.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        frame_image = Image.open("image\\frame\\Network_Settings_Frame_Client.png")
        frame_photo = ImageTk.PhotoImage(frame_image)
        frame_label = tk.Label(self, image=frame_photo, bd=0)
        frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        frame_label.image = frame_photo

        custom_font = font.Font(family="Classic Console Neue", size=14, weight="normal", slant="roman")

        self.style.map('TButton', background=[('!active', '#a9aaa7'), ('pressed', '#858283'), ('active', '#a9aaa7')])
        self.style.configure("Custom.TButton", font=custom_font)
        self.style.configure("TEntry",
                             background="green",
                             foreground="black",
                             fieldbackground="#a9aaa7")

        self.OK_network_settings = ttk.Button(self, text="OK", command=self.get_player_info)
        self.OK_network_settings.place(x=406, y=455, height=30, width=137)

        self.name_player = ttk.Entry(self, style="TEntry", font=custom_font, justify="center")
        self.name_player.insert(0, "Client")
        self.name_player.place(x=400, y=342, height=30, width=301)

        self.set_ipv4_server = ttk.Entry(self, style="TEntry", font=custom_font, justify="center")
        self.set_ipv4_server.insert(0, "IPv4")
        self.set_ipv4_server.place(x=400, y=408, height=30, width=301)

        self.cancel_network_settings = ttk.Button(self, text="Cancel", command=lambda: controller.show_frame("Menu"))
        self.cancel_network_settings.place(x=558, y=455, height=30, width=137)

        self.OK_network_settings.configure(style="Custom.TButton")
        self.cancel_network_settings.configure(style="Custom.TButton")


    def get_player_info(self):
        self.controller.frames["PokerClient"].update_player_info(self.name_player.get(), self.set_ipv4_server.get())
        self.controller.show_frame("PokerClient")
#
# if __name__ == "__main__":
#     app = Client_Settings()
#     app.mainloop()