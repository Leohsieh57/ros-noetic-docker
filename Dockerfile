FROM osrf/ros:noetic-desktop-full

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN sudo apt update
RUN sudo apt -y upgrade

RUN sudo apt -y install nvidia-driver-510
RUN sudo apt -y install libgoogle-glog-dev
RUN sudo apt -y install python3-pip
RUN sudo apt -y install git
RUN sudo apt -y install libatlas-base-dev
RUN sudo apt -y install libsuitesparse-dev

#RUN pip3 install torch
#RUN pip3 install torchvision
RUN pip3 install pandas
RUN pip3 install opencv-python

COPY . .
RUN python3 install_thirdparty.py

ENV USER_NAME=user
RUN useradd -ms /bin/bash $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME
COPY setup.bash /home/$USER_NAME/setup.bash