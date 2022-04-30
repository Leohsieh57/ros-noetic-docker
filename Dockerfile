# pull ros noetic
FROM osrf/ros:noetic-desktop-full


# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics


#fetch apt
RUN sudo apt update
RUN sudo apt -y upgrade


#install dependencies
COPY . .
RUN python3 python/remote_install.py
RUN python3 python/make_install.py


#setup user
ENV USER_NAME=user
RUN useradd -ms /bin/bash $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME
COPY script/setup.bash /home/$USER_NAME/setup.bash