# ROS_Py
Robot Operating System written in Python 2 / Learning tool Saint Martin University CSC577

# Requirements:

ROS Melodic Morenia, Ubuntu 18.04.4 LTS (Bionic Beaver) Caktlin and Python 2

# Installation:

## To make the chapter packages available to your ROS distribution, complete the following steps.

Create a ROS workspace with a src directory.

Download and unzip or (fork! and) clone this repository to the src directory.

git clone https://github.com/regenalgrant/ROS_Py.git

In the workspace, make.

catkin_make

Source your workspace.

source devel/setup.bash

The chapter packages are now available to your ROS distribution. If you have rosbash installed (and you should), the chapter packages should appear to roscd and rosls.

#Organization:

Due to the developing nature of the text and code, chapter numbers are omitted and instead are identified by abbreviated name. For instance, the chapter ROS topics is abbreviated topics as Topics. The prefix rico_ is included to differentiate the textbook packages.

# Origins:

This repository began as a fork of the sample code repository that accompanies the excellent text Programming Robots with ROS, by Morgan Quigley, Brian Gerkey and William D. Smart (O'Reilly Media, Inc., 2015). The original repository was distributed under the Apache 2.0 license. Differences in ROS and Ubuntu software versions, book organizational structure, and code details suggested moving from fork to distinct project, but I express my significant debt to this original repository and gratitude to its authors.

written format is source from Dr. Rico Picone