# Copyright (c) 2023 Alexa George-Catalin. All rights reserved.
from tkinter import *
from tkinter import ttk

def open_instructions(root):
    """Funcție ce deschide fereastra cu instrucțiuni ale jocului"""
    instruc_window = Toplevel(root)

    instruc_window.title("Instrucțiuni")
    instruc_window.geometry("400x270")
    instruc_window.configure(bg="#a1adb0")
    instruc_window.resizable(False, False)

    instruc = Label(
        instruc_window,
        bg="#a1adb0",
        fg="black",
        wraplength=300,
        justify="center",
        text="Regulile jocului sunt foarte simple. Tabla este împărțită în celule, cu mine distribuite la întâmplare. "
        "Pentru a câștiga, trebuie să deschizi toate celulele folosind click stânga fără să dai peste o mină. "
        "Cifra dintr-o celulă deschisă reprezintă numărul de mine care sunt in vecinătatea sa, astfel determinând "
        "dacă o celulă este sigură sau nu. Celulele suspicioase pot fi marcate apăsând click dreapta pe acestea",
        font=("", 13),
    )
    instruc.pack()

    instruc_window.update()
    exit_instruc = ttk.Button(
        instruc_window, text="Ieșire", command=instruc_window.destroy
    )
    exit_instruc.pack()
    instruc_window.update()