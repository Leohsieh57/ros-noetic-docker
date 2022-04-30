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

RUN pip3 install pandas

