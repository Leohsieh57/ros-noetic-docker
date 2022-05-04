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
echo ""
echo "###############################################"
echo "#                                             #"
echo "#          ros-noetic-docker(bionic)          #"
echo "#                                             #"
echo "#  enter container:                           #"
echo "#     1. open a new terminal                  #"
echo "#     2. run script/enter_container.bash      #"
echo "#                                             #"
echo "#  stop container:                            #"
echo "#     1. ctrl+d on this terminal              #"
echo "#                                             #"
echo "###############################################"
echo ""
docker run -it --rm --gpus all \
    --net host --privileged \
    --name bionic \
    -v $HOME:/shared -e \
    DISPLAY=$DISPLAY -e \
    LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH \
    -v /dev:/dev \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/ros-noetic-docker/catkin_ws:/home/user/catkin_ws:rw \
    -v $HOME/ros-noetic-docker/data:/data:ro \
    -v $HOME/.ros-noetic-docker-bash-history:/home/user/.bash_history:rw \
    ros-noetic-docker /bin/bash > /dev/null

echo "ros-noetic-docker stopped"