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

RUN pip3 install pandas
#RUN pip3 install torch
#RUN pip3 install torchvision

WORKDIR /catkin_ws
COPY . . 

RUN python3 install_thirdparty.py

RUN mkdir fbow-arm64/build && cd fbow-arm64/build && cmake ..
RUN cd fbow-arm64/build && sudo make install -j24