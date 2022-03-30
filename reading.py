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
    temp = config.readline()
    mode.sort = int(temp[10])
    config.close()
    return mode


def printConfig(mode):
    if mode.display == 1:
        if mode.main == 1:
            print("Selected mode: Name Changer.")
        elif mode.main == 2:
            print("Selected mode: Extension Changer.")
        elif mode.main == 0:
            print("Mode not selected.\n")
        if mode.numbering == 1:
            print("Selected numbering mode: Just numbers.")
        elif mode.numbering == 2:
            print("Selected numbering mode: Numbers in brackets.")
        elif mode.numbering == 0:
            print("Numbering mode not selected")
        if mode.zero == 1:
            print("Counting from zero.")
        elif mode.zero == 2:
            print("Counting from one.")
        elif mode.zero == 0:
            print("Counting mode not selected.")
        if mode.sort == 1:
            print("Sorting mode: By date of edition from the newest")
        elif mode.sort == 2:
            print("Sorting mode: By date od edition from the oldest")
        elif mode.sort == 3:
            print("Sorting mode: By name alphabetically from A to Z")
        elif mode.sort == 4:
            print("Sorting mode: By name alphabetically from Z to A")
        elif mode.sort == 5:
            print("Sorting mode: By size from the smallest:")
        elif mode.sort == 6:
            print("Sorting mode: By size from the biggest:")
        elif mode.sort == 7:
            print("Sorting mode: By type alphabetically (then by name) from A to Z")
        elif mode.sort == 8:
            print("Sorting mode: By type alphabetically (then by name) from Z to A")
        elif mode.sort == 0:
            print("Sorting mode not selected")