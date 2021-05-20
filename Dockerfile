FROM ros:noetic as BASE

RUN sudo apt-get update

SHELL ["/bin/bash", "-c"]

RUN source /opt/ros/noetic/setup.bash && \
        mkdir -p /home/ci/catkin_ws/src && cd /home/ci/catkin_ws && catkin_make

COPY tutorial /home/ci/catkin_ws/src/tutorial

COPY service_1 /home/ci/catkin_ws/src/service_1

RUN source /opt/ros/noetic/setup.bash && \
        cd /home/ci/catkin_ws && catkin_make

RUN cd /home/ci/catkin_ws && sudo su

RUN source /opt/ros/noetic/setup.bash && cd /home/ci/catkin_ws && catkin_make install 


FROM ros:noetic 

RUN sudo apt-get update

SHELL ["/bin/bash", "-c"]

RUN source /opt/ros/noetic/setup.bash && \
        mkdir -p /home/ci/catkin_ws/src && cd /home/ci/catkin_ws && catkin_make

COPY --from=BASE /home/ci/catkin_ws/install /home/ci/catkin_ws/install

RUN source /opt/ros/noetic/setup.bash && \
        cd /home/ci/catkin_ws && catkin_make

CMD source /home/ci/catkin_ws/install/setup.bash && roslaunch service_1 talker.launch