# Turtlebot Spy package
This is the solution for the final assignment of Robotics Automation QSTP 2021. In this package, a PID algorithm is used to control the TurtleBot spy to move to the location of the thief. On approaching the thief, the spy publishes a message "Found you!" on the topic '/gotcha'.

## Build Instructions
1. Copy this package to your existing catkin workspace's source folder `catkin_ws/src` and build using `catkin build` or `catkin_make`
## Launch Instructions
Launch the catch_me launch file. The launch file launches turtlebot in an spy world.
```
roslaunch turtlebot_spy catch_me.launch
```
