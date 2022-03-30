import os
from selecting import *
from reading import *
import text
from renaming import *


class Mods:
    def __init__(self, default, display, main, numbering, zero, sort):
        self.default = default
        self.display = display
        self.main = main
        self.numbering = numbering
        self.zero = zero
        self.sort = sort


mode = Mods(0, 0, 0, 0, 0, 0)
# main

print("Welcome to the nameChanger app.\n")
mode.default = select_mode(text.t_default, mode.default)
if mode.default == 1:  # reading info from config.ini
    mode.numbering = select_mode(text.t_numbering, mode.numbering)
    mode.zero = select_mode(text.t_zero, mode.zero) + 1
    mode.sort = select_mode_sort(text.t_sort, mode.sort, 8)
    readConfig(mode)
    print("Default settings loaded.\n")
    printConfig(mode)
mode.main = select_mode(text.t_main, mode.main)
if mode.main == 1:  # mode.main 1 - renaming files beginning
    rename(mode)
    # mode.main 1 end
if mode.main == 2:  # mode.main 2 - extension changing beggining
    changingExtensions(mode)
    # mode.main 2 end
