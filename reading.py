def readConfig(mode):
    config = open("config.ini", "r")
    temp = config.readline()
    mode.display = int(temp[17])
    temp = config.readline()
    mode.main = int(temp[5])
    temp = config.readline()
    mode.numbering = int(temp[15])
    temp = config.readline()
    mode.zero = int(temp[10])
    config.close()
    return mode


def printConfig(mode):
    if mode.display == 1:
        if mode.main == 1:
            print("Selected mode: Name Changer.\n")
        elif mode.main == 2:
            print("Selected mode: Extension Changer.\n")
        elif mode.main == 0:
            print("Mode not selected.\n")
        if mode.numbering == 1:
            print("Selected numbering mode: Just numbers.\n")
        elif mode.numbering == 2:
            print("Selected numbering mode: Numbers in brackets.\n")
        elif mode.numbering == 0:
            print("Numbering mode not selected\n")
        if mode.zero == 1:
            print("Counting from zero.\n")
        elif mode.zero == 2:
            print("Counting from one.\n")
        elif mode.zero == 0:
            print("Counting mode not selected.\n")
