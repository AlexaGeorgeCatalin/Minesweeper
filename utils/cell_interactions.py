# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.

from tkinter import *
import random
from windows import lose_window
from utils import wincon

def clicked_mine(
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
):
    """Deschide fereastra ce anunță utilizatorul că a apăsat pe o mină și că a pierdut, acesta putând să închidă
    jocul sau să încerce din nou"""
    if not is_flagged[row][column]:
        message = "Ai apăsat pe o mină și ai pierdut!"
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


def clicked_safe_cell(
    row,
    column,
    mine_count,
    button,
    is_flagged,
    win,
    game_frame,
    top_frame,
    game_width,
    game_height,
    bomb_count,
    restart_button,
    second_count,
):
    """Afișează numărul de bombe din vecinătate și blochează butonul apăsat"""
    if not is_flagged[row][column]:
        button.configure(text=mine_count[row][column])
        mine_count[row][column] = -1
        button["state"] = DISABLED
    wincon.win_condition(
        mine_count,
        win,
        game_frame,
        top_frame,
        game_width,
        game_height,
        bomb_count,
        restart_button,
        second_count,
    )


def create_mines(cols, rows, bomb_count):
    """Amplasează minele la întâmplare pe tabla de joc și returnează o listă boolean a acestora"""
    is_mine = []
    for i in range(rows):
        is_mine.append([])
        for j in range(cols):
            is_mine[i].append(False)
    while bomb_count != 0:
        rand_col = random.randint(0, cols - 1)
        rand_row = random.randint(0, rows - 1)
        while is_mine[rand_row][rand_col]:
            rand_col = random.randint(0, cols - 1)
            rand_row = random.randint(0, rows - 1)
        is_mine[rand_row][rand_col] = True
        bomb_count -= 1
    return is_mine


def show_neighbours(cols, rows, mine_cells):
    """Determină câte mine sunt în vecinătatea unei celule"""
    neighbour_mines = []
    for i in range(rows):
        neighbour_mines.append([])
        for j in range(cols):
            neighbour_mines[i].append(0)
    for i in range(rows):
        for j in range(cols):
            if mine_cells[i][j]:
                neighbour_mines[i][j] = -1
            else:
                mine_count = 0
                if i != 0 and j != 0:
                    if mine_cells[i - 1][j - 1]:
                        mine_count += 1
                if i != 0:
                    if mine_cells[i - 1][j]:
                        mine_count += 1
                if i != 0 and j != cols - 1:
                    if mine_cells[i - 1][j + 1]:
                        mine_count += 1
                if j != 0:
                    if mine_cells[i][j - 1]:
                        mine_count += 1
                if j != cols - 1:
                    if mine_cells[i][j + 1]:
                        mine_count += 1
                if i != rows - 1 and j != 0:
                    if mine_cells[i + 1][j - 1]:
                        mine_count += 1
                if i != rows - 1:
                    if mine_cells[i + 1][j]:
                        mine_count += 1
                if i != rows - 1 and j != cols - 1:
                    if mine_cells[i + 1][j + 1]:
                        mine_count += 1
                neighbour_mines[i][j] = mine_count

    return neighbour_mines


def flag_cell(row, column, button, is_flagged):
    """Pune un steag pe celulă, dezactivând abilitatea de a face click stanga pe aceasta"""
    if button[row][column].cget("text") == "" and not is_flagged[row][column]:
        button[row][column].configure(text="steag")
        is_flagged[row][column] = True


def remove_flag_cell(row, column, button, is_flagged):
    """Scoate semnul întrebării de pe o celulă"""
    if button[row][column].cget("text") == "???":
        button[row][column].configure(text="")
        is_flagged[row][column] = False


def flagger(row, column, drawn_cells, is_flagged):
    """Decide dacă pe celulă trebuie pus un steag/semn al întrebării sau dacă trebuie scos un semn al întrebării"""
    if is_flagged[row][column]:
        if drawn_cells[row][column].cget("text") == "steag":
            drawn_cells[row][column].configure(text="???")
        else:
            remove_flag_cell(row, column, drawn_cells, is_flagged)
    else:
        flag_cell(row, column, drawn_cells, is_flagged)