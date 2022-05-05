#!/usr/bin/env python3
import os


terminal_size = os.get_terminal_size()

COLS = terminal_size.columns
ROWS = terminal_size.lines
MAX_COLS = 70
MAX_ROWS = 20


def get_cols():
    return min(MAX_COLS, COLS)


def get_rows():
    return min(MAX_ROWS, ROWS)


def get_left_padding(): 
    padding = COLS - get_cols()
    return int(padding/2)


def get_vertical_padding(): 
    padding = ROWS - get_rows()
    top_padding = int(padding/2)
    return top_padding, padding - top_padding


def print_vertical_bound(): 
    left_padding = get_left_padding()
    left_padding+=1
    print(' '*left_padding+'#'*(get_cols()-2))


def print_single_line(line:str="", center:bool=True): 
    left_padding = get_left_padding()
    gap = max(0, get_cols()-4-len(line))
    if center: 
        left_margin = int(gap/2)
        right_margin = gap-left_margin
        line = ' '*left_padding+" #"+left_margin*' '+line+right_margin*' '+'# '
    else: 
        line = ' '*left_padding+" #"+line+gap*' '+'# '
    print(line)


def print_pannel(lines: list[tuple[str, bool]]): 
    gap = max(0, get_rows()-2-len(lines))
    top_margin = int(gap/2)
    bottom_margin = gap - top_margin
    top_padding, bottom_padding = get_vertical_padding()
    for _ in range(top_padding):
        print("")

    print_vertical_bound()
    for _ in range(top_margin): 
        print_single_line()

    for line, is_center in lines: 
        print_single_line(line, is_center)

    for _ in range(bottom_margin): 
        print_single_line()

    print_vertical_bound()
    for _ in range(bottom_padding-1):
        print("")


if __name__ == "__main__": 
    os.system("clear")
    print_pannel([
        ("ros-noetic-docker(bionic)", True), 
        ("", True), 
        ("", True),
        ("   - enter container:", False), 
        ("      1. open a new terminal", False),
        ("      2. run script/enter_container.bash", False), 
        ("", True), 
        ("   - stop container:", False), 
        ("      1. open a new terminal", False)
    ])
      

