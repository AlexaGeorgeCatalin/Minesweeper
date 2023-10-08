# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from utils import retry

def restart(
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
    """Funcție ce permite resetarea jocului chiar dacă utilizatorul a pierdut sau nu"""
    win.withdraw()
    retry.try_again(
        win,
        lost,
        game_frame,
        top_frame,
        game_width,
        game_height,
        bomb_count,
        restart_button,
        second_count,
    )
