import os
from reading import *
import text
from renaming import *
import tkinter as tk
from tkinter import filedialog


class Mods:
    def __init__(self, config, main, numbering, zero, sort, path):
        self.default = config
        self.main = main
        self.numbering = numbering
        self.zero = zero
        self.sort = sort
        self.path = path

    def select_modes(self):
        self.default = self.select_mode(0, text.t_default, 1, 2)
        if self.default == 1:  # reading info from config.ini
            readConfig(self)
            print("Default settings loaded.\n")
            printConfig(mode)
            print(
                "If some of the settings were 0 (not selected) or incorrect, you will be asked to select them now.")
        if self.main == 0:
            self.main = self.select_mode(0, text.t_main, 1, 2)
        if self.main == 1:
            if self.sort == 0:
                self.sort = self.select_mode(0, text.t_sort, 1, 8)
            if self.numbering == 0:
                self.numbering = self.select_mode(0, text.t_numbering, 1, 2)
            if self.zero == 0:
                self.zero = self.select_mode(0, text.t_zero, 1, 2)
        if self.default == 2:
            if (self.select_mode(0, text.t_save, 1, 2)) == 2 :
                saveConfig(mode)

    def select_mode(self, mode, text, choices_low, choices_up):
        mode = input(text)
        if mode.isdigit():
            mode = int(mode)
            if choices_low <= mode <= choices_up:
                return mode
        else:
            print("Invalid input. The value must a number between",
                  choices_low, "and", choices_up, ".\nTry again.")
            return self.select_mode(mode, text, choices_low, choices_up)

    def select_path(self):
        root = tk.Tk()
        root.withdraw()
        print("Select the directory you want to rename the files in.")
        self.path = filedialog.askdirectory()
        if self.path == "":
            print("No directory selected. Try Again.")
            self.select_path()
        print("Selected path is:", self.path)


mode = Mods(0, 0, 0, 0, 0, 0)
print("Welcome to the nameChanger app.\n")

mode.select_modes()
printConfig(mode)
mode.select_path()
if mode.main == 1:  # mode.main 1 - renaming files beginning
    rename(mode)
if mode.main == 2:  # mode.main 2 - extension changing beggining
    changingExtensions(mode)
