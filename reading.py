def readConfig(mode):
    config = open("config.ini", "r")
    temp = config.readline()
    tempmain = temp[5]
    if tempmain.isdigit():
        if 1 <= int(tempmain) <= 2:
            mode.main = int(tempmain)
    temp = config.readline()
    tempnumbering = temp[15]
    if tempnumbering.isdigit():
        if 1 <= int(tempnumbering) <= 2:
            mode.numbering = int(tempnumbering)
    temp = config.readline()
    tempzero = temp[10]
    if tempzero.isdigit():
        if 1 <= int(tempzero) <= 2:
            mode.zero = int(tempzero)
    temp = config.readline()
    tempsort = temp[10]
    if tempsort.isdigit():
        if 1 <= int(tempsort) <= 8:
            mode.sort = int(tempsort)
    config.close()
    return mode


def saveConfig(mode):
    config = open("config.ini", "w")
    config.write("mode " + str(mode.main) + "\n" + "numbering_mode " + str(mode.numbering) +
                 "\n" + "zero_mode " + str(mode.zero) + "\n" + "sort_mode " + str(mode.sort) + "\n")


def printConfig(mode):
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
