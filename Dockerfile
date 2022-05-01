# pull ros noetic
FROM osrf/ros:noetic-desktop-full


# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics


#setup user
ENV USER_NAME=user
RUN adduser --disabled-password --gecos '' ${USER_NAME}
RUN adduser ${USER_NAME} sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}
COPY script/setup.bash /home/${USER_NAME}/setup.bash


#install dependencies
FROM ros_noetic_docker:latest
COPY . .
RUN python3 python/remote_install.py
RUN python3 python/make_install.py