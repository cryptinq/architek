import os
import re

initialized = False
DEFAULT_COLOR = ""

FORMAT_CODES = {

    # Foreground colors
    "∑c": "160", "∑4": "1", "∑6": "208", "∑e": "227", "∑2": "34", "∑a": "48",
    "∑b": "38", "∑3": "33", "∑1": "21", "∑9": "63", "∑d": "99", "∑5": "93",
    "∑f": "255", "∑7": "238", "∑8": "235", "∑0": "232", "∑r": "0",

    # Background colors
    "∑c.": "160", "∑4.": "1", "∑6.": "208", "∑e.": "227", "∑2.": "34", "∑a.": "48",
    "∑b.": "38", "∑3.": "33", "∑1.": "21", "∑9.": "63", "∑d.": "99", "∑5.": "93",
    "∑f.": "255", "∑7.": "238", "∑8.": "235", "∑0.": "232", "∑r.": "0"

}


def initialize():
    global initialized

    if not initialized:
        os.system("")
        initialized = True


def get_format_codes():
    return FORMAT_CODES


def format_color(color_code):
    return get_format_codes().get(color_code, "")


def c(text, reset_fg=True, reset_bg=True) -> str:
    initialize()

    global DEFAULT_COLOR
    text = DEFAULT_COLOR + text
    text = re.sub(r'\\∑', '∑', text)

    def repl(match):

        color_code = match.group(0)
        color_value = format_color(color_code)

        if color_code.endswith('.'):
            color_value = format_color(color_code)
            return f"\33[48;5;{color_value}m"
        return f"\33[38;5;{color_value}m"

    text = re.sub(r'(∑[0-9a-fA-Fr]\.?)', repl, text)

    if reset_fg and not reset_bg:
        text += "\33[0m"
    elif reset_bg and not reset_fg:
        text += "\33[49m"
        print("added reset bg")
    elif reset_bg and reset_fg:
        text += "\33[0m\33[49m"

    return text


# =====================================================================================================

def printAllColors():
    initialize()

    fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\033[0m\033[K"

    def print_six(row, format, end="\n"):
        for col in range(6):
            color = row * 6 + col - 2
            if color >= 0:
                text = "{:3d}".format(color)
                print(format(text, color), end=" ")
            else:
                print(end="    ")  # four spaces
        print(end=end)

    for row in range(0, 43):
        print_six(row, fg, " ")
        print_six(row, bg)


# =====================================================================================================

if __name__ == "__main__":
    printAllColors()
