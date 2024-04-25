fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"  # noqa
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"  # noqa


def print_six(row, format, end="\n"):
    for col in range(6):
        color = row*6 + col - 2
        if color >= 0:
            text = "{:3d}".format(color)
            print(format(text, color), end=" ")
        else:
            print(end="    ")   # four spaces
    print(end=end)


for row in range(0, 43):
    print_six(row, fg, " ")
    print_six(row, bg)

# Simple usage: print(fg("text", 160))
