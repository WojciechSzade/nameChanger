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


# main

mode = 0

print("Welcome to the nameChanger app.\n")


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


while (True):
    if mode_select():
        break
# print(mode)
if mode == 1:  # mode 1 - renaming files beginning
    path = input("Enter the path to the folder with the files you want names to to be changed.\n"
                 "The selected path will be opened.\n")
    os.startfile(path)
    base = input("Enter the base name (rest of the files will be named basename+number.extension.\n"
                 "For example for base name file, files will be named:\n"
                 "file1.txt, file2.txt, file3.txt, etc.\n")
    cont = "0"
    while cont != "Y" or cont != "y":
        print("Are you sure you want to continue? All the files in the ", path, " directory will be renamed. Y/N")
        cont = input()
        if cont == "N" or cont == "n":
            quit()
        elif cont == "Y" or cont == "y":
            break
        else:
            print("Wrong input.")
    for i, file in enumerate(sorted(os.scandir(path), key=lambda t: t.stat().st_mtime)):
        if file.is_file():
            ext = get_extension(file.name)
            os.rename(create_path(path, file.name), create_path(path, base + str(i) + ext))
    print("File names in ", path, " changed.\n")
    # mode 1 end
if mode == 2:   # mode 2 - extension changing beggining
    print("mode 2 selected\n")
    # mode 2 end
