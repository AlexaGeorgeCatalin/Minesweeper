# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import *
import tkinter.messagebox
from utils import game_initialization

def open_win(bomb_count, game_width, game_height, root, second_count):
    """Funcție ce avertizează utilizatorul dacă a selectat prea multe bombe sau care, în caz contrar, inițializează
    jocul"""

    if bomb_count >= game_width * game_height:
        tkinter.messagebox.showinfo(
            "Avertisment!",
            "Prea multe bombe! Mărește dimensiunea tablei sau scade numarul de bombe!",
        )
    else:

        root.destroy()
        win = Tk()

        game_width *= 76
        game_height *= 25
        win.geometry(f"{game_width}x{50 + game_height}")
        win.title("Minesweeper")
        win.configure(bg="#a1adb0")
        win.resizable(False, False)
        top_frame = Frame(win, bg="#7c8d91", width=game_width, height=50)
        top_frame.place(x=0, y=0)
        game_frame = Frame(
            win, bg="#7c8d91", width=game_width, height=game_height
        )
        game_frame.place(x=0, y=50)

        game_initialization.initialize_game(
            game_width / 76,
            game_height / 25,
            bomb_count,
            top_frame,
            win,
            game_frame,
            second_count,
        )

        win.mainloop()
