# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import *
from tkinter import ttk
from utils import start_function
from windows import instructions_window


def start_window():
    """Deschide fereastra ce apare la pornirea aplicației"""
    size_options = list(range(5, 10))
    bomb_options = list(range(5, 50))
    time_options = list(range(60, 301))

    root = Tk()

    table_width = 405
    table_height = 320

    root.geometry(f"{table_width}x{table_height}")
    root.title("Minesweeper")

    root.configure(bg="#a1adb0")
    root.resizable(False, False)

    main_frame = Frame(
        root, bg="#a1adb0", width=table_width, height=table_height
    )
    main_frame.place(x=0, y=0)

    size_label = Label(
        main_frame,
        bg="#a1adb0",
        fg="black",
        text="Dimensiunile tablei de joc: ",
        font=("", 15),
    )
    size_label.place(x=20, y=10)

    row_num = StringVar()
    row_num.set("5")
    col_num = StringVar()
    col_num.set("5")

    root.update()
    set_row = OptionMenu(main_frame, row_num, *size_options)
    set_row.place(x=20 + size_label.winfo_width(), y=10)

    root.update()
    x_label = Label(
        main_frame, bg="#a1adb0", fg="black", text="x", font=("", 15)
    )
    x_label.place(
        x=25 + set_row.winfo_width() + size_label.winfo_width(), y=10
    )

    root.update()
    set_col = OptionMenu(main_frame, col_num, *size_options)
    set_col.place(
        x=30
        + set_row.winfo_width()
        + size_label.winfo_width()
        + x_label.winfo_width(),
        y=10,
    )
    root.update()

    root.update()
    bomb_label = Label(
        main_frame,
        bg="#a1adb0",
        fg="black",
        text="Numărul de bombe:",
        font=("", 15),
    )
    bomb_label.place(
        x=20, y=20 + size_label.winfo_height() + set_col.winfo_height()
    )

    root.update()
    bomb_label2 = Label(
        main_frame,
        bg="#a1adb0",
        fg="black",
        text="Între 5 și 49 inclusiv",
        font=("", 10),
    )
    bomb_label2.place(
        x=20,
        y=20
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height(),
    )

    root.update()
    set_bomb = Spinbox(main_frame, values=bomb_options, width=10)
    set_bomb.place(
        x=20 + bomb_label.winfo_width(),
        y=26 + size_label.winfo_height() + set_col.winfo_height(),
    )

    root.update()
    time_label = Label(
        main_frame,
        bg="#a1adb0",
        fg="black",
        text="Setează timpul în secunde:",
        font=("", 15),
    )
    time_label.place(
        x=20,
        y=20
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height(),
    )

    root.update()
    time_label2 = Label(
        main_frame,
        bg="#a1adb0",
        fg="black",
        text="Între 60 și 300 de secunde ",
        font=("", 10),
    )
    time_label2.place(
        x=20,
        y=20
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height()
        + time_label.winfo_height(),
    )

    root.update()
    set_time = Spinbox(main_frame, values=time_options, width=10)
    set_time.place(
        x=20 + time_label.winfo_width(),
        y=26
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height(),
    )

    root.update()
    start = ttk.Button(
        root,
        text="Start",
        command=lambda: start_function.open_win(
            int(set_bomb.get()),
            int(col_num.get()),
            int(row_num.get()),
            root,
            int(set_time.get()),
        ),
    )
    start.place(
        x=table_width / 2 - 76 / 2,
        y=40
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height()
        + time_label.winfo_height()
        + time_label2.winfo_height(),
    )

    root.update()
    instructions = ttk.Button(
        root, text="Instrucțiuni", command=lambda: instructions_window.open_instructions(root)
    )
    instructions.place(
        x=table_width / 2 - 76 / 2,
        y=50
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height()
        + start.winfo_height()
        + time_label.winfo_height()
        + time_label2.winfo_height(),
    )

    root.update()
    quit_game = ttk.Button(root, text="Ieșire", command=root.destroy)
    quit_game.place(
        x=table_width / 2 - 76 / 2,
        y=60
        + size_label.winfo_height()
        + set_col.winfo_height()
        + bomb_label.winfo_height()
        + bomb_label2.winfo_height()
        + start.winfo_height()
        + instructions.winfo_height()
        + time_label.winfo_height()
        + time_label2.winfo_height(),
    )

    root.mainloop()