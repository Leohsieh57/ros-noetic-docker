import os
import glob
import pandas as pd
from utils.utils import log_error



SUFFIXES = [".cpp", ".c", ".cc", ".cu", ".cuh", 
    ".h", ".hpp", ".cmake.in", "CMakeLists.txt"]


class PackageRepository:
    def __init__(self, name:str, force_remake:bool, commit:str="") -> None:
        self.name = name
        self.commit = commit
        self.from_git = bool(commit)
        
        self.cache_file = ".cache"
        if not os.path.exists(self.cache_file): 
            os.mkdir(self.cache_file)
        
        self.cache_file = os.path.join(self.cache_file, self.name+".csv")

        filenames = self.get_all_filenames()
        if force_remake: 
            log_error("forced reinstallation for '%s'"%self.name)

        self.remake = force_remake or not os.path.exists(self.cache_file)
        self.remake = True if self.remake else self.check_modified(filenames)
        if self.remake: 
            self.export_cache_csv(filenames)
            

    def get_all_filenames(self): 
        if self.from_git: 
            return ["commit"]

        filenames = []
        for suffix in SUFFIXES: 
            search_path = os.path.join(self.name, "**", '*'+suffix)
            filenames+=glob.glob(search_path, recursive=True)

        return sorted(filenames)


    def check_modified(self, filenames):
        cache_df = pd.read_csv(self.cache_file)
        cached_filenames = sorted(list(cache_df))[1:]
        if filenames != cached_filenames: 
            log_error("file creation/removal in repo '%s'" % self.name)
            return True

        for fn in filenames:  
            cache_lines = [line for line in cache_df[fn] if line != "0"]
            curr_lines = [self.commit] if self.from_git else open(fn).readlines()
            if curr_lines != cache_lines: 
                log_error("file modification in  '%s'" % fn)
                return True

        return False


    def export_cache_csv(self, filenames): 
        filelines = {"commit": [self.commit]}
        if not self.from_git: 
            filelines = {fn: open(fn).readlines() for fn in filenames}

        max_line_num = 0
        for _, lines in filelines.items(): 
            max_line_num = max(max_line_num, len(lines))

        for key in filelines: 
            lines = filelines[key]
            lines += [0]*(max_line_num-len(lines))

        df = pd.DataFrame.from_dict(filelines)
        df.to_csv(self.cache_file)

        log_error("saved cache file at '%s'" % self.cache_file)