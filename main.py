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


# main


print("Welcome to the nameChanger app.\n")
default_mode = 0


def default_select():
    global default_mode
    default_mode = input("Would you like to use the default settings from the config.ini file or"
                         " make every choice by yourself?\n"
                         "Type 1 for default or 2 for personal settings\n")
    default_mode = int(default_mode)
    if default_mode == 1 or default_mode == 2:
        return True
    else:
        return False

while True:
    if default_select():
        break
mode = 0
numbering_mode = 0
if default_mode == 1:
    config = open("config.ini", "r")
    temp = config.readline()
    mode = int(temp[-2])
    temp = config.readline()
    numbering_mode = int(temp[-2])
config.close()
print("mode =", mode, "numbering_mode =", numbering_mode)

def mode_select():
    global mode
    mode = input("There are two available modes at this moment:\n"
                 "1. Changing name of every file in a chosen folder to predefined name + number,\n"
                 "2. Changing extension of every file in a chosen folder.\n"
                 "Please enter 1 or 2 to select mode.\n")
    mode = int(mode)
    if mode == 1 or mode == 2:
        return True
    else:
        return False


while True:
    if mode_select():
        break
# print(mode)
if mode == 1:  # mode 1 - renaming files beginning
    path = input("Enter the path to the folder with the files you want names to to be changed.\n"
                 "The selected path will be opened.\n")
    os.startfile(path)


    def numbering_select():
        global numbering_mode
        numbering_mode = input("You can use two syntheses:\n"
                               "1. basename+number.extension, example: file1.txt, file2.txt\n"
                               "2. basename+(number).extension, example: file(1).txt, file(2).txt\n"
                               "Please enter 1 or 2 to select mode.\n")
        numbering_mode = int(numbering_mode)
        if numbering_mode == 1 or numbering_mode == 2:
            return True
        else:
            return False


    while (True):
        if numbering_select():
            break
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

    # mode 1 end
if mode == 2:  # mode 2 - extension changing beggining
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
    # mode 2 end
