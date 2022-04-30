#!/usr/bin/env python3
import os


def remote_install(cmd:str, dependencies:str)->None: 
    for dep in open(dependencies).readlines(): 
        os.system("%s %s" % (cmd, dep if dep[-1] != '\n' else dep[:-1]))


if __name__ == "__main__": 
    remote_install("apt-get install -y", "dependencies/apt.txt")
    remote_install("pip3 install", "dependencies/pip.txt")