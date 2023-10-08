# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
import threading
from tkinter import *
from tkinter import ttk
from utils import cell_interactions
from utils import restart_game
from utils import drawing_table
from utils import countdown
def initialize_game(
    game_width,
    game_height,
    bomb_count,
    top_frame,
    win,
    game_frame,
    second_count,
):
    """Setează datele jocului când este necesar (la prima inițializare a jocului sau la un restart al acestuia)"""
    game_width = int(game_width)
    game_height = int(game_height)
    mine_cells = cell_interactions.create_mines(game_width, game_height, bomb_count)
    neighbour_mines = cell_interactions.show_neighbours(game_width, game_height, mine_cells)
    is_flagged = []
    for i in range(game_height):
        is_flagged.append([])
        for j in range(game_width):
            is_flagged[i].append(False)

    restart_button = ttk.Button(
        top_frame,
        text="Restart",
        command=lambda: restart_game.restart(
            win,
            bomb_count,
            game_frame,
            top_frame,
            game_width,
            game_height,
            bomb_count,
            restart_button,
            second_count,
        ),
    )
    win.update()
    restart_button.place(relx=0.5, rely=0.5, anchor="center")

    drawn_cells = drawing_table.draw_table(
        int(game_width),
        int(game_height),
        game_frame,
        mine_cells,
        win,
        neighbour_mines,
        is_flagged,
        top_frame,
        game_width,
        game_height,
        bomb_count,
        restart_button,
        second_count,
    )
    for i in range(int(game_height)):
        for j in range(int(game_width)):
            drawn_cells[i][j].bind(
                "<Button-3>",
                lambda e, row=i, column=j: cell_interactions.flagger(
                    row,
                    column,
                    drawn_cells,
                    is_flagged,
                ),
            )

    second = StringVar()
    second.set(str(second_count))
    second_label = Label(
        top_frame,
        width=5,
        font=("Arial", 13, ""),
        textvariable=second,
        bg="#7c8d91",
        fg="red",
    )
    second_label.place(x=0, y=0)

    temp = int(second.get())
    th = threading.Thread(
        target=countdown.timer,
        args=[
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
        ],
    )
    th.start()






