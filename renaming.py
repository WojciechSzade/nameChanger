import text
import os


def create_path(*args):
    return '\\'.join(args)


def get_extension(name):
    return name[name.rfind('.'):]


def get_filename(name):
    return name[:name.rfind('.')]


def selectKey(mode):
    if mode.sort == 1 or mode.sort == 2:
        return lambda t: t.stat().st_mtime
    elif mode.sort == 5 or mode.sort == 6:
        return lambda t: t.stat().st_size


tempdir = 0
tempdir_exist = 0
rev = False


def numberedRename1(mode, path, base, sort_key, rev):
    global tempdir
    global tempdir_exist
    for i, file in enumerate(sorted(os.scandir(path), key=sort_key, reverse=rev)):
        if file.is_file():
            ext = get_extension(file.name)
            try:
                os.rename(create_path(path, file.name), create_path(path, base + str(i + mode.zero - 2) + ext))
            except OSError as error:
                tempdir = create_path(path, 'temp')
                if not os.path.exists(tempdir):
                    os.mkdir(tempdir)
                os.rename(create_path(path, file.name), create_path(tempdir, base + str(i + mode.zero - 2) + ext))
                tempdir_exist = 1


def numberedRename2(mode, path, base, sort_key, rev):
    global tempdir
    global tempdir_exist
    for i, file in enumerate(sorted(os.scandir(path), key=sort_key, reverse=rev)):
        if file.is_file():
            ext = get_extension(file.name)
            try:
                os.rename(create_path(path, file.name),
                          create_path(path, base + '(' + str(i + mode.zero - 2) + ')' + ext))
            except OSError as error:
                tempdir = create_path(path, 'temp')
                if not os.path.exists(tempdir):
                    os.mkdir(tempdir)
                os.rename(create_path(path, file.name),
                          create_path(tempdir, base + '(' + str(i + mode.zero - 2) + ')' + ext))
                tempdir_exist = 1


def tempDirF(tempdir_exist, mode, path, base):
    if tempdir_exist:
        for i, file in enumerate(sorted(os.scandir(tempdir), key=lambda t: t.stat().st_mtime)):
            if file.is_file():
                ext = get_extension(file.name)
                os.rename(create_path(tempdir, file.name), create_path(path, file.name))
        os.rmdir(tempdir)


def rename(mode):
    global tempdir_exist
    global rev
    path = input(text.t_path1)
    os.startfile(path)
    base = input(text.t_basename)
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
    sort_key = selectKey(mode)
    if mode.sort%2 == 0:
        rev = True
    if mode.numbering == 1:
        numberedRename1(mode, path, base, sort_key, rev)
    elif mode.numbering == 2:
        numberedRename2(mode, path, base, sort_key, rev)
    tempDirF(tempdir_exist, mode, path, base)
    print("File names in", path, "changed.\n")


def changingExtensions(mode):
    path = input()
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
