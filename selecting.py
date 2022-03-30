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


def select_mode_low_sort(text, mode, choices):
    global global_mode
    global_mode = mode
    if 1 <= global_mode < choices:
        return global_mode
    global_mode = input(text)
    global_mode = int(global_mode)
    if 1 <= global_mode < choices:
        return global_mode
    else:
        return 0


def select_mode_sort(text, mode, choices):
    global global_mode
    while True:
        if select_mode_low_sort(text,mode, choices):
            return global_mode
