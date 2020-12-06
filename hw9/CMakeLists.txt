cmake_minimum_required(VERSION 2.8.3)
project(hw9)

find_package(catkin REQUIRED COMPONENTS
  gazebo_msgs
  message_runtime
  rospy
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
   src/main.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
