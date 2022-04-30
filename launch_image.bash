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
docker run -it \
    --gpus all \
    --net host --privileged \
    -v $HOME:/shared -e \
    DISPLAY=$DISPLAY -e \
    LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/ros_noetic_docker/catkin_ws:/home/user/catkin_ws:rw \
    -v $HOME/ros_noetic_docker/data:/data:ro \
    ros_noetic_docker

    
echo "exiting docker"
