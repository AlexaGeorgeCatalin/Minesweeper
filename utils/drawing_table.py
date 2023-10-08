# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import ttk
from utils import cell_interactions

def draw_table(
    cols,
    rows,
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
):
    """Amplasează butoanele pe tablă în funcție de dimensiunile alese și returnează o listă cu acestea"""
    table_buttons = [[] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if mine_cells[i][j]:
                table_buttons[i].append(
                    ttk.Button(
                        game_frame,
                        text="",
                        command=lambda row=i, column=j: cell_interactions.clicked_mine(
                            row,
                            column,
                            win,
                            is_flagged,
                            game_frame,
                            top_frame,
                            game_width,
                            game_height,
                            bomb_count,
                            restart_button,
                            second_count,
                        ),
                    )
                )
                table_buttons[i][j].grid(row=i, column=j)
            else:

                table_buttons[i].append(
                    ttk.Button(
                        game_frame,
                        text="",
                        command=lambda row=i, column=j: cell_interactions.clicked_safe_cell(
                            row,
                            column,
                            neighbour_mines,
                            table_buttons[row][column],
                            is_flagged,
                            win,
                            game_frame,
                            top_frame,
                            game_width,
                            game_height,
                            bomb_count,
                            restart_button,
                            second_count,
                        ),
                    )
                )
                table_buttons[i][j].grid(row=i, column=j)

    return table_buttons