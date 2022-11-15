


























# global_mode = 0


# def select_mode_low(text, mode, choices_low, choices_up):
#     global global_mode
#     global_mode = mode
#     if choices_low <= global_mode <= choices_up:
#         return global_mode
#     global_mode = input(text)
#     global_mode = int(global_mode)
#     if choices_low <= global_mode <= choices_up:
#         return global_mode
#     else:
#         return 0


# def select_mode(text, mode, choices_low, choices_up):
#     global global_mode
#     while True:
#         if select_mode_low(text, mode, choices_low, choices_up) >= choices_low:
#             return global_mode

#
# def select_mode_low_sort(text, mode, choices):
#     global global_mode
#     global_mode = mode
#     if 1 <= global_mode < choices:
#         return global_mode
#     global_mode = input(text)
#     global_mode = int(global_mode)
#     if 1 <= global_mode < choices:
#         return global_mode
#     else:
#         return 0
#
#
# def select_mode_sort(text, mode, choices):
#     global global_mode
#     while True:
#         if select_mode_low_sort(text,mode, choices):
#             return global_mode
