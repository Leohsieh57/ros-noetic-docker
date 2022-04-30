#!/usr/bin/env python3
import os
import glob


NUM_PROC=24


def git_clone(url:str, commit:str="HEAD")->None: 
    os.system("git clone %s" % url)
    pkg_name = url.split('/')[-1].split('.')[0]
    os.chdir(pkg_name)
    os.system("git reset --hard %s" %commit)
    os.chdir("..")


def make_install(pkg_dir: str)->None: 
    os.chdir(pkg_dir)
    os.mkdir("build")
    os.chdir("build")
    os.system("cmake ..")
    os.system("sudo make install -j%i" % NUM_PROC)
    os.chdir("../..")


def is_cmake_repo(pkg_dir: str)->None:
    return os.path.exists(os.path.join(pkg_dir, "CMakeLists.txt"))



if __name__ == "__main__": 
    lines = open("dependencies/git.txt").readlines()
    lines = [line[:-1] for line in lines if len(line) > 5]
    
    urls = [line for i, line in enumerate(lines) if not i % 2]
    commits = [line for i, line in enumerate(lines) if i % 2]
 
    os.chdir("kit")
    for url, commit in zip(urls, commits): 
        git_clone(url, commit)
    
    repo_list = [fn for fn in glob.glob("*") if is_cmake_repo(fn)]
    for repo in repo_list: 
        make_install(repo)
    
    os.chdir("..")