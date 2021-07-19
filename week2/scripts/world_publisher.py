#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class world:
    def __init__(self):
        self.word = "World!"
        self.pub = rospy.Publisher('/world', String, queue_size=1)
        self.rate = rospy.Rate(1)
    
    def publish_word(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.word)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('world_publisher')
    object = world()
    object.publish_word()