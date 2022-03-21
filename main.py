"""import tkinter as tk
window = tk.Tk()
lbl_greeting = tk.Label(
    text="Welcome to nameChanger \n What is your name?",
    fg="white",
    bg="darkblue",
    width=40,
    height=20
)
lbl_greeting.pack()
window.mainloop()
"""
import os


def create_path(*args):
    return '\\'.join(args)


def get_extension(name):
    return name[name.rfind('.'):]


def get_filename(name):
    return name[:name.rfind('.')]


global_mode = 0


def select_mode_low(text, mode):
    global global_mode
    global_mode = mode
    if global_mode == 1 or global_mode == 2:
        return global_mode
    global_mode = input(text)
    global_mode = int(global_mode)
    if global_mode == 1 or global_mode == 2:
        return global_mode
    else:
        return 0


def select_mode(text, mode):
    global global_mode
    while True:
        if select_mode_low(text, mode):
            return global_mode

        # main


print("Welcome to the nameChanger app.\n")
default_mode = 0

# def default_select():
#     global default_mode
#     default_mode = input("Would you like to use the default settings from the config.ini file or"
#                          " make every choice by yourself?\n"
#                          "Type 1 for default or 2 for personal settings\n")
#     default_mode = int(default_mode)
#     if default_mode == 1 or default_mode == 2:
#         return True
#     else:
#         return False

#
# while True:
#     if default_select():
#         break
text_default = "Would you like to use the default settings from the config.ini file or make every choice by " \
               "yourself?\nType 1 for default or 2 for personal settings\n "
default_mode = select_mode(text_default, default_mode)
print(default_mode)

main_mode = 0
numbering_mode = 0
if default_mode == 1:
    config = open("config.ini", "r")
    temp = config.readline()
    display_settings = int(temp[-2])
    temp = config.readline()
    main_mode = int(temp[-2])
    temp = config.readline()
    numbering_mode = int(temp[-2])
    config.close()
    print("Default settings loaded.\n")
    if display_settings == 1:
        if main_mode == 1:
            print("Selected mode: Name Changer\n")
        elif main_mode == 2:
            print("Selected mode: Extension Changer\n")
        elif main_mode == 0:
            print("Mode not selected.\n")
        if numbering_mode == 1:
            print("Selected numbering mode: Just numbers\n")
        elif numbering_mode == 2:
            print("Selected numbering mode: Numbers in brackets\n")
        elif numbering_mode == 0:
            print("Numbering mode not selected\n")

# print("main_mode =", main_mode, "numbering_mode =", numbering_mode) debug


# def main_mode_select():
#     global main_mode
#     if main_mode == 1 or main_mode == 2:
#         return True
#     main_mode = input("There are two available modes at this moment:\n"
#                       "1. Changing name of every file in a chosen folder to predefined name + number,\n"
#                       "2. Changing extension of every file in a chosen folder.\n"
#                       "Please enter 1 or 2 to select mode.\n")
#     main_mode = int(main_mode)
#     if main_mode == 1 or main_mode == 2:
#         return True
#     else:
#         return False
#
#
# while True:
#     if main_mode_select():
#         break
# print(main_mode)
text_main = "There are two available modes at this moment:\n1. Changing name of every file in a chosen folder to " \
            "predefined name + number,\n2. Changing extension of every file in a chosen folder.\nPlease enter 1 or 2 " \
            "to select mode.\n "
main_mode = select_mode(text_main, main_mode)

if main_mode == 1:  # main_mode 1 - renaming files beginning
    path = input("Enter the path to the folder with the files you want names to to be changed.\n"
                 "The selected path will be opened.\n")
    os.startfile(path)
    text_numbering = "You can use two syntheses:\n" \
                     "1. basename+number.extension, example: file1.txt, file2.txt\n" \
                     "2. basename+(number).extension, example: file(1).txt, file(2).txt\n" \
                     "Please enter 1 or 2 to select mode.\n"
    numbering_mode = select_mode(text_numbering, numbering_mode)
    base = input("Enter the base name (rest of the files will be named basename+number.extension.\n")
    cont = "0"
    while cont != "Y" or cont != "y":
        print("Are you sure you want to continue? All the files in the", path, "directory will be renamed. Y/N")
        cont = input()
        if cont == "N" or cont == "n":
            quit()
        elif cont == "Y" or cont == "y":
            break
        else:
            print("Wrong input.")
    if numbering_mode == 1:
        for i, file in enumerate(sorted(os.scandir(path), key=lambda t: t.stat().st_mtime)):
            if file.is_file():
                ext = get_extension(file.name)
                os.rename(create_path(path, file.name), create_path(path, base + str(i) + ext))
    elif numbering_mode == 2:
        for i, file in enumerate(sorted(os.scandir(path), key=lambda t: t.stat().st_mtime)):
            if file.is_file():
                ext = get_extension(file.name)
                os.rename(create_path(path, file.name), create_path(path, base + '(' + str(i) + ')' + ext))
    print("File names in", path, "changed.\n")

    # main_mode 1 end
if main_mode == 2:  # main_mode 2 - extension changing beggining
    path = input("Enter the path to the folder with the files you want extensions to to be changed.\n"
                 "The selected path will be opened.\n")
    os.startfile(path)
    ext = input("Enter the extension you want all the files in the selected path to have.\n"
                "Skip the dot. ('jpg' for example)\n")
    cont = "0"
    while cont != "Y" or cont != "y":
        print("Are you sure you want to continue? All the extensions of files in the", path,
              "directory will be renamed. Y/N")
        cont = input()
        if cont == "N" or cont == "n":
            quit()
        elif cont == "Y" or cont == "y":
            break
        else:
            print("Wrong input.")
    for i, file in enumerate(sorted(os.scandir(path), key=lambda t: t.stat().st_mtime)):
        if file.is_file():
            filename = get_filename(file.name)
            os.rename(create_path(path, file.name), create_path(path, filename + '.' + ext))
    print("File extensions in", path, "changed.")
    # main_mode 2 end
