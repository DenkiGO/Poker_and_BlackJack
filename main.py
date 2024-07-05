import tkinter as tk
from tkinter import font
from interface import Start_Menu, New_Game, New_Game_Frame, Network_Game_Client, Network_Game_Server, Server_Configuration_Frame, Client_Configuration_Frame, BlackJack, Menu_Game_Mods, Game


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        with open('save.txt', 'a') as file:
            pass

        self.title("Texas holdem")
        self.geometry("1100x800")
        self.resizable(False, False)

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        menubar = tk.Menu(self, font="Helvetica")

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Start menu", command=lambda: self.show_frame("Menu"))
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=lambda: self.exit())
        menubar.add_cascade(label="Menu", menu=settings_menu)

        # menubar.add_cascade(label="Menu", command=lambda: self.show_frame("Game_Mods"))

        games_menu = tk.Menu(menubar, tearoff=0)
        games_menu.add_command(label="Texas holdem", command=lambda: self.show_frame("Game"))
        games_menu.add_command(label="Blackjack", command=lambda: self.show_frame("BlackJack"))
        menubar.add_cascade(label="Games", menu=games_menu)

        network_game_menu = tk.Menu(menubar, tearoff=0)
        network_game_menu.add_command(label="Create a game", command=lambda: self.show_frame("Server_Config"))
        network_game_menu.add_command(label="Join the game", command=lambda: self.show_frame("Client_Settings"))
        menubar.add_cascade(label="Network", menu=network_game_menu)

        self.config(menu=menubar)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Start_Menu.Menu, New_Game.New_game, New_Game_Frame.New_game_frame, Game.Game, Server_Configuration_Frame.Server_Config, Client_Configuration_Frame.Client_Settings, Network_Game_Server.PokerServer, Network_Game_Client.PokerClient, BlackJack.BlackJack, Menu_Game_Mods.Game_Mods):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
