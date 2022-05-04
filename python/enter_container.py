#!/usr/bin/env python3

import os
import pandas as pd
from io import BytesIO
from subprocess import Popen, PIPE


if __name__ == "__main__": 
    cmd = ["docker", "container", "ls"]
    df = pd.read_csv(BytesIO(Popen( cmd, stdout=PIPE).communicate()[0]))
    active_containers = [str(col).split('  ')[:2] for col in df[list(df)[0]]]
    active_containers = [[mem.replace(' ', '') for mem in col] for col in active_containers]
    found_container = False
    for id, image in active_containers: 
        if image == "ros-noetic-docker": 
            os.system("echo 'entered ros-noetic-container(%s)'" % id)
            os.system("docker exec -it %s /bin/bash"%id)
            found_container = True
            break

    if not found_container: 
        raise Exception("please run script/launch.bash first, aborting..")
    
    os.system("echo 'leaving ros-noetic-container(%s)'" % id)