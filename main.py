'''import tkinter as tk
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
'''
import os

def create_path(*args):
    return '\\'.join(args)

def get_extension(name):
    return name[name.rfind('.'):]
path = input("Welcome to the nameChanger app.\nEnter the path to the folder with the files you want names to to be changed.\nThe selected path will be opened.\n")
os.startfile(path)
base = input("Enter the base name (rest of the files will be named basename+number.extension.\nFor example for base name file, files will be named:\nfile1.txt, file2.txt, file3.txt, etc.\n")
cont = "0"
while cont != "Y" or cont != "y":
    print("Are you sure you want to continue? All the files in the ", path, " directory will be renamed. Y/N")
    cont = input()
    if cont == "N" or cont == "n": quit()
    elif cont == "Y" or cont == "y": break
    else: print("Wrong input.")
for i, file in enumerate(sorted(os.scandir(path), key = lambda t: t.stat().st_mtime)):
    if file.is_file():
        ext = get_extension(file.name)
        os.rename(create_path(path, file.name), create_path(path, base + str(i) + ext))
print("File names in ", path, " changed.\n")