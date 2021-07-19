#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

rospy.init_node('radius_publisher')
pub = rospy.Publisher('/radius', Float32, queue_size=1)
rate = rospy.Rate(1)

if __name__ == '__main__':
    while not rospy.is_shutdown():
        pub.publish(0.5)
        rate.sleep()