# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from utils import game_initialization

def try_again(
    win,
    lost,
    game_frame,
    top_frame,
    game_width,
    game_height,
    bomb_count,
    restart_button,
    second_count,
):
    """Permite utilizatorului să joace după ce a pierdut"""
    win.deiconify()
    try:
        lost.destroy()
    except AttributeError:
        pass
    for widget in top_frame.winfo_children():
        if widget != restart_button:
            widget.destroy()
    for widget in game_frame.winfo_children():
        widget.destroy()

    game_initialization.initialize_game(
        game_width,
        game_height,
        bomb_count,
        top_frame,
        win,
        game_frame,
        second_count,
    )