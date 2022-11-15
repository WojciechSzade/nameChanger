import random
import string
import text
import os

def ask_if_sure(path):
    answ = input("Are you sure you want to continue? All the files in the " + str(path) + " directory will be renamed. Y/N\n")
    answ = answ.lower()
    if answ == "n":
        quit()
    elif answ == "y":
        return True
    else:
        print("Wrong input. Enter Y or N. Try again.")
        return ask_if_sure(path)

def create_path(*args):
    return '/'.join(args)

def create_name_argument(mode, i):
    if mode.numbering == 1:
         return str(i + mode.zero - 1)
    elif mode.numbering == 2:
        return '(' + str(i + mode.zero - 1) + ')'


def get_extension(name):
    return name[name.rfind('.'):]


def get_filename(name):
    return name[:name.rfind('.')]


def selectKey(mode):
    if mode.sort == 1 or mode.sort == 2:
        return lambda t: t.stat().st_mtime
    elif mode.sort == 5 or mode.sort == 6:
        return lambda t: t.stat().st_size
    elif mode.sort == 3 or mode.sort == 4:
        return lambda file: file.name
    elif mode.sort == 7 or  mode.sort == 8:
        return lambda file: get_extension(file.name)


def tempDirF(mode, tempdir, sort_key):
    for i, file in enumerate(sorted(os.scandir(tempdir), key=sort_key)):
        if file.is_file():
            ext = get_extension(file.name)
            os.rename(create_path(tempdir, file.name), create_path(mode.path, file.name))
    os.rmdir(tempdir)


def rename(mode):
    tempdir = ""
    base = input(text.t_basename)
    ask_if_sure(mode.path)
    sort_key = selectKey(mode)
    if mode.sort%2 == 0:
        rev = True
    else:
        rev = False
    for i, file in enumerate(sorted(os.scandir(mode.path), key=sort_key, reverse=rev)):
        if file.is_file():
            ext = get_extension(file.name)
            if tempdir == "":
                tempdir = create_path(mode.path, 'temp' + str(random.randint(0, 999)) + str(random.randint(0, 999))) #creating a random name, so the directory doesn't already exist
            if not os.path.exists(tempdir):
                os.mkdir(tempdir)
            os.rename(create_path(mode.path, file.name), create_path(tempdir, base + create_name_argument(mode, i) + ext))
    if tempdir != "":
        tempDirF(mode, tempdir, sort_key)
    print("File names in", mode.path, "changed.\n")


def changingExtensions(mode):
    ext = input("Enter the extension you want all the files in the selected path to have.\n"
                "Skip the dot. ('jpg' for example)\n")
    ask_if_sure(mode.path)
    for i, file in enumerate(sorted(os.scandir(mode.path), key=lambda t: t.stat().st_mtime)):
        if file.is_file():
            filename = get_filename(file.name)
            os.rename(create_path(mode.path, file.name), create_path(mode.path, filename + '.' + ext))
    print("File extensions in", mode.path, "changed.")
