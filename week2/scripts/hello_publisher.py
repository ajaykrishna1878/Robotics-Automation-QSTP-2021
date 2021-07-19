#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class hello:
    def __init__(self):
        self.word = "Hello,"
        self.pub = rospy.Publisher('/hello', String, queue_size=1)
        self.rate = rospy.Rate(1)
    
    def publish_word(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.word)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('hello_publisher')
    object = hello()
    object.publish_word()