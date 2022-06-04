XAUTH=/tmp/.docker.xauth
if [ ! -f $XAUTH ]
then
    xauth_list=$(xauth nlist :0 | sed -e 's/^..../ffff/')
    if [ ! -z "$xauth_list" ]
    then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi

xhost +local:root;
python3 python/print_pannel.py
docker run -it --rm --gpus all \
    --net host --privileged \
    --name focal \
    -v $HOME:/shared -e \
    DISPLAY=$DISPLAY -e \
    LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH \
    -v /dev:/dev \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/ros-noetic-docker/catkin_ws:/home/user/catkin_ws:rw \
    -v $HOME/ros-noetic-docker/data:/data:rw \
    -v $HOME/.ros-noetic-docker-bash-history:/home/user/.bash_history:rw \
    ros-noetic-docker /bin/bash > /dev/null

clear
echo "ros-noetic-docker stopped"
