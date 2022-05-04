#pull prebuilt images
ARG IMAGE=bardiche4768/ros-noetic-docker
ARG TAG=latest

FROM ${IMAGE}:${TAG}
ARG FROM_CUDA=0


#install ros
COPY . .
ENV USER_NAME=user
RUN bash script/install_ros.bash ${FROM_CUDA}
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}


#install dependencies
COPY . .
COPY script/setup.bash /home/${USER_NAME}/setup.bash
RUN python3 python/remote_install.py
RUN python3 python/make_install.py
