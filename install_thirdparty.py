#!/usr/bin/env python3
import os
import glob

NUM_PROC=24
BASEDIR="$PWD"


def clone_git_pkg(url:str, commit:str="HEAD")->None: 
    os.system("git clone %s" % url)
    pkg_name = url.split('/')[-1].split('.')[0]
    os.chdir(pkg_name)
    os.system("git reset --hard %s" %commit)
    os.chdir("..")


def install_local_pkg(pkg_dir: str)->None: 
    os.chdir(pkg_dir)
    os.mkdir("build")
    os.chdir("build")
    os.system("cmake ..")
    os.system("sudo make install -j%i" % NUM_PROC)
    os.chdir("../..")


def is_cmake_repo(pkg_dir: str)->None:
    return os.path.exists(os.path.join(pkg_dir, "CMakeLists.txt"))



if __name__ == "__main__": 
    clone_git_pkg("https://github.com/jlblancoc/nanoflann.git", 
        "c52ae8d1ac7836385ac54460be64ba39f258e64c")
    
    clone_git_pkg("https://github.com/ceres-solver/ceres-solver.git", 
        "f1414cb5bd3fafb54cc4f5bc2d4d4df5f4149ccc")

    clone_git_pkg("https://github.com/RainerKuemmerle/g2o.git", 
        "b1ba729aa569267e179fa2e237db0b3ad5169e2e")
    
    clone_git_pkg("https://github.com/strasdat/Sophus.git", 
        "4ac843dd9050a5d175e5c0a857da9315fbc436f0")
    
    clone_git_pkg("https://github.com/stevenlovegrove/Pangolin.git", 
        "d64507241dc79ecd98c1dea267d74dac34663629")

    repo_list = [fn for fn in glob.glob("*") if is_cmake_repo(fn)]
    for repo in repo_list: 
        install_local_pkg(repo)
    