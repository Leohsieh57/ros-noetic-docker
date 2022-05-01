#!/usr/bin/env python3
import os
from utils.utils import get_lines


def remote_install(cmd:str, filename:str): 
    for dep in get_lines(os.path.join("requirements", filename)): 
        os.system("%s %s" % (cmd, dep))


if __name__ == "__main__": 
    os.system("sudo apt-get update")
    os.system("sudo apt-get -y upgrade")
    
    remote_install("sudo apt-get install -y", "apt_packages.txt")
    remote_install("pip3 install", "pip_packages.txt")