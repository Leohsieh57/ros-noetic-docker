#!/bin/bash

touch ~/.ros-noetic-docker-bash-history
docker build -t ros_noetic_docker . --no-cache \
    --build-arg IMAGE=nvidia/cuda \
    --build-arg TAG=11.6.0-devel-ubuntu20.04 \
    --build-arg FROM_CUDA=1
