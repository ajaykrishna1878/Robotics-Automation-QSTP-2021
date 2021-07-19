#!/usr/bin/env python3

import rospy
from rospy.core import is_shutdown
from std_msgs.msg import String

class hello_world:
    def __init__(self):
        self.pub = rospy.Publisher('/helloworld', String, queue_size=1)
        self.rate = rospy.Rate(1)
        self.hello_word = None
        self.world_word = None

    def callback_hello(self, msg):
        self.hello_word = msg.data

    def callback_world(self, msg):
        self.world_word = msg.data

    def subscribe_to_word(self):
        self.sub_hello = rospy.Subscriber('/hello', String, self.callback_hello)
        self.sub_world = rospy.Subscriber('/world', String, self.callback_world)

    def publish_word(self):
        self.subscribe_to_word()
        while not is_shutdown():
            self.pub.publish(str(self.hello_word) + " " + str(self.world_word))
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('hello_world_publisher')
    object = hello_world()
    object.publish_word()
    rospy.spin()
