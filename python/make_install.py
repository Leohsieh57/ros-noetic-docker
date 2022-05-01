#!/usr/bin/env python3
import os
import glob
from utils.pkg_repo import PackageRepository
from utils.utils import *

    
if __name__ == "__main__": 
    lines = get_lines("requirements/git_packages.txt", 5)
    remake = set(get_lines("requirements/force_reinstall.txt"))
    
    urls = [line for i, line in enumerate(lines) if not i%2]
    commits = [line for i, line in enumerate(lines) if i%2]
    
    os.system("sudo chown -R ${USER_NAME}:root kit")
    os.chdir("kit")
    
    package_repos = {}
    for url, commit in zip(urls, commits): 
        repo = PackageRepository.git_clone(url, commit)
        pkg_repo = PackageRepository(repo, repo in remake, commit)
        package_repos[repo] = pkg_repo

    for repo in glob.glob("*"):
        if is_cmake_repo(repo) and repo not in package_repos: 
            pkg_repo = PackageRepository(repo, repo in remake)
            package_repos[repo] = pkg_repo
            
    pkg_repo: PackageRepository
    for repo, pkg_repo in package_repos.items(): 
        if pkg_repo.reinstall_required():
            pkg_repo.make_install()
        else: 
            log_error("skipped consistant package '%s'"%repo)
    
    os.chdir("..")