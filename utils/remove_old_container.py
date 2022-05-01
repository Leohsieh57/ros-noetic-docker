#!/usr/bin/env python3
import os

if __name__ == "__main__": 
    txt_path = 'old_containers.txt'
    if not os.path.exists(txt_path): 
        txt_path = os.path.join('utils', txt_path)

    lines = open(txt_path).readlines()
    lines = [[x for x in line.split("  ") if x] for line in lines]
    for image_id in [line[0] for line in lines]: 
        assert len(image_id) == 12
        os.system("docker container rm -f %s"%image_id)

    os.system("docker container ls -a")