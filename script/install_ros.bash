#!/bin/bash
su -
apt-get update
apt-get -y install lsb-release
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

apt-get install -y curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

apt-get update
DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
apt-get install -y ros-noetic-desktop-full
source /opt/ros/noetic/setup.bash

apt-get install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
echo -ne '\n' | rosdep init
echo "conducting rosped udpate..."