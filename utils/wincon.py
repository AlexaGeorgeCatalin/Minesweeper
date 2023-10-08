# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import *
from tkinter import ttk
from utils import retry

def win_condition(
    mine_count,
    win,
    game_frame,
    top_frame,
    game_width,
    game_height,
    bomb_count,
    restart_button,
    second_count,
):
    """Verifică dacă utilizatorul a câștigat jocul și îl anunță când acest lucru se întâmplă"""
    game_won = True
    for i in range(len(mine_count)):
        for j in range(len(mine_count[0])):
            if mine_count[i][j] != -1:
                game_won = False
                continue
    if game_won:
        win.withdraw()
        won = Toplevel()
        won.title("Ai câștigat!")
        won.resizable(False, False)
        won.geometry("250x150")
        won.configure(bg="#a1adb0")
        message = "Felicitări! Ai evitat toate minele și ai câștigat!"
        Label(won, text=message, bg="#a1adb0").pack()
        ttk.Button(won, text="Închide jocul", command=win.destroy).place(
            x=10, y=115
        )
        ttk.Button(
            won,
            text="Joacă din nou",
            command=lambda: retry.try_again(
                win,
                won,
                game_frame,
                top_frame,
                game_width,
                game_height,
                bomb_count,
                restart_button,
                second_count,
            ),
        ).place(x=142, y=115)