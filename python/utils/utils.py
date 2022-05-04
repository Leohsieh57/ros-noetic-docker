import os
from datetime import datetime


def get_lines(filename:str, min_len:int=0): 
    lines = open(filename).readlines()
    lines = [line for line in lines if len(line) > min_len and line[0] != '#']
    for i, line in enumerate(lines): 
        lines[i] = line[:-1] if line[-1] == '\n' else line

    return lines


def log_error(log:str): 
    now = str(datetime.now().time())
    log = "\033[0;31m ---DOCKER BUILD [%s] %s\033[0m" % (now, log)
    os.system("echo '%s'" % log)


def is_cmake_repo(pkg_dir: str):
    return os.path.exists(os.path.join(pkg_dir, "CMakeLists.txt"))
