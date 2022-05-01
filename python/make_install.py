#!/usr/bin/env python3
import os
import glob
import pandas as pd
from utils.pkg_repo import PackageRepository
from utils.utils import *


NUM_PROC=24


def git_clone(url:str, commit:str="HEAD")->None: 
    pkg_name = url.split('/')[-1].split('.')[0]
    if not os.path.exists(pkg_name): 
        os.system("git clone %s" % url)
    
    os.chdir(pkg_name)
    os.system("git reset --hard %s" %commit)
    os.chdir("..")

    return pkg_name


def make_install(pkg_dir: str)->None: 
    os.chdir(pkg_dir)
    if os.path.exists("build"): 
        os.system("rm -rf build/")

    os.mkdir("build")
    os.chdir("build")
    os.system("cmake ..")
    os.system("sudo make install -j%i" % NUM_PROC)
    os.chdir("../..")


def is_cmake_repo(pkg_dir: str)->None:
    return os.path.exists(os.path.join(pkg_dir, "CMakeLists.txt"))


    
if __name__ == "__main__": 
    lines = get_lines("requirements/git_packages.txt", 5)
    remake = {repo:True for repo in get_lines("requirements/force_reinstall.txt")}
    
    urls = [line for i, line in enumerate(lines) if not i%2]
    commits = [line for i, line in enumerate(lines) if i%2]
    
    os.system("sudo chown -R ${USER_NAME}:root kit")
    os.chdir("kit")

    repo_commits = {}
    for url, commit in zip(urls, commits): 
        repo = git_clone(url, commit)
        repo_commits[repo] = commit
    
    repo_list = [fn for fn in glob.glob("*") if is_cmake_repo(fn)]
    for repo in repo_list: 
        commit = "" if repo not in repo_commits else repo_commits[repo]
        pkg_repo = PackageRepository(repo, repo in remake, commit)
        if pkg_repo.remake: 
            make_install(repo)
        else: 
            log_error("skipped existing pacakge '%s'"%repo)
    
    os.chdir("..")