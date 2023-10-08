# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
import time
from windows import lose_window


def timer(
        temp,
        second,
        win,
        game_frame,
        top_frame,
        game_width,
        game_height,
        bomb_count,
        restart_button,
        second_count,
):
    """Funcția face astfel încât cronometrul să meargă simultan cu jocul"""
    while temp > -1:
        second.set(temp)
        win.update()
        time.sleep(1)
        if temp == 0:
            message = "Ai rămas fără timp! "
            lose_window.lost_window(
                win,
                message,
                game_frame,
                top_frame,
                game_width,
                game_height,
                bomb_count,
                restart_button,
                second_count,
            )
        temp -= 1
