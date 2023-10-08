# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import *
from tkinter import ttk
from utils import retry


def lost_window(
        win,
        message,
        game_frame,
        top_frame,
        game_width,
        game_height,
        bomb_count,
        restart_button,
        second_count,
):
    """Functie ce anunta utilizatorul modul in care a pierdut"""
    win.withdraw()
    lost = Toplevel()
    lost.title("Ai pierdut!")
    lost.resizable(False, False)
    lost.geometry("250x150")
    lost.configure(bg="#a1adb0")
    Label(lost, text=message, bg="#a1adb0").pack()
    ttk.Button(lost, text="Închide jocul", command=win.destroy).place(
        x=10, y=115
    )
    ttk.Button(
        lost,
        text="Încearcă din nou",
        command=lambda: retry.try_again(
            win,
            lost,
            game_frame,
            top_frame,
            game_width,
            game_height,
            bomb_count,
            restart_button,
            second_count,
        ),
    ).place(x=142, y=115)
