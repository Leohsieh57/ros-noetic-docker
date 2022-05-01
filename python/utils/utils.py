import os


def get_lines(filename:str, min_len:int=0): 
    lines = open(filename).readlines()
    lines = [line for line in lines if len(line) > min_len]
    for i, line in enumerate(lines): 
        lines[i] = line[:-1] if line[-1] == '\n' else line

    return lines


def log_error(log:str): 
    os.system("echo '%s'" % "\033[91m[Docker INFO] " + log + '\033[0m')


def is_cmake_repo(pkg_dir: str):
    return os.path.exists(os.path.join(pkg_dir, "CMakeLists.txt"))