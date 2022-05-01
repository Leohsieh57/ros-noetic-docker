#!/usr/bin/env python3
import os

if __name__ == "__main__": 
    txt_path = 'old_images.txt'
    if not os.path.exists(txt_path): 
        txt_path = os.path.join('utils', txt_path)

    lines = open(txt_path).readlines()
    lines = [[x for x in line.split("  ") if x] for line in lines]
    for image_id in [line[2] for line in lines]: 
        while image_id[-1] == ' ': 
            image_id = image_id[:-1]
        while image_id[0] == ' ': 
            image_id = image_id[1:]

        assert len(image_id) == 12
        os.system("docker image rm -f %s"%image_id)

    os.system("docker images")